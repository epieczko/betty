# Betty Skills Framework


This document defines the complete taxonomy of skills that make up the Betty Framework.  
Each skill is implemented as a Claude Code-compatible plugin and published through the Betty Marketplace once certified.

---

## 1. Core Definition Skills (The Betty Kernel)

| Skill ID | Description |
|-----------|--------------|
| `agent.define` | Create and validate agent manifests. |
| `skill.define` | Define, validate, and version skill manifests. |
| `command.define` | Register executable commands and their I/O schemas. |
| `hook.define` | Create pre- and post-execution hooks for skills and workflows. |
| `context.schema` | Define and validate structured context objects shared between skills. |
| `evaluation.define` | Define evaluation metrics and test conditions for skills. |

---

## 2. Runtime & Execution Skills

| Skill ID | Description |
|-----------|--------------|
| `runtime.execute` | Execute skills or workflows within the Claude Code runtime. |
| `workflow.compose` | Compose declarative, multi-step workflows. |
| `hook.run` | Execute pre- and post-execution hooks. |
| `sandbox.run` | Run commands in isolated, secure sandboxes. |
| `policy.enforce` | Enforce Betty governance policies during execution. |

---

## 3. Integration & Marketplace Skills

| Skill ID | Description |
|-----------|--------------|
| `plugin.install` | Install and update Claude Code plugins from sources. |
| `marketplace.sync` | Sync available plugins from the RiskExec Marketplace. |
| `registry.update` | Update the Betty Skill Registry with new definitions. |
| `dependency.graph` | Generate dependency maps between skills and agents. |
| `tool.register` | Register external tools or APIs for use in workflows. |

---

## 4. Governance & Observability Skills

| Skill ID | Description |
|-----------|--------------|
| `audit.log` | Log all skill and agent executions with structured metadata. |
| `telemetry.capture` | Collect runtime metrics for analysis and optimization. |
| `provenance.track` | Track data lineage across the SDLC. |
| `qa.evaluate` | Run QA checks and validation suites. |
| `policy.validate` | Validate outputs against organizational and compliance policies. |

---

## 5. Lifecycle & Evolution Skills

| Skill ID | Description |
|-----------|--------------|
| `bootstrap.project` | Initialize new Betty projects and repositories. |
| `update.self` | Update Betty’s own skills and core logic. |
| `refactor.skill` | Refactor and migrate skills to new versions. |
| `archive.deprecated` | Deactivate and archive outdated skills. |
| `generate.docs` | Automatically generate documentation from manifests. |

---

## 6. Meta & Self-Referential Skills (Betty Bootstrapping Layer)

| Skill ID | Description |
|-----------|--------------|
| `skill.clone` | Clone existing skill manifests. |
| `skill.compose` | Compose multiple skills into a composite skill. |
| `skill.inspect` | Inspect and summarize skill metadata. |
| `skill.evaluate` | Test and evaluate skill performance. |
| `skill.publish` | Publish skills to the Marketplace after validation. |

---

## Notes

- Skills marked as **core** are required for any Betty-based project.
- Non-core skills can be installed independently as plugins.
- All skills will include manifests in `/skills/<name>/skill.yaml`.
- Each category will have a `README.md` describing its scope and current implementation status.

---

## Next Steps

1. Scaffold each skill folder under `/skills/`.
2. Create a minimal `skill.yaml` and `README.md` for each skill.
3. Generate `/registry/skills.json` once all skills have placeholders.
