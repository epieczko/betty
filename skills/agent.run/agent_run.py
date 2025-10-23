#!/usr/bin/env python3
"""
agent_run.py – Implementation of the agent.run Skill

Executes a registered Betty agent by loading its manifest, constructing a Claude-friendly
prompt, invoking the Claude API (or simulating), and logging execution results.

This skill supports both iterative and oneshot reasoning modes and can execute
skills based on the agent's workflow pattern.
"""
import os
import sys
import yaml
import json
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import (
    AGENTS_DIR, AGENTS_REGISTRY_FILE, REGISTRY_FILE,
    get_agent_manifest_path, get_skill_manifest_path,
    BETTY_HOME
)
from betty.validation import validate_path
from betty.logging_utils import setup_logger
from betty.errors import BettyError, format_error_response
from betty.telemetry_capture import capture_skill_execution, capture_audit_entry

logger = setup_logger(__name__)

# Agent logs directory
AGENT_LOGS_DIR = os.path.join(BETTY_HOME, "agent_logs")


def build_response(
    ok: bool,
    errors: Optional[List[str]] = None,
    details: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Build standardized response.

    Args:
        ok: Whether the operation was successful
        errors: List of error messages
        details: Additional details to include

    Returns:
        Standardized response dictionary
    """
    response: Dict[str, Any] = {
        "ok": ok,
        "status": "success" if ok else "failed",
        "errors": errors or [],
        "timestamp": datetime.now(timezone.utc).isoformat()
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
        BettyError: If agent cannot be loaded or is invalid
    """
    # Check if it's a direct path to agent.yaml
    if os.path.exists(agent_path) and agent_path.endswith('.yaml'):
        manifest_path = agent_path
    # Check if it's an agent name
    else:
        manifest_path = get_agent_manifest_path(agent_path)
        if not os.path.exists(manifest_path):
            raise BettyError(
                f"Agent not found: {agent_path}",
                details={
                    "agent_path": agent_path,
                    "expected_path": manifest_path,
                    "suggestion": "Use 'betty agent list' to see available agents"
                }
            )

    try:
        with open(manifest_path) as f:
            manifest = yaml.safe_load(f)

        if not isinstance(manifest, dict):
            raise BettyError("Agent manifest must be a dictionary")

        # Validate required fields
        required_fields = ["name", "version", "description", "capabilities",
                          "skills_available", "reasoning_mode"]
        missing = [f for f in required_fields if f not in manifest]
        if missing:
            raise BettyError(
                f"Agent manifest missing required fields: {', '.join(missing)}",
                details={"missing_fields": missing}
            )

        return manifest
    except yaml.YAMLError as e:
        raise BettyError(f"Invalid YAML in agent manifest: {e}")


def load_skill_registry() -> Dict[str, Any]:
    """
    Load the skills registry.

    Returns:
        Skills registry dictionary
    """
    try:
        with open(REGISTRY_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning(f"Skills registry not found: {REGISTRY_FILE}")
        return {"skills": []}
    except json.JSONDecodeError as e:
        raise BettyError(f"Invalid JSON in skills registry: {e}")


def get_skill_info(skill_name: str, registry: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Get skill information from registry.

    Args:
        skill_name: Name of the skill
        registry: Skills registry

    Returns:
        Skill info dictionary or None if not found
    """
    for skill in registry.get("skills", []):
        if skill.get("name") == skill_name:
            return skill
    return None


def construct_agent_prompt(
    agent_manifest: Dict[str, Any],
    task_context: Optional[str] = None
) -> str:
    """
    Construct a Claude-friendly prompt for the agent.

    Args:
        agent_manifest: Agent manifest dictionary
        task_context: User-provided task or query

    Returns:
        Constructed system prompt string suitable for Claude API
    """
    agent_name = agent_manifest.get("name", "unknown")
    description = agent_manifest.get("description", "")
    capabilities = agent_manifest.get("capabilities", [])
    skills_available = agent_manifest.get("skills_available", [])
    reasoning_mode = agent_manifest.get("reasoning_mode", "oneshot")
    workflow_pattern = agent_manifest.get("workflow_pattern", "")
    context_requirements = agent_manifest.get("context_requirements", {})

    # Build system prompt
    prompt = f"""You are {agent_name}, a specialized Betty Framework agent.

## AGENT DESCRIPTION
{description}

## CAPABILITIES
You have the following capabilities:
"""
    for cap in capabilities:
        prompt += f"  • {cap}\n"

    prompt += f"""
## REASONING MODE
{reasoning_mode.upper()}: """

    if reasoning_mode == "iterative":
        prompt += """You will analyze results from each skill invocation and determine
the next steps dynamically. You may retry failed operations or adjust your
approach based on feedback."""
    else:
        prompt += """You will plan and execute all necessary skills in a single pass.
Analyze the task completely before determining the sequence of skill invocations."""

    prompt += """

## AVAILABLE SKILLS
You have access to the following Betty skills:
"""
    for skill in skills_available:
        prompt += f"  • {skill}\n"

    if workflow_pattern:
        prompt += f"""
## RECOMMENDED WORKFLOW
{workflow_pattern}
"""

    if context_requirements:
        prompt += """
## CONTEXT REQUIREMENTS
The following context may be required for optimal performance:
"""
        for key, value_type in context_requirements.items():
            prompt += f"  • {key}: {value_type}\n"

    if task_context:
        prompt += f"""
## TASK
{task_context}

## INSTRUCTIONS
Analyze the task above and respond with a JSON object describing your execution plan:

{{
  "analysis": "Brief analysis of the task",
  "skills_to_invoke": [
    {{
      "skill": "skill.name",
      "purpose": "Why this skill is needed",
      "inputs": {{"param": "value"}},
      "order": 1
    }}
  ],
  "reasoning": "Explanation of your approach"
}}

Select skills from your available skills list and arrange them according to the
workflow pattern. Ensure the sequence makes logical sense for accomplishing the task.
"""
    else:
        prompt += """
## READY STATE
You are initialized and ready to accept tasks. When given a task, you will:
1. Analyze the requirements
2. Select appropriate skills from your available skills
3. Determine the execution order based on your workflow pattern
4. Provide a structured execution plan
"""

    return prompt


def call_claude_api(prompt: str, agent_name: str) -> Dict[str, Any]:
    """
    Call the Claude API with the constructed prompt.

    Currently simulates the API call. In production, this would:
    1. Use the Anthropic API client
    2. Send the prompt with appropriate parameters
    3. Parse the structured response

    Args:
        prompt: The constructed system prompt
        agent_name: Name of the agent (for context)

    Returns:
        Claude's response (currently mocked)
    """
    # Check if we have ANTHROPIC_API_KEY in environment
    api_key = os.environ.get("ANTHROPIC_API_KEY")

    if api_key:
        logger.info("Anthropic API key found - would call real API")
        # TODO: Implement actual API call
        # from anthropic import Anthropic
        # client = Anthropic(api_key=api_key)
        # response = client.messages.create(
        #     model="claude-3-5-sonnet-20241022",
        #     max_tokens=4096,
        #     system=prompt,
        #     messages=[{"role": "user", "content": "Execute the task"}]
        # )
        # return parse_claude_response(response)

    logger.info("No API key found - using mock response")
    return generate_mock_response(prompt, agent_name)


def generate_mock_response(prompt: str, agent_name: str) -> Dict[str, Any]:
    """
    Generate a mock Claude response for simulation.

    Args:
        prompt: The system prompt
        agent_name: Name of the agent

    Returns:
        Mock response dictionary
    """
    # Extract task from prompt if present
    task_section = ""
    if "## TASK" in prompt:
        task_start = prompt.index("## TASK")
        task_end = prompt.index("## INSTRUCTIONS") if "## INSTRUCTIONS" in prompt else len(prompt)
        task_section = prompt[task_start:task_end].replace("## TASK", "").strip()

    # Generate plausible skill selections based on agent name
    skills_to_invoke = []

    if "api.designer" in agent_name:
        skills_to_invoke = [
            {
                "skill": "api.define",
                "purpose": "Create initial OpenAPI specification from requirements",
                "inputs": {"guidelines": "zalando", "format": "openapi-3.1"},
                "order": 1
            },
            {
                "skill": "api.validate",
                "purpose": "Validate the generated specification for compliance",
                "inputs": {"strict_mode": True},
                "order": 2
            },
            {
                "skill": "api.generate-models",
                "purpose": "Generate type-safe models from validated spec",
                "inputs": {"language": "typescript", "framework": "zod"},
                "order": 3
            }
        ]
    elif "api.analyzer" in agent_name:
        skills_to_invoke = [
            {
                "skill": "api.validate",
                "purpose": "Analyze API specification for issues and best practices",
                "inputs": {"include_warnings": True},
                "order": 1
            },
            {
                "skill": "api.compatibility",
                "purpose": "Check compatibility with existing APIs",
                "inputs": {"check_breaking_changes": True},
                "order": 2
            }
        ]
    else:
        # Generic response - extract skills from prompt
        if "AVAILABLE SKILLS" in prompt:
            skills_section_start = prompt.index("AVAILABLE SKILLS")
            skills_section_end = prompt.index("##", skills_section_start + 10) if prompt.count("##", skills_section_start) > 0 else len(prompt)
            skills_text = prompt[skills_section_start:skills_section_end]

            import re
            skill_names = re.findall(r'• (\S+)', skills_text)

            for i, skill_name in enumerate(skill_names[:3], 1):
                skills_to_invoke.append({
                    "skill": skill_name,
                    "purpose": f"Execute {skill_name} as part of agent workflow",
                    "inputs": {},
                    "order": i
                })

    response = {
        "analysis": f"As {agent_name}, I will approach this task using my available skills in a structured sequence.",
        "skills_to_invoke": skills_to_invoke,
        "reasoning": "Selected skills follow the agent's workflow pattern and capabilities.",
        "mode": "simulated",
        "note": "This is a mock response. In production, Claude API would provide real analysis."
    }

    return response


def execute_skills(
    skills_plan: List[Dict[str, Any]],
    reasoning_mode: str
) -> List[Dict[str, Any]]:
    """
    Execute the planned skills (currently simulated).

    In production, this would:
    1. For each skill in the plan:
       - Load the skill manifest
       - Prepare inputs
       - Execute the skill handler
       - Capture output
    2. In iterative mode: analyze results and potentially invoke more skills

    Args:
        skills_plan: List of skills to invoke with their inputs
        reasoning_mode: 'iterative' or 'oneshot'

    Returns:
        List of execution results
    """
    results = []

    for skill_info in skills_plan:
        execution_result = {
            "skill": skill_info.get("skill"),
            "purpose": skill_info.get("purpose"),
            "status": "simulated",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "output": {
                "note": f"Simulated execution of {skill_info.get('skill')}",
                "inputs": skill_info.get("inputs", {}),
                "success": True
            }
        }

        results.append(execution_result)

        # In iterative mode, we might make decisions based on results
        if reasoning_mode == "iterative":
            execution_result["iterative_note"] = (
                "In iterative mode, the agent would analyze this result "
                "and potentially invoke additional skills or retry."
            )

    return results


def save_execution_log(
    agent_name: str,
    execution_data: Dict[str, Any]
) -> str:
    """
    Save execution log to agent_logs/<agent>.json

    Args:
        agent_name: Name of the agent
        execution_data: Complete execution data to log

    Returns:
        Path to the saved log file
    """
    # Ensure logs directory exists
    os.makedirs(AGENT_LOGS_DIR, exist_ok=True)

    # Generate log filename with timestamp
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    log_filename = f"{agent_name}_{timestamp}.json"
    log_path = os.path.join(AGENT_LOGS_DIR, log_filename)

    # Also maintain a "latest" symlink
    latest_path = os.path.join(AGENT_LOGS_DIR, f"{agent_name}_latest.json")

    try:
        with open(log_path, 'w') as f:
            json.dump(execution_data, f, indent=2)

        # Create/update latest symlink
        if os.path.exists(latest_path):
            os.remove(latest_path)
        os.symlink(os.path.basename(log_path), latest_path)

        logger.info(f"Execution log saved to {log_path}")
        return log_path
    except Exception as e:
        logger.error(f"Failed to save execution log: {e}")
        raise BettyError(f"Failed to save execution log: {e}")


def run_agent(
    agent_path: str,
    task_context: Optional[str] = None,
    save_log: bool = True
) -> Dict[str, Any]:
    """
    Execute a Betty agent.

    Args:
        agent_path: Path to agent manifest or agent name
        task_context: User-provided task or query
        save_log: Whether to save execution log to disk

    Returns:
        Execution result dictionary
    """
    logger.info(f"Running agent: {agent_path}")

    # Track execution time for telemetry
    start_time = datetime.now(timezone.utc)

    try:
        # Load agent manifest
        agent_manifest = load_agent_manifest(agent_path)
        agent_name = agent_manifest.get("name")
        reasoning_mode = agent_manifest.get("reasoning_mode", "oneshot")

        logger.info(f"Loaded agent: {agent_name} (mode: {reasoning_mode})")

        # Load skill registry
        skill_registry = load_skill_registry()

        # Validate that agent's skills are available
        skills_available = agent_manifest.get("skills_available", [])
        skills_info = []
        missing_skills = []

        for skill_name in skills_available:
            skill_info = get_skill_info(skill_name, skill_registry)
            if skill_info:
                skills_info.append({
                    "name": skill_name,
                    "description": skill_info.get("description", ""),
                    "status": skill_info.get("status", "unknown")
                })
            else:
                missing_skills.append(skill_name)
                logger.warning(f"Skill not found in registry: {skill_name}")

        # Construct agent prompt
        logger.info("Constructing agent prompt...")
        prompt = construct_agent_prompt(agent_manifest, task_context)

        # Call Claude API (or mock)
        logger.info("Invoking Claude API...")
        claude_response = call_claude_api(prompt, agent_name)

        # Execute skills based on Claude's plan
        skills_plan = claude_response.get("skills_to_invoke", [])
        logger.info(f"Executing {len(skills_plan)} skills...")
        execution_results = execute_skills(skills_plan, reasoning_mode)

        # Build complete execution data
        execution_data = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "agent": {
                "name": agent_name,
                "version": agent_manifest.get("version"),
                "description": agent_manifest.get("description"),
                "reasoning_mode": reasoning_mode,
                "status": agent_manifest.get("status", "unknown")
            },
            "task_context": task_context or "No task provided",
            "prompt": prompt,
            "skills_available": skills_info,
            "missing_skills": missing_skills,
            "claude_response": claude_response,
            "execution_results": execution_results,
            "summary": {
                "skills_planned": len(skills_plan),
                "skills_executed": len(execution_results),
                "success": all(r.get("output", {}).get("success", False) for r in execution_results)
            }
        }

        # Save log if requested
        log_path = None
        if save_log:
            log_path = save_execution_log(agent_name, execution_data)
            execution_data["log_path"] = log_path

        # Calculate execution duration
        end_time = datetime.now(timezone.utc)
        duration_ms = int((end_time - start_time).total_seconds() * 1000)

        # Capture telemetry for successful agent execution
        capture_skill_execution(
            skill_name="agent.run",
            inputs={
                "agent": agent_name,
                "task_context": task_context or "No task provided",
            },
            status="success" if execution_data["summary"]["success"] else "failed",
            duration_ms=duration_ms,
            agent=agent_name,
            caller="cli",
            reasoning_mode=reasoning_mode,
            skills_planned=len(skills_plan),
            skills_executed=len(execution_results),
        )

        # Log audit entry for agent execution
        capture_audit_entry(
            skill_name="agent.run",
            status="success" if execution_data["summary"]["success"] else "failed",
            duration_ms=duration_ms,
            errors=None,
            metadata={
                "agent": agent_name,
                "reasoning_mode": reasoning_mode,
                "skills_executed": len(execution_results),
                "task_context": task_context or "No task provided",
            }
        )

        return build_response(
            ok=True,
            details=execution_data
        )

    except BettyError as e:
        logger.error(f"Agent execution failed: {e}")
        error_info = format_error_response(e, include_traceback=False)

        # Calculate execution duration for failed case
        end_time = datetime.now(timezone.utc)
        duration_ms = int((end_time - start_time).total_seconds() * 1000)

        # Capture telemetry for failed agent execution
        capture_skill_execution(
            skill_name="agent.run",
            inputs={"agent_path": agent_path},
            status="failed",
            duration_ms=duration_ms,
            caller="cli",
            error=str(e),
        )

        # Log audit entry for failed agent execution
        capture_audit_entry(
            skill_name="agent.run",
            status="failed",
            duration_ms=duration_ms,
            errors=[str(e)],
            metadata={
                "agent_path": agent_path,
                "error_type": "BettyError",
            }
        )

        return build_response(
            ok=False,
            errors=[str(e)],
            details={"error": error_info}
        )
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        error_info = format_error_response(e, include_traceback=True)

        # Calculate execution duration for failed case
        end_time = datetime.now(timezone.utc)
        duration_ms = int((end_time - start_time).total_seconds() * 1000)

        # Capture telemetry for unexpected error
        capture_skill_execution(
            skill_name="agent.run",
            inputs={"agent_path": agent_path},
            status="failed",
            duration_ms=duration_ms,
            caller="cli",
            error=str(e),
        )

        # Log audit entry for unexpected error
        capture_audit_entry(
            skill_name="agent.run",
            status="failed",
            duration_ms=duration_ms,
            errors=[f"Unexpected error: {str(e)}"],
            metadata={
                "agent_path": agent_path,
                "error_type": type(e).__name__,
            }
        )

        return build_response(
            ok=False,
            errors=[f"Unexpected error: {str(e)}"],
            details={"error": error_info}
        )


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        message = "Usage: agent_run.py <agent_path> [task_context] [--no-save-log]"
        response = build_response(
            False,
            errors=[message],
            details={
                "usage": message,
                "examples": [
                    "agent_run.py api.designer",
                    "agent_run.py api.designer 'Create API for user management'",
                    "agent_run.py agents/api.designer/agent.yaml 'Design REST API'"
                ]
            }
        )
        print(json.dumps(response, indent=2), file=sys.stderr)
        sys.exit(1)

    agent_path = sys.argv[1]

    # Parse optional arguments
    task_context = None
    save_log = True

    for arg in sys.argv[2:]:
        if arg == "--no-save-log":
            save_log = False
        elif task_context is None:
            task_context = arg

    try:
        result = run_agent(agent_path, task_context, save_log)

        # Check if execution was successful
        if result['ok'] and 'details' in result and 'agent' in result['details']:
            # Pretty print for CLI usage
            print("\n" + "="*80)
            print(f"AGENT EXECUTION: {result['details']['agent']['name']}")
            print("="*80)

            agent_info = result['details']['agent']
            print(f"\nAgent: {agent_info['name']} v{agent_info['version']}")
            print(f"Mode: {agent_info['reasoning_mode']}")
            print(f"Status: {agent_info['status']}")

            print(f"\nTask: {result['details']['task_context']}")

            print("\n" + "-"*80)
            print("CLAUDE RESPONSE:")
            print("-"*80)
            print(json.dumps(result['details']['claude_response'], indent=2))

            print("\n" + "-"*80)
            print("EXECUTION RESULTS:")
            print("-"*80)
            for exec_result in result['details']['execution_results']:
                print(f"\n  ✓ {exec_result['skill']}")
                print(f"    Purpose: {exec_result['purpose']}")
                print(f"    Status: {exec_result['status']}")

            if 'log_path' in result['details']:
                print(f"\n📝 Log saved to: {result['details']['log_path']}")

            print("\n" + "="*80)
            print("EXECUTION COMPLETE")
            print("="*80 + "\n")
        else:
            # Execution failed - print error details
            print("\n" + "="*80)
            print("AGENT EXECUTION FAILED")
            print("="*80)
            print(f"\nErrors:")
            for error in result.get('errors', ['Unknown error']):
                print(f"  ✗ {error}")
            print()

        # Also output full JSON for programmatic use
        print(json.dumps(result, indent=2))
        sys.exit(0 if result['ok'] else 1)

    except KeyboardInterrupt:
        print("\n\nInterrupted by user", file=sys.stderr)
        sys.exit(130)


if __name__ == "__main__":
    main()
