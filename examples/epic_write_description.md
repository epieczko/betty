# Name: epic.write

# Purpose:
Generate an Agile Epic from a high-level goal, feature request, or strategic initiative. Creates structured Agile Epic document that follows best practices.

# Inputs:
- initiative_name (string, required): The overarching initiative or product goal
- context (string, required): Relevant background, rationale, and success criteria
- stakeholders (array of strings, required): Who cares about this and why
- output_path (string, optional): Where to save the epic.md file (default: ./epic.md)

# Outputs:
- epic.md: Markdown file with structured Epic fields (title, summary, background, acceptance criteria, stakeholders, next steps)

# Produces Artifacts:
- agile-epic

# Permissions:
- filesystem:read
- filesystem:write

# Implementation Notes:
Validate all required inputs are provided. Generate clear, measurable acceptance criteria. Format output following Agile Epic standards. Include metadata for artifact tracking. Provide clear guidance on next step (epic.decompose).

# Examples:
- python3 skills/epic.write/epic_write.py --initiative-name "Customer Self-Service Portal" --context "Enable customers to manage accounts" --stakeholders "Product Team,Engineering"
