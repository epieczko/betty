# Name: epic.decompose

# Purpose:
Take an Epic (as Markdown) and decompose it into user stories. Analyzes Epic document and identifies major deliverables, grouping them by persona or capability.

# Inputs:
- epic_file (string, required): Path to the epic.md file to decompose
- max_stories (integer, optional): Maximum number of stories to generate (default: 5)
- output_path (string, optional): Where to save the stories.json file (default: ./stories.json)

# Outputs:
- stories.json: Structured JSON list of story summaries with persona, goal, benefit, and acceptance criteria

# Consumes Artifacts:
- agile-epic

# Produces Artifacts:
- user-stories-list

# Permissions:
- filesystem:read
- filesystem:write

# Implementation Notes:
Parse Markdown structure to extract Epic components. Use NLP techniques to identify distinct user stories. Ensure stories are independent and testable (INVEST criteria). Generate meaningful acceptance criteria. Validate output against JSON schema. Include metadata for traceability to source Epic.

# Examples:
- python3 skills/epic.decompose/epic_decompose.py --epic-file ./epic.md --max-stories 5
