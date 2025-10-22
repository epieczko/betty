#!/usr/bin/env python3
"""
skill_define.py – Implementation of the skill.define Skill
Validates skill manifests (.skill.yaml) and registers them in the Skill Registry.
"""

import os, sys, json, yaml
from datetime import datetime, timezone

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
REGISTRY = os.path.join(BASE, "registry", "skills.json")
REQUIRED_FIELDS = ["name", "version", "description", "inputs", "outputs", "status"]

def validate_manifest(path):
    """Validate that required fields exist in a skill manifest."""
    try:
        with open(path) as f:
            manifest = yaml.safe_load(f)
    except Exception as e:
        return {"valid": False, "error": f"Failed to parse YAML: {e}"}

    missing = [f for f in REQUIRED_FIELDS if f not in manifest]
    valid = not missing
    return {
        "valid": valid,
        "missing": missing,
        "path": path,
        "manifest": manifest if valid else None
    }

def update_registry(manifest):
    """Add or update the skill manifest in the registry."""
    os.makedirs(os.path.dirname(REGISTRY), exist_ok=True)
    registry = {"registry_version": "1.0.0", "generated_at": datetime.now(timezone.utc).isoformat(), "skills": []}

    if os.path.exists(REGISTRY):
        try:
            with open(REGISTRY) as f:
                registry = json.load(f)
        except Exception:
            pass

    # Replace or append entry
    registry["skills"] = [s for s in registry["skills"] if s.get("name") != manifest["name"]]
    registry["skills"].append(manifest)

    with open(REGISTRY, "w") as f:
        json.dump(registry, f, indent=2)

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: skill_define.py <path_to_skill.yaml>"}))
        sys.exit(1)

    path = sys.argv[1]
    result = validate_manifest(path)

    if result["valid"]:
        registry_updater = os.path.join(BASE_DIR, "skills", "registry.update", "registry_update.py")
        manifest_path = path
        if os.path.exists(registry_updater):
            print("🔁 Delegating registry update to registry.update skill...")
            subprocess.run([sys.executable, registry_updater, manifest_path])
        else:
            update_registry(result["manifest"])
        result["status"] = "registered"
Hello.

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
