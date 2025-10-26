#!/usr/bin/env python3
"""
Audit Artifact Registry - Scan and verify artifact type consistency across Betty

This script:
1. Extracts all artifact types from the registry (artifact_define.py)
2. Scans all skill.yaml files for artifact_metadata references
3. Scans all agent.yaml files for artifact references
4. Scans template files for artifact type identifiers
5. Compares declared vs referenced artifacts
6. Generates a comprehensive audit report
"""

import os
import sys
import json
import yaml
import re
from pathlib import Path
from typing import Dict, Set, List, Any
from collections import defaultdict

# Add betty to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from betty.config import BASE_DIR
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)


def extract_registry_types() -> Dict[str, Dict[str, Any]]:
    """Extract all artifact types from the registry"""
    logger.info("Extracting artifact types from registry...")

    # Load the registry file directly
    registry_file = Path(BASE_DIR) / "skills" / "artifact.define" / "artifact_define.py"

    # Parse the Python file to extract KNOWN_ARTIFACT_TYPES
    import ast

    with open(registry_file, 'r') as f:
        content = f.read()

    # Extract the KNOWN_ARTIFACT_TYPES dictionary
    tree = ast.parse(content)

    known_types = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == 'KNOWN_ARTIFACT_TYPES':
                    # Evaluate the dictionary literal
                    known_types = ast.literal_eval(node.value)
                    break

    logger.info(f"Found {len(known_types)} artifact types in registry")
    return known_types


def scan_skill_files() -> Dict[str, List[Dict[str, Any]]]:
    """Scan all skill.yaml files for artifact_metadata references"""
    logger.info("Scanning skill.yaml files...")

    skill_refs = defaultdict(list)
    skills_dir = Path(BASE_DIR) / "skills"

    for skill_yaml in skills_dir.rglob("skill.yaml"):
        try:
            with open(skill_yaml, 'r') as f:
                data = yaml.safe_load(f)

            if not data or 'artifact_metadata' not in data:
                continue

            metadata = data['artifact_metadata']
            skill_name = skill_yaml.parent.name

            # Extract produces
            if 'produces' in metadata:
                for artifact in metadata['produces']:
                    if 'type' in artifact:
                        skill_refs[artifact['type']].append({
                            'source': 'skill',
                            'skill_name': skill_name,
                            'file': str(skill_yaml),
                            'role': 'producer',
                            'description': artifact.get('description', '')
                        })

            # Extract consumes
            if 'consumes' in metadata:
                for artifact in metadata['consumes']:
                    if 'type' in artifact:
                        skill_refs[artifact['type']].append({
                            'source': 'skill',
                            'skill_name': skill_name,
                            'file': str(skill_yaml),
                            'role': 'consumer',
                            'description': artifact.get('description', '')
                        })

        except Exception as e:
            logger.warning(f"Error parsing {skill_yaml}: {e}")

    total_refs = sum(len(refs) for refs in skill_refs.values())
    logger.info(f"Found {total_refs} artifact references in {len(list(skills_dir.rglob('skill.yaml')))} skill files")
    return dict(skill_refs)


def scan_agent_files() -> Dict[str, List[Dict[str, Any]]]:
    """Scan all agent.yaml files for artifact references"""
    logger.info("Scanning agent.yaml files...")

    agent_refs = defaultdict(list)
    agents_dir = Path(BASE_DIR) / "agents"

    for agent_yaml in agents_dir.rglob("agent.yaml"):
        try:
            with open(agent_yaml, 'r') as f:
                data = yaml.safe_load(f)

            if not data:
                continue

            agent_name = agent_yaml.parent.name

            # Check system_prompt for artifact type mentions
            system_prompt = data.get('system_prompt', '')
            if system_prompt:
                # Look for artifact type patterns (kebab-case words)
                artifact_patterns = re.findall(r'\b([a-z]+-[a-z-]+)\b', system_prompt)
                for artifact_type in set(artifact_patterns):
                    agent_refs[artifact_type].append({
                        'source': 'agent',
                        'agent_name': agent_name,
                        'file': str(agent_yaml),
                        'role': 'reference',
                        'context': 'system_prompt'
                    })

            # Check description for artifact mentions
            description = data.get('description', '')
            if description:
                artifact_patterns = re.findall(r'\b([a-z]+-[a-z-]+)\b', description)
                for artifact_type in set(artifact_patterns):
                    agent_refs[artifact_type].append({
                        'source': 'agent',
                        'agent_name': agent_name,
                        'file': str(agent_yaml),
                        'role': 'reference',
                        'context': 'description'
                    })

        except Exception as e:
            logger.warning(f"Error parsing {agent_yaml}: {e}")

    total_refs = sum(len(refs) for refs in agent_refs.values())
    logger.info(f"Found {total_refs} artifact references in {len(list(agents_dir.rglob('agent.yaml')))} agent files")
    return dict(agent_refs)


def scan_template_files() -> Dict[str, List[Dict[str, Any]]]:
    """Scan template files for artifact type identifiers"""
    logger.info("Scanning template files...")

    template_refs = defaultdict(list)
    templates_dir = Path(BASE_DIR) / "templates"

    # Scan both .md and .yaml template files
    for template_file in templates_dir.rglob("*"):
        if not template_file.is_file():
            continue

        if template_file.suffix not in ['.md', '.yaml', '.yml']:
            continue

        try:
            # Extract artifact type from filename
            # Pattern: *.artifact-type.{md,yaml}
            filename = template_file.stem

            # Check if this matches an artifact pattern
            # Templates are often named after artifact types
            if '-' in filename:
                artifact_type = filename
                template_refs[artifact_type].append({
                    'source': 'template',
                    'file': str(template_file),
                    'category': template_file.parent.name,
                    'format': template_file.suffix
                })

        except Exception as e:
            logger.warning(f"Error processing {template_file}: {e}")

    total_refs = sum(len(refs) for refs in template_refs.values())
    logger.info(f"Found {total_refs} template files")
    return dict(template_refs)


def scan_artifact_descriptions() -> Set[str]:
    """Scan artifact_descriptions directory for defined types"""
    logger.info("Scanning artifact descriptions...")

    descriptions = set()
    descriptions_dir = Path(BASE_DIR) / "artifact_descriptions"

    if not descriptions_dir.exists():
        logger.warning(f"Artifact descriptions directory not found: {descriptions_dir}")
        return descriptions

    for desc_file in descriptions_dir.glob("*.md"):
        # Artifact type is the filename without extension
        artifact_type = desc_file.stem
        descriptions.add(artifact_type)

    logger.info(f"Found {len(descriptions)} artifact descriptions")
    return descriptions


def compare_and_analyze(
    registry_types: Dict[str, Dict[str, Any]],
    skill_refs: Dict[str, List[Dict[str, Any]]],
    agent_refs: Dict[str, List[Dict[str, Any]]],
    template_refs: Dict[str, List[Dict[str, Any]]],
    descriptions: Set[str]
) -> Dict[str, Any]:
    """Compare declared vs referenced artifacts and identify discrepancies"""
    logger.info("Analyzing artifact consistency...")

    # Create sets for comparison
    declared_types = set(registry_types.keys())
    referenced_types = set(skill_refs.keys()) | set(agent_refs.keys()) | set(template_refs.keys())

    # Identify discrepancies
    missing_in_registry = referenced_types - declared_types
    unused_in_registry = declared_types - referenced_types

    # Filter out false positives (common words that match kebab-case pattern)
    common_words = {
        'add-on', 'back-end', 'front-end', 'well-known', 'run-time', 'build-time',
        'up-to-date', 'self-service', 'role-based', 'time-based', 'event-driven',
        'real-time', 'near-real-time', 'end-to-end', 'point-to-point'
    }

    missing_in_registry = {t for t in missing_in_registry if t not in common_words and len(t) > 5}

    # Build detailed analysis
    audit_results = []

    # Check each artifact type
    all_types = declared_types | referenced_types

    for artifact_type in sorted(all_types):
        result = {
            'artifact_type': artifact_type,
            'in_registry': artifact_type in declared_types,
            'has_description': artifact_type in descriptions,
            'skill_references': len(skill_refs.get(artifact_type, [])),
            'agent_references': len(agent_refs.get(artifact_type, [])),
            'template_files': len(template_refs.get(artifact_type, [])),
            'total_references': (
                len(skill_refs.get(artifact_type, [])) +
                len(agent_refs.get(artifact_type, [])) +
                len(template_refs.get(artifact_type, []))
            ),
            'status': 'ok',
            'fix_applied': False
        }

        # Determine status
        if artifact_type not in declared_types:
            if result['total_references'] > 0:
                result['status'] = 'missing_in_registry'
            else:
                result['status'] = 'unknown'
        elif result['total_references'] == 0:
            result['status'] = 'unused'
        elif not result['has_description']:
            result['status'] = 'missing_description'
        else:
            result['status'] = 'ok'

        # Add reference details
        result['references'] = {
            'skills': skill_refs.get(artifact_type, []),
            'agents': agent_refs.get(artifact_type, []),
            'templates': template_refs.get(artifact_type, [])
        }

        audit_results.append(result)

    # Generate summary
    summary = {
        'total_artifact_types': len(all_types),
        'declared_in_registry': len(declared_types),
        'referenced_in_code': len(referenced_types),
        'with_descriptions': len(descriptions),
        'missing_in_registry': len(missing_in_registry),
        'unused_in_registry': len(unused_in_registry),
        'status_counts': defaultdict(int)
    }

    for result in audit_results:
        summary['status_counts'][result['status']] += 1

    return {
        'summary': summary,
        'missing_in_registry': sorted(missing_in_registry),
        'unused_in_registry': sorted(unused_in_registry),
        'audit_results': audit_results
    }


def generate_registry_json(registry_types: Dict[str, Dict[str, Any]], output_path: Path):
    """Generate artifact_types.json from current registry"""
    logger.info(f"Generating registry JSON file: {output_path}")

    artifact_types = []

    for name, metadata in sorted(registry_types.items()):
        artifact_types.append({
            'name': name,
            'description': metadata.get('description', ''),
            'file_pattern': metadata.get('file_pattern', ''),
            'content_type': metadata.get('content_type', ''),
            'schema': metadata.get('schema', '')
        })

    registry_data = {
        'version': '1.0.0',
        'generated_at': '',  # Will be set when writing
        'artifact_types': artifact_types
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(registry_data, f, indent=2)

    logger.info(f"Generated registry JSON with {len(artifact_types)} types")


def generate_audit_report(analysis: Dict[str, Any], output_path: Path):
    """Generate artifact_registry_audit.json report"""
    logger.info(f"Generating audit report: {output_path}")

    report = {
        'audit_timestamp': '',  # Will be set when writing
        'summary': analysis['summary'],
        'findings': {
            'missing_in_registry': analysis['missing_in_registry'],
            'unused_in_registry': analysis['unused_in_registry']
        },
        'detailed_results': analysis['audit_results']
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)

    logger.info(f"Generated audit report with {len(analysis['audit_results'])} entries")


def print_summary(analysis: Dict[str, Any]):
    """Print human-readable summary"""
    summary = analysis['summary']

    print("\n" + "="*80)
    print("ARTIFACT REGISTRY AUDIT SUMMARY")
    print("="*80)
    print(f"\nTotal artifact types: {summary['total_artifact_types']}")
    print(f"  - Declared in registry: {summary['declared_in_registry']}")
    print(f"  - Referenced in code: {summary['referenced_in_code']}")
    print(f"  - With descriptions: {summary['with_descriptions']}")
    print(f"\nDiscrepancies:")
    print(f"  - Missing in registry: {summary['missing_in_registry']}")
    print(f"  - Unused in registry: {summary['unused_in_registry']}")
    print(f"\nStatus breakdown:")
    for status, count in sorted(summary['status_counts'].items()):
        print(f"  - {status}: {count}")

    if analysis['missing_in_registry']:
        print(f"\nMissing types (first 10): {', '.join(analysis['missing_in_registry'][:10])}")

    if analysis['unused_in_registry']:
        print(f"\nUnused types (first 10): {', '.join(analysis['unused_in_registry'][:10])}")

    print("\n" + "="*80)


def main():
    """Main audit function"""
    logger.info("Starting artifact registry audit...")

    try:
        # Step 1: Extract registry types
        registry_types = extract_registry_types()

        # Step 2: Scan all references
        skill_refs = scan_skill_files()
        agent_refs = scan_agent_files()
        template_refs = scan_template_files()
        descriptions = scan_artifact_descriptions()

        # Step 3: Compare and analyze
        analysis = compare_and_analyze(
            registry_types,
            skill_refs,
            agent_refs,
            template_refs,
            descriptions
        )

        # Step 4: Generate outputs
        registry_dir = Path(BASE_DIR) / "registry"

        generate_registry_json(
            registry_types,
            registry_dir / "artifact_types.json"
        )

        generate_audit_report(
            analysis,
            registry_dir / "artifact_registry_audit.json"
        )

        # Step 5: Print summary
        print_summary(analysis)

        logger.info("Artifact registry audit completed successfully")

        # Return exit code based on findings
        if analysis['summary']['missing_in_registry'] > 0:
            logger.warning(f"Found {analysis['summary']['missing_in_registry']} missing artifact types")
            return 1

        return 0

    except Exception as e:
        logger.error(f"Audit failed: {e}", exc_info=True)
        return 1


if __name__ == '__main__':
    sys.exit(main())
