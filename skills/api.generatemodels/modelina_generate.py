#!/usr/bin/env python3
"""
Generate type-safe models from OpenAPI and AsyncAPI specifications using Modelina.

This skill uses AsyncAPI Modelina to generate models in various languages
from API specifications.
"""

import sys
import json
import argparse
import subprocess
import shutil
from pathlib import Path
from typing import Dict, Any, List

# Add betty module to path

from betty.logging_utils import setup_logger
from betty.errors import format_error_response, BettyError
from betty.validation import validate_path

logger = setup_logger(__name__)

# Supported languages
SUPPORTED_LANGUAGES = [
    "typescript",
    "python",
    "java",
    "go",
    "csharp",
    "rust",
    "kotlin",
    "dart"
]

# Language-specific configurations
LANGUAGE_CONFIG = {
    "typescript": {
        "extension": ".ts",
        "package_json_required": False,
        "modelina_generator": "typescript"
    },
    "python": {
        "extension": ".py",
        "package_json_required": False,
        "modelina_generator": "python"
    },
    "java": {
        "extension": ".java",
        "package_json_required": False,
        "modelina_generator": "java"
    },
    "go": {
        "extension": ".go",
        "package_json_required": False,
        "modelina_generator": "go"
    },
    "csharp": {
        "extension": ".cs",
        "package_json_required": False,
        "modelina_generator": "csharp"
    }
}


def check_node_installed() -> bool:
    """
    Check if Node.js is installed.

    Returns:
        True if Node.js is available, False otherwise
    """
    try:
        result = subprocess.run(
            ["node", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            version = result.stdout.strip()
            logger.info(f"Node.js found: {version}")
            return True
        return False
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def check_npx_installed() -> bool:
    """
    Check if npx is installed.

    Returns:
        True if npx is available, False otherwise
    """
    try:
        result = subprocess.run(
            ["npx", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def generate_modelina_script(
    spec_path: str,
    language: str,
    output_dir: str,
    package_name: str = None
) -> str:
    """
    Generate a Node.js script that uses Modelina to generate models.

    Args:
        spec_path: Path to spec file
        language: Target language
        output_dir: Output directory
        package_name: Package name (optional)

    Returns:
        JavaScript code as string
    """
    # Modelina generator based on language
    generator_map = {
        "typescript": "TypeScriptGenerator",
        "python": "PythonGenerator",
        "java": "JavaGenerator",
        "go": "GoGenerator",
        "csharp": "CSharpGenerator"
    }

    generator_class = generator_map.get(language, "TypeScriptGenerator")

    script = f"""
const {{ {generator_class} }} = require('@asyncapi/modelina');
const fs = require('fs');
const path = require('path');

async function generate() {{
    try {{
        // Read the spec file
        const spec = fs.readFileSync('{spec_path}', 'utf8');
        const specData = JSON.parse(spec);

        // Create generator
        const generator = new {generator_class}();

        // Generate models
        const models = await generator.generate(specData);

        // Ensure output directory exists
        const outputDir = '{output_dir}';
        if (!fs.existsSync(outputDir)) {{
            fs.mkdirSync(outputDir, {{ recursive: true }});
        }}

        // Write models to files
        const filesGenerated = [];
        for (const model of models) {{
            const filePath = path.join(outputDir, model.name + model.extension);
            fs.writeFileSync(filePath, model.result);
            filesGenerated.push(filePath);
        }}

        // Output result
        console.log(JSON.stringify({{
            success: true,
            files_generated: filesGenerated,
            model_count: models.length
        }}));

    }} catch (error) {{
        console.error(JSON.stringify({{
            success: false,
            error: error.message,
            stack: error.stack
        }}));
        process.exit(1);
    }}
}}

generate();
"""
    return script


def generate_models_datamodel_code_generator(
    spec_path: str,
    language: str,
    output_dir: str,
    package_name: str = None
) -> Dict[str, Any]:
    """
    Generate models using datamodel-code-generator (Python fallback).

    This is used when Modelina/Node.js is not available.
    Works for OpenAPI specs only, generating Python/TypeScript models.

    Args:
        spec_path: Path to specification file
        language: Target language
        output_dir: Output directory
        package_name: Package name

    Returns:
        Result dictionary
    """
    try:
        # Check if datamodel-code-generator is installed
        result = subprocess.run(
            ["datamodel-codegen", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode != 0:
            raise BettyError(
                "datamodel-code-generator not installed. "
                "Install with: pip install datamodel-code-generator"
            )

    except FileNotFoundError:
        raise BettyError(
            "datamodel-code-generator not found. "
            "Install with: pip install datamodel-code-generator"
        )

    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Determine output file based on language
    if language == "python":
        output_file = output_path / "models.py"
        cmd = [
            "datamodel-codegen",
            "--input", spec_path,
            "--output", str(output_file),
            "--input-file-type", "openapi",
            "--output-model-type", "pydantic_v2.BaseModel",
            "--snake-case-field",
            "--use-standard-collections"
        ]
    elif language == "typescript":
        output_file = output_path / "models.ts"
        cmd = [
            "datamodel-codegen",
            "--input", spec_path,
            "--output", str(output_file),
            "--input-file-type", "openapi",
            "--output-model-type", "typescript"
        ]
    else:
        raise BettyError(
            f"datamodel-code-generator fallback only supports Python and TypeScript, not {language}"
        )

    # Run code generator
    logger.info(f"Running datamodel-code-generator: {' '.join(cmd)}")
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=60
    )

    if result.returncode != 0:
        raise BettyError(f"Code generation failed: {result.stderr}")

    # Count generated files
    files_generated = [str(output_file)]

    return {
        "models_path": str(output_path),
        "files_generated": files_generated,
        "model_count": 1,
        "generator_used": "datamodel-code-generator"
    }


def generate_models_simple(
    spec_path: str,
    language: str,
    output_dir: str,
    package_name: str = None
) -> Dict[str, Any]:
    """
    Simple model generation without external tools.

    Generates basic model files from OpenAPI schemas as a last resort.

    Args:
        spec_path: Path to specification file
        language: Target language
        output_dir: Output directory
        package_name: Package name

    Returns:
        Result dictionary
    """
    import yaml

    # Load spec
    with open(spec_path, 'r') as f:
        spec = yaml.safe_load(f)

    # Get schemas
    schemas = spec.get("components", {}).get("schemas", {})

    if not schemas:
        raise BettyError("No schemas found in specification")

    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    files_generated = []

    # Generate basic models for each schema
    for schema_name, schema_def in schemas.items():
        if language == "typescript":
            content = generate_typescript_interface(schema_name, schema_def)
            file_path = output_path / f"{schema_name}.ts"
        elif language == "python":
            content = generate_python_dataclass(schema_name, schema_def)
            file_path = output_path / f"{schema_name.lower()}.py"
        else:
            raise BettyError(f"Simple generation only supports TypeScript and Python, not {language}")

        with open(file_path, 'w') as f:
            f.write(content)

        files_generated.append(str(file_path))
        logger.info(f"Generated {file_path}")

    return {
        "models_path": str(output_path),
        "files_generated": files_generated,
        "model_count": len(schemas),
        "generator_used": "simple"
    }


def generate_typescript_interface(name: str, schema: Dict[str, Any]) -> str:
    """Generate TypeScript interface from schema."""
    properties = schema.get("properties") or {}
    required = schema.get("required", [])

    lines = [f"export interface {name} {{"]

    if not properties:
        lines.append("  // No properties defined")

    for prop_name, prop_def in properties.items():
        prop_type = map_openapi_type_to_typescript(prop_def.get("type", "any"))
        optional = "" if prop_name in required else "?"
        description = prop_def.get("description", "")

        if description:
            lines.append(f"  /** {description} */")
        lines.append(f"  {prop_name}{optional}: {prop_type};")

    lines.append("}")

    return "\n".join(lines)


def generate_python_dataclass(name: str, schema: Dict[str, Any]) -> str:
    """Generate Python dataclass from schema."""
    properties = schema.get("properties") or {}
    required = schema.get("required", [])

    lines = [
        "from dataclasses import dataclass",
        "from typing import Optional",
        "from datetime import datetime",
        "",
        "@dataclass",
        f"class {name}:"
    ]

    if not properties:
        lines.append("    pass")
    else:
        for prop_name, prop_def in properties.items():
            prop_type = map_openapi_type_to_python(prop_def)
            description = prop_def.get("description", "")

            if prop_name not in required:
                prop_type = f"Optional[{prop_type}]"

            if description:
                lines.append(f"    # {description}")

            default = " = None" if prop_name not in required else ""
            lines.append(f"    {prop_name}: {prop_type}{default}")

    return "\n".join(lines)


def map_openapi_type_to_typescript(openapi_type: str) -> str:
    """Map OpenAPI type to TypeScript type."""
    type_map = {
        "string": "string",
        "number": "number",
        "integer": "number",
        "boolean": "boolean",
        "array": "any[]",
        "object": "object"
    }
    return type_map.get(openapi_type, "any")


def map_openapi_type_to_python(prop_def: Dict[str, Any]) -> str:
    """Map OpenAPI type to Python type."""
    openapi_type = prop_def.get("type", "Any")
    format_type = prop_def.get("format", "")

    if openapi_type == "string":
        if format_type == "date-time":
            return "datetime"
        elif format_type == "uuid":
            return "str"  # or UUID from uuid module
        return "str"
    elif openapi_type == "number" or openapi_type == "integer":
        return "int" if openapi_type == "integer" else "float"
    elif openapi_type == "boolean":
        return "bool"
    elif openapi_type == "array":
        return "list"
    elif openapi_type == "object":
        return "dict"
    return "Any"


def generate_models(
    spec_path: str,
    language: str,
    output_dir: str = "src/models",
    package_name: str = None
) -> Dict[str, Any]:
    """
    Generate models from API specification.

    Args:
        spec_path: Path to specification file
        language: Target language
        output_dir: Output directory
        package_name: Package name

    Returns:
        Result dictionary with generated files info

    Raises:
        BettyError: If generation fails
    """
    # Validate language
    if language not in SUPPORTED_LANGUAGES:
        raise BettyError(
            f"Unsupported language '{language}'. "
            f"Supported: {', '.join(SUPPORTED_LANGUAGES)}"
        )

    # Validate spec file exists
    if not Path(spec_path).exists():
        raise BettyError(f"Specification file not found: {spec_path}")

    logger.info(f"Generating {language} models from {spec_path}")

    # Try datamodel-code-generator first (most reliable for OpenAPI)
    try:
        logger.info("Attempting generation with datamodel-code-generator")
        result = generate_models_datamodel_code_generator(
            spec_path, language, output_dir, package_name
        )
        return result
    except BettyError as e:
        logger.warning(f"datamodel-code-generator not available: {e}")

    # Fallback to simple generation
    logger.info("Using simple built-in generator")
    result = generate_models_simple(
        spec_path, language, output_dir, package_name
    )

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Generate type-safe models from API specifications using Modelina"
    )
    parser.add_argument(
        "spec_path",
        type=str,
        help="Path to API specification file (OpenAPI or AsyncAPI)"
    )
    parser.add_argument(
        "language",
        type=str,
        choices=SUPPORTED_LANGUAGES,
        help="Target language for generated models"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="src/models",
        help="Output directory for generated models (default: src/models)"
    )
    parser.add_argument(
        "--package-name",
        type=str,
        help="Package/module name for generated code"
    )

    args = parser.parse_args()

    try:
        # Validate inputs
        validate_path(args.spec_path)

        # Generate models
        result = generate_models(
            spec_path=args.spec_path,
            language=args.language,
            output_dir=args.output_dir,
            package_name=args.package_name
        )

        # Return structured result
        output = {
            "status": "success",
            "data": result
        }
        print(json.dumps(output, indent=2))

    except Exception as e:
        logger.error(f"Model generation failed: {e}")
        print(json.dumps(format_error_response(e), indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
