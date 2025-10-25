#!/usr/bin/env python3
"""
artifact.review skill - AI-powered artifact content review

Reviews artifact quality, completeness, and best practices compliance.
Generates detailed assessments with actionable recommendations.
"""

import sys
import os
import argparse
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple
import yaml


def load_artifact_registry() -> Dict[str, Any]:
    """Load artifact registry from artifact.define skill"""
    registry_file = Path(__file__).parent.parent / "artifact.define" / "artifact_define.py"

    if not registry_file.exists():
        raise FileNotFoundError(f"Artifact registry not found: {registry_file}")

    with open(registry_file, 'r') as f:
        content = f.read()

    start_marker = "KNOWN_ARTIFACT_TYPES = {"
    start_idx = content.find(start_marker)
    if start_idx == -1:
        raise ValueError("Could not find KNOWN_ARTIFACT_TYPES in registry file")

    start_idx += len(start_marker) - 1

    brace_count = 0
    end_idx = start_idx
    for i in range(start_idx, len(content)):
        if content[i] == '{':
            brace_count += 1
        elif content[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                end_idx = i + 1
                break

    dict_str = content[start_idx:end_idx]
    artifacts = eval(dict_str)
    return artifacts


def detect_artifact_type(file_path: Path, content: str) -> Optional[str]:
    """Detect artifact type from filename or content"""
    filename = file_path.stem
    registry = load_artifact_registry()

    if filename in registry:
        return filename

    for artifact_type in registry.keys():
        if artifact_type in filename:
            return artifact_type

    if file_path.suffix in ['.yaml', '.yml']:
        try:
            data = yaml.safe_load(content)
            if isinstance(data, dict) and 'metadata' in data:
                metadata = data['metadata']
                if 'artifactType' in metadata:
                    return metadata['artifactType']
        except:
            pass

    return None


def load_artifact_description(artifact_type: str) -> Optional[str]:
    """Load artifact description for reference"""
    desc_dir = Path(__file__).parent.parent.parent / "artifact_descriptions"
    desc_file = desc_dir / f"{artifact_type}.md"

    if desc_file.exists():
        with open(desc_file, 'r') as f:
            return f.read()
    return None


def analyze_content_completeness(content: str, data: Dict[str, Any], file_format: str) -> Dict[str, Any]:
    """Analyze content completeness and depth"""
    issues = []
    strengths = []
    recommendations = []

    word_count = len(content.split())

    # Check content depth
    if word_count < 100:
        issues.append("Very brief content - needs significant expansion")
        recommendations.append("Add detailed explanations, examples, and context")
    elif word_count < 300:
        issues.append("Limited content depth - could be more comprehensive")
        recommendations.append("Expand key sections with more details and examples")
    else:
        strengths.append(f"Good content depth ({word_count} words)")

    # Check for placeholder content
    placeholder_patterns = [
        r'TODO',
        r'Lorem ipsum',
        r'placeholder',
        r'REPLACE THIS',
        r'FILL IN',
        r'TBD',
        r'coming soon'
    ]

    placeholder_count = 0
    for pattern in placeholder_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        placeholder_count += len(matches)

    if placeholder_count > 10:
        issues.append(f"Many placeholders found ({placeholder_count}) - content is incomplete")
    elif placeholder_count > 5:
        issues.append(f"Several placeholders found ({placeholder_count}) - needs completion")
    elif placeholder_count > 0:
        recommendations.append(f"Replace {placeholder_count} placeholder(s) with actual content")
    else:
        strengths.append("No placeholder text found")

    # YAML specific checks
    if file_format in ['yaml', 'yml'] and isinstance(data, dict):
        if 'content' in data:
            content_section = data['content']
            if isinstance(content_section, dict):
                filled_fields = [k for k, v in content_section.items() if v and str(v).strip() and 'TODO' not in str(v)]
                total_fields = len(content_section)
                completeness_pct = (len(filled_fields) / total_fields * 100) if total_fields > 0 else 0

                if completeness_pct < 30:
                    issues.append(f"Content section is {completeness_pct:.0f}% complete - needs significant work")
                elif completeness_pct < 70:
                    issues.append(f"Content section is {completeness_pct:.0f}% complete - needs more details")
                elif completeness_pct < 100:
                    recommendations.append(f"Content section is {completeness_pct:.0f}% complete - finish remaining fields")
                else:
                    strengths.append("Content section is fully populated")

    score = max(0, 100 - (len(issues) * 25) - (placeholder_count * 2))

    return {
        'score': min(score, 100),
        'word_count': word_count,
        'placeholder_count': placeholder_count,
        'issues': issues,
        'strengths': strengths,
        'recommendations': recommendations
    }


def analyze_professional_quality(content: str, file_format: str) -> Dict[str, Any]:
    """Analyze professional writing quality and tone"""
    issues = []
    strengths = []
    recommendations = []

    # Check for professional tone indicators
    has_executive_summary = 'executive summary' in content.lower() or 'overview' in content.lower()
    has_clear_structure = bool(re.search(r'^#+\s+\w+', content, re.MULTILINE)) if file_format == 'md' else True

    if has_executive_summary:
        strengths.append("Includes executive summary/overview")
    else:
        recommendations.append("Consider adding an executive summary for stakeholders")

    if has_clear_structure:
        strengths.append("Clear document structure")

    # Check for unprofessional elements
    informal_markers = [
        (r'\b(gonna|wanna|gotta)\b', 'informal contractions'),
        (r'\b(lol|omg|wtf)\b', 'casual internet slang'),
        (r'!!!+', 'excessive exclamation marks'),
        (r'\?\?+', 'multiple question marks')
    ]

    for pattern, issue_name in informal_markers:
        if re.search(pattern, content, re.IGNORECASE):
            issues.append(f"Contains {issue_name} - use professional language")

    # Check for passive voice (simplified check)
    passive_patterns = r'\b(is|are|was|were|be|been|being)\s+\w+ed\b'
    passive_count = len(re.findall(passive_patterns, content, re.IGNORECASE))
    total_sentences = len(re.findall(r'[.!?]', content))

    if total_sentences > 0:
        passive_ratio = passive_count / total_sentences
        if passive_ratio > 0.5:
            recommendations.append("Consider reducing passive voice for clearer communication")

    # Check for jargon overuse
    jargon_markers = [
        'synergy', 'leverage', 'paradigm shift', 'circle back', 'touch base',
        'low-hanging fruit', 'move the needle', 'boil the ocean'
    ]
    jargon_count = sum(1 for marker in jargon_markers if marker in content.lower())
    if jargon_count > 3:
        recommendations.append("Reduce business jargon - use clear, specific language")

    score = max(0, 100 - (len(issues) * 20))

    return {
        'score': score,
        'issues': issues,
        'strengths': strengths,
        'recommendations': recommendations
    }


def check_best_practices(content: str, artifact_type: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """Check adherence to artifact-specific best practices"""
    issues = []
    strengths = []
    recommendations = []

    # Load artifact description for best practices reference
    description = load_artifact_description(artifact_type)

    # Common best practices
    if isinstance(data, dict):
        # Metadata best practices
        if 'metadata' in data:
            metadata = data['metadata']

            # Version control
            if 'version' in metadata and metadata['version']:
                if re.match(r'^\d+\.\d+\.\d+$', str(metadata['version'])):
                    strengths.append("Uses semantic versioning")
                else:
                    recommendations.append("Consider using semantic versioning (e.g., 1.0.0)")

            # Classification
            if 'classification' in metadata and metadata['classification']:
                if metadata['classification'] in ['Public', 'Internal', 'Confidential', 'Restricted']:
                    strengths.append("Proper document classification set")
                else:
                    issues.append("Invalid classification level")

            # Approval workflow
            if 'approvers' in metadata and isinstance(metadata['approvers'], list):
                if len(metadata['approvers']) > 0:
                    strengths.append("Approval workflow defined")
                else:
                    recommendations.append("Add approvers to metadata for proper governance")

        # Change history best practice
        if 'changeHistory' in data:
            history = data['changeHistory']
            if isinstance(history, list) and len(history) > 0:
                strengths.append("Maintains change history")
            else:
                recommendations.append("Document changes in change history")

        # Related documents
        if 'relatedDocuments' in data or ('metadata' in data and 'relatedDocuments' in data['metadata']):
            strengths.append("Links to related documents")
        else:
            recommendations.append("Link related artifacts for traceability")

    # Artifact-specific checks based on type
    if artifact_type == 'business-case':
        if 'roi' in content.lower() or 'return on investment' in content.lower():
            strengths.append("Includes ROI analysis")
        else:
            recommendations.append("Add ROI/financial justification")

    elif artifact_type == 'threat-model':
        if 'stride' in content.lower() or 'attack vector' in content.lower():
            strengths.append("Uses threat modeling methodology")
        else:
            recommendations.append("Apply threat modeling framework (e.g., STRIDE)")

    elif 'test' in artifact_type:
        if 'pass' in content.lower() and 'fail' in content.lower():
            strengths.append("Includes test criteria")

    score = max(0, 100 - (len(issues) * 20))

    return {
        'score': score,
        'issues': issues,
        'strengths': strengths,
        'recommendations': recommendations,
        'has_description': description is not None
    }


def check_industry_standards(content: str, artifact_type: str) -> Dict[str, Any]:
    """Check alignment with industry standards and frameworks"""
    strengths = []
    recommendations = []
    referenced_standards = []

    # Common industry standards
    standards = {
        'TOGAF': r'\bTOGAF\b',
        'ISO 27001': r'\bISO\s*27001\b',
        'NIST': r'\bNIST\b',
        'PCI-DSS': r'\bPCI[-\s]?DSS\b',
        'GDPR': r'\bGDPR\b',
        'SOC 2': r'\bSOC\s*2\b',
        'HIPAA': r'\bHIPAA\b',
        'SAFe': r'\bSAFe\b',
        'ITIL': r'\bITIL\b',
        'COBIT': r'\bCOBIT\b',
        'PMBOK': r'\bPMBOK\b',
        'OWASP': r'\bOWASP\b'
    }

    for standard, pattern in standards.items():
        if re.search(pattern, content, re.IGNORECASE):
            referenced_standards.append(standard)

    if referenced_standards:
        strengths.append(f"References industry standards: {', '.join(referenced_standards)}")
    else:
        # Suggest relevant standards based on artifact type
        if 'security' in artifact_type or 'threat' in artifact_type:
            recommendations.append("Consider referencing security standards (ISO 27001, NIST, OWASP)")
        elif 'architecture' in artifact_type:
            recommendations.append("Consider referencing architecture frameworks (TOGAF, Zachman)")
        elif 'governance' in artifact_type or 'portfolio' in artifact_type:
            recommendations.append("Consider referencing governance frameworks (COBIT, PMBOK)")

    score = 100 if referenced_standards else 70

    return {
        'score': score,
        'referenced_standards': referenced_standards,
        'strengths': strengths,
        'recommendations': recommendations
    }


def calculate_readiness_score(review_results: Dict[str, Any]) -> int:
    """Calculate overall readiness score"""
    scores = []
    weights = []

    # Content completeness (35%)
    scores.append(review_results['completeness']['score'])
    weights.append(0.35)

    # Professional quality (25%)
    scores.append(review_results['professional_quality']['score'])
    weights.append(0.25)

    # Best practices (25%)
    scores.append(review_results['best_practices']['score'])
    weights.append(0.25)

    # Industry standards (15%)
    scores.append(review_results['industry_standards']['score'])
    weights.append(0.15)

    readiness_score = sum(s * w for s, w in zip(scores, weights))
    return int(readiness_score)


def determine_quality_rating(readiness_score: int) -> str:
    """Determine quality rating from readiness score"""
    if readiness_score >= 90:
        return "Excellent"
    elif readiness_score >= 75:
        return "Good"
    elif readiness_score >= 60:
        return "Fair"
    elif readiness_score >= 40:
        return "Needs Improvement"
    else:
        return "Poor"


def generate_summary_recommendations(review_results: Dict[str, Any]) -> List[str]:
    """Generate prioritized summary recommendations"""
    all_recommendations = []

    # Critical issues first
    for category in ['completeness', 'professional_quality', 'best_practices']:
        for issue in review_results[category].get('issues', []):
            all_recommendations.append(f"🔴 CRITICAL: {issue}")

    # Standard recommendations
    for category in ['completeness', 'professional_quality', 'best_practices', 'industry_standards']:
        for rec in review_results[category].get('recommendations', []):
            if rec not in all_recommendations:  # Avoid duplicates
                all_recommendations.append(f"🟡 {rec}")

    return all_recommendations[:10]  # Top 10 recommendations


def review_artifact(
    artifact_path: str,
    artifact_type: Optional[str] = None,
    review_level: str = 'standard',
    focus_areas: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Review artifact content for quality and best practices

    Args:
        artifact_path: Path to artifact file
        artifact_type: Type of artifact (auto-detected if not provided)
        review_level: Review depth (quick, standard, comprehensive)
        focus_areas: Specific areas to focus on

    Returns:
        Review report with quality assessment and recommendations
    """
    file_path = Path(artifact_path)

    if not file_path.exists():
        return {
            'success': False,
            'error': f"Artifact file not found: {artifact_path}",
            'quality_rating': 'N/A',
            'readiness_score': 0
        }

    with open(file_path, 'r') as f:
        content = f.read()

    file_format = file_path.suffix.lstrip('.')
    if file_format not in ['yaml', 'yml', 'md']:
        return {
            'success': False,
            'error': f"Unsupported file format: {file_format}",
            'quality_rating': 'N/A',
            'readiness_score': 0
        }

    # Detect artifact type
    detected_type = detect_artifact_type(file_path, content)
    final_type = artifact_type or detected_type or "unknown"

    # Parse YAML if applicable
    data = {}
    if file_format in ['yaml', 'yml']:
        try:
            data = yaml.safe_load(content)
        except:
            data = {}

    # Initialize review results
    review_results = {
        'artifact_path': str(file_path.absolute()),
        'artifact_type': final_type,
        'file_format': file_format,
        'review_level': review_level,
        'reviewed_at': datetime.now().isoformat()
    }

    # Perform reviews
    review_results['completeness'] = analyze_content_completeness(content, data, file_format)
    review_results['professional_quality'] = analyze_professional_quality(content, file_format)
    review_results['best_practices'] = check_best_practices(content, final_type, data)
    review_results['industry_standards'] = check_industry_standards(content, final_type)

    # Calculate overall scores
    readiness_score = calculate_readiness_score(review_results)
    quality_rating = determine_quality_rating(readiness_score)

    # Generate summary
    summary_recommendations = generate_summary_recommendations(review_results)

    # Collect all strengths
    all_strengths = []
    for category in ['completeness', 'professional_quality', 'best_practices', 'industry_standards']:
        all_strengths.extend(review_results[category].get('strengths', []))

    return {
        'success': True,
        'review_results': review_results,
        'readiness_score': readiness_score,
        'quality_rating': quality_rating,
        'summary_recommendations': summary_recommendations,
        'strengths': all_strengths[:10]  # Top 10 strengths
    }


def main():
    """Main entry point for artifact.review skill"""
    parser = argparse.ArgumentParser(
        description='AI-powered artifact content review for quality and best practices'
    )
    parser.add_argument(
        'artifact_path',
        type=str,
        help='Path to artifact file to review'
    )
    parser.add_argument(
        '--artifact-type',
        type=str,
        help='Type of artifact (auto-detected if not provided)'
    )
    parser.add_argument(
        '--review-level',
        type=str,
        choices=['quick', 'standard', 'comprehensive'],
        default='standard',
        help='Review depth level'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='Save review report to file'
    )

    args = parser.parse_args()

    # Review artifact
    result = review_artifact(
        artifact_path=args.artifact_path,
        artifact_type=args.artifact_type,
        review_level=args.review_level
    )

    # Save to file if requested
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            yaml.dump(result, f, default_flow_style=False, sort_keys=False)
        print(f"\nReview report saved to: {output_path}")

    # Print report
    if not result['success']:
        print(f"\n{'='*70}")
        print(f"✗ Review Failed")
        print(f"{'='*70}")
        print(f"Error: {result['error']}")
        print(f"{'='*70}\n")
        return 1

    rr = result['review_results']

    print(f"\n{'='*70}")
    print(f"Artifact Content Review Report")
    print(f"{'='*70}")
    print(f"Artifact:        {rr['artifact_path']}")
    print(f"Type:            {rr['artifact_type']}")
    print(f"Review Level:    {rr['review_level']}")
    print(f"")
    print(f"Quality Rating:  {result['quality_rating']}")
    print(f"Readiness Score: {result['readiness_score']}/100")
    print(f"")

    # Content Completeness
    comp = rr['completeness']
    print(f"Content Completeness: {comp['score']}/100")
    print(f"  Word Count: {comp['word_count']}")
    print(f"  Placeholders: {comp['placeholder_count']}")
    if comp['strengths']:
        for strength in comp['strengths']:
            print(f"  ✅ {strength}")
    if comp['issues']:
        for issue in comp['issues']:
            print(f"  ❌ {issue}")
    print()

    # Professional Quality
    prof = rr['professional_quality']
    print(f"Professional Quality: {prof['score']}/100")
    if prof['strengths']:
        for strength in prof['strengths']:
            print(f"  ✅ {strength}")
    if prof['issues']:
        for issue in prof['issues']:
            print(f"  ❌ {issue}")
    print()

    # Best Practices
    bp = rr['best_practices']
    print(f"Best Practices: {bp['score']}/100")
    if bp['strengths']:
        for strength in bp['strengths']:
            print(f"  ✅ {strength}")
    if bp['issues']:
        for issue in bp['issues']:
            print(f"  ❌ {issue}")
    print()

    # Industry Standards
    ist = rr['industry_standards']
    print(f"Industry Standards: {ist['score']}/100")
    if ist['referenced_standards']:
        print(f"  ✅ References: {', '.join(ist['referenced_standards'])}")
    if ist['strengths']:
        for strength in ist['strengths']:
            print(f"  ✅ {strength}")
    print()

    # Top Recommendations
    print(f"Top Recommendations:")
    for rec in result['summary_recommendations']:
        print(f"  {rec}")
    print()

    # Overall Assessment
    print(f"Overall Assessment:")
    if result['readiness_score'] >= 90:
        print(f"  ✅ Excellent quality - ready for approval/publication")
    elif result['readiness_score'] >= 75:
        print(f"  ✅ Good quality - minor improvements recommended")
    elif result['readiness_score'] >= 60:
        print(f"  🟡 Fair quality - needs refinement before approval")
    elif result['readiness_score'] >= 40:
        print(f"  🟠 Needs improvement - significant work required")
    else:
        print(f"  🔴 Poor quality - major revision needed")

    print(f"{'='*70}\n")

    return 0


if __name__ == '__main__':
    sys.exit(main())
