# Setting Up Zally for Complete API Validation

## What is Zally?

Zally is Zalando's official API linter that validates OpenAPI specifications against their complete RESTful API Guidelines (100+ rules).

**Official Repository**: https://github.com/zalando/zally

## Why Use Zally?

- ✅ **Complete validation**: 100+ rules vs Betty's built-in 14 rules
- ✅ **Official**: Maintained by Zalando
- ✅ **Always up-to-date**: New guidelines added automatically
- ✅ **Authoritative**: "Validated with Zally" is the gold standard

## Betty's Integration Strategy

Betty automatically uses Zally if available, otherwise falls back to built-in validator:

```bash
# Betty checks if Zally is running
# If yes → uses Zally (100+ rules)
# If no → uses built-in (14 rules) + shows warning

python skills/api.validate/api_validate.py specs/user.yaml zalando
```

---

## Installation Options

### Option 1: Docker Compose (Recommended)

**Easiest way to run Zally server**

1. **Create docker-compose.yml**:
```yaml
version: '3'
services:
  zally:
    image: zalando/zally:latest
    ports:
      - "8000:8000"
    environment:
      - SPRING_PROFILES_ACTIVE=dev
```

2. **Start Zally**:
```bash
docker-compose up -d
```

3. **Verify it's running**:
```bash
curl http://localhost:8000/health
# Should return: {"status":"UP"}
```

4. **Validate with Betty**:
```bash
python skills/api.validate/api_validate.py specs/user.yaml zalando
# Betty will automatically detect and use Zally
```

---

### Option 2: Docker Run (Simple)

**Quick one-liner**

```bash
docker run -d -p 8000:8000 zalando/zally:latest
```

---

### Option 3: Build from Source

**For development or customization**

1. **Clone Zally**:
```bash
git clone https://github.com/zalando/zally.git
cd zally
```

2. **Build and run**:
```bash
./gradlew bootRun
```

Zally will start on http://localhost:8000

---

## Usage with Betty

### Automatic (Recommended)

Betty automatically detects Zally:

```bash
# Just run validation as normal
python skills/api.validate/api_validate.py specs/user.yaml zalando

# If Zally is running:
# → Uses Zally (100+ rules)
# → Shows: "Using Zally for complete Zalando validation"

# If Zally is not running:
# → Uses built-in (14 rules)
# → Shows warning with setup instructions
```

### Force Built-in Validator

If you want to use only Betty's built-in validator (faster, but fewer rules):

```bash
python skills/api.validate/api_validate.py specs/user.yaml zalando --use-builtin
```

---

## Validation Comparison

### With Zally (100+ rules)
```bash
$ python skills/api.validate/api_validate.py specs/user.yaml zalando

Using Zally for complete Zalando validation (100+ rules)

✅ Validation PASSED
- Checked: 127 rules
- Errors: 0
- Warnings: 3
```

### With Built-in (14 rules)
```bash
$ python skills/api.validate/api_validate.py specs/user.yaml zalando --use-builtin

Using built-in validator (14 rules)

✅ Validation PASSED
- Checked: 14 rules
- Errors: 0
- Warnings: 2
```

---

## Troubleshooting

### Zally Not Detected

**Problem**: Betty says "Zally server not available"

**Solution**:
1. Check if Zally is running:
   ```bash
   curl http://localhost:8000/health
   ```

2. If not running, start it:
   ```bash
   docker-compose up -d
   ```

3. If running but not detected, check the port:
   ```bash
   # Betty looks for Zally at http://localhost:8000
   # If running on different port, update ZALLY_SERVER_URL in api_validate.py
   ```

### Docker Not Installed

**Problem**: Don't have Docker

**Solution**: Use Betty's built-in validator (14 rules):
```bash
python skills/api.validate/api_validate.py specs/user.yaml zalando --use-builtin
```

While not complete, it still validates:
- Required metadata (x-api-id, x-audience)
- Naming conventions (snake_case)
- Error response formats (RFC 7807)
- HTTP headers (X-Flow-ID)
- Basic HTTP method usage

---

## Recommended Workflow

### Development
Use built-in validator for speed:
```bash
python skills/api.validate/api_validate.py specs/user.yaml zalando --use-builtin
```

### Pre-commit / CI/CD
Use Zally for complete validation:
```bash
# Start Zally in CI
docker run -d -p 8000:8000 zalando/zally:latest

# Wait for it to be ready
sleep 5

# Run validation
python skills/api.validate/api_validate.py specs/user.yaml zalando

# Betty will use Zally automatically
```

---

## Configuration

### Custom Zally Server URL

If running Zally on a different host/port, update:

```python
# skills/api.validate/api_validate.py
ZALLY_SERVER_URL = "http://your-zally-server:8000"
```

Or set environment variable:
```bash
export ZALLY_URL=http://your-zally-server:8000
```

---

## Zally Web UI (Bonus)

Zally also provides a web interface:

1. Start Zally with web UI:
```bash
docker-compose up
```

2. Open browser to http://localhost:8000

3. Paste your OpenAPI spec and get visual validation results

---

## Summary

**Quick Setup**:
```bash
# 1. Start Zally
docker run -d -p 8000:8000 zalando/zally:latest

# 2. Validate with Betty (automatically uses Zally)
python skills/api.validate/api_validate.py specs/user.yaml zalando

# Done! You're now using official Zalando validation
```

**Without Zally**:
```bash
# Betty falls back to built-in validator
python skills/api.validate/api_validate.py specs/user.yaml zalando --use-builtin
```

---

## See Also

- [Zally GitHub](https://github.com/zalando/zally)
- [Zalando API Guidelines](https://opensource.zalando.com/restful-api-guidelines/)
- [Betty API Validation](../skills/api.validate/SKILL.md)
