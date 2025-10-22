#!/usr/bin/env python3
"""
registry_update.py – Implementation of the registry.update Skill
Adds, updates, or removes entries in the Betty Framework Skill Registry.
"""

import os, sys, json, yaml
from datetime import datetime, timezone

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
REGISTRY = os.path.join(BASE, "registry", "skills.json")

def load_manifest(path):
    with open(path) as f:
        return yaml.safe_load(f)

def load_registry():
    if not os.path.exists(REGISTRY):
        return {"registry_version": "1.0.0", "generated_at": datetime.now(timezone.utc).isoformat(), "skills": []}
    with open(REGISTRY) as f:
        return json.load(f)

def save_registry(registry):
    registry["generated_at"] = datetime.now(timezone.utc).isoformat()
    os.makedirs(os.path.dirname(REGISTRY), exist_ok=True)
    with open(REGISTRY, "w") as f:
        json.dump(registry, f, indent=2)

def update_registry(manifest_path):
    """Add or update a skill manifest in the registry."""
    manifest = load_manifest(manifest_path)
    registry = load_registry()

    # Replace or append entry
    registry["skills"] = [s for s in registry["skills"] if s.get("name") != manifest["name"]]
    registry["skills"].append(manifest)
    save_registry(registry)

    return {
        "status": "success",
        "updated": manifest["name"],
        "registry_path": REGISTRY,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: registry_update.py <path_to_skill.yaml>"}))
        sys.exit(1)

    path = sys.argv[1]
    result = update_registry(path)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
