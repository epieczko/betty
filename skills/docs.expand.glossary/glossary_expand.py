#!/usr/bin/env python3
"""
glossary_expand.py - Implementation of the docs.expand.glossary Skill

Extract undocumented terms from Betty manifests and docs, then enrich glossary.md
with new definitions.
"""

import os
import sys
import json
import yaml
import re
from typing import Dict, Any, List, Set, Optional
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict


from betty.config import BASE_DIR
from betty.logging_utils import setup_logger
from betty.errors import BettyError

logger = setup_logger(__name__)


# Common field names found in manifests
SKILL_FIELDS = {
    "name", "version", "description", "inputs", "outputs", "dependencies",
    "entrypoints", "status", "tags", "runtime", "handler", "permissions",
    "parameters", "command", "required", "type", "default"
}

AGENT_FIELDS = {
    "name", "version", "description", "capabilities", "skills_available",
    "reasoning_mode", "context_requirements", "workflow_pattern",
    "error_handling", "output", "status", "tags", "dependencies",
    "max_retries", "timeout_seconds", "on_validation_failure",
    "on_generation_failure", "on_compilation_failure"
}

COMMAND_FIELDS = {
    "name", "description", "execution", "parameters", "version", "status",
    "tags", "delegate_to", "workflow", "agent", "skill"
}

HOOK_FIELDS = {
    "name", "description", "event", "command", "enabled", "blocking",
    "timeout", "version", "status", "tags"
}

# Terms that are already well-documented or common
SKIP_TERMS = {
    "name", "version", "description", "true", "false", "string", "boolean",
    "integer", "array", "object", "list", "dict", "file", "path", "url",
    "id", "uuid", "timestamp", "date", "time", "json", "yaml", "xml"
}


def build_response(
    ok: bool,
    errors: Optional[List[str]] = None,
    details: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Build standardized response."""
    response: Dict[str, Any] = {
        "ok": ok,
        "status": "success" if ok else "failed",
        "errors": errors or [],
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    if details is not None:
        response["details"] = details
    return response


def load_glossary(glossary_path: str) -> Dict[str, str]:
    """
    Load existing glossary and extract defined terms.

    Args:
        glossary_path: Path to glossary.md

    Returns:
        Dictionary mapping term names to their sections
    """
    if not os.path.exists(glossary_path):
        logger.warning(f"Glossary not found: {glossary_path}")
        return {}

    terms = {}
    with open(glossary_path, 'r') as f:
        content = f.read()

    # Extract term headings (### Term Name)
    pattern = r'^###\s+(.+)$'
    matches = re.finditer(pattern, content, re.MULTILINE)

    for match in matches:
        term = match.group(1).strip()
        terms[term.lower()] = term

    logger.info(f"Loaded {len(terms)} existing glossary terms")
    return terms


def scan_yaml_files(pattern: str, base_dir: str) -> List[Dict[str, Any]]:
    """
    Scan YAML files matching pattern.

    Args:
        pattern: File pattern (e.g., "skill.yaml", "agent.yaml")
        base_dir: Base directory to search

    Returns:
        List of parsed YAML data
    """
    files = []
    for root, dirs, filenames in os.walk(base_dir):
        for filename in filenames:
            if filename == pattern:
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r') as f:
                        data = yaml.safe_load(f)
                        if data:
                            data['_source_path'] = file_path
                            files.append(data)
                except Exception as e:
                    logger.warning(f"Failed to parse {file_path}: {e}")

    logger.info(f"Scanned {len(files)} {pattern} files")
    return files


def scan_markdown_files(docs_dir: str) -> List[str]:
    """
    Scan markdown files for capitalized terms that might need definitions.

    Args:
        docs_dir: Directory containing markdown files

    Returns:
        List of potential terms found in docs
    """
    terms = set()

    for file_path in Path(docs_dir).glob("*.md"):
        try:
            with open(file_path, 'r') as f:
                content = f.read()

            # Find capitalized phrases (potential terms)
            # Look for patterns like "Breaking Change", "Blocking Hook", etc.
            pattern = r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b'
            matches = re.finditer(pattern, content)

            for match in matches:
                term = match.group(1)
                # Filter out common words and single words
                if len(term.split()) > 1 or term.lower() not in SKIP_TERMS:
                    terms.add(term)

        except Exception as e:
            logger.warning(f"Failed to scan {file_path}: {e}")

    logger.info(f"Found {len(terms)} potential terms in docs")
    return list(terms)


def extract_terms_from_manifests(
    skills: List[Dict[str, Any]],
    agents: List[Dict[str, Any]]
) -> Dict[str, List[str]]:
    """
    Extract field names and values from manifests.

    Args:
        skills: List of skill manifests
        agents: List of agent manifests

    Returns:
        Dictionary of term categories to terms
    """
    terms = defaultdict(set)

    # Extract from skills
    for skill in skills:
        # Status values
        if 'status' in skill:
            terms['status'].add(skill['status'])

        # Runtime values
        for ep in skill.get('entrypoints', []):
            if 'runtime' in ep:
                terms['runtime'].add(ep['runtime'])
            if 'permissions' in ep:
                for perm in ep['permissions']:
                    terms['permissions'].add(perm)

        # Input/output types
        for input_def in skill.get('inputs', []):
            if isinstance(input_def, dict) and 'type' in input_def:
                terms['types'].add(input_def['type'])

        for output_def in skill.get('outputs', []):
            if isinstance(output_def, dict) and 'type' in output_def:
                terms['types'].add(output_def['type'])

    # Extract from agents
    for agent in agents:
        # Reasoning modes
        if 'reasoning_mode' in agent:
            terms['reasoning_mode'].add(agent['reasoning_mode'])

        # Status values
        if 'status' in agent:
            terms['status'].add(agent['status'])

        # Error handling strategies
        error_handling = agent.get('error_handling', {})
        for key in error_handling:
            if key.startswith('on_'):
                terms['error_handling'].add(key)

    # Convert sets to sorted lists
    return {k: sorted(v) for k, v in terms.items()}


def generate_definition(term: str, category: str, context: Dict[str, Any]) -> Optional[str]:
    """
    Generate a glossary definition for a term.

    Args:
        term: Term to define
        category: Category of the term (e.g., 'status', 'runtime')
        context: Additional context from manifests

    Returns:
        Generated definition or None if unable to generate
    """
    definitions = {
        # Status values
        'active': 'A status indicating that a component is production-ready and available for use in workflows and operations.',
        'draft': 'A status indicating that a component is under development and not yet production-ready. Draft components are excluded from production operations.',
        'deprecated': 'A status indicating that a component is no longer recommended for use and may be removed in future versions.',
        'archived': 'A status indicating that a component has been retired and is no longer maintained or available.',

        # Runtime values
        'python': 'A runtime environment for executing Python-based skills and operations.',
        'javascript': 'A runtime environment for executing JavaScript/Node.js-based skills and operations.',
        'bash': 'A runtime environment for executing shell scripts and command-line operations.',

        # Permissions
        'filesystem:read': 'Permission to read files and directories from the filesystem.',
        'filesystem:write': 'Permission to write, modify, or delete files and directories.',
        'network:http': 'Permission to make HTTP/HTTPS network requests.',
        'network:all': 'Permission to make any network connections.',

        # Reasoning modes (already in glossary but we can check)
        'iterative': 'A reasoning mode where an agent can retry operations based on feedback, useful for tasks requiring refinement.',
        'oneshot': 'A reasoning mode where an agent executes once without retries, suitable for deterministic tasks.',

        # Types
        'string': 'A text value type.',
        'boolean': 'A true/false value type.',
        'integer': 'A whole number value type.',
        'object': 'A structured data type containing key-value pairs.',
        'array': 'A list of values.',

        # Error handling
        'on_validation_failure': 'Error handling strategy that defines actions to take when validation fails.',
        'on_generation_failure': 'Error handling strategy that defines actions to take when generation fails.',
        'on_compilation_failure': 'Error handling strategy that defines actions to take when compilation fails.',

        # Other common terms
        'max_retries': 'The maximum number of retry attempts allowed for an operation before failing.',
        'timeout_seconds': 'The maximum time in seconds that an operation is allowed to run before being terminated.',
        'blocking': 'A property indicating that an operation must complete (or fail) before subsequent operations can proceed.',
        'fuzzy': 'A matching mode that allows approximate string matching rather than exact matches.',
        'handler': 'The script or function that implements the core logic of a skill or operation.',
        'strict': 'A validation mode where warnings are treated as errors.',
        'dry_run': 'A mode that previews an operation without actually executing it or making changes.',
        'overwrite': 'An option to replace existing content rather than preserving or merging it.',
    }

    # Return predefined definition if available
    if term.lower() in definitions:
        return definitions[term.lower()]

    # Generate contextual definitions based on category
    if category == 'permissions':
        parts = term.split(':')
        if len(parts) == 2:
            resource, action = parts
            return f"Permission to {action} {resource} resources."

    return None


def update_glossary(
    glossary_path: str,
    new_terms: Dict[str, str],
    dry_run: bool = False
) -> str:
    """
    Update glossary.md with new term definitions.

    Args:
        glossary_path: Path to glossary.md
        new_terms: Dictionary mapping terms to definitions
        dry_run: If True, don't write to file

    Returns:
        Updated glossary content
    """
    # Read existing glossary
    with open(glossary_path, 'r') as f:
        content = f.read()

    # Group terms by first letter
    terms_by_letter = defaultdict(list)
    for term, definition in sorted(new_terms.items()):
        first_letter = term[0].upper()
        terms_by_letter[first_letter].append((term, definition))

    # Find insertion points and add new terms
    lines = content.split('\n')
    new_lines = []
    current_section = None

    for i, line in enumerate(lines):
        new_lines.append(line)

        # Detect section headers (## A, ## B, etc.)
        section_match = re.match(r'^##\s+([A-Z])\s*$', line)
        if section_match:
            current_section = section_match.group(1)

            # If we have new terms for this section, add them
            if current_section in terms_by_letter:
                # Find the right place to insert (alphabetically)
                # For now, append at the end of the section
                for term, definition in terms_by_letter[current_section]:
                    new_lines.append('')
                    new_lines.append(f'### {term}')
                    new_lines.append(definition)

    new_content = '\n'.join(new_lines)

    if not dry_run:
        with open(glossary_path, 'w') as f:
            f.write(new_content)
        logger.info(f"Updated glossary with {len(new_terms)} new terms")

    return new_content


def expand_glossary(
    glossary_path: Optional[str] = None,
    base_dir: Optional[str] = None,
    dry_run: bool = False,
    include_auto_generated: bool = True
) -> Dict[str, Any]:
    """
    Main function to expand glossary with undocumented terms.

    Args:
        glossary_path: Path to glossary.md (default: docs/glossary.md)
        base_dir: Base directory to scan (default: BASE_DIR)
        dry_run: Preview changes without writing
        include_auto_generated: Include auto-generated definitions

    Returns:
        Result with new terms and summary
    """
    # Set defaults
    if base_dir is None:
        base_dir = BASE_DIR

    if glossary_path is None:
        glossary_path = os.path.join(base_dir, "docs", "glossary.md")

    logger.info(f"Expanding glossary at {glossary_path}")

    # Load existing glossary
    existing_terms = load_glossary(glossary_path)

    # Scan manifests
    skills = scan_yaml_files("skill.yaml", os.path.join(base_dir, "skills"))
    agents = scan_yaml_files("agent.yaml", os.path.join(base_dir, "agents"))

    # Extract terms from manifests
    manifest_terms = extract_terms_from_manifests(skills, agents)

    # Scan docs for additional terms
    docs_dir = os.path.join(base_dir, "docs")
    doc_terms = scan_markdown_files(docs_dir)

    # Find undocumented terms
    new_terms = {}
    skipped_terms = []

    for category, terms in manifest_terms.items():
        for term in terms:
            term_lower = term.lower()

            # Skip if already in glossary
            if term_lower in existing_terms:
                continue

            # Skip common terms
            if term_lower in SKIP_TERMS:
                skipped_terms.append(term)
                continue

            # Generate definition
            if include_auto_generated:
                definition = generate_definition(term, category, {
                    'category': category,
                    'skills': skills,
                    'agents': agents
                })

                if definition:
                    # Capitalize term name properly
                    term_name = term.title() if term.islower() else term
                    new_terms[term_name] = definition
                else:
                    skipped_terms.append(term)

    # Update glossary
    updated_content = None
    if new_terms:
        updated_content = update_glossary(glossary_path, new_terms, dry_run)

    # Build summary
    summary = {
        "glossary_path": glossary_path,
        "existing_terms_count": len(existing_terms),
        "new_terms_count": len(new_terms),
        "new_terms": list(new_terms.keys()),
        "skipped_terms_count": len(skipped_terms),
        "scanned_files": {
            "skills": len(skills),
            "agents": len(agents)
        },
        "dry_run": dry_run
    }

    if dry_run and updated_content:
        summary["preview"] = updated_content

    # Build detailed output
    details = {
        "summary": summary,
        "new_definitions": new_terms,
        "manifest_terms": manifest_terms,
        "skipped_terms": skipped_terms[:20]  # Limit to first 20
    }

    return build_response(ok=True, details=details)


def main():
    """Main CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Expand glossary.md with undocumented terms from manifests",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Expand glossary with new terms
  glossary_expand.py

  # Preview changes without writing
  glossary_expand.py --dry-run

  # Use custom glossary path
  glossary_expand.py --glossary-path /path/to/glossary.md

  # Skip auto-generated definitions (only show what's missing)
  glossary_expand.py --no-auto-generate
        """
    )

    parser.add_argument(
        "--glossary-path",
        help="Path to glossary.md file"
    )
    parser.add_argument(
        "--base-dir",
        help="Base directory to scan for manifests"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing to glossary"
    )
    parser.add_argument(
        "--no-auto-generate",
        action="store_true",
        help="Don't auto-generate definitions, only report missing terms"
    )
    parser.add_argument(
        "--format",
        choices=["json", "summary"],
        default="summary",
        help="Output format"
    )

    args = parser.parse_args()

    try:
        result = expand_glossary(
            glossary_path=args.glossary_path,
            base_dir=args.base_dir,
            dry_run=args.dry_run,
            include_auto_generated=not args.no_auto_generate
        )

        if args.format == "json":
            print(json.dumps(result, indent=2))
        else:
            # Pretty summary output
            details = result["details"]
            summary = details["summary"]

            print("\n" + "="*80)
            print("GLOSSARY EXPANSION SUMMARY")
            print("="*80)
            print(f"\nGlossary: {summary['glossary_path']}")
            print(f"Existing terms: {summary['existing_terms_count']}")
            print(f"New terms added: {summary['new_terms_count']}")
            print(f"Scanned: {summary['scanned_files']['skills']} skills, "
                  f"{summary['scanned_files']['agents']} agents")

            if summary['new_terms_count'] > 0:
                print(f"\n{'-'*80}")
                print("NEW TERMS:")
                print(f"{'-'*80}")
                for term in summary['new_terms']:
                    definition = details['new_definitions'][term]
                    print(f"\n### {term}")
                    print(definition)
                print(f"\n{'-'*80}")

            if summary['dry_run']:
                print("\n[DRY RUN] No changes written to glossary")
            else:
                print(f"\nGlossary updated successfully!")

            print("\n" + "="*80 + "\n")

        sys.exit(0 if result['ok'] else 1)

    except BettyError as e:
        logger.error(f"Failed to expand glossary: {e}")
        result = build_response(ok=False, errors=[str(e)])
        print(json.dumps(result, indent=2))
        sys.exit(1)

    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        result = build_response(ok=False, errors=[f"Unexpected error: {str(e)}"])
        print(json.dumps(result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
