#!/usr/bin/env python3
"""
Library of specialized template generators for all major artifact types.
Each function returns a complete, industry-standard template.
"""

def get_openapi_template(name):
    """OpenAPI 3.1 specification with REST best practices."""
    # Use the OpenAPI template from threat-model example approach
    return open('/home/user/betty/template_generator.py').read().split('def _generate_openapi_template')[1].split('def _generate_asyncapi_template')[0].split('return \'\'\'')[1].split('\'\'\'')[0]

def get_asyncapi_template(name):
    """AsyncAPI 2.6 specification for event-driven APIs."""
    return open('/home/user/betty/template_generator.py').read().split('def _generate_asyncapi_template')[1].split('# Will add more')[0].split('return \'\'\'')[1].split('\'\'\'')[0]

# Continue with more templates...
