#!/usr/bin/env python3
"""
Rewrite artifact templates based on their descriptions.

This script reads each artifact description and rewrites its corresponding
template to be more specific, helpful, and aligned with the artifact's purpose.
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import date


class TemplateRewriter:
    def __init__(self, base_dir: str = "."):
        self.base_dir = Path(base_dir)
        self.descriptions_dir = self.base_dir / "artifact_descriptions"
        self.templates_dir = self.base_dir / "templates"
        self.stats = {
            "total_descriptions": 0,
            "templates_rewritten": 0,
            "templates_created": 0,
            "errors": []
        }

    def find_template_path(self, artifact_name: str) -> Optional[Path]:
        """Find the template file path for an artifact."""
        # Search for the template in all subdirectories
        for ext in ['.yaml', '.md']:
            matches = list(self.templates_dir.rglob(f"{artifact_name}{ext}"))
            if matches:
                return matches[0]
        return None

    def parse_description(self, desc_path: Path) -> Dict:
        """Parse artifact description to extract key information."""
        with open(desc_path, 'r') as f:
            content = f.read()

        data = {
            'artifact_name': desc_path.stem,
            'content': content,
            'format': 'markdown',  # default
            'executive_summary': '',
            'purpose': '',
            'scope_in': [],
            'scope_out': [],
            'best_practices': [],
            'fields': [],
            'examples': [],
            'target_audience': {'primary': [], 'secondary': []},
            'quality_criteria': [],
        }

        # Extract format
        format_match = re.search(r'\*\*Format\*\*:\s*(\w+)', content, re.IGNORECASE)
        if format_match:
            fmt = format_match.group(1).lower()
            data['format'] = fmt

        # Extract executive summary
        exec_match = re.search(
            r'## Executive Summary\s*\n\n(.*?)(?=\n##|\Z)',
            content,
            re.DOTALL
        )
        if exec_match:
            data['executive_summary'] = exec_match.group(1).strip()

        # Extract purpose
        purpose_match = re.search(
            r'### Primary Purpose\s*\n\n(.*?)(?=\n###|\n##|\Z)',
            content,
            re.DOTALL
        )
        if purpose_match:
            data['purpose'] = purpose_match.group(1).strip()

        # Extract scope (in scope items)
        scope_in_match = re.search(
            r'\*\*In Scope\*\*:\s*\n(.*?)(?=\n\*\*Out of Scope|\Z)',
            content,
            re.DOTALL
        )
        if scope_in_match:
            items = re.findall(r'^-\s*(.+)$', scope_in_match.group(1), re.MULTILINE)
            data['scope_in'] = [item.strip() for item in items]

        # Extract best practices
        bp_section = re.search(
            r'## Best Practices\s*\n\n(.*?)(?=\n##|\Z)',
            content,
            re.DOTALL
        )
        if bp_section:
            practices = re.findall(r'^\*\*(.+?)\*\*:\s*(.+)$', bp_section.group(1), re.MULTILINE)
            data['best_practices'] = [(title.strip(), desc.strip()) for title, desc in practices]

        # Extract quality criteria
        qc_section = re.search(
            r'## Quality Criteria\s*\n\n.*?\n\n(.*?)(?=\n##|\Z)',
            content,
            re.DOTALL
        )
        if qc_section:
            criteria = re.findall(r'✓\s*\*\*(.+?)\*\*:\s*(.+)$', qc_section.group(1), re.MULTILINE)
            data['quality_criteria'] = [(title.strip(), desc.strip()) for title, desc in criteria]

        # Extract target audience
        primary_match = re.search(
            r'\*\*Primary Audience\*\*:\s*\n(.*?)(?=\n\*\*Secondary|\Z)',
            content,
            re.DOTALL
        )
        if primary_match:
            items = re.findall(r'^-\s*(.+)$', primary_match.group(1), re.MULTILINE)
            data['target_audience']['primary'] = [item.strip() for item in items]

        # Extract YAML/code examples
        yaml_examples = re.findall(r'```(?:yaml|yml)\s*\n(.*?)\n```', content, re.DOTALL)
        data['examples'] = yaml_examples

        return data

    def generate_yaml_template(self, data: Dict) -> str:
        """Generate a YAML template based on artifact description."""
        artifact_name = data['artifact_name']

        template_lines = [
            f"# {artifact_name.replace('-', ' ').title()}",
            f"# See also: artifact_descriptions/{artifact_name}.md for complete guidance",
            "",
        ]

        # Add executive summary as comment if available
        if data['executive_summary']:
            summary = data['executive_summary'].split('\n')[0][:200]
            template_lines.append(f"# {summary}")
            template_lines.append("")

        # Metadata section
        template_lines.extend([
            "metadata:",
            "  # Document Control",
            "  version: \"1.0.0\"  # Semantic versioning (MAJOR.MINOR.PATCH)",
            "  created: \"YYYY-MM-DD\"  # Date this artifact was created",
            "  lastModified: \"YYYY-MM-DD\"  # Date of most recent update",
            "  status: \"Draft\"  # Draft | Review | Approved | Published | Deprecated",
            "",
            "  # Ownership & Accountability",
            "  author: \"Author Name\"  # Primary author of this artifact",
            "  documentOwner: \"Owner Role/Name\"  # Person/role responsible for maintenance",
            "  classification: \"Internal\"  # Public | Internal | Confidential | Restricted",
            "",
        ])

        # Add approvers section
        template_lines.extend([
            "  # Approvals",
            "  approvers:",
            "    - name: \"Approver Name\"",
            "      role: \"Approver Role\"",
            "      approvalDate: null  # Date of approval (YYYY-MM-DD)",
            "",
        ])

        # Add purpose section
        if data['purpose']:
            purpose_short = data['purpose'][:300].replace('\n', ' ')
            template_lines.extend([
                "# PURPOSE",
                f"# {purpose_short}...",
                "",
            ])

        # Main content section
        template_lines.extend([
            "# MAIN CONTENT",
            "# Complete the sections below based on your specific artifact needs",
            "",
        ])

        # Add best practices as comments
        if data['best_practices']:
            template_lines.append("# BEST PRACTICES:")
            for title, desc in data['best_practices'][:5]:  # First 5 practices
                template_lines.append(f"# - {title}: {desc[:100]}")
            template_lines.append("")

        # Content structure
        template_lines.extend([
            "content:",
            "  overview: |",
            "    # Provide a high-level overview of this artifact",
            "    # What is this document about?",
            "    # Why does it exist?",
            "    ",
        ])

        # Add scope-specific fields
        if data['scope_in']:
            template_lines.extend([
                "  scope:",
                "    inScope:",
            ])
            for item in data['scope_in'][:3]:  # First 3 items as examples
                clean_item = item.split(':')[0]  # Take first part before colon
                template_lines.append(f"      - \"{clean_item}\"")
            template_lines.extend([
                "      # Add additional in-scope items",
                "    outOfScope:",
                "      - \"Item explicitly out of scope\"",
                "      # Add additional out-of-scope items",
                "",
            ])

        # Add details section
        template_lines.extend([
            "  details: |",
            "    # Provide detailed information specific to this artifact type",
            "    # Include all necessary technical details",
            "    # Reference the artifact description for required sections",
            "    ",
        ])

        # Quality checklist
        if data['quality_criteria']:
            template_lines.extend([
                "# QUALITY CHECKLIST",
                "# Before finalizing, verify:",
            ])
            for title, desc in data['quality_criteria'][:5]:
                template_lines.append(f"# ✓ {title}: {desc}")
            template_lines.append("")

        # Related documents
        template_lines.extend([
            "relatedDocuments:",
            "  - type: \"Related Artifact Type\"",
            "    path: \"path/to/related/artifact\"",
            "    relationship: \"depends-on | references | supersedes | implements\"",
            "",
        ])

        # Change history
        template_lines.extend([
            "changeHistory:",
            "  - version: \"1.0.0\"",
            "    date: \"YYYY-MM-DD\"",
            "    author: \"Author Name\"",
            "    changes: \"Initial version\"",
        ])

        return '\n'.join(template_lines) + '\n'

    def generate_markdown_template(self, data: Dict) -> str:
        """Generate a Markdown template based on artifact description."""
        artifact_name = data['artifact_name']
        title = artifact_name.replace('-', ' ').title()

        template_lines = [
            f"# {title}",
            "",
            f"> **See also**: `artifact_descriptions/{artifact_name}.md` for complete guidance",
            "",
            "## Document Control",
            "",
            "| Field | Value |",
            "|-------|-------|",
            "| **Version** | 1.0.0 |",
            "| **Status** | Draft |",
            "| **Created** | YYYY-MM-DD |",
            "| **Last Updated** | YYYY-MM-DD |",
            "| **Author** | Author Name |",
            "| **Owner** | Owner Name/Role |",
            "| **Classification** | Internal |",
            "",
        ]

        # Add executive summary
        if data['executive_summary']:
            template_lines.extend([
                "## Executive Summary",
                "",
                "<!-- Provide a 2-3 paragraph overview for executive audience -->",
                "<!-- What is this document about and why does it matter? -->",
                "",
            ])

        # Purpose and scope
        if data['purpose']:
            template_lines.extend([
                "## Purpose",
                "",
                f"<!-- {data['purpose'][:200]}... -->",
                "",
            ])

        if data['scope_in']:
            template_lines.extend([
                "## Scope",
                "",
                "### In Scope",
                "",
            ])
            for item in data['scope_in'][:5]:
                clean_item = item.split(':')[0]
                template_lines.append(f"- {clean_item}")
            template_lines.extend([
                "",
                "### Out of Scope",
                "",
                "- Items explicitly not covered by this artifact",
                "",
            ])

        # Target audience
        if data['target_audience']['primary']:
            template_lines.extend([
                "## Target Audience",
                "",
                "### Primary Audience",
                "",
            ])
            for audience in data['target_audience']['primary'][:3]:
                template_lines.append(f"- {audience}")
            template_lines.extend([
                "",
                "### Secondary Audience",
                "",
                "- Additional stakeholders who may reference this document",
                "",
            ])

        # Main content sections
        template_lines.extend([
            "## [Main Section 1]",
            "",
            "<!-- Complete this section with artifact-specific content -->",
            "<!-- Refer to the artifact description for required structure -->",
            "",
            "## [Main Section 2]",
            "",
            "<!-- Add additional sections as needed -->",
            "",
        ])

        # Best practices
        if data['best_practices']:
            template_lines.extend([
                "## Best Practices",
                "",
            ])
            for title, desc in data['best_practices'][:5]:
                template_lines.append(f"**{title}**: {desc}")
                template_lines.append("")

        # Quality checklist
        if data['quality_criteria']:
            template_lines.extend([
                "## Quality Checklist",
                "",
                "Before finalizing this artifact, verify:",
                "",
            ])
            for title, desc in data['quality_criteria'][:5]:
                template_lines.append(f"- [ ] **{title}**: {desc}")
            template_lines.append("")

        # Related documents
        template_lines.extend([
            "## Related Documents",
            "",
            "- [Related Artifact]: Description and relationship",
            "",
        ])

        # Approvals
        template_lines.extend([
            "## Approvals",
            "",
            "| Role | Name | Date | Status |",
            "|------|------|------|--------|",
            "| Approver | Name | YYYY-MM-DD | Pending |",
            "",
        ])

        # Document history
        template_lines.extend([
            "---",
            "",
            "## Document History",
            "",
            "| Version | Date | Author | Changes |",
            "|---------|------|--------|---------|",
            "| 1.0.0 | YYYY-MM-DD | Author Name | Initial version |",
        ])

        return '\n'.join(template_lines) + '\n'

    def rewrite_template(self, desc_path: Path) -> bool:
        """Rewrite a single template based on its description."""
        try:
            # Parse description
            data = self.parse_description(desc_path)
            artifact_name = data['artifact_name']

            print(f"Processing: {artifact_name}")

            # Find template path
            template_path = self.find_template_path(artifact_name)

            if not template_path:
                print(f"  ⚠ Template not found for {artifact_name}")
                self.stats['errors'].append(f"Template not found: {artifact_name}")
                return False

            # Determine format based on actual template file extension, not description
            is_yaml = template_path.suffix == '.yaml'

            # Generate new template
            if is_yaml:
                new_content = self.generate_yaml_template(data)
            else:
                new_content = self.generate_markdown_template(data)

            # Write template
            with open(template_path, 'w') as f:
                f.write(new_content)

            print(f"  ✓ Rewrote {template_path.relative_to(self.base_dir)}")
            self.stats['templates_rewritten'] += 1
            return True

        except Exception as e:
            error_msg = f"Error processing {desc_path.name}: {str(e)}"
            print(f"  ✗ {error_msg}")
            self.stats['errors'].append(error_msg)
            return False

    def rewrite_all(self):
        """Rewrite all templates based on their descriptions."""
        desc_files = sorted(self.descriptions_dir.glob("*.md"))
        self.stats['total_descriptions'] = len(desc_files)

        print(f"Found {len(desc_files)} artifact descriptions")
        print("=" * 80)

        for desc_file in desc_files:
            self.rewrite_template(desc_file)

        # Print summary
        print("\n" + "=" * 80)
        print("SUMMARY")
        print("=" * 80)
        print(f"Total descriptions: {self.stats['total_descriptions']}")
        print(f"Templates rewritten: {self.stats['templates_rewritten']}")
        print(f"Errors: {len(self.stats['errors'])}")

        if self.stats['errors']:
            print("\nErrors encountered:")
            for error in self.stats['errors'][:10]:  # Show first 10 errors
                print(f"  - {error}")
            if len(self.stats['errors']) > 10:
                print(f"  ... and {len(self.stats['errors']) - 10} more")

        return self.stats


def main():
    rewriter = TemplateRewriter()
    stats = rewriter.rewrite_all()

    # Exit with error code if there were errors
    if stats['errors']:
        exit(1)
    else:
        exit(0)


if __name__ == "__main__":
    main()
