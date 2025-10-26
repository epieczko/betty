# Betty Taxonomy Specification

## Canonical Domains

The following ten domains organize all Betty components:

- **architecture**: 14 skills, 0 agents
- **api**: 5 skills, 3 agents
- **data**: 1 skills, 2 agents
- **security**: 0 skills, 1 agents
- **testing**: 1 skills, 1 agents
- **deployment**: 3 skills, 0 agents
- **governance**: 5 skills, 0 agents
- **docs**: 5 skills, 0 agents
- **operations**: 9 skills, 5 agents
- **ai**: 6 skills, 8 agents

## Functional Roles

Components are assigned one of seven functional roles:

- **create**: Components that create artifacts or processes
- **validate**: Components that validate artifacts or processes
- **review**: Components that review artifacts or processes
- **analyze**: Components that analyze artifacts or processes
- **orchestrate**: Components that orchestrate artifacts or processes
- **govern**: Components that govern artifacts or processes
- **observe**: Components that observe artifacts or processes

## Naming Standards

### Skills
- Format: `domain.action`
- Example: `api.validate`, `docs.sync.readme`

### Agents
- Format: `domain.role`
- Example: `api.analyzer`, `security.architect`

### Hooks
- Format: `on_<event>__<target>` or `pre_/post_<event>`
- Example: `on_commit__policy-enforce`

### Commands
- Format: `/domain-action`
- Example: `/api-validate`, `/create-pr`
