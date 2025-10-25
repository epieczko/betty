# File.Processor Agent

## Purpose

Processes files through various transformations including format conversion, compression, encryption, and batch operations.

## Skills

This agent uses the following skills:


## Artifact Flow

### Consumes

- `file-list`
- `transformation-config`

### Produces

- `processed-files`
- `processing-report`
- `file.convert`
- `file.compress`
- `file.encrypt`
- `batch.processor`
- `Sequential: Process files one by one`
- `Parallel: Process multiple files concurrently`
- `Pipeline: Chain multiple transformations`
- `Files processed successfully`
- `Files that failed with error details`
- `Processing time and performance metrics`
- `Storage space saved`
- `Transformation details for each file`

## Usage

```bash
# Activate the agent
/agent file.processor

# Or invoke directly
betty agent run file.processor --input <path>
```

## Created By

This agent was created by **meta.agent**, the meta-agent for creating agents.

---

*Part of the Betty Framework*
