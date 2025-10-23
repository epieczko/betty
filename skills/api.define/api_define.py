#!/usr/bin/env python3
"""
Create OpenAPI and AsyncAPI specifications from templates.

This skill scaffolds API specifications following enterprise guidelines
with proper structure and best practices built-in.
"""

import sys
import json
import argparse
import uuid
import re
from pathlib import Path
from typing import Dict, Any

# Add betty module to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from betty.logging_utils import setup_logger
from betty.errors import format_error_response, BettyError
from betty.validation import validate_skill_name

logger = setup_logger(__name__)


def to_snake_case(text: str) -> str:
    """Convert text to snake_case."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    return s2.lower().replace('-', '_').replace(' ', '_')


def to_kebab_case(text: str) -> str:
    """Convert text to kebab-case."""
    return to_snake_case(text).replace('_', '-')


def to_title_case(text: str) -> str:
    """Convert text to TitleCase."""
    return ''.join(word.capitalize() for word in re.split(r'[-_\s]', text))


def pluralize(word: str) -> str:
    """Simple pluralization (works for most common cases)."""
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word.endswith('s'):
        return word + 'es'
    else:
        return word + 's'


def load_template(template_name: str, spec_type: str) -> str:
    """
    Load template file content.

    Args:
        template_name: Template name (zalando, basic, minimal)
        spec_type: Specification type (openapi or asyncapi)

    Returns:
        Template content as string

    Raises:
        BettyError: If template not found
    """
    template_file = Path(__file__).parent / "templates" / f"{spec_type}-{template_name}.yaml"

    if not template_file.exists():
        raise BettyError(
            f"Template not found: {spec_type}-{template_name}.yaml. "
            f"Available templates in {template_file.parent}: "
            f"{', '.join([f.stem for f in template_file.parent.glob(f'{spec_type}-*.yaml')])}"
        )

    try:
        with open(template_file, 'r') as f:
            content = f.read()
        logger.info(f"Loaded template: {template_file}")
        return content
    except Exception as e:
        raise BettyError(f"Failed to load template: {e}")


def render_template(template: str, variables: Dict[str, str]) -> str:
    """
    Render template with variables.

    Args:
        template: Template string with {{variable}} placeholders
        variables: Variable values to substitute

    Returns:
        Rendered template string
    """
    result = template
    for key, value in variables.items():
        placeholder = f"{{{{{key}}}}}"
        result = result.replace(placeholder, str(value))

    # Check for unrendered variables
    unrendered = re.findall(r'\{\{(\w+)\}\}', result)
    if unrendered:
        logger.warning(f"Unrendered template variables: {', '.join(set(unrendered))}")

    return result


def extract_resource_name(service_name: str) -> str:
    """
    Extract primary resource name from service name.

    Examples:
        user-service -> user
        order-api -> order
        payment-gateway -> payment
    """
    # Remove common suffixes
    for suffix in ['-service', '-api', '-gateway', '-manager']:
        if service_name.endswith(suffix):
            return service_name[:-len(suffix)]

    return service_name


def generate_openapi_spec(
    service_name: str,
    template_name: str = "zalando",
    version: str = "1.0.0",
    output_dir: str = "specs"
) -> Dict[str, Any]:
    """
    Generate OpenAPI specification from template.

    Args:
        service_name: Service/API name
        template_name: Template to use
        version: API version
        output_dir: Output directory

    Returns:
        Result dictionary with spec path and content
    """
    # Generate API ID
    api_id = str(uuid.uuid4())

    # Extract resource name
    resource_name = extract_resource_name(service_name)

    # Generate template variables
    variables = {
        "service_name": to_kebab_case(service_name),
        "service_title": to_title_case(service_name),
        "version": version,
        "description": f"RESTful API for {service_name.replace('-', ' ')} management",
        "team_name": "Platform Team",
        "team_email": "platform@company.com",
        "api_id": api_id,
        "audience": "company-internal",
        "resource_singular": to_snake_case(resource_name),
        "resource_plural": pluralize(to_snake_case(resource_name)),
        "resource_title": to_title_case(resource_name),
        "resource_schema": to_title_case(resource_name)
    }

    logger.info(f"Generated template variables: {variables}")

    # Load and render template
    template = load_template(template_name, "openapi")
    spec_content = render_template(template, variables)

    # Parse to validate YAML
    try:
        import yaml
        spec_dict = yaml.safe_load(spec_content)
    except Exception as e:
        raise BettyError(f"Failed to parse generated spec: {e}")

    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Write specification file
    spec_filename = f"{to_kebab_case(service_name)}.openapi.yaml"
    spec_path = output_path / spec_filename

    with open(spec_path, 'w') as f:
        f.write(spec_content)

    logger.info(f"Generated OpenAPI spec: {spec_path}")

    return {
        "spec_path": str(spec_path),
        "spec_content": spec_dict,
        "api_id": api_id,
        "template_used": template_name,
        "service_name": to_kebab_case(service_name)
    }


def generate_asyncapi_spec(
    service_name: str,
    template_name: str = "basic",
    version: str = "1.0.0",
    output_dir: str = "specs"
) -> Dict[str, Any]:
    """
    Generate AsyncAPI specification from template.

    Args:
        service_name: Service/API name
        template_name: Template to use
        version: API version
        output_dir: Output directory

    Returns:
        Result dictionary with spec path and content
    """
    # Basic AsyncAPI template (inline for now)
    resource_name = extract_resource_name(service_name)

    asyncapi_template = f"""asyncapi: 3.0.0

info:
  title: {to_title_case(service_name)} Events
  version: {version}
  description: Event-driven API for {service_name.replace('-', ' ')} lifecycle notifications

servers:
  production:
    host: kafka.company.com:9092
    protocol: kafka
    description: Production Kafka cluster

channels:
  {to_snake_case(resource_name)}.created:
    address: {to_snake_case(resource_name)}.created.v1
    messages:
      {to_title_case(resource_name)}Created:
        $ref: '#/components/messages/{to_title_case(resource_name)}Created'

  {to_snake_case(resource_name)}.updated:
    address: {to_snake_case(resource_name)}.updated.v1
    messages:
      {to_title_case(resource_name)}Updated:
        $ref: '#/components/messages/{to_title_case(resource_name)}Updated'

  {to_snake_case(resource_name)}.deleted:
    address: {to_snake_case(resource_name)}.deleted.v1
    messages:
      {to_title_case(resource_name)}Deleted:
        $ref: '#/components/messages/{to_title_case(resource_name)}Deleted'

operations:
  publish{to_title_case(resource_name)}Created:
    action: send
    channel:
      $ref: '#/channels/{to_snake_case(resource_name)}.created'

  subscribe{to_title_case(resource_name)}Created:
    action: receive
    channel:
      $ref: '#/channels/{to_snake_case(resource_name)}.created'

components:
  messages:
    {to_title_case(resource_name)}Created:
      name: {to_title_case(resource_name)}Created
      title: {to_title_case(resource_name)} Created Event
      contentType: application/json
      payload:
        $ref: '#/components/schemas/{to_title_case(resource_name)}CreatedPayload'

    {to_title_case(resource_name)}Updated:
      name: {to_title_case(resource_name)}Updated
      title: {to_title_case(resource_name)} Updated Event
      contentType: application/json
      payload:
        $ref: '#/components/schemas/{to_title_case(resource_name)}UpdatedPayload'

    {to_title_case(resource_name)}Deleted:
      name: {to_title_case(resource_name)}Deleted
      title: {to_title_case(resource_name)} Deleted Event
      contentType: application/json
      payload:
        $ref: '#/components/schemas/{to_title_case(resource_name)}DeletedPayload'

  schemas:
    {to_title_case(resource_name)}CreatedPayload:
      type: object
      required: [event_id, {to_snake_case(resource_name)}_id, occurred_at]
      properties:
        event_id:
          type: string
          format: uuid
        {to_snake_case(resource_name)}_id:
          type: string
          format: uuid
        occurred_at:
          type: string
          format: date-time

    {to_title_case(resource_name)}UpdatedPayload:
      type: object
      required: [event_id, {to_snake_case(resource_name)}_id, occurred_at, changes]
      properties:
        event_id:
          type: string
          format: uuid
        {to_snake_case(resource_name)}_id:
          type: string
          format: uuid
        changes:
          type: object
        occurred_at:
          type: string
          format: date-time

    {to_title_case(resource_name)}DeletedPayload:
      type: object
      required: [event_id, {to_snake_case(resource_name)}_id, occurred_at]
      properties:
        event_id:
          type: string
          format: uuid
        {to_snake_case(resource_name)}_id:
          type: string
          format: uuid
        occurred_at:
          type: string
          format: date-time
"""

    # Parse to validate YAML
    try:
        import yaml
        spec_dict = yaml.safe_load(asyncapi_template)
    except Exception as e:
        raise BettyError(f"Failed to parse generated spec: {e}")

    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Write specification file
    spec_filename = f"{to_kebab_case(service_name)}.asyncapi.yaml"
    spec_path = output_path / spec_filename

    with open(spec_path, 'w') as f:
        f.write(asyncapi_template)

    logger.info(f"Generated AsyncAPI spec: {spec_path}")

    return {
        "spec_path": str(spec_path),
        "spec_content": spec_dict,
        "template_used": template_name,
        "service_name": to_kebab_case(service_name)
    }


def main():
    parser = argparse.ArgumentParser(
        description="Create OpenAPI and AsyncAPI specifications from templates"
    )
    parser.add_argument(
        "service_name",
        type=str,
        help="Name of the service/API (e.g., user-service, order-api)"
    )
    parser.add_argument(
        "spec_type",
        type=str,
        nargs="?",
        default="openapi",
        choices=["openapi", "asyncapi"],
        help="Type of specification (default: openapi)"
    )
    parser.add_argument(
        "--template",
        type=str,
        default="zalando",
        help="Template to use (default: zalando for OpenAPI, basic for AsyncAPI)"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="specs",
        help="Output directory (default: specs)"
    )
    parser.add_argument(
        "--version",
        type=str,
        default="1.0.0",
        help="API version (default: 1.0.0)"
    )

    args = parser.parse_args()

    try:
        # Check if PyYAML is installed
        try:
            import yaml
        except ImportError:
            raise BettyError(
                "PyYAML is required for api.define. Install with: pip install pyyaml"
            )

        # Generate specification
        logger.info(
            f"Generating {args.spec_type.upper()} spec for '{args.service_name}' "
            f"using template '{args.template}'"
        )

        if args.spec_type == "openapi":
            result = generate_openapi_spec(
                service_name=args.service_name,
                template_name=args.template,
                version=args.version,
                output_dir=args.output_dir
            )
        elif args.spec_type == "asyncapi":
            result = generate_asyncapi_spec(
                service_name=args.service_name,
                template_name=args.template,
                version=args.version,
                output_dir=args.output_dir
            )
        else:
            raise BettyError(f"Unsupported spec type: {args.spec_type}")

        # Return structured result
        output = {
            "status": "success",
            "data": result
        }
        print(json.dumps(output, indent=2))

    except Exception as e:
        logger.error(f"Failed to generate specification: {e}")
        print(json.dumps(format_error_response(e), indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
