# Betty API Development Commands

## ⚙️ **Integration Note: Claude Code Plugin System**

**Betty commands are Claude Code slash commands.** These commands are **executed by Claude Code**, not by a standalone `betty` CLI.

- **Claude Code provides the runtime** for all command execution
- Commands are defined in `.claude/commands/` as markdown files
- Commands are automatically discovered and available in Claude Code's command palette
- Typing `/` in Claude Code shows all available Betty commands

**No separate installation is needed** — commands are available immediately when you run Claude Code in the Betty repository.

---

These slash commands provide a simplified interface for API-driven development with Betty.

## Available Commands

### `/api-design <service-name>`

Design a complete API from scratch with automatic validation and code generation.

**Example:**
```
/api-design user-service
```

**What it does:**
1. Creates Zalando-compliant OpenAPI specification
2. Validates spec (0 errors guaranteed)
3. Generates TypeScript models
4. Generates Python models

**Output:**
- `specs/user-service.openapi.yaml` - API specification
- `src/models/user-service/*.ts` - TypeScript interfaces
- `backend/models/user-service/*.py` - Python dataclasses

---

### `/api-validate <spec-path>`

Validate an API specification against enterprise guidelines.

**Example:**
```
/api-validate specs/user-service.openapi.yaml
```

**What it does:**
1. Validates spec against Zalando RESTful API Guidelines
2. Shows errors and warnings with explanations
3. Suggests fixes for any issues

**Checks:**
- Required metadata (x-api-id, x-audience)
- Naming conventions (snake_case properties)
- HTTP method usage
- Error response formats (RFC 7807)
- Security schemes

---

### `/api-generate <spec-path> <language>`

Generate type-safe models from an API specification.

**Examples:**
```
/api-generate specs/user-service.openapi.yaml typescript
/api-generate specs/user-service.openapi.yaml python
```

**Supported Languages:**
- `typescript` - TypeScript interfaces
- `python` - Python dataclasses
- `java` - Java classes (planned)
- `go` - Go structs (planned)
- `csharp` - C# classes (planned)

**Output:**
- Type-safe model files in specified output directory
- Proper typing and optional fields
- Documentation comments from spec

---

### `/api-compatibility <old-spec> <new-spec>`

Check for breaking changes between API versions.

**Example:**
```
/api-compatibility specs/user-v1.yaml specs/user-v2.yaml
```

**What it does:**
1. Compares two specification versions
2. Identifies breaking changes
3. Categorizes changes (breaking vs non-breaking)
4. Provides migration recommendations

**Breaking Changes Detected:**
- Removed endpoints or operations
- Removed schemas or properties
- Changed property types
- Made optional fields required

**Non-Breaking Changes:**
- Added endpoints or operations
- Added optional properties
- Added new schemas

---

## Quick Start

### Design a New API

```bash
# One command does everything
/api-design payment-service

# Result: Complete API with validated spec and generated models
```

### Validate an Existing API

```bash
/api-validate specs/payment-service.openapi.yaml

# Fix any issues, then generate models
/api-generate specs/payment-service.openapi.yaml typescript
```

### Check Compatibility Before Release

```bash
/api-compatibility specs/payment-v1.yaml specs/payment-v2.yaml

# If breaking changes found, fix them or bump major version
```

---

## Integration with Hooks

Commands work seamlessly with Betty's automatic validation hooks:

- Edit `*.openapi.yaml` → Automatic validation on save
- Commit changes → Automatic compatibility check
- Push to remote → Full validation suite runs

---

## See Also

- [Betty Architecture](../../docs/betty-architecture.md) - Understand the five-layer model
- [API-Driven Development Guide](../../docs/api-driven-development.md) - Complete workflow guide
- [Skill Documentation](../../skills/) - Individual skill references
