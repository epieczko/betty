# Betty Framework Marketplace

A lightweight, static JSON-based catalog of certified Betty skills and agents, designed for discoverability and integration with Claude Code.

## Overview

The Betty Marketplace provides a curated collection of production-ready skills and agents that have been validated against the Betty Framework's quality standards. This enables Claude and other AI agents to discover and utilize certified capabilities.

## Structure

```
marketplace/
├── skills.json      # Certified skills catalog
├── agents.json      # Certified agents catalog
└── README.md        # This file
```

## Catalog Schema

### Skills Catalog (`skills.json`)

Each skill entry includes:

- **name**: Unique skill identifier (e.g., `api.validate`)
- **version**: Semantic version number
- **description**: Clear description of functionality
- **status**: Certification level (`certified` or `draft`)
- **tags**: Searchable keywords
- **maintainer**: Team or individual responsible
- **usage_examples**: Practical command examples
- **documentation_url**: Link to full documentation
- **dependencies**: Required skills
- **entrypoints**: Available command interfaces
- **inputs**: Expected input parameters
- **outputs**: Generated outputs

### Agents Catalog (`agents.json`)

Each agent entry includes:

- **name**: Unique agent identifier (e.g., `api.designer`)
- **version**: Semantic version number
- **description**: Clear description of capabilities
- **status**: Certification level (`certified` or `draft`)
- **tags**: Searchable keywords
- **maintainer**: Team or individual responsible
- **usage_examples**: Practical usage scenarios
- **documentation_url**: Link to full documentation
- **reasoning_mode**: Agent reasoning type (`iterative`, `oneshot`, etc.)
- **skills_available**: Skills the agent can use
- **capabilities**: What the agent can accomplish
- **dependencies**: Required skills or components

## Certification Levels

### Certified
Production-ready skills/agents that have:
- Passed validation tests
- Complete documentation
- Defined usage examples
- Active maintenance commitment

### Draft
Work-in-progress skills/agents that:
- May have incomplete features
- Are under active development
- Not recommended for production use

## Generating the Marketplace

The marketplace is generated from the Betty Framework registry using the `generate_marketplace.py` script.

### Basic Usage

```bash
# Generate marketplace with certified items only
python generate_marketplace.py

# Include draft items
python generate_marketplace.py --include-drafts

# Custom paths
python generate_marketplace.py --registry-dir path/to/registry --output-dir path/to/output
```

### Automation

Add to your CI/CD pipeline:

```yaml
# .github/workflows/marketplace.yml
name: Update Marketplace

on:
  push:
    branches: [main]
    paths:
      - 'registry/**'

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Generate Marketplace
        run: python generate_marketplace.py
      - name: Commit Changes
        run: |
          git config user.name "Betty Bot"
          git config user.email "bot@betty-framework.dev"
          git add marketplace/
          git commit -m "Update marketplace catalog" || exit 0
          git push
```

## Using the Marketplace

### Query Available Skills

```python
import json
import requests

# Load from local file
with open('marketplace/skills.json') as f:
    marketplace = json.load(f)

# Or fetch from GitHub Pages
url = 'https://your-org.github.io/betty/marketplace/skills.json'
marketplace = requests.get(url).json()

# Find skills by tag
api_skills = [
    skill for skill in marketplace['catalog']
    if 'api' in skill.get('tags', [])
]

# Find certified skills only
certified = [
    skill for skill in marketplace['catalog']
    if skill['status'] == 'certified'
]
```

### Claude Integration

Claude can reference the marketplace to discover available capabilities:

```
User: "I need to validate an OpenAPI spec"

Claude: "I can help with that using the certified api.validate skill from the Betty Marketplace.

        Usage: /skill/api/validate --spec_path api.yaml --guideline_set zalando

        This skill validates OpenAPI and AsyncAPI specifications against enterprise guidelines."
```

## Accessing the Marketplace

### Option 1: Local File Access

```bash
cat marketplace/skills.json | jq '.catalog[] | select(.tags[] == "api")'
```

### Option 2: GitHub Pages (Recommended)

1. Enable GitHub Pages in repository settings
2. Set source to `main` branch, `/marketplace` folder
3. Access via: `https://your-org.github.io/betty/marketplace/skills.json`

### Option 3: Internal HTTP Endpoint

Host the marketplace files on your internal infrastructure:

```nginx
# nginx.conf
location /marketplace/ {
    alias /path/to/betty/marketplace/;
    add_header Access-Control-Allow-Origin *;
    add_header Content-Type application/json;
}
```

## Marketplace Statistics

View current marketplace stats:

```bash
python generate_marketplace.py 2>&1 | tail -n 10
```

Example output:
```
✓ Skills marketplace generated: marketplace/skills.json
  - Total: 14
  - Certified: 14
  - Draft: 0

✓ Agents marketplace generated: marketplace/agents.json
  - Total: 2
  - Certified: 0
  - Draft: 2
```

## Adding New Skills/Agents

To add your skill or agent to the marketplace:

1. Ensure it's registered in `registry/skills.json` or `registry/agents.json`
2. Set `status: "active"` for skills (or `status: "certified"` for agents)
3. Add metadata in `generate_marketplace.py`:

```python
SKILL_METADATA = {
    "my.skill": {
        "maintainer": "Your Team",
        "certification_status": "certified",
        "usage_examples": [
            "Example usage: /skill/my.skill --param value"
        ],
        "documentation_url": "https://docs.example.com/my-skill"
    }
}
```

4. Run `python generate_marketplace.py` to regenerate the catalog

## Versioning

The marketplace uses semantic versioning:

- **marketplace_version**: Schema version for the catalog format
- **Individual items**: Each skill/agent has its own version

Breaking changes to the catalog schema will increment the major version.

## API

### Endpoints

If hosted via HTTP:

- `GET /marketplace/skills.json` - Full skills catalog
- `GET /marketplace/agents.json` - Full agents catalog

### Response Format

```json
{
  "marketplace_version": "1.0.0",
  "generated_at": "2025-10-23T17:04:16.151865+00:00",
  "description": "Betty Framework Certified Skills Marketplace",
  "total_skills": 14,
  "certified_count": 14,
  "draft_count": 0,
  "catalog": [...]
}
```

## Contributing

To contribute to the marketplace:

1. Create a new skill/agent following Betty Framework standards
2. Add appropriate tests and documentation
3. Submit for certification review
4. Update metadata in `generate_marketplace.py`
5. Submit a pull request

## Support

- Documentation: https://betty-framework.dev/docs
- Issues: https://github.com/your-org/betty/issues
- Discussions: https://github.com/your-org/betty/discussions

## License

The Betty Marketplace catalog is provided under the same license as the Betty Framework.
