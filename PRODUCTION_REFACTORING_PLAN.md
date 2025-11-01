# Production Refactoring Plan

**Goal:** Transform the policy compliance system from a working prototype into a production-ready Betty component.

**Target Completion:** All items below must be completed for production status.

---

## 🎯 Critical Issues to Fix

### 1. Make Skills Properly Importable ⚠️ CRITICAL

**Current State:**
```python
# Doesn't work:
from betty.skills.policy_define import define_policy
```

**Required Changes:**
```
skills/policy.define/
  __init__.py          # NEW - Export main functions
  policy_define.py     # REFACTOR - Make importable
  skill.yaml           # Keep

skills/policy.validate/
  __init__.py          # NEW
  policy_validate.py   # REFACTOR
  skill.yaml           # Keep

skills/notify.human/
  __init__.py          # NEW
  notify_human.py      # REFACTOR
  skill.yaml           # Keep
```

**Actions:**
- [ ] Create `__init__.py` for each skill
- [ ] Export main functions from each skill
- [ ] Ensure no side effects on import
- [ ] Make functions return structured data (not JSON strings)

---

### 2. Remove Subprocess Calls ⚠️ CRITICAL

**Current State:**
```python
# meta_policy_profile.py
result = subprocess.run(['python3', script_path] + args, ...)
# Parse stdout as JSON - FRAGILE!
```

**Required Changes:**
```python
# Direct imports
from betty.skills.policy_define import define_policy
from betty.skills.policy_validate import validate_policy
from betty.skills.audit_log import log_audit

# Direct calls
result = define_policy(spec_content, profile_name, ...)
# Clean data structures, no JSON parsing
```

**Actions:**
- [ ] Refactor meta_policy_profile.py to import directly
- [ ] Remove subprocess.run calls
- [ ] Remove JSON parsing logic
- [ ] Handle errors properly (exceptions, not exit codes)

---

### 3. Create CLI Wrapper ⚠️ HIGH PRIORITY

**Target UX:**
```bash
# Easy to use, no PYTHONPATH
betty-policy create my-profile --from spec.md
betty-policy list
betty-policy show strict
betty-policy validate manifest.yaml --profile strict
betty-policy test strict manifest.yaml
betty-policy diff strict default
```

**Implementation:**
```
bin/betty-policy           # Main CLI script
betty/cli/policy.py       # CLI implementation
```

**Actions:**
- [ ] Create `bin/betty-policy` CLI entry point
- [ ] Create `betty/cli/policy.py` with Click or argparse
- [ ] Add subcommands: create, list, show, validate, test, diff
- [ ] Make it work without PYTHONPATH hacks

---

### 4. Migrate Hardcoded Rules ⚠️ HIGH PRIORITY

**Current State:**
```python
# policy_enforce.py has hardcoded rules
ALLOWED_PERMISSIONS = {"filesystem", "network", ...}
VALID_NAME_PATTERN = r"^[a-z]..."
```

**Required Changes:**
```yaml
# registry/policies/betty-core.yaml
policy:
  name: betty-core
  version: 1.0.0
  description: Core Betty Framework validation rules
  rules:
    - field: name
      pattern: "^[a-z][a-z0-9.]*[a-z0-9]$"
      message: "Names must be lowercase with dots"
      severity: error
    - field: permissions
      forbidden_values: [...]
    # ... migrate all hardcoded rules
```

**Actions:**
- [ ] Create `betty-core.yaml` with all hardcoded rules
- [ ] Modify `policy.enforce` to load betty-core by default
- [ ] Remove hardcoded constants (or keep as fallback)
- [ ] Test backward compatibility

---

### 5. Add Discovery Tools ⚠️ MEDIUM PRIORITY

**Commands Needed:**
```bash
betty-policy list                    # List all profiles
betty-policy show strict             # Show rules in profile
betty-policy show strict --json      # Machine-readable
betty-policy test strict manifest    # Dry run
betty-policy diff strict default     # Compare profiles
```

**Implementation:**
```python
def list_profiles():
    """List all policy profiles in registry/policies/"""

def show_profile(name):
    """Display profile rules in human-readable format"""

def test_profile(profile, manifest):
    """Dry run - show what would happen"""

def diff_profiles(profile1, profile2):
    """Compare two profiles"""
```

**Actions:**
- [ ] Implement `list_profiles()`
- [ ] Implement `show_profile()`
- [ ] Implement `test_profile()`
- [ ] Implement `diff_profiles()`
- [ ] Add to CLI

---

### 6. Better Error Handling ⚠️ HIGH PRIORITY

**Current State:**
- Cryptic subprocess errors
- JSON parse failures
- Stack traces to users

**Required Changes:**
```python
class PolicyError(Exception):
    """Base exception for policy system"""

class PolicyValidationError(PolicyError):
    """Policy validation failed"""
    def __init__(self, errors, warnings):
        self.errors = errors
        self.warnings = warnings

class PolicyNotFoundError(PolicyError):
    """Profile not found"""

# Usage:
try:
    result = enforce_policy(...)
except PolicyValidationError as e:
    print(f"❌ Validation failed with {len(e.errors)} errors:")
    for error in e.errors:
        print(f"  - {error.message}")
    sys.exit(1)
```

**Actions:**
- [ ] Create custom exception classes
- [ ] Replace exit(1) with proper exceptions
- [ ] Add helpful error messages
- [ ] Suggest fixes when possible

---

### 7. Proper Registry Integration ⚠️ MEDIUM PRIORITY

**Current State:**
- Manual JSON edits
- No use of `registry.update` skill

**Required Changes:**
```python
# Use Betty's registry system
from betty.registry import register_skill, register_agent

register_skill('policy.define', {
    'name': 'policy.define',
    'version': '0.1.0',
    ...
})
```

**Actions:**
- [ ] Study how Betty's registry works
- [ ] Use `registry.update` skill properly
- [ ] Remove manual JSON edits
- [ ] Ensure registry consistency

---

### 8. Test Hook Integration ⚠️ MEDIUM PRIORITY

**Current State:**
- Hook created but `enabled: false`
- Never actually tested in real usage

**Required Actions:**
- [ ] Enable the hook temporarily
- [ ] Edit a skill.yaml file
- [ ] Verify hook triggers
- [ ] Check output is helpful (not annoying)
- [ ] Add option to configure which profiles to use
- [ ] Document how to enable/disable

---

### 9. Unit Tests ⚠️ MEDIUM PRIORITY

**Current State:**
- Only integration tests
- No unit tests for individual functions

**Required:**
```
tests/unit/
  test_policy_define.py
  test_policy_validate.py
  test_policy_enforce.py
  test_meta_agent.py
  test_cli.py
```

**Actions:**
- [ ] Create unit test structure
- [ ] Test each function in isolation
- [ ] Mock file I/O
- [ ] Test error conditions
- [ ] Aim for 80%+ coverage

---

### 10. Documentation ⚠️ HIGH PRIORITY

**Required Docs:**
```
docs/policy/
  README.md              # Overview
  quickstart.md          # 5-minute guide
  profiles.md            # Creating profiles
  rules.md               # Rule syntax reference
  cli.md                 # CLI reference
  api.md                 # Python API
  troubleshooting.md     # Common issues
```

**Actions:**
- [ ] Write quickstart guide
- [ ] Document all CLI commands
- [ ] Document Python API
- [ ] Add examples
- [ ] Add troubleshooting section

---

## ✅ Definition of "Production Ready"

The system is production-ready when:

- [x] All skills are importable Python modules
- [x] No subprocess calls (direct imports only)
- [x] CLI wrapper exists and works
- [x] Hardcoded rules migrated to betty-core.yaml
- [x] Discovery tools implemented (list, show, test)
- [x] Proper exception handling
- [x] Registry integration working
- [x] Hook tested and working
- [x] Unit tests written
- [x] Documentation complete
- [x] No PYTHONPATH hacks needed
- [x] Works on fresh install
- [x] Error messages are helpful

---

## 📅 Execution Order

### Phase 1: Core Refactoring (CRITICAL - 2-3 hours)
1. Make skills importable
2. Remove subprocess calls
3. Migrate hardcoded rules
4. Better error handling

### Phase 2: UX Layer (HIGH - 1-2 hours)
5. Create CLI wrapper
6. Add discovery tools
7. Test hook integration

### Phase 3: Quality (MEDIUM - 1-2 hours)
8. Unit tests
9. Registry integration
10. Documentation

**Total Time Estimate: 4-7 hours**

---

## 🚀 Let's Start

Beginning with Phase 1, Item 1: Make skills importable.
