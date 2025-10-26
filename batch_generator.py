#!/usr/bin/env python3
"""
Batch template generator for all 391 artifacts.
Processes artifacts systematically using industry best practices.
"""
import os
import sys
from pathlib import Path
from datetime import datetime

# Import the category mapping
from generate_templates import CATEGORY_MAPPING, get_category

class ComprehensiveTemplateGenerator:
    """Generates industry-standard templates for all artifact types."""

    def __init__(self):
        self.base_dir = Path('/home/user/betty')
        self.desc_dir = self.base_dir / 'artifact_descriptions'
        self.template_dir = self.base_dir / 'templates'
        self.templates_path = Path(__file__).parent / 'template_library'
        self.generated_count = 0
        self.failed = []

    def read_description(self, artifact_name):
        """Read artifact description."""
        desc_file = self.desc_dir / f"{artifact_name}.md"
        if desc_file.exists():
            return desc_file.read_text()
        return ""

    def determine_format(self, artifact_name):
        """Determine YAML vs MD format."""
        yaml_patterns = [
            'schema', 'spec', 'contract', 'sla', 'slo', 'config',
            'manifest', 'policy', 'matrix', 'catalog', 'registry',
            'model', 'definition', 'dag', 'rules', 'scoring',
            'inventory', 'register', 'schedule', 'proto'
        ]

        for pattern in yaml_patterns:
            if pattern in artifact_name:
                return 'yaml'

        return 'md'

    def save_template(self, artifact_name, content):
        """Save generated template."""
        category = get_category(artifact_name)
        fmt = self.determine_format(artifact_name)

        category_dir = self.template_dir / category
        category_dir.mkdir(parents=True, exist_ok=True)

        output_file = category_dir / f"{artifact_name}.{fmt}"
        output_file.write_text(content)
        return output_file

    def process_artifact(self, artifact_name):
        """Process a single artifact."""
        try:
            description = self.read_description(artifact_name)
            category = get_category(artifact_name)

            # Route to appropriate generator
            template_content = self.route_to_generator(artifact_name, category, description)

            # Save template
            output_file = self.save_template(artifact_name, template_content)
            self.generated_count += 1

            return True, output_file
        except Exception as e:
            self.failed.append((artifact_name, str(e)))
            return False, str(e)

    def route_to_generator(self, name, category, description):
        """Route to appropriate template generator based on artifact type."""

        # Use specialized generators based on patterns
        generators = [
            (lambda n: 'openapi' in n, self.gen_openapi),
            (lambda n: 'asyncapi' in n, self.gen_asyncapi),
            (lambda n: 'graphql' in n, self.gen_graphql),
            (lambda n: 'grpc' in n or 'proto' in n, self.gen_grpc),
            (lambda n: 'threat-model' in n, self.gen_threat_model),
            (lambda n: 'runbook' in n, self.gen_runbook),
            (lambda n: 'data-contract' in n, self.gen_data_contract),
            (lambda n: 'slo' in n or 'service-level' in n, self.gen_slo),
            (lambda n: 'test-plan' in n or 'test-strategy' in n, self.gen_test_plan),
            (lambda n: 'incident' in n and 'report' in n, self.gen_incident_report),
            (lambda n: 'architecture' in n and 'diagram' in n, self.gen_architecture_diagram),
            (lambda n: 'model-card' in n, self.gen_model_card),
            (lambda n: 'sbom' in n or 'bill-of-materials' in n, self.gen_sbom),
            (lambda n: 'dpia' in n or 'privacy-impact' in n, self.gen_dpia),
            (lambda n: 'helm' in n or 'chart' in n, self.gen_helm_chart),
            (lambda n: 'docker' in n, self.gen_dockerfile),
        ]

        for matcher, generator in generators:
            if matcher(name):
                return generator(name, description)

        # Category-based routing
        category_generators = {
            'ai-ml': self.gen_ai_ml,
            'security': self.gen_security,
            'testing': self.gen_testing,
            'data': self.gen_data,
            'operations': self.gen_operations,
            'compliance': self.gen_compliance,
        }

        if category in category_generators:
            return category_generators[category](name, description)

        # Default generator
        return self.gen_generic(name, description)

    # Specialized generators will be added here
    # For now, using imports from external template files

def main():
    """Main batch processing function."""
    generator = ComprehensiveTemplateGenerator()

    # Get all artifacts
    artifacts = sorted([f.stem for f in generator.desc_dir.glob('*.md')])
    total = len(artifacts)

    print(f"╔═══════════════════════════════════════════════════════════╗")
    print(f"║  Batch Template Generator - Processing {total} artifacts  ║")
    print(f"╚═══════════════════════════════════════════════════════════╝\n")

    # Process each artifact
    for i, artifact in enumerate(artifacts, 1):
        success, result = generator.process_artifact(artifact)

        if success:
            if i % 10 == 0 or i == total:
                print(f"[{i:3d}/{total}] ✓ Generated {artifact}")
        else:
            print(f"[{i:3d}/{total}] ✗ FAILED {artifact}: {result}")

    print(f"\n╔═══════════════════════════════════════════════════════════╗")
    print(f"║  Processing Complete                                       ║")
    print(f"╠═══════════════════════════════════════════════════════════╣")
    print(f"║  Total Processed:  {total:3d}                                    ║")
    print(f"║  Successfully Generated: {generator.generated_count:3d}                          ║")
    print(f"║  Failed: {len(generator.failed):3d}                                         ║")
    print(f"╚═══════════════════════════════════════════════════════════╝")

    if generator.failed:
        print(f"\nFailed artifacts:")
        for name, error in generator.failed:
            print(f"  - {name}: {error}")

if __name__ == '__main__':
    # Import specialized generators
    sys.path.insert(0, str(Path(__file__).parent / 'generators'))

    # Add methods from specialized generator files
    from specialized_generators import *

    main()
