#!/usr/bin/env python3
"""
Registry Validation Skill for Betty Framework

Validates registry files for schema compliance, consistency, and completeness.
Provides dry-run mode to test changes before committing.

Usage:
    python registry_validate.py --registry_files '["registry/skills.json"]'
"""

import argparse
import json
import logging
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

try:
    from pydantic import ValidationError
except ImportError:
    print("Error: pydantic not installed. Run: pip install pydantic", file=sys.stderr)
    sys.exit(1)

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

try:
    from betty.models import SkillManifest
except ImportError:
    # If betty.models not available, define minimal version
    class SkillManifest:
        pass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class RegistryValidator:
    """Validates Betty Framework registry files."""

    def __init__(self):
        self.errors: List[Dict[str, Any]] = []
        self.warnings: List[Dict[str, Any]] = []
        self.suggestions: List[str] = []
        self.artifact_types_cache: Dict[str, Any] = {}

    def add_error(self, file: str, item: str, field: str, message: str):
        """Add an error to the error list."""
        self.errors.append({
            'file': file,
            'item': item,
            'field': field,
            'message': message,
            'severity': 'error'
        })
        logger.error(f"❌ {file} - {item}.{field}: {message}")

    def add_warning(self, file: str, item: str, field: str, message: str):
        """Add a warning to the warning list."""
        self.warnings.append({
            'file': file,
            'item': item,
            'field': field,
            'message': message,
            'severity': 'warning'
        })
        logger.warning(f"⚠️  {file} - {item}.{field}: {message}")

    def add_suggestion(self, suggestion: str):
        """Add a suggestion for improvement."""
        self.suggestions.append(suggestion)

    def load_artifact_types(self, artifact_types_path: str = "registry/artifact_types.json") -> Dict[str, Any]:
        """Load artifact types registry."""
        if self.artifact_types_cache:
            return self.artifact_types_cache

        try:
            with open(artifact_types_path, 'r') as f:
                registry = json.load(f)
                self.artifact_types_cache = {
                    artifact['name']: artifact
                    for artifact in registry.get('artifact_types', [])
                }
                return self.artifact_types_cache
        except FileNotFoundError:
            logger.warning(f"Artifact types registry not found: {artifact_types_path}")
            return {}
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in artifact types registry: {e}")
            return {}

    def validate_json_syntax(self, file_path: str) -> Tuple[bool, Any]:
        """Validate JSON syntax and load data."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            return True, data
        except FileNotFoundError:
            self.add_error(file_path, 'file', 'existence', 'File not found')
            return False, None
        except json.JSONDecodeError as e:
            self.add_error(file_path, 'file', 'syntax', f'Invalid JSON: {e}')
            return False, None

    def validate_skill(self, skill: Dict[str, Any], file_path: str):
        """Validate a single skill against SkillManifest schema."""
        skill_name = skill.get('name', '<unknown>')

        # Check required fields
        required_fields = ['name', 'version', 'description', 'inputs', 'outputs', 'status']
        for field in required_fields:
            if field not in skill:
                self.add_error(file_path, skill_name, field, f'Missing required field: {field}')

        # Validate with Pydantic if available
        if SkillManifest != type:  # Check if we have real SkillManifest
            try:
                SkillManifest(**skill)
            except ValidationError as e:
                for error in e.errors():
                    field = '.'.join(str(loc) for loc in error['loc'])
                    self.add_error(file_path, skill_name, field, error['msg'])
            except Exception as e:
                self.add_warning(file_path, skill_name, 'validation', f'Could not validate with Pydantic: {e}')

    def validate_artifact_references(
        self,
        skill: Dict[str, Any],
        file_path: str,
        artifact_types: Dict[str, Any]
    ):
        """Validate artifact type references in skill."""
        skill_name = skill.get('name', '<unknown>')

        if 'artifact_metadata' not in skill:
            return

        metadata = skill['artifact_metadata']

        # Validate produces
        for artifact in metadata.get('produces', []):
            artifact_type = artifact.get('type')
            if artifact_type and artifact_type not in artifact_types:
                self.add_error(
                    file_path,
                    skill_name,
                    f'artifact_metadata.produces.type',
                    f'Unknown artifact type: {artifact_type}'
                )

        # Validate consumes
        for artifact in metadata.get('consumes', []):
            if isinstance(artifact, dict):
                artifact_type = artifact.get('type')
            else:
                artifact_type = artifact  # String format

            if artifact_type and artifact_type not in artifact_types:
                self.add_error(
                    file_path,
                    skill_name,
                    f'artifact_metadata.consumes.type',
                    f'Unknown artifact type: {artifact_type}'
                )

    def validate_file_paths(self, skill: Dict[str, Any], file_path: str):
        """Validate that referenced files exist."""
        skill_name = skill.get('name', '<unknown>')

        # Check entrypoint handlers
        for entrypoint in skill.get('entrypoints', []):
            handler = entrypoint.get('handler')
            if handler:
                handler_path = f"skills/{skill_name}/{handler}"
                if not os.path.exists(handler_path):
                    self.add_error(
                        file_path,
                        skill_name,
                        'entrypoints.handler',
                        f'Handler file not found: {handler_path}'
                    )

        # Check schemas in artifact_metadata
        if 'artifact_metadata' in skill:
            for artifact in skill['artifact_metadata'].get('produces', []):
                schema = artifact.get('schema')
                if schema and not os.path.exists(schema):
                    self.add_warning(
                        file_path,
                        skill_name,
                        'artifact_metadata.produces.schema',
                        f'Schema file not found: {schema}'
                    )

    def detect_duplicates(self, items: List[Dict[str, Any]], file_path: str, item_type: str):
        """Detect duplicate names/versions in registry."""
        seen = {}
        for item in items:
            name = item.get('name', '<unknown>')
            version = item.get('version', '<unknown>')
            key = f"{name}:{version}"

            if key in seen:
                self.add_error(
                    file_path,
                    name,
                    'name+version',
                    f'Duplicate {item_type}: {key}'
                )
            seen[key] = True

    def detect_circular_dependencies(self, skills: List[Dict[str, Any]], file_path: str):
        """Detect circular dependencies between skills."""
        # Build dependency graph
        graph: Dict[str, Set[str]] = defaultdict(set)

        for skill in skills:
            skill_name = skill.get('name')
            if not skill_name:
                continue

            # Check dependencies field
            for dep in skill.get('dependencies', []):
                if '/' not in dep:  # Not a Python package, might be skill dependency
                    graph[skill_name].add(dep)

        # Find cycles using DFS
        visited = set()
        rec_stack = set()
        cycles = []

        def dfs(node: str, path: List[str]):
            visited.add(node)
            rec_stack.add(node)
            path.append(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor, path.copy()):
                        return True
                elif neighbor in rec_stack:
                    cycle_start = path.index(neighbor)
                    cycles.append(path[cycle_start:] + [neighbor])
                    return True

            rec_stack.remove(node)
            return False

        for skill_name in graph.keys():
            if skill_name not in visited:
                dfs(skill_name, [])

        if cycles:
            for cycle in cycles:
                cycle_str = ' → '.join(cycle)
                self.add_error(
                    file_path,
                    cycle[0],
                    'dependencies',
                    f'Circular dependency: {cycle_str}'
                )

    def validate_skills_registry(
        self,
        file_path: str,
        check_file_paths: bool,
        check_artifacts: bool,
        check_dependencies: bool
    ) -> Dict[str, Any]:
        """Validate skills.json registry."""
        logger.info(f"Validating skills registry: {file_path}")

        # Load and validate JSON
        valid, data = self.validate_json_syntax(file_path)
        if not valid:
            return {'valid': False, 'skill_count': 0}

        skills = data.get('skills', [])

        # Load artifact types if needed
        artifact_types = {}
        if check_artifacts:
            artifact_types = self.load_artifact_types()

        # Detect duplicates
        self.detect_duplicates(skills, file_path, 'skill')

        # Validate each skill
        skills_with_artifacts = 0
        skills_with_tests = 0

        for skill in skills:
            # Basic validation
            self.validate_skill(skill, file_path)

            # Artifact reference validation
            if check_artifacts and 'artifact_metadata' in skill:
                self.validate_artifact_references(skill, file_path, artifact_types)
                skills_with_artifacts += 1

            # File path validation
            if check_file_paths:
                self.validate_file_paths(skill, file_path)

            # Check for tests
            skill_name = skill.get('name', '')
            test_path = f"skills/{skill_name}/test_{skill_name.replace('.', '_')}.py"
            if os.path.exists(test_path):
                skills_with_tests += 1

        # Check circular dependencies
        if check_dependencies:
            self.detect_circular_dependencies(skills, file_path)

        # Generate suggestions
        if skills_with_tests < len(skills) / 2:
            self.add_suggestion(f"{len(skills) - skills_with_tests} skills missing test coverage")

        if skills_with_artifacts < len(skills) / 2:
            self.add_suggestion(f"{len(skills) - skills_with_artifacts} skills missing artifact_metadata")

        return {
            'valid': True,
            'skill_count': len(skills),
            'skills_with_artifacts': skills_with_artifacts,
            'skills_with_tests': skills_with_tests
        }

    def validate_agents_registry(self, file_path: str) -> Dict[str, Any]:
        """Validate agents.json registry."""
        logger.info(f"Validating agents registry: {file_path}")

        # Load and validate JSON
        valid, data = self.validate_json_syntax(file_path)
        if not valid:
            return {'valid': False, 'agent_count': 0}

        agents = data.get('agents', [])

        # Detect duplicates
        self.detect_duplicates(agents, file_path, 'agent')

        # Validate each agent
        for agent in agents:
            agent_name = agent.get('name', '<unknown>')

            # Check required fields
            required_fields = ['name', 'version', 'description', 'reasoning_mode']
            for field in required_fields:
                if field not in agent:
                    self.add_error(file_path, agent_name, field, f'Missing required field: {field}')

        return {
            'valid': True,
            'agent_count': len(agents)
        }

    def validate_artifact_types_registry(self, file_path: str) -> Dict[str, Any]:
        """Validate artifact_types.json registry."""
        logger.info(f"Validating artifact types registry: {file_path}")

        # Load and validate JSON
        valid, data = self.validate_json_syntax(file_path)
        if not valid:
            return {'valid': False, 'artifact_type_count': 0}

        artifact_types = data.get('artifact_types', [])

        # Detect duplicates
        self.detect_duplicates(artifact_types, file_path, 'artifact type')

        # Validate each artifact type
        for artifact_type in artifact_types:
            type_name = artifact_type.get('name', '<unknown>')

            # Check required fields
            required_fields = ['name', 'file_pattern', 'content_type']
            for field in required_fields:
                if field not in artifact_type:
                    self.add_error(file_path, type_name, field, f'Missing required field: {field}')

        return {
            'valid': True,
            'artifact_type_count': len(artifact_types)
        }


def validate_registries(
    registry_files: List[str],
    check_file_paths: bool = True,
    check_artifacts: bool = True,
    check_dependencies: bool = True,
    strict_mode: bool = False,
    output_format: str = "detailed"
) -> Dict[str, Any]:
    """
    Validate Betty Framework registry files.

    Args:
        registry_files: List of registry file paths
        check_file_paths: Whether to verify referenced files exist
        check_artifacts: Whether to validate artifact type references
        check_dependencies: Whether to check for circular dependencies
        strict_mode: Whether to treat warnings as errors
        output_format: Output format ("json", "summary", "detailed")

    Returns:
        Validation results dictionary
    """
    validator = RegistryValidator()
    validation_results = {}
    start_time = datetime.now(timezone.utc)

    for file_path in registry_files:
        if 'skills.json' in file_path:
            result = validator.validate_skills_registry(
                file_path, check_file_paths, check_artifacts, check_dependencies
            )
        elif 'agents.json' in file_path:
            result = validator.validate_agents_registry(file_path)
        elif 'artifact_types.json' in file_path:
            result = validator.validate_artifact_types_registry(file_path)
        else:
            logger.warning(f"Unknown registry type: {file_path}")
            continue

        # Add timing info
        result['validated_at'] = datetime.now(timezone.utc).isoformat()

        # Add errors/warnings for this file
        file_errors = [e for e in validator.errors if e['file'] == file_path]
        file_warnings = [w for w in validator.warnings if w['file'] == file_path]

        result['errors'] = file_errors
        result['warnings'] = file_warnings
        result['valid'] = len(file_errors) == 0 and (not strict_mode or len(file_warnings) == 0)

        validation_results[file_path] = result

    # Calculate stats
    end_time = datetime.now(timezone.utc)
    validation_time_ms = int((end_time - start_time).total_seconds() * 1000)

    stats = {
        'validation_time_ms': validation_time_ms
    }

    # Aggregate counts
    for result in validation_results.values():
        for key in ['skill_count', 'agent_count', 'artifact_type_count']:
            if key in result:
                stats_key = key.replace('_count', 's')  # skill_count → skills
                stats[f'total_{stats_key}'] = stats.get(f'total_{stats_key}', 0) + result[key]

    # Overall validity
    all_valid = all(result['valid'] for result in validation_results.values())

    if strict_mode and validator.warnings:
        all_valid = False

    return {
        'valid': all_valid,
        'validation_results': validation_results,
        'errors': validator.errors,
        'warnings': validator.warnings,
        'suggestions': validator.suggestions,
        'stats': stats
    }


def format_output(result: Dict[str, Any], output_format: str) -> str:
    """Format validation result based on output_format."""
    if output_format == "json":
        return json.dumps(result, indent=2)

    elif output_format == "summary":
        lines = ["=== Registry Validation Summary ===\n"]

        for file_path, file_result in result['validation_results'].items():
            status = "✅ Valid" if file_result['valid'] else "❌ Invalid"
            error_count = len(file_result.get('errors', []))
            warning_count = len(file_result.get('warnings', []))

            lines.append(f"{status} {file_path}")
            if 'skill_count' in file_result:
                lines.append(f"  Skills: {file_result['skill_count']}")
            if 'agent_count' in file_result:
                lines.append(f"  Agents: {file_result['agent_count']}")
            if 'artifact_type_count' in file_result:
                lines.append(f"  Artifact Types: {file_result['artifact_type_count']}")

            if error_count:
                lines.append(f"  Errors: {error_count}")
            if warning_count:
                lines.append(f"  Warnings: {warning_count}")
            lines.append("")

        overall = "✅ PASSED" if result['valid'] else "❌ FAILED"
        lines.append(f"Overall: {overall}")
        lines.append(f"Validation time: {result['stats']['validation_time_ms']}ms")

        return '\n'.join(lines)

    else:  # detailed
        lines = ["=== Registry Validation Report ===\n"]

        for file_path, file_result in result['validation_results'].items():
            status = "✅ Valid" if file_result['valid'] else "❌ Invalid"
            lines.append(f"{file_path}: {status}")

            # Show errors
            for error in file_result.get('errors', []):
                lines.append(f"  ❌ {error['item']}.{error['field']}: {error['message']}")

            # Show warnings
            for warning in file_result.get('warnings', []):
                lines.append(f"  ⚠️  {warning['item']}.{warning['field']}: {warning['message']}")

            lines.append("")

        # Show suggestions
        if result['suggestions']:
            lines.append("Suggestions:")
            for suggestion in result['suggestions']:
                lines.append(f"  💡 {suggestion}")
            lines.append("")

        overall = "✅ PASSED" if result['valid'] else "❌ FAILED"
        lines.append(f"Overall: {overall}")
        lines.append(f"Time: {result['stats']['validation_time_ms']}ms")

        return '\n'.join(lines)


def main():
    """Main entry point for registry.validate skill."""
    parser = argparse.ArgumentParser(
        description="Validate Betty Framework registry files"
    )

    parser.add_argument(
        '--registry_files',
        type=str,
        required=True,
        help='JSON array of registry file paths (e.g., \'["registry/skills.json"]\')'
    )

    parser.add_argument(
        '--check_file_paths',
        type=lambda x: x.lower() == 'true',
        default=True,
        help='Whether to verify referenced files exist (default: true)'
    )

    parser.add_argument(
        '--check_artifacts',
        type=lambda x: x.lower() == 'true',
        default=True,
        help='Whether to validate artifact type references (default: true)'
    )

    parser.add_argument(
        '--check_dependencies',
        type=lambda x: x.lower() == 'true',
        default=True,
        help='Whether to check for circular dependencies (default: true)'
    )

    parser.add_argument(
        '--strict_mode',
        type=lambda x: x.lower() == 'true',
        default=False,
        help='Whether to treat warnings as errors (default: false)'
    )

    parser.add_argument(
        '--output_format',
        type=str,
        default='detailed',
        choices=['json', 'summary', 'detailed'],
        help='Output format (default: detailed)'
    )

    parser.add_argument(
        '--output',
        type=str,
        help='Output file path for validation report (optional)'
    )

    args = parser.parse_args()

    try:
        # Parse registry_files JSON
        registry_files = json.loads(args.registry_files)

        if not isinstance(registry_files, list):
            logger.error("registry_files must be a JSON array")
            sys.exit(1)

        logger.info(f"Validating {len(registry_files)} registry files...")

        # Perform validation
        result = validate_registries(
            registry_files=registry_files,
            check_file_paths=args.check_file_paths,
            check_artifacts=args.check_artifacts,
            check_dependencies=args.check_dependencies,
            strict_mode=args.strict_mode,
            output_format=args.output_format
        )

        # Add status for JSON output
        result['ok'] = result['valid']
        result['status'] = 'success' if result['valid'] else 'validation_failed'

        # Format output
        output = format_output(result, args.output_format)

        # Save to file if specified
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            if args.output_format == 'json':
                with open(output_path, 'w') as f:
                    json.dump(result, f, indent=2)
            else:
                with open(output_path, 'w') as f:
                    f.write(output)

            logger.info(f"Validation report saved to: {output_path}")
            result['validation_report_path'] = str(output_path)

        # Print output
        print(output)

        # Exit with appropriate code
        sys.exit(0 if result['valid'] else 1)

    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in registry_files parameter: {e}")
        print(json.dumps({
            'ok': False,
            'status': 'error',
            'error': f'Invalid JSON: {str(e)}'
        }, indent=2))
        sys.exit(1)

    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        print(json.dumps({
            'ok': False,
            'status': 'error',
            'error': str(e)
        }, indent=2))
        sys.exit(1)


if __name__ == '__main__':
    main()
