#!/usr/bin/env python3
"""
run_agent.py – Implementation of the run.agent Skill
Simulates execution of Betty agents by loading manifests and demonstrating behavior.
"""
import os
import sys
import yaml
import json
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import (
    AGENTS_DIR, AGENTS_REGISTRY_FILE, REGISTRY_FILE,
    get_agent_manifest_path, get_skill_manifest_path
)
from betty.validation import validate_path
from betty.logging_utils import setup_logger
from betty.errors import format_error_response

logger = setup_logger(__name__)


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
    }
    if details is not None:
        response["details"] = details
    return response


def load_agent_manifest(agent_path: str) -> Dict[str, Any]:
    """
    Load agent manifest from path or agent name.

    Args:
        agent_path: Path to agent.yaml or agent name (e.g., api.designer)

    Returns:
        Agent manifest dictionary

    Raises:
        Exception: If agent cannot be loaded
    """
    # Check if it's a direct path to agent.yaml
    if os.path.exists(agent_path) and agent_path.endswith('.yaml'):
        manifest_path = agent_path
    # Check if it's an agent name
    else:
        manifest_path = get_agent_manifest_path(agent_path)
        if not os.path.exists(manifest_path):
            raise ValueError(f"Agent not found: {agent_path}")

    try:
        with open(manifest_path) as f:
            manifest = yaml.safe_load(f)
        return manifest
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML in agent manifest: {e}")


def load_skill_registry() -> Dict[str, Any]:
    """Load the skills registry."""
    try:
        with open(REGISTRY_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return {"skills": []}
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in skills registry: {e}")


def get_skill_info(skill_name: str, registry: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Get skill information from registry."""
    for skill in registry.get("skills", []):
        if skill.get("name") == skill_name:
            return skill
    return None


def construct_agent_prompt(
    agent_manifest: Dict[str, Any],
    input_text: Optional[str] = None
) -> str:
    """
    Construct the prompt that would be sent to Claude for this agent.

    Args:
        agent_manifest: Agent manifest dictionary
        input_text: Optional user input

    Returns:
        Constructed prompt string
    """
    agent_name = agent_manifest.get("name", "unknown")
    description = agent_manifest.get("description", "")
    capabilities = agent_manifest.get("capabilities", [])
    skills_available = agent_manifest.get("skills_available", [])
    reasoning_mode = agent_manifest.get("reasoning_mode", "oneshot")
    workflow_pattern = agent_manifest.get("workflow_pattern", "")

    prompt = f"""You are {agent_name}, a specialized Betty Framework agent.

DESCRIPTION:
{description}

CAPABILITIES:
"""
    for cap in capabilities:
        prompt += f"  - {cap}\n"

    prompt += f"""
REASONING MODE: {reasoning_mode}

AVAILABLE SKILLS:
"""
    for skill in skills_available:
        prompt += f"  - {skill}\n"

    if workflow_pattern:
        prompt += f"""
WORKFLOW PATTERN:
{workflow_pattern}
"""

    if input_text:
        prompt += f"""
TASK:
{input_text}

Please analyze this task and determine which skills to invoke and in what order.
"""
    else:
        prompt += """
You are ready to accept tasks. When given a task, analyze it and determine
which skills to invoke and in what order based on your workflow pattern.
"""

    return prompt


def generate_mock_response(
    agent_manifest: Dict[str, Any],
    input_text: Optional[str] = None
) -> Dict[str, Any]:
    """
    Generate a mock response showing what the agent would do.

    Args:
        agent_manifest: Agent manifest dictionary
        input_text: Optional user input

    Returns:
        Mock response dictionary
    """
    agent_name = agent_manifest.get("name", "unknown")
    reasoning_mode = agent_manifest.get("reasoning_mode", "oneshot")
    skills_available = agent_manifest.get("skills_available", [])

    # Determine which skills would likely be invoked based on the agent type
    # and available skills
    skills_to_invoke = []

    if "api.designer" in agent_name:
        # API designer would likely use these skills in sequence
        if "api.define" in skills_available:
            skills_to_invoke.append({
                "skill": "api.define",
                "purpose": "Create initial OpenAPI specification"
            })
        if "api.validate" in skills_available:
            skills_to_invoke.append({
                "skill": "api.validate",
                "purpose": "Validate the generated API specification"
            })
        if "api.generate-models" in skills_available:
            skills_to_invoke.append({
                "skill": "api.generate-models",
                "purpose": "Generate client/server models"
            })
    elif "api.analyzer" in agent_name:
        # API analyzer would likely use validation and compatibility
        if "api.validate" in skills_available:
            skills_to_invoke.append({
                "skill": "api.validate",
                "purpose": "Analyze API specification for issues"
            })
        if "api.compatibility" in skills_available:
            skills_to_invoke.append({
                "skill": "api.compatibility",
                "purpose": "Check compatibility with existing APIs"
            })
    else:
        # For other agents, just list first 3 available skills as examples
        for skill in skills_available[:3]:
            skills_to_invoke.append({
                "skill": skill,
                "purpose": f"Execute {skill} based on task requirements"
            })

    response = {
        "agent": agent_name,
        "reasoning_mode": reasoning_mode,
        "task": input_text or "No specific task provided",
        "analysis": f"As {agent_name}, I would approach this task by invoking the following skills:",
        "skills_to_invoke": skills_to_invoke,
        "execution_plan": []
    }

    # Add execution steps
    for i, skill_info in enumerate(skills_to_invoke, 1):
        step = {
            "step": i,
            "skill": skill_info["skill"],
            "purpose": skill_info["purpose"],
            "status": "simulated"
        }
        response["execution_plan"].append(step)

    if reasoning_mode == "iterative":
        response["note"] = (
            "This agent uses iterative reasoning. In a real execution, "
            "it would analyze results from each skill and potentially invoke "
            "additional skills or retry based on feedback."
        )

    return response


def simulate_agent_execution(
    agent_path: str,
    input_text: Optional[str] = None
) -> Dict[str, Any]:
    """
    Simulate agent execution.

    Args:
        agent_path: Path to agent manifest or agent name
        input_text: Optional input text

    Returns:
        Execution log dictionary
    """
    logger.info(f"Loading agent: {agent_path}")

    # Load agent manifest
    agent_manifest = load_agent_manifest(agent_path)
    agent_name = agent_manifest.get("name", "unknown")

    # Load skill registry to get info about available skills
    skill_registry = load_skill_registry()

    # Get info about skills available to this agent
    skills_info = []
    for skill_name in agent_manifest.get("skills_available", []):
        skill_info = get_skill_info(skill_name, skill_registry)
        if skill_info:
            skills_info.append({
                "name": skill_name,
                "description": skill_info.get("description", ""),
                "status": skill_info.get("status", "unknown")
            })
        else:
            skills_info.append({
                "name": skill_name,
                "description": "Skill not found in registry",
                "status": "unknown"
            })

    # Construct prompt
    logger.info("Constructing agent prompt...")
    prompt = construct_agent_prompt(agent_manifest, input_text)

    # Generate mock response
    logger.info("Generating mock Claude response...")
    mock_response = generate_mock_response(agent_manifest, input_text)

    # Build execution log
    execution_log = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "agent": {
            "name": agent_name,
            "version": agent_manifest.get("version", "unknown"),
            "description": agent_manifest.get("description", ""),
            "reasoning_mode": agent_manifest.get("reasoning_mode", "oneshot"),
            "status": agent_manifest.get("status", "unknown")
        },
        "input": input_text or "No input provided",
        "prompt": prompt,
        "skills_available": skills_info,
        "mock_response": mock_response,
        "simulation_mode": True,
        "note": (
            "This is a simulated execution. In production, the agent would "
            "invoke real skills through the Claude Code Plugin runtime."
        )
    }

    # Print formatted output
    print("\n" + "="*80)
    print(f"AGENT SIMULATION: {agent_name}")
    print("="*80)

    print(f"\nAgent: {agent_name} v{agent_manifest.get('version', 'unknown')}")
    print(f"Reasoning Mode: {agent_manifest.get('reasoning_mode', 'oneshot')}")
    print(f"Status: {agent_manifest.get('status', 'unknown')}")

    print("\n" + "-"*80)
    print("PROMPT SENT TO AGENT:")
    print("-"*80)
    print(prompt)

    print("\n" + "-"*80)
    print("MOCK CLAUDE RESPONSE:")
    print("-"*80)
    print(json.dumps(mock_response, indent=2))

    print("\n" + "-"*80)
    print("SKILLS THAT WOULD BE INVOKED:")
    print("-"*80)
    for skill_info in skills_info:
        print(f"  • {skill_info['name']}")
        print(f"    {skill_info['description']}")
        print(f"    Status: {skill_info['status']}")

    print("\n" + "="*80)
    print("END SIMULATION")
    print("="*80 + "\n")

    return execution_log


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        message = "Usage: run_agent.py <agent_path> [input_text]"
        response = build_response(
            False,
            errors=[message],
            details={"error": {"error": "UsageError", "message": message, "details": {}}}
        )
        print(json.dumps(response, indent=2))
        sys.exit(1)

    agent_path = sys.argv[1]
    input_text = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        execution_log = simulate_agent_execution(agent_path, input_text)

        response = build_response(
            True,
            details=execution_log
        )

        print(json.dumps(response, indent=2))
        sys.exit(0)

    except Exception as e:
        logger.error(f"Agent simulation failed: {e}")
        error_info = format_error_response(e, include_traceback=True)
        response = build_response(
            False,
            errors=[error_info.get("message", str(e))],
            details={"error": error_info}
        )
        print(json.dumps(response, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
