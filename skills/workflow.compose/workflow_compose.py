#!/usr/bin/env python3
"""
workflow_compose.py – Implementation of the workflow.compose Skill
Executes multi-step Betty Framework workflows by chaining existing skills.
"""

import os, sys, yaml, subprocess, json
from datetime import datetime

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
WORKFLOW_LOG = os.path.join(BASE, "registry", "workflow_history.json")

def run_skill(skill_path, args):
    """Run a skill handler as a subprocess."""
    print(f"▶ Running {skill_path} {' '.join(args)}")
    result = subprocess.run([sys.executable, skill_path] + args, capture_output=True, text=True)
    print(result.stdout)
    return result.stdout

def execute_workflow(workflow_file):
    """Read a workflow YAML and execute skills in order."""
    with open(workflow_file) as f:
        workflow = yaml.safe_load(f)

    log = {
        "workflow": os.path.basename(workflow_file),
        "timestamp": datetime.utcnow().isoformat(),
        "steps": []
    }

    for step in workflow.get("steps", []):
        skill_name = step["skill"]
        handler = os.path.join(BASE, "skills", skill_name, f"{skill_name.replace('.', '_')}.py")

        args = step.get("args", [])
        print(f"\n=== Executing {skill_name} ===")
        output = run_skill(handler, args)
        log["steps"].append({
            "skill": skill_name,
            "args": args,
            "output": output.strip()
        })

    # Save workflow history
    os.makedirs(os.path.dirname(WORKFLOW_LOG), exist_ok=True)
    history = []
    if os.path.exists(WORKFLOW_LOG):
        try:
            with open(WORKFLOW_LOG) as f:
                history = json.load(f)
        except Exception:
            pass
    history.append(log)
    with open(WORKFLOW_LOG, "w") as f:
        json.dump(history, f, indent=2)
    print(f"\n✅ Workflow completed. Log saved to {WORKFLOW_LOG}")

def main():
    if len(sys.argv) < 2:
        print("Usage: workflow_compose.py <workflow.yaml>")
        sys.exit(1)
    execute_workflow(sys.argv[1])

if __name__ == "__main__":
    main()
