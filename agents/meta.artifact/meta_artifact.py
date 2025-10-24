#!/usr/bin/env python3
"""
meta.artifact - The Artifact Standards Authority

THE single source of truth for all artifact type definitions in Betty Framework.
Manages schemas, documentation, and registry for all artifact types.
"""

import json
import yaml
import sys
import os
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime

# Add parent directory to path for imports
parent_dir = str(Path(__file__).parent.parent.parent)
sys.path.insert(0, parent_dir)


class ArtifactAuthority:
    """The artifact standards authority - manages all artifact type definitions"""

    def __init__(self, base_dir: str = "."):
        """Initialize with base directory"""
        self.base_dir = Path(base_dir)
        self.standards_doc = self.base_dir / "docs" / "ARTIFACT_STANDARDS.md"
        self.schemas_dir = self.base_dir / "schemas"
        self.artifact_define = self.base_dir / "skills" / "artifact.define" / "artifact_define.py"

    def parse_description(self, description_path: str) -> Dict[str, Any]:
        """
        Parse artifact type description from Markdown or JSON file

        Args:
            description_path: Path to artifact_type_description.md or .json

        Returns:
            Parsed description with all artifact metadata
        """
        path = Path(description_path)

        if not path.exists():
            raise FileNotFoundError(f"Description not found: {description_path}")

        # Handle JSON format
        if path.suffix == ".json":
            with open(path) as f:
                return json.load(f)

        # Handle Markdown format
        with open(path) as f:
            content = f.read()

        # Parse Markdown sections
        description = {
            "name": "",
            "purpose": "",
            "format": "",
            "file_pattern": "",
            "content_type": "",
            "schema_properties": {},
            "required_fields": [],
            "producers": [],
            "consumers": [],
            "examples": [],
            "validation_rules": [],
            "related_types": []
        }

        current_section = None
        for line in content.split('\n'):
            line = line.strip()

            # Section headers
            if line.startswith('# Name:'):
                description["name"] = line.replace('# Name:', '').strip()
            elif line.startswith('# Purpose:'):
                current_section = "purpose"
            elif line.startswith('# Format:'):
                description["format"] = line.replace('# Format:', '').strip()
            elif line.startswith('# File Pattern:'):
                description["file_pattern"] = line.replace('# File Pattern:', '').strip()
            elif line.startswith('# Content Type:'):
                description["content_type"] = line.replace('# Content Type:', '').strip()
            elif line.startswith('# Schema Properties:'):
                current_section = "schema_properties"
            elif line.startswith('# Required Fields:'):
                current_section = "required_fields"
            elif line.startswith('# Producers:'):
                current_section = "producers"
            elif line.startswith('# Consumers:'):
                current_section = "consumers"
            elif line.startswith('# Examples:'):
                current_section = "examples"
            elif line.startswith('# Validation Rules:'):
                current_section = "validation_rules"
            elif line.startswith('# Related Types:'):
                current_section = "related_types"
            elif line and not line.startswith('#'):
                # Content for current section
                if current_section == "purpose":
                    description["purpose"] += line + " "
                elif current_section in ["producers", "consumers", "required_fields",
                                         "validation_rules", "related_types"] and line.startswith('-'):
                    description[current_section].append(line[1:].strip())
                elif current_section == "schema_properties" and line.startswith('-'):
                    # Parse property definitions like: "- optimizations (array): List of optimizations"
                    match = re.match(r'-\s+(\w+)\s+\((\w+)\):\s*(.+)', line)
                    if match:
                        prop_name, prop_type, prop_desc = match.groups()
                        description["schema_properties"][prop_name] = {
                            "type": prop_type,
                            "description": prop_desc
                        }

        description["purpose"] = description["purpose"].strip()

        # Infer content_type from format if not specified
        if not description["content_type"] and description["format"]:
            format_to_mime = {
                "JSON": "application/json",
                "YAML": "application/yaml",
                "Markdown": "text/markdown",
                "Python": "text/x-python",
                "TypeScript": "text/x-typescript",
                "Go": "text/x-go",
                "Text": "text/plain"
            }
            description["content_type"] = format_to_mime.get(description["format"], "")

        return description

    def check_existence(self, artifact_name: str) -> Tuple[bool, Optional[str]]:
        """
        Check if artifact type already exists

        Args:
            artifact_name: Name of artifact type to check

        Returns:
            Tuple of (exists: bool, location: Optional[str])
        """
        # Check in ARTIFACT_STANDARDS.md
        if self.standards_doc.exists():
            with open(self.standards_doc) as f:
                content = f.read()
                if f"`{artifact_name}`" in content or f"({artifact_name})" in content:
                    return True, str(self.standards_doc)

        # Check in schemas directory
        schema_file = self.schemas_dir / f"{artifact_name}.json"
        if schema_file.exists():
            return True, str(schema_file)

        # Check in KNOWN_ARTIFACT_TYPES
        if self.artifact_define.exists():
            with open(self.artifact_define) as f:
                content = f.read()
                if f'"{artifact_name}"' in content:
                    return True, str(self.artifact_define)

        return False, None

    def generate_json_schema(
        self,
        artifact_desc: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate JSON Schema from artifact description

        Args:
            artifact_desc: Parsed artifact description

        Returns:
            JSON Schema dictionary
        """
        schema = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "title": artifact_desc["name"].replace("-", " ").title(),
            "description": artifact_desc["purpose"],
            "type": "object"
        }

        # Add required fields
        if artifact_desc.get("required_fields"):
            schema["required"] = artifact_desc["required_fields"]

        # Add properties from schema_properties
        if artifact_desc.get("schema_properties"):
            schema["properties"] = {}
            for prop_name, prop_info in artifact_desc["schema_properties"].items():
                prop_schema = {}

                # Map simple types to JSON Schema types
                type_mapping = {
                    "string": "string",
                    "number": "number",
                    "integer": "integer",
                    "boolean": "boolean",
                    "array": "array",
                    "object": "object"
                }

                prop_type = prop_info.get("type", "string").lower()
                prop_schema["type"] = type_mapping.get(prop_type, "string")

                if "description" in prop_info:
                    prop_schema["description"] = prop_info["description"]

                schema["properties"][prop_name] = prop_schema

        # Add examples if provided
        if artifact_desc.get("examples"):
            schema["examples"] = artifact_desc["examples"]

        return schema

    def update_standards_doc(self, artifact_desc: Dict[str, Any]) -> None:
        """
        Update ARTIFACT_STANDARDS.md with new artifact type

        Args:
            artifact_desc: Parsed artifact description
        """
        if not self.standards_doc.exists():
            raise FileNotFoundError(f"Standards document not found: {self.standards_doc}")

        with open(self.standards_doc) as f:
            content = f.read()

        # Find the "## Artifact Types" section
        artifact_types_match = re.search(r'## Artifact Types\n', content)
        if not artifact_types_match:
            raise ValueError("Could not find '## Artifact Types' section in standards doc")

        # Find where to insert (before "## Artifact Metadata Schema" or at end)
        insert_before_match = re.search(r'\n## Artifact Metadata Schema\n', content)

        # Generate new section
        artifact_name = artifact_desc["name"]
        section_number = self._get_next_artifact_number(content)

        new_section = f"""
### {section_number}. {artifact_name.replace('-', ' ').title()} (`{artifact_name}`)

**Description:** {artifact_desc["purpose"]}

**Convention:**
- File pattern: `{artifact_desc.get("file_pattern", f"*.{artifact_name}.{artifact_desc['format'].lower()}")}`
- Format: {artifact_desc["format"]}
"""

        if artifact_desc.get("content_type"):
            new_section += f"- Content type: {artifact_desc['content_type']}\n"

        if artifact_desc.get("schema_properties"):
            new_section += f"\n**Schema:** `schemas/{artifact_name}.json`\n"

        if artifact_desc.get("producers"):
            new_section += "\n**Produced by:**\n"
            for producer in artifact_desc["producers"]:
                new_section += f"- `{producer}`\n"

        if artifact_desc.get("consumers"):
            new_section += "\n**Consumed by:**\n"
            for consumer in artifact_desc["consumers"]:
                new_section += f"- `{consumer}`\n"

        if artifact_desc.get("related_types"):
            new_section += "\n**Related types:**\n"
            for related in artifact_desc["related_types"]:
                new_section += f"- `{related}`\n"

        new_section += "\n---\n"

        # Insert the new section
        if insert_before_match:
            insert_pos = insert_before_match.start()
        else:
            insert_pos = len(content)

        updated_content = content[:insert_pos] + new_section + content[insert_pos:]

        # Update Quick Reference table
        updated_content = self._update_quick_reference(updated_content, artifact_desc)

        # Write back
        with open(self.standards_doc, 'w') as f:
            f.write(updated_content)

    def _get_next_artifact_number(self, standards_content: str) -> int:
        """Get the next artifact type number for documentation"""
        # Find all artifact type sections like "### 1. ", "### 2. ", etc.
        matches = re.findall(r'### (\d+)\. .+? \(`[\w-]+`\)', standards_content)
        if matches:
            return max(int(m) for m in matches) + 1
        return 1

    def _update_quick_reference(
        self,
        content: str,
        artifact_desc: Dict[str, Any]
    ) -> str:
        """Update the Quick Reference table with new artifact type"""
        # Find the Quick Reference table
        table_match = re.search(
            r'\| Artifact Type \| File Pattern \| Schema \| Producers \| Consumers \|.*?\n\|.*?\n((?:\|.*?\n)*)',
            content,
            re.DOTALL
        )

        if not table_match:
            return content

        artifact_name = artifact_desc["name"]
        file_pattern = artifact_desc.get("file_pattern", f"*.{artifact_name}.{artifact_desc['format'].lower()}")
        schema = f"schemas/{artifact_name}.json" if artifact_desc.get("schema_properties") else "-"
        producers = ", ".join(artifact_desc.get("producers", [])) or "-"
        consumers = ", ".join(artifact_desc.get("consumers", [])) or "-"

        new_row = f"| {artifact_name} | {file_pattern} | {schema} | {producers} | {consumers} |\n"

        # Insert before the end of the table
        table_end = table_match.end()
        return content[:table_end] + new_row + content[table_end:]

    def update_registry(self, artifact_desc: Dict[str, Any]) -> None:
        """
        Update KNOWN_ARTIFACT_TYPES in artifact_define.py

        Args:
            artifact_desc: Parsed artifact description
        """
        if not self.artifact_define.exists():
            raise FileNotFoundError(f"Artifact registry not found: {self.artifact_define}")

        with open(self.artifact_define) as f:
            content = f.read()

        # Find KNOWN_ARTIFACT_TYPES dictionary
        match = re.search(r'KNOWN_ARTIFACT_TYPES = \{', content)
        if not match:
            raise ValueError("Could not find KNOWN_ARTIFACT_TYPES in artifact_define.py")

        artifact_name = artifact_desc["name"]

        # Generate new entry
        entry = f'    "{artifact_name}": {{\n'

        if artifact_desc.get("schema_properties"):
            entry += f'        "schema": "schemas/{artifact_name}.json",\n'

        file_pattern = artifact_desc.get("file_pattern")
        if file_pattern:
            entry += f'        "file_pattern": "{file_pattern}",\n'

        if artifact_desc.get("content_type"):
            entry += f'        "content_type": "{artifact_desc["content_type"]}",\n'

        entry += f'        "description": "{artifact_desc["purpose"]}"\n'
        entry += '    },\n'

        # Find the end of the dictionary (last closing brace before the closing of KNOWN_ARTIFACT_TYPES)
        # Insert before the last }
        closing_brace_match = list(re.finditer(r'\n\}', content))
        if closing_brace_match:
            # Find the one that's part of KNOWN_ARTIFACT_TYPES
            # This is a bit tricky, but we'll insert before the last } in the KNOWN_ARTIFACT_TYPES section
            insert_pos = closing_brace_match[0].start()

            # Insert the new entry
            updated_content = content[:insert_pos] + entry + content[insert_pos:]

            # Write back
            with open(self.artifact_define, 'w') as f:
                f.write(updated_content)

    def create_artifact_type(
        self,
        description_path: str,
        force: bool = False
    ) -> Dict[str, Any]:
        """
        Create a new artifact type from description

        Args:
            description_path: Path to artifact description file
            force: Force creation even if type exists

        Returns:
            Summary of created files and changes
        """
        # Parse description
        artifact_desc = self.parse_description(description_path)
        artifact_name = artifact_desc["name"]

        # Validate name format (kebab-case)
        if not re.match(r'^[a-z0-9-]+$', artifact_name):
            raise ValueError(
                f"Artifact name must be kebab-case (lowercase with hyphens): {artifact_name}"
            )

        # Check existence
        exists, location = self.check_existence(artifact_name)
        if exists and not force:
            raise ValueError(
                f"Artifact type '{artifact_name}' already exists at: {location}\n"
                f"Use --force to overwrite."
            )

        result = {
            "artifact_name": artifact_name,
            "created_files": [],
            "updated_files": [],
            "errors": []
        }

        # Generate and save JSON schema (if applicable)
        if artifact_desc.get("schema_properties") or artifact_desc["format"] in ["JSON", "YAML"]:
            schema = self.generate_json_schema(artifact_desc)
            schema_file = self.schemas_dir / f"{artifact_name}.json"

            self.schemas_dir.mkdir(parents=True, exist_ok=True)
            with open(schema_file, 'w') as f:
                json.dump(schema, f, indent=2)

            result["created_files"].append(str(schema_file))

        # Update ARTIFACT_STANDARDS.md
        try:
            self.update_standards_doc(artifact_desc)
            result["updated_files"].append(str(self.standards_doc))
        except Exception as e:
            result["errors"].append(f"Failed to update standards doc: {e}")

        # Update artifact registry
        try:
            self.update_registry(artifact_desc)
            result["updated_files"].append(str(self.artifact_define))
        except Exception as e:
            result["errors"].append(f"Failed to update registry: {e}")

        return result


def main():
    """CLI entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="meta.artifact - The Artifact Standards Authority"
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Create command
    create_parser = subparsers.add_parser('create', help='Create new artifact type')
    create_parser.add_argument(
        "description",
        help="Path to artifact type description file (.md or .json)"
    )
    create_parser.add_argument(
        "--force",
        action="store_true",
        help="Force creation even if type exists"
    )

    # Check command
    check_parser = subparsers.add_parser('check', help='Check if artifact type exists')
    check_parser.add_argument("name", help="Artifact type name")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    authority = ArtifactAuthority()

    if args.command == 'create':
        print(f"🏛️  meta.artifact - Creating artifact type from {args.description}")

        try:
            result = authority.create_artifact_type(args.description, force=args.force)

            print(f"\n✨ Artifact type '{result['artifact_name']}' created successfully!\n")

            if result["created_files"]:
                print("📄 Created files:")
                for file in result["created_files"]:
                    print(f"   - {file}")

            if result["updated_files"]:
                print("\n📝 Updated files:")
                for file in result["updated_files"]:
                    print(f"   - {file}")

            if result["errors"]:
                print("\n⚠️  Warnings:")
                for error in result["errors"]:
                    print(f"   - {error}")

            print(f"\n✅ Artifact type '{result['artifact_name']}' is now registered")
            print("   All agents and skills can now use this artifact type.")

        except Exception as e:
            print(f"\n❌ Error creating artifact type: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == 'check':
        exists, location = authority.check_existence(args.name)

        if exists:
            print(f"✅ Artifact type '{args.name}' exists")
            print(f"   Location: {location}")
        else:
            print(f"❌ Artifact type '{args.name}' does not exist")
            print(f"   Use 'meta.artifact create' to define it")
            sys.exit(1)


if __name__ == "__main__":
    main()
