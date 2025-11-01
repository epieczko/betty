# risk.review - AI-Native Risk Assessment

## Overview

The `risk.review` skill is now **AI-native**, using Claude for semantic understanding of security, privacy, compliance, and operational risks. This provides dramatically better accuracy compared to pattern matching.

## Assessment Modes

### 🧠 Smart Mode (Default - Recommended)
Fast pre-check + AI semantic analysis

```bash
/skill/risk/review artifact.yaml
# or explicitly:
/skill/risk/review artifact.yaml --mode=smart
```

**How it works:**
1. Fast regex check for obvious critical issues (hardcoded credentials)
2. If critical issues found → immediate response (no API cost)
3. If no critical issues → AI semantic analysis for nuanced assessment

**Best for:** Most use cases - balances speed, cost, and accuracy

---

### 🤖 AI Mode (Pure AI)
Full AI semantic analysis without pre-checks

```bash
/skill/risk/review artifact.yaml --mode=ai
```

**How it works:**
- Sends entire artifact to Claude for analysis
- AI understands context, distinguishes implementation vs planning
- Provides evidence-based findings with specific quotes

**Best for:** High-stakes assessments where accuracy is paramount

**Example AI understanding:**
```yaml
# AI correctly identifies these as DIFFERENT risk levels:

"We will implement MFA next quarter"
→ AI: HIGH RISK - No auth currently deployed (planned ≠ implemented)

"MFA is enabled via OAuth 2.0"
→ AI: LOW RISK - Authentication properly implemented
```

---

### ⚡ Fast Mode (Regex-Only)
Pattern-based assessment for CI/CD and offline use

```bash
/skill/risk/review artifact.yaml --mode=fast
```

**How it works:**
- Uses regex patterns to detect known risk indicators
- No AI/API calls - instant results
- Good for known patterns, misses context

**Best for:**
- CI/CD pipelines (fast feedback)
- Offline environments
- Cost-sensitive bulk scanning

---

## Cost & Performance

| Mode | Speed | Cost per Artifact | Accuracy | When to Use |
|------|-------|-------------------|----------|-------------|
| **smart** | 2-5s | $0.00-0.05 | High | Default - most cases |
| **ai** | 3-6s | $0.01-0.05 | Highest | Critical assessments |
| **fast** | <1s | $0.00 (free) | Moderate | CI/CD, offline, bulk |

### Cost Optimization

**Caching (Automatic)**
- AI assessments cached for 24 hours
- Cache based on artifact content + frameworks
- Repeat assessments are instant and free

```bash
# First run: $0.03, 3 seconds
/skill/risk/review artifact.yaml

# Second run: $0.00, <0.1 seconds (cached)
/skill/risk/review artifact.yaml
```

**Disable caching:**
```bash
/skill/risk/review artifact.yaml --no-cache
```

**Clear cache:**
```bash
rm -rf ~/.betty/cache/risk_review
```

---

## Why AI-Native?

### Pattern Matching Limitations

**Regex can't understand context:**
```yaml
# These are SEMANTICALLY DIFFERENT but regex treats them the same:

❌ "No encryption implemented"
✓ "Encryption requirements documented"
✓ "Planning to add encryption in Q2"
✓ "Encryption fully operational"
```

All mention "encryption" → Regex marks all as ✓ compliant!

### AI Semantic Understanding

**Claude understands:**
- **Implementation vs Planning:** "will implement" ≠ "is implemented"
- **Negation:** "No security issues" vs "Security controls present"
- **Implicit Risks:** "Public S3 bucket" → data exposure risk
- **Context:** "Basic logging" vs "Comprehensive audit logging"

### Real Example

**Artifact:**
```yaml
security_plan:
  authentication: "We plan to migrate to OAuth 2.0 next quarter"
  encryption: "Currently using HTTP, HTTPS upgrade scheduled"
```

**Regex Engine:**
- ✓ Mentions "authentication" → Compliant
- ✓ Mentions "encryption" → Compliant
- **Risk Score:** 20 (LOW)

**AI Engine:**
- 🚨 Authentication planned but not implemented (HIGH RISK)
- 🚨 Currently using unencrypted HTTP (CRITICAL)
- 🚨 Both are future plans, not current controls
- **Risk Score:** 85 (CRITICAL)

---

## Setup

### Install Dependencies

```bash
cd /home/user/betty/skills/risk.review
pip install -r requirements.txt
```

**Required:**
- `pyyaml>=6.0` - YAML parsing
- `anthropic>=0.39.0` - Claude API client

### Configure API Key

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

**Or** add to your `~/.bashrc` or `~/.zshrc`:
```bash
echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.bashrc
source ~/.bashrc
```

### Verify Setup

```bash
# Test AI mode
/skill/risk/review tests/fixtures/high-risk-artifact.yaml --mode=ai

# Should see:
# 🤖 AI Risk Assessment Mode
#    Estimated cost: $0.0234
# ✓ AI analysis complete in 3.2s
```

---

## Usage Examples

### Basic Assessment (Smart Mode)
```bash
/skill/risk/review deployments/prod-api.yaml
```

### Specific Frameworks
```bash
/skill/risk/review security-policy.yaml \
  --policy-frameworks SOC2 HIPAA GDPR \
  --mode=ai
```

### CI/CD Pipeline
```bash
# Fast mode for quick feedback
/skill/risk/review $ARTIFACT_PATH --mode=fast --quiet

# Exit code: 0 (pass) or 1 (fail)
```

### Save Report
```bash
/skill/risk/review architecture.yaml \
  --mode=ai \
  --output reports/risk-assessment-$(date +%Y%m%d).yaml
```

---

## Sample Output

### Smart Mode with Critical Detection

```
🧠 Smart Mode (Fast Check + AI Analysis)
⚠️  Critical issues detected: Hardcoded credentials detected
   Skipping AI analysis (obvious failure)

================================================================================
RISK ASSESSMENT & COMPLIANCE AUDIT REPORT
================================================================================
Artifact:        /path/to/deployment-plan.yaml
OVERALL RISK RATING: CRITICAL
Risk Score:          95/100

CRITICAL & HIGH SEVERITY FINDINGS:

  🔴 CRITICAL: Hardcoded credentials detected
     Evidence: password: admin123
     Impact: Unauthorized access, credential exposure
     Remediation: Use secure credential management (vault, environment variables)
```

### AI Mode Semantic Analysis

```
🤖 AI Risk Assessment Mode
   Estimated cost: $0.0234
✓ AI analysis complete in 3.4s

================================================================================
RISK ASSESSMENT & COMPLIANCE AUDIT REPORT
================================================================================
OVERALL RISK RATING: HIGH
Risk Score:          68/100

SUMMARY:
  Authentication and encryption controls are documented as future plans but not
  currently implemented. The system is operating without critical security controls
  in production.

CRITICAL & HIGH SEVERITY FINDINGS:

  🟠 HIGH: Authentication not implemented
     Evidence: "We plan to migrate to OAuth 2.0 next quarter"
     Impact: Current production system lacks authentication
     Remediation: Implement authentication immediately before production deployment
```

---

## API Integration

### Python API

```python
from risk_review import review_risk

# AI mode
result = review_risk(
    artifact_path="deployment.yaml",
    policy_frameworks=["SOC2", "GDPR"],
    mode="ai",  # or "smart", "fast"
    cache_enabled=True,
    verbose=True
)

print(f"Risk Score: {result['risk_assessment']['risk_score']}")
print(f"Rating: {result['risk_assessment']['risk_rating']}")

for finding in result['audit_report']['findings']:
    print(f"[{finding['severity']}] {finding['finding']}")
```

### Batch Processing

```python
import glob
from risk_review import review_risk

artifacts = glob.glob("artifacts/**/*.yaml", recursive=True)

for artifact in artifacts:
    result = review_risk(artifact, mode="smart", verbose=False)

    if result['risk_assessment']['risk_score'] > 50:
        print(f"⚠️  {artifact}: {result['risk_assessment']['risk_rating']}")
```

---

## Comparison: Regex vs AI

| Feature | Regex (Fast) | AI (Smart/AI) |
|---------|--------------|---------------|
| Hardcoded credentials | ✓ Detects | ✓ Detects |
| HTTP vs HTTPS | ✓ Detects | ✓ Detects |
| Implementation vs Planning | ❌ Can't distinguish | ✓ Understands |
| Context-aware | ❌ No | ✓ Yes |
| Implicit risks | ❌ Misses | ✓ Identifies |
| Multi-language | ❌ English-only patterns | ✓ Any language |
| Novel threats | ❌ Unknown patterns missed | ✓ Reasons about new scenarios |
| Evidence quotes | ❌ No | ✓ Yes |
| Speed | ⚡ <1s | 🧠 2-5s |
| Cost | Free | ~$0.01-0.05 |

---

## Troubleshooting

### "AI mode unavailable"

**Problem:** `ANTHROPIC_API_KEY` not set or `anthropic` package missing

**Solution:**
```bash
pip install anthropic
export ANTHROPIC_API_KEY="sk-ant-..."
```

### "API call failed"

**Problem:** Network issues or invalid API key

**Solution:**
```bash
# Test API key
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{"model":"claude-sonnet-4-20250514","max_tokens":10,"messages":[{"role":"user","content":"test"}]}'

# Fallback to fast mode
/skill/risk/review artifact.yaml --mode=fast
```

### High API Costs

**Solution:**
```bash
# Check cache is enabled (default)
ls ~/.betty/cache/risk_review/

# Use smart mode (pre-checks reduce API calls)
/skill/risk/review artifact.yaml --mode=smart

# Use fast mode for bulk scanning
for f in artifacts/*.yaml; do
  /skill/risk/review "$f" --mode=fast
done
```

---

## Future Enhancements

- [ ] Multi-artifact batch analysis
- [ ] Custom policy framework definitions
- [ ] Integration with vulnerability databases (CVE)
- [ ] Risk trend analysis over time
- [ ] Configurable AI model selection
- [ ] Streaming output for long assessments

---

## Related Documentation

- [Main README](README.md) - Feature overview and usage
- [Test Documentation](tests/README.md) - Test suite details
- [skill.yaml](skill.yaml) - Skill manifest
