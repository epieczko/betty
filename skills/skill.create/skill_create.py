#!/usr/bin/env python3
"""
Skill Create - Implementation Script
Creates new Claude Code-compatible Skills inside the Betty Framework.

Usage:
    python skill_create.py <skill_name> "<description>" [--inputs input1,input2] [--outputs output1,output2]
"""

import os
import sys
import yaml
import json
import argparse
from datetime import datetime, timezone
import subprocess

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
SKILLS_DIR = os.path.join(BASE_DIR, "skills")
REGISTRY_FILE = os.path.join(BASE_DIR, "registry", "skills.json")
VALIDATOR_PATH = os.path.join(BASE_DIR, "tools", "skill_define.py")

def ensure_dirs():
    os.makedirs(SKILLS_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(REGISTRY_FILE), exist_ok=True)

def run_validator(skill_path):
    """Run skill.define validator if available."""
    if os.path.exists(VALIDATOR_PATH):
        print(f"🔍 Validating new skill with {VALIDATOR_PATH}...")
        subprocess.run([sys.executable, VALIDATOR_PATH, skill_path])
    else:
        print("⚠ skill_define.py not found — skipping validation.")

def update_registry(manifest):
    """Add the new skill manifest to registry/skills.json."""
    ensure_dirs()
    registry = {"registry_version": "1.0.0", "generated_at": datetime.utcnow().isoformat(), "skills": []}

    if os.path.exists(REGISTRY_FILE):
        try:
            with open(REGISTRY_FILE) as f:
                registry = json.load(f)
        except Exception:
            pass

    # Replace entry if skill already exists
    registry["skills"] = [s for s in registry["skills"] if s.get("name") != manifest["name"]]
    registry["skills"].append(manifest)

    with open(REGISTRY_FILE, "w") as f:
        json.dump(registry, f, indent=2)

def create_skill(skill_name, description, inputs, outputs):
    """Scaffold a new skill directory and manifest."""
    folder_path = os.path.join(SKILLS_DIR, skill_name)
    if os.path.exists(folder_path):
        print(f"⚠ Skill {skill_name} already exists.")
        return

    os.makedirs(folder_path, exist_ok=True)
    manifest = {
        "name": skill_name,
        "version": "0.1.0",
        "description": description,
        "inputs": inputs,
        "outputs": outputs,
        "dependencies": ["skill.define"],
        "status": "draft",
    }

    # Write skill.yaml
    manifest_path = os.path.join(folder_path, "skill.yaml")
    with open(manifest_path, "w") as f:
        yaml.dump(manifest, f, sort_keys=False)

    # Create minimal SKILL.md
    skill_md = os.path.join(folder_path, "SKILL.md")
    with open(skill_md, "w") as f:
        f.write(f"---\nname: {skill_name}\ndescription: {description}\n---\n\n")
        f.write(f"# {skill_name}\n\nAuto-generated via `skill.create`.\n")

    print(f"✅ Created new skill: {skill_name}")
    print(f"📄 Manifest: {manifest_path}")

    # Validate
    run_validator(manifest_path)

    # Update registry using registry.update skill
    registry_updater = os.path.join(BASE_DIR, "skills", "registry.update", "registry_update.py")
    if os.path.exists(registry_updater):
        print("🔁 Updating registry via registry.update...")
        subprocess.run([sys.executable, registry_updater, manifest_path])
    else:
        print("⚠ registry.update not found — writing directly as fallback.")
        update_registry(manifest)


def main():
    parser = argparse.ArgumentParser(description="Create a new Betty Framework Skill.")
    parser.add_argument("skill_name", help="Name of the new skill (e.g., runtime.execute)")
    parser.add_argument("description", help="Description of what the skill does.")
    parser.add_argument("--inputs", help="Comma-separated list of inputs", default="")
    parser.add_argument("--outputs", help="Comma-separated list of outputs", default="")
    args = parser.parse_args()

    inputs = [i.strip() for i in args.inputs.split(",") if i.strip()]
    outputs = [o.strip() for o in args.outputs.split(",") if o.strip()]

    create_skill(args.skill_name, args.description, inputs, outputs)

if __name__ == "__main__":
    main()
