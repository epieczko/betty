# Component Relationships

Inter-component dependencies and flows.

## Skills → Agents

```mermaid
graph LR
    skill_create[skill.create] --> meta_skill[meta.skill]
    skill_define[skill.define] --> meta_skill[meta.skill]
    artifact_define[artifact.define] --> meta_skill[meta.skill]
    artifact_create[artifact.create] --> security_architect[security.architect]
    artifact_validate[artifact.validate] --> security_architect[security.architect]
    artifact_review[artifact.review] --> security_architect[security.architect]
    agent_compose[agent.compose] --> meta_agent[meta.agent]
    artifact_define[artifact.define] --> meta_agent[meta.agent]
    registry_update[registry.update] --> meta_agent[meta.agent]
    workflow_validate[workflow.validate] --> data_validator[data.validator]
    api_validate[api.validate] --> data_validator[data.validator]
    hook_define[hook.define] --> meta_hook[meta.hook]
    hook_register[hook.register] --> meta_hook[meta.hook]
    hook_simulate[hook.simulate] --> meta_hook[meta.hook]
    artifact_create[artifact.create] --> strategy_architect[strategy.architect]
    artifact_validate[artifact.validate] --> strategy_architect[strategy.architect]
    artifact_review[artifact.review] --> strategy_architect[strategy.architect]
    artifact_create[artifact.create] --> governance_manager[governance.manager]
    artifact_validate[artifact.validate] --> governance_manager[governance.manager]
    artifact_review[artifact.review] --> governance_manager[governance.manager]
```

## Hooks → Commands

| Hook | Command |
|------|---------|
| `performance-monitor-pre` | `/performance` |
| `performance-monitor-post` | `/performance` |
| `auto-stage-edited-files` | `/dev` |
