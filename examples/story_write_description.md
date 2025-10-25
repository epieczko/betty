# Name: story.write

# Purpose:
Convert decomposed items from epic.decompose into fully formatted user stories. Generates individual Markdown files for each story following standard user story format.

# Inputs:
- stories_file (string, required): Path to the stories.json file from epic.decompose
- epic_reference (string, optional): Reference to the source Epic for traceability
- output_dir (string, optional): Directory to save story files (default: ./stories/)

# Outputs:
- story_<n>.md: Markdown file per story with persona, goal, benefit, acceptance criteria, and metadata
- stories_index.md: Summary index of all created stories

# Consumes Artifacts:
- user-stories-list

# Produces Artifacts:
- user-story

# Permissions:
- filesystem:read
- filesystem:write

# Implementation Notes:
Load and parse stories.json. Generate unique story ID for each item. Format as standard user story (As a/I want/So that). Convert acceptance criteria to checklist format. Add traceability links to Epic. Include metadata for tracking. Create summary index file listing all stories. Support batch processing. Validate each story against INVEST criteria.

# Examples:
- python3 skills/story.write/story_write.py --stories-file ./stories.json --epic-reference "EPIC-001" --output-dir ./stories/
