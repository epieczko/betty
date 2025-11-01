#!/usr/bin/env python3
"""
AI-powered risk assessment engine for risk.review skill

Uses Claude API for semantic analysis of security, privacy, compliance, and operational risks.
"""

import os
import json
import time
import hashlib
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime


# Token estimation (rough approximation: 1 token ≈ 4 characters)
def estimate_tokens(text: str) -> int:
    """Estimate token count for cost calculation"""
    return len(text) // 4


# Cost estimation based on Claude Sonnet 4 pricing
COST_PER_INPUT_TOKEN = 0.000003  # $3 per million input tokens
COST_PER_OUTPUT_TOKEN = 0.000015  # $15 per million output tokens
ESTIMATED_OUTPUT_TOKENS = 2000  # Typical response size


def estimate_cost(content: str) -> float:
    """Estimate API call cost in USD"""
    input_tokens = estimate_tokens(content)
    input_cost = input_tokens * COST_PER_INPUT_TOKEN
    output_cost = ESTIMATED_OUTPUT_TOKENS * COST_PER_OUTPUT_TOKEN
    return input_cost + output_cost


class AIRiskAnalyzer:
    """AI-powered semantic risk assessment engine"""

    def __init__(self, model: str = "claude-sonnet-4-20250514", temperature: float = 0):
        self.model = model
        self.temperature = temperature
        self.api_available = self._check_api_availability()

    def _check_api_availability(self) -> bool:
        """Check if Claude API is available"""
        try:
            import anthropic
            api_key = os.environ.get('ANTHROPIC_API_KEY')
            if not api_key:
                print("⚠️  ANTHROPIC_API_KEY not set - AI mode unavailable")
                return False
            return True
        except ImportError:
            print("⚠️  anthropic package not installed - AI mode unavailable")
            return False

    def assess(
        self,
        content: str,
        data: Dict[str, Any],
        artifact_type: str,
        frameworks: List[str],
        verbose: bool = True
    ) -> Dict[str, Any]:
        """
        Perform AI-powered risk assessment

        Args:
            content: Artifact content as string
            data: Parsed artifact data (YAML/JSON)
            artifact_type: Type of artifact being assessed
            frameworks: List of compliance frameworks to evaluate
            verbose: Print progress and cost information

        Returns:
            Structured risk assessment results
        """
        if not self.api_available:
            raise RuntimeError("AI engine not available - use --mode=fast or install anthropic package")

        # Estimate cost
        cost_estimate = estimate_cost(content)
        if verbose:
            print(f"🤖 AI Risk Assessment Mode")
            print(f"   Estimated cost: ${cost_estimate:.4f}")

        # Build prompt
        prompt = self._build_assessment_prompt(content, artifact_type, frameworks)

        # Call Claude API
        start_time = time.time()
        response = self._call_claude_api(prompt, verbose)
        duration = time.time() - start_time

        if verbose:
            print(f"✓ AI analysis complete in {duration:.1f}s")

        # Parse structured response
        result = self._parse_response(response, frameworks)

        return result

    def _build_assessment_prompt(
        self,
        content: str,
        artifact_type: str,
        frameworks: List[str]
    ) -> str:
        """Build comprehensive risk assessment prompt"""

        framework_details = {
            'SOC2': 'SOC 2 Type II (Security, Availability, Processing Integrity, Confidentiality, Privacy)',
            'ISO27001': 'ISO/IEC 27001 (Information Security Management)',
            'GDPR': 'GDPR (General Data Protection Regulation)',
            'HIPAA': 'HIPAA (Health Insurance Portability and Accountability Act)',
            'PCI-DSS': 'PCI-DSS (Payment Card Industry Data Security Standard)',
            'NIST': 'NIST Cybersecurity Framework (Identify, Protect, Detect, Respond, Recover)'
        }

        frameworks_str = '\n'.join([
            f"- {fw}: {framework_details.get(fw, fw)}"
            for fw in frameworks
        ])

        prompt = f"""You are a senior security and compliance expert conducting a comprehensive risk assessment.

ARTIFACT TYPE: {artifact_type}

COMPLIANCE FRAMEWORKS TO EVALUATE:
{frameworks_str}

ARTIFACT CONTENT:
{content}

ASSESSMENT INSTRUCTIONS:

1. CRITICAL DISTINCTION: Differentiate between:
   - ✓ IMPLEMENTED controls (currently active and operational)
   - ⚠️  PLANNED controls (documented intent, future roadmap)
   - ❌ MISSING controls (not mentioned or explicitly absent)

   Example: "We will implement MFA next quarter" = MISSING (not yet active)

2. SECURITY RISK ASSESSMENT:
   - Authentication and authorization controls
   - Encryption (at rest and in transit)
   - Credential management (detect hardcoded secrets)
   - Vulnerability management
   - Network security
   - Audit logging and monitoring

3. PRIVACY RISK ASSESSMENT:
   - Personal data handling (PII, PHI, sensitive data)
   - Consent mechanisms
   - Data subject rights
   - Data minimization and anonymization
   - Third-party data sharing and DPAs
   - Cross-border data transfers

4. OPERATIONAL RISK ASSESSMENT:
   - Business continuity and disaster recovery
   - Incident response procedures
   - Change management processes
   - Service level commitments
   - Backup and recovery testing

5. COMPLIANCE ASSESSMENT:
   For each framework, identify:
   - Coverage score (0-100%)
   - Specific gaps and missing controls
   - Compliant areas
   - Priority for remediation

6. RISK SCORING:
   - Calculate overall risk score (0-100, higher = more risk)
   - Assign rating: CRITICAL (75-100), HIGH (50-74), MEDIUM (25-49), LOW (0-24)
   - Consider: Security (40%), Privacy (25%), Operational (20%), Compliance (15%)

OUTPUT FORMAT (strict JSON):
{{
  "risk_score": <0-100>,
  "risk_rating": "CRITICAL|HIGH|MEDIUM|LOW",
  "assessment_summary": "<2-3 sentence executive summary>",
  "findings": [
    {{
      "category": "security|privacy|operational|compliance",
      "severity": "critical|high|medium|low",
      "finding": "<specific issue found>",
      "evidence": "<quote from artifact showing the issue>",
      "impact": "<business/technical impact>",
      "remediation": "<specific, actionable remediation step>",
      "confidence": <0.0-1.0, how certain you are about this finding>
    }}
  ],
  "compliance_status": {{
    "FRAMEWORK_NAME": {{
      "compliance_score": <0-100>,
      "status": "compliant|partial|non-compliant",
      "gaps": [
        {{
          "gap": "<missing control or requirement>",
          "requirement": "<specific framework requirement>",
          "priority": "high|medium|low"
        }}
      ],
      "compliant_areas": ["<area 1>", "<area 2>"]
    }}
  }},
  "security_assessment": {{
    "risk_level": <0-100>,
    "coverage_score": <0-100>,
    "compliant_items": ["<positive finding 1>", "<positive finding 2>"],
    "risks": [/* findings with category="security" */]
  }},
  "privacy_assessment": {{
    "risk_level": <0-100>,
    "privacy_coverage": <number>,
    "compliant_items": ["<positive finding 1>"],
    "risks": [/* findings with category="privacy" */]
  }},
  "operational_assessment": {{
    "risk_level": <0-100>,
    "compliant_items": ["<positive finding 1>"],
    "risks": [/* findings with category="operational" */]
  }}
}}

IMPORTANT:
- Be precise and evidence-based
- Quote specific text from the artifact as evidence
- Distinguish clearly between implemented vs planned controls
- Provide actionable, specific remediation steps
- Consider implicit risks (e.g., "public S3 bucket" implies data exposure risk)
- Output ONLY valid JSON, no additional text
"""

        return prompt

    def _call_claude_api(self, prompt: str, verbose: bool = True) -> str:
        """Call Claude API for risk assessment with retry logic"""
        try:
            import anthropic
        except ImportError:
            raise RuntimeError("anthropic package not installed. Run: pip install anthropic")

        api_key = os.environ.get('ANTHROPIC_API_KEY')
        if not api_key:
            raise RuntimeError("ANTHROPIC_API_KEY environment variable not set")

        client = anthropic.Anthropic(api_key=api_key)

        # Retry logic for transient failures
        max_retries = 3
        retry_delay = 2  # seconds

        for attempt in range(max_retries):
            try:
                response = client.messages.create(
                    model=self.model,
                    max_tokens=4096,
                    temperature=self.temperature,
                    messages=[{
                        "role": "user",
                        "content": prompt
                    }]
                )

                # Track actual usage for cost transparency
                if verbose and hasattr(response, 'usage'):
                    input_tokens = response.usage.input_tokens
                    output_tokens = response.usage.output_tokens
                    actual_cost = (input_tokens * COST_PER_INPUT_TOKEN) + (output_tokens * COST_PER_OUTPUT_TOKEN)
                    print(f"   📊 Tokens: {input_tokens} in + {output_tokens} out = {input_tokens + output_tokens} total")
                    print(f"   💰 Actual cost: ${actual_cost:.4f}")

                return response.content[0].text

            except anthropic.RateLimitError as e:
                if attempt < max_retries - 1:
                    if verbose:
                        print(f"⚠️  Rate limit hit, retrying in {retry_delay}s... (attempt {attempt + 1}/{max_retries})")
                    time.sleep(retry_delay)
                    retry_delay *= 2  # Exponential backoff
                else:
                    raise RuntimeError(f"Rate limit exceeded after {max_retries} attempts: {e}")

            except anthropic.APIConnectionError as e:
                if attempt < max_retries - 1:
                    if verbose:
                        print(f"⚠️  Connection error, retrying in {retry_delay}s... (attempt {attempt + 1}/{max_retries})")
                    time.sleep(retry_delay)
                    retry_delay *= 2
                else:
                    raise RuntimeError(f"API connection failed after {max_retries} attempts: {e}")

            except anthropic.APIError as e:
                # Don't retry on auth errors or bad requests
                if e.status_code in [401, 403]:
                    raise RuntimeError(f"API authentication failed: {e}")
                elif e.status_code == 400:
                    raise RuntimeError(f"Invalid API request: {e}")
                elif attempt < max_retries - 1:
                    if verbose:
                        print(f"⚠️  API error, retrying in {retry_delay}s... (attempt {attempt + 1}/{max_retries})")
                    time.sleep(retry_delay)
                    retry_delay *= 2
                else:
                    raise RuntimeError(f"API error after {max_retries} attempts: {e}")

            except Exception as e:
                if verbose:
                    print(f"❌ Unexpected error: {e}")
                raise RuntimeError(f"Unexpected API error: {e}")

    def _parse_response(self, response: str, frameworks: List[str]) -> Dict[str, Any]:
        """Parse and validate AI response with robust error handling"""
        try:
            # Extract JSON from response (handle markdown code blocks)
            response = response.strip()

            # Handle markdown code blocks
            if '```json' in response:
                # Extract content between ```json and ```
                start = response.find('```json') + 7
                end = response.find('```', start)
                response = response[start:end].strip()
            elif '```' in response:
                # Extract first code block
                start = response.find('```') + 3
                # Skip language identifier if present
                newline = response.find('\n', start)
                if newline != -1:
                    start = newline + 1
                end = response.find('```', start)
                response = response[start:end].strip()

            # Try parsing JSON
            try:
                result = json.loads(response)
            except json.JSONDecodeError as e:
                # Attempt to fix common JSON issues
                print(f"⚠️  Initial JSON parse failed, attempting repair...")

                # Remove trailing commas
                response = response.replace(',]', ']').replace(',}', '}')

                # Try again
                try:
                    result = json.loads(response)
                    print(f"   ✓ JSON repaired successfully")
                except json.JSONDecodeError:
                    # Give up and raise informative error
                    print(f"   ❌ JSON repair failed")
                    print(f"   Response preview: {response[:500]}")
                    raise ValueError(f"Failed to parse AI response as JSON: {e}")

            # Validate required fields
            required_fields = ['risk_score', 'risk_rating', 'findings']
            missing_fields = [f for f in required_fields if f not in result]

            if missing_fields:
                print(f"⚠️  Missing fields in AI response: {missing_fields}")
                # Provide defaults for missing fields
                if 'risk_score' not in result:
                    result['risk_score'] = 50  # Default to medium
                if 'risk_rating' not in result:
                    result['risk_rating'] = 'MEDIUM'
                if 'findings' not in result:
                    result['findings'] = []
                print(f"   ✓ Using default values for missing fields")

            # Organize findings by category
            security_risks = [f for f in result['findings'] if f['category'] == 'security']
            privacy_risks = [f for f in result['findings'] if f['category'] == 'privacy']
            operational_risks = [f for f in result['findings'] if f['category'] == 'operational']

            # Ensure assessments exist
            if 'security_assessment' not in result:
                result['security_assessment'] = {
                    'risk_level': self._calculate_category_risk(security_risks),
                    'coverage_score': 50,
                    'compliant_items': [],
                    'risks': security_risks
                }

            if 'privacy_assessment' not in result:
                result['privacy_assessment'] = {
                    'risk_level': self._calculate_category_risk(privacy_risks),
                    'privacy_coverage': len(privacy_risks),
                    'compliant_items': [],
                    'risks': privacy_risks
                }

            if 'operational_assessment' not in result:
                result['operational_assessment'] = {
                    'risk_level': self._calculate_category_risk(operational_risks),
                    'compliant_items': [],
                    'risks': operational_risks
                }

            return result

        except json.JSONDecodeError as e:
            print(f"❌ Failed to parse AI response as JSON: {e}")
            print(f"Response: {response[:500]}")
            raise ValueError("AI returned invalid JSON response")

    def _calculate_category_risk(self, risks: List[Dict[str, Any]]) -> int:
        """Calculate risk level from findings"""
        if not risks:
            return 0

        severity_weights = {
            'critical': 35,
            'high': 25,
            'medium': 15,
            'low': 5
        }

        total = sum(severity_weights.get(r.get('severity', 'low'), 5) for r in risks)
        return min(total, 100)


class ArtifactCache:
    """Simple file-based cache for AI assessments"""

    def __init__(self, cache_dir: Optional[Path] = None, ttl: int = 86400):
        self.cache_dir = cache_dir or Path.home() / '.betty' / 'cache' / 'risk_review'
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.ttl = ttl

    def _get_cache_key(self, artifact_path: str, frameworks: List[str]) -> str:
        """Generate cache key from artifact content and frameworks"""
        # Hash artifact content
        content_hash = hashlib.sha256(
            Path(artifact_path).read_bytes()
        ).hexdigest()[:16]

        # Hash frameworks
        frameworks_str = ','.join(sorted(frameworks))
        frameworks_hash = hashlib.md5(frameworks_str.encode()).hexdigest()[:8]

        return f"{content_hash}_{frameworks_hash}"

    def get(self, artifact_path: str, frameworks: List[str]) -> Optional[Dict[str, Any]]:
        """Retrieve cached assessment"""
        key = self._get_cache_key(artifact_path, frameworks)
        cache_file = self.cache_dir / f"{key}.json"

        if not cache_file.exists():
            return None

        # Check if cache is expired
        age = time.time() - cache_file.stat().st_mtime
        if age > self.ttl:
            cache_file.unlink()
            return None

        try:
            with open(cache_file, 'r') as f:
                cached = json.load(f)
            print(f"✓ Using cached assessment (age: {age/3600:.1f}h)")
            return cached
        except Exception:
            return None

    def set(self, artifact_path: str, frameworks: List[str], result: Dict[str, Any]):
        """Cache assessment result"""
        key = self._get_cache_key(artifact_path, frameworks)
        cache_file = self.cache_dir / f"{key}.json"

        try:
            with open(cache_file, 'w') as f:
                json.dump(result, f, indent=2)
        except Exception as e:
            print(f"⚠️  Failed to cache result: {e}")

    def clear(self):
        """Clear all cached assessments"""
        for cache_file in self.cache_dir.glob("*.json"):
            cache_file.unlink()
        print(f"✓ Cache cleared: {self.cache_dir}")
