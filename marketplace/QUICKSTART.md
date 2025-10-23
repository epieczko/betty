# Marketplace Quick Start

Get started with the Betty Framework Marketplace in 5 minutes.

## Quick Links

- **Browse Online**: [View Marketplace](./index.html)
- **Skills API**: [skills.json](./skills.json)
- **Agents API**: [agents.json](./agents.json)

## For Developers

### 1. Generate the Marketplace

```bash
# Install Betty Framework
git clone https://github.com/your-org/betty.git
cd betty

# Generate marketplace (certified items only)
python generate_marketplace.py

# Include drafts for development
python generate_marketplace.py --include-drafts
```

### 2. Query the Catalog

**Find Skills by Tag:**
```bash
# Using jq
cat marketplace/skills.json | jq '.catalog[] | select(.tags[] == "api")'

# Using Python
python -c "
import json
with open('marketplace/skills.json') as f:
    data = json.load(f)
    api_skills = [s for s in data['catalog'] if 'api' in s.get('tags', [])]
    print(json.dumps(api_skills, indent=2))
"
```

**Find Certified Skills:**
```bash
cat marketplace/skills.json | jq '.catalog[] | select(.status == "certified")'
```

### 3. Use in Your Code

**Python:**
```python
import json
import requests

# From local file
with open('marketplace/skills.json') as f:
    marketplace = json.load(f)

# From GitHub Pages
url = 'https://your-org.github.io/betty/marketplace/skills.json'
marketplace = requests.get(url).json()

# Find a specific skill
skill = next(s for s in marketplace['catalog'] if s['name'] == 'api.validate')
print(f"Skill: {skill['name']}")
print(f"Description: {skill['description']}")
print(f"Usage: {skill['usage_examples'][0]}")
```

**JavaScript/Node.js:**
```javascript
const fs = require('fs');

// From local file
const marketplace = JSON.parse(fs.readFileSync('marketplace/skills.json'));

// From URL
fetch('https://your-org.github.io/betty/marketplace/skills.json')
  .then(res => res.json())
  .then(marketplace => {
    const apiSkills = marketplace.catalog.filter(s =>
      s.tags && s.tags.includes('api')
    );
    console.log(`Found ${apiSkills.length} API skills`);
  });
```

**cURL:**
```bash
# Get all skills
curl https://your-org.github.io/betty/marketplace/skills.json

# Get specific skill (with jq)
curl -s https://your-org.github.io/betty/marketplace/skills.json | \
  jq '.catalog[] | select(.name == "api.validate")'
```

## For Claude/AI Agents

### Reference the Marketplace

```
Claude can discover available skills from the Betty Marketplace:

User: "I need to validate an OpenAPI specification"

Claude queries the marketplace:
- GET marketplace/skills.json
- Filters for skills with tag "api" and "validation"
- Finds "api.validate" skill
- Responds with usage example
```

### Integration Pattern

```python
# AI agent integration example
class BettyMarketplaceClient:
    def __init__(self, marketplace_url):
        self.marketplace_url = marketplace_url
        self.skills = self._load_skills()

    def _load_skills(self):
        response = requests.get(f"{self.marketplace_url}/skills.json")
        return response.json()['catalog']

    def find_skills_by_capability(self, query):
        """Find skills matching a natural language query."""
        results = []
        query_lower = query.lower()

        for skill in self.skills:
            # Search in name, description, and tags
            if (query_lower in skill['name'].lower() or
                query_lower in skill['description'].lower() or
                any(query_lower in tag.lower() for tag in skill.get('tags', []))):
                results.append(skill)

        return results

    def get_skill_usage(self, skill_name):
        """Get usage examples for a specific skill."""
        skill = next((s for s in self.skills if s['name'] == skill_name), None)
        if skill:
            return skill.get('usage_examples', [])
        return []

# Usage
client = BettyMarketplaceClient('https://your-org.github.io/betty/marketplace')
api_skills = client.find_skills_by_capability('api validation')
print(f"Found {len(api_skills)} skills for API validation")
```

## Common Use Cases

### 1. Discover All API-Related Skills

```bash
python -c "
import json
with open('marketplace/skills.json') as f:
    data = json.load(f)
    api_skills = [s['name'] for s in data['catalog'] if 'api' in s.get('tags', [])]
    print('API Skills:', ', '.join(api_skills))
"
```

### 2. Get Skill Documentation

```bash
python -c "
import json
with open('marketplace/skills.json') as f:
    data = json.load(f)
    skill = next(s for s in data['catalog'] if s['name'] == 'api.validate')
    print(f\"Documentation: {skill['documentation_url']}\")
"
```

### 3. List All Certified Skills

```bash
python -c "
import json
with open('marketplace/skills.json') as f:
    data = json.load(f)
    certified = [s['name'] for s in data['catalog'] if s['status'] == 'certified']
    print(f\"Certified skills ({len(certified)}):\")
    for skill in certified:
        print(f\"  - {skill}\")
"
```

### 4. Check Skill Dependencies

```bash
python -c "
import json
with open('marketplace/skills.json') as f:
    data = json.load(f)
    skill = next(s for s in data['catalog'] if s['name'] == 'workflow.compose')
    print(f\"Dependencies for {skill['name']}:\")
    for dep in skill.get('dependencies', []):
        print(f\"  - {dep}\")
"
```

## GitHub Pages Setup

Enable hosting for your organization:

1. Go to repository Settings → Pages
2. Source: Deploy from branch
3. Branch: `main`, Folder: `/marketplace`
4. Save

Your marketplace will be available at:
```
https://your-org.github.io/betty/marketplace/
```

## Automation

The marketplace auto-updates when registry changes:

```yaml
# Triggered by:
- Push to main branch with changes to registry/
- Manual workflow dispatch

# Generates:
- marketplace/skills.json
- marketplace/agents.json

# Commits:
- Automated commit with timestamp
```

## Next Steps

1. **Browse the catalog**: Open `marketplace/index.html` in a browser
2. **Add your skill**: Follow the [Contributing Guide](./README.md#adding-new-skillsagents)
3. **Integrate with Claude**: Reference marketplace in your prompts
4. **Automate updates**: Enable GitHub Actions workflow

## Support

- Issues: https://github.com/your-org/betty/issues
- Docs: https://betty-framework.dev/docs
- Discussions: https://github.com/your-org/betty/discussions
