# Name: kustomize-manifests

## Executive Summary

Kustomize Manifests are declarative Kubernetes configuration artifacts that enable template-free, environment-specific customization of YAML manifests through a layered overlay approach. As a native Kubernetes configuration management tool (kubectl apply -k), Kustomize uses bases, overlays, patches, and generators to maintain DRY (Don't Repeat Yourself) principles while supporting GitOps workflows and progressive delivery patterns.

Unlike templating systems (Helm, Jsonnet), Kustomize operates on pure Kubernetes YAML through strategic merge patches, JSON patches, and resource transformers, preserving the declarative nature of Kubernetes manifests while enabling composition, reuse, and environment-specific variations. This approach aligns with GitOps principles by keeping all configuration in version control with clear provenance and auditability.

### Strategic Importance

- **Template-Free Customization**: Maintains pure Kubernetes YAML without introducing templating languages or complex abstractions
- **GitOps Native**: Seamlessly integrates with ArgoCD and Flux for declarative, Git-based configuration management
- **Environment Parity**: Enables consistent base configurations with minimal, explicit environment-specific overrides
- **Composition & Reuse**: Supports component-based architecture through bases, overlays, and remote references
- **Validation & Testing**: Enables automated validation and testing of composed manifests before cluster application
- **Configuration DRY**: Eliminates duplication through strategic merge patches, JSON patches, and resource generators
- **Progressive Delivery**: Facilitates canary and blue-green deployments through overlay-based configuration variations

## Purpose & Scope

### Primary Purpose

This artifact defines the Kustomize directory structure, kustomization.yaml files, bases, overlays, patches, and resource generators that compose environment-specific Kubernetes manifests. It enables teams to maintain a single source of truth for base configurations while applying targeted customizations for development, staging, production, and multi-region deployments.

### Scope

**In Scope**:
- kustomization.yaml files defining resources, generators, transformers, and patches
- Base directories containing common Kubernetes manifests
- Overlay directories for environment-specific customizations (dev, staging, production)
- Strategic merge patches for partial resource modifications
- JSON patches (RFC 6902) for precise field updates
- ConfigMap generators (configMapGenerator) from files, literals, or env files
- Secret generators (secretGenerator) with similar sourcing options
- Resource transformers (namePrefix, nameSuffix, namespace, labels, annotations)
- Image transformers for container image references
- Replica count transformers for scaling
- Remote bases and components (Git repositories, HTTP URLs)
- Component composition and inheritance patterns
- Multi-base and multi-overlay architectures
- Kustomize plugins and custom transformers

**Out of Scope**:
- Helm charts and Helm-specific templating (covered by installer-manifests)
- Raw Kubernetes manifests without Kustomize organization
- Infrastructure provisioning outside Kubernetes (Terraform, Pulumi, CloudFormation)
- CI/CD pipeline definitions (maintained in pipeline repositories)
- Application source code (managed in application repositories)

### Target Audience

**Primary Audience**:
- Platform Engineers designing Kustomize structure and reusable components
- DevOps Engineers managing environment-specific overlays and deployments
- Application Developers consuming base configurations and creating service-specific overlays

**Secondary Audience**:
- SRE Teams reviewing configuration changes and troubleshooting deployments
- Security Engineers auditing configuration transformations and patches
- GitOps Operators (ArgoCD, Flux) consuming kustomization.yaml for automated sync

## Document Information

**Format**: YAML

**File Pattern**: `*.kustomize-manifests.yaml`

**Naming Convention**: Follow standard pattern with project/initiative identifier, artifact type, and appropriate extension

**Template Location**: Access approved template from centralized template repository

**Storage & Access**: Store in designated document repository with appropriate access controls based on classification

**Classification**: [Define typical classification level - Public | Internal | Confidential | Restricted]

**Retention**: [Define retention period per organizational records management policy]


### Document Control

**Version Information**:
- `version`: Semantic version number (MAJOR.MINOR.PATCH)
- `documentId`: Unique identifier in document management system
- `createdDate`: ISO 8601 timestamp of initial creation
- `lastModified`: ISO 8601 timestamp of most recent update
- `nextReviewDate`: Scheduled date for next formal review
- `documentOwner`: Role/person responsible for maintenance
- `classification`: Information classification level
- `retentionPeriod`: How long document must be retained

**Authorship & Review**:
- `primaryAuthor`: Lead author name and role
- `contributors`: Additional contributors and their roles
- `reviewers`: Designated reviewers (technical, security, compliance, etc.)
- `approvers`: Formal approvers with sign-off authority
- `reviewStatus`: Current review status
- `approvalDate`: Date of formal approval

**Document Purpose**:
- `executiveSummary`: 2-3 paragraph overview for executive audience
- `businessContext`: Why this document exists and its business value
- `scope`: What is covered and what is explicitly out of scope
- `applicability`: Who this applies to and under what circumstances
- `relatedDocuments`: References to related artifacts and dependencies

### Main Content Sections

(Content structure will vary based on specific artifact type. Include all relevant sections needed to fully document the subject matter.)

**Core Information**:
- Document the primary information this artifact is meant to capture
- Organize in logical sections appropriate to the content type
- Use consistent formatting and structure
- Include sufficient detail for intended audience
- Provide examples where helpful

**Supporting Information**:
- Background context necessary for understanding
- Assumptions and constraints
- Dependencies on other artifacts or systems
- Related information and cross-references


## Best Practices

**Minimal Overlays**: Keep overlays small - override only what differs from base, avoiding duplication
**Base Reusability**: Design bases to be reusable across multiple environments and teams
**Semantic Versioning**: Version remote bases using Git tags following semantic versioning
**Hash Suffixes**: Enable hash suffixes for ConfigMaps/Secrets to trigger rolling updates on changes
**Strategic Merge First**: Prefer strategic merge patches over JSON patches for better readability
**Component Composition**: Extract cross-cutting concerns into components (monitoring, security, networking)
**Clear Directory Structure**: Maintain consistent directory structure (base/, overlays/env/, components/)
**Validate Before Merge**: Run kustomize build and schema validation in CI before merging changes
**Document Patches**: Add comments explaining why patches are necessary and what they modify
**Avoid Vars**: Use replacements instead of deprecated vars functionality
**Test Compositions**: Test complete kustomizations with kubeval and conftest in pipelines
**GitOps Workflow**: Store all Kustomize manifests in Git and deploy via ArgoCD/Flux
**Image Digests**: Use image digests instead of tags for immutability and security
**Namespace Consistency**: Set namespace in kustomization.yaml rather than individual resources
**Remote Base Pinning**: Pin remote bases to specific Git commits or tags, not branches
**Patch Ordering**: Understand patch application order (strategic merge, then JSON, then inline)
**Label Standards**: Use consistent labels across all resources (app, version, component, part-of, managed-by)
**Resource Limits**: Include resource requests/limits in base, override in overlays for environment-specific tuning
**ConfigMap Generation**: Use configMapGenerator instead of static ConfigMaps for better change tracking
**Immutable Configs**: Generate immutable ConfigMaps/Secrets for safer rollbacks

## Quality Criteria

Before considering this artifact complete and ready for approval, verify:

✓ **Completeness**: All required sections present and adequately detailed
✓ **Accuracy**: Information verified and validated by appropriate subject matter experts
✓ **Clarity**: Written in clear, unambiguous language appropriate for intended audience
✓ **Consistency**: Aligns with organizational standards, templates, and related artifacts
✓ **Currency**: Based on current information; outdated content removed or updated
✓ **Traceability**: Includes references to source materials and related documents
✓ **Stakeholder Review**: Reviewed by all key stakeholders with feedback incorporated
✓ **Technical Review**: Technical accuracy verified by qualified technical reviewers
✓ **Compliance**: Meets all applicable regulatory, policy, and contractual requirements
✓ **Approval**: All required approvals obtained and documented
✓ **Accessibility**: Stored in accessible location with appropriate permissions
✓ **Metadata**: Complete metadata enables search, categorization, and lifecycle management

## Common Pitfalls & How to Avoid

❌ **Incomplete Information**: Rushing to complete without gathering all necessary inputs
   ✓ *Solution*: Create comprehensive checklist of required information; allocate sufficient time

❌ **Lack of Stakeholder Input**: Creating in isolation without engaging affected parties
   ✓ *Solution*: Identify all stakeholders early; schedule working sessions for collaborative development

❌ **Outdated Content**: Using old information or not updating when conditions change
   ✓ *Solution*: Establish refresh schedule; define triggers requiring immediate update

❌ **Inconsistent Format**: Not following organizational templates and standards
   ✓ *Solution*: Always start from approved template; verify against style guide before submission

❌ **Missing Approvals**: Publishing without proper authorization
   ✓ *Solution*: Understand approval chain; route through all required approvers with evidence

❌ **Poor Version Control**: Making changes without maintaining history
   ✓ *Solution*: Use proper version control system; never directly edit published version

❌ **Inadequate Distribution**: Completing artifact but stakeholders unaware it exists
   ✓ *Solution*: Define distribution list; actively communicate availability and location

❌ **No Maintenance Plan**: Creating artifact as one-time activity with no ongoing ownership
   ✓ *Solution*: Assign owner; schedule regular reviews; define update triggers

## Related Standards & Frameworks

**Kustomize Core**:
- Kustomize (SIG CLI, native kubectl integration with kubectl apply -k)
- kustomization.yaml specification
- kustomize build command for manifest generation
- kustomize edit commands for declarative updates
- API versioning (kustomize.config.k8s.io/v1beta1)

**Resource Management**:
- resources field (list of manifest files and directories)
- Remote resources (Git repos, HTTP URLs)
- Component resources for modular composition
- CRDs (Custom Resource Definitions) handling
- Namespace-scoped vs cluster-scoped resources

**Generators**:
- configMapGenerator (from files, literals, envs)
- secretGenerator (from files, literals, envs, with encryption options)
- generatorOptions (labels, annotations, disableNameSuffixHash)
- Automatic hash suffixing for ConfigMaps/Secrets
- Immutable ConfigMaps and Secrets generation

**Transformers**:
- namePrefix and nameSuffix for resource naming
- namespace transformer for resource scoping
- commonLabels and commonAnnotations
- images transformer for container image management
- replicas transformer for scaling
- Label and annotation selectors

**Patches**:
- Strategic merge patches (patchesStrategicMerge)
- JSON patches (patchesJson6902) following RFC 6902
- Inline patches (patches field with target selectors)
- Patch target selectors (group, version, kind, name, namespace, labelSelector, annotationSelector)

**Composition Patterns**:
- Base and overlay architecture
- Multi-layer overlays (base -> common -> environment-specific)
- Component-based composition
- Inheritance and override patterns
- Remote base references

**GitOps Integration**:
- ArgoCD Kustomize support and integration
- Flux Kustomization CRD
- Automatic sync and drift detection
- Kustomize build caching
- Progressive delivery with overlays

**Directory Structure Patterns**:
- Base directory with common manifests
- Overlays directory with environment subdirectories (dev, staging, prod)
- Components directory for reusable modules
- Environment-specific overlay structure

**Validation & Testing**:
- kustomize build for dry-run validation
- kubeval for Kubernetes schema validation
- conftest for policy-as-code testing
- kustomize-controller reconciliation
- Pre-merge validation in CI pipelines

**Advanced Features**:
- Kustomize plugins (KRM functions)
- Exec plugins for custom transformations
- Go plugins (deprecated in favor of KRM)
- vars and variable substitution (deprecated, use replacements)
- replacements for field value substitution

**Best Practice Patterns**:
- Minimal overlays (override only what differs)
- Avoid duplication between environments
- Use components for cross-cutting concerns
- Remote bases for shared platform components
- Semantic versioning for remote bases

**Security & Secrets**:
- SOPS integration for encrypted secrets
- sealed-secrets generator integration
- Secret generators with encryption
- External Secrets Operator integration
- Avoiding plaintext secrets in Git

**Multi-Cluster Management**:
- Per-cluster overlays
- Cluster-specific configurations
- Federation patterns with Kustomize
- Multi-region deployment configurations

**CI/CD Integration**:
- kustomize build in CI pipelines
- Automated validation and testing
- Image digest updates via kustomize edit set image
- GitOps PR workflows with Kustomize

**Kubernetes Compatibility**:
- kubectl apply -k native support (v1.14+)
- API version compatibility
- Resource ordering and dependencies
- CRD handling and validation

**Reference**: Consult organizational platform engineering and GitOps teams for detailed guidance on Kustomize architecture patterns and best practices

## Integration Points

### Upstream Dependencies (Required Inputs)

These artifacts or information sources should exist before this artifact can be completed:

- [List artifacts that provide input to this one]
- [Data sources that feed this artifact]
- [Prerequisites that must be satisfied]

### Downstream Consumers (Who Uses This)

This artifact provides input to:

- [Artifacts that consume information from this one]
- [Processes that use this artifact]
- [Teams or roles that rely on this information]

### Related Artifacts

Closely related artifacts that should be referenced or aligned with:

- [Complementary artifacts in same phase]
- [Artifacts in adjacent phases]
- [Cross-cutting artifacts (e.g., risk register)]

## Review & Approval Process

### Review Workflow

1. **Author Self-Review**: Creator performs completeness check against template and quality criteria
2. **Peer Review**: Subject matter expert review for technical accuracy and completeness
3. **Stakeholder Review**: Review by all affected stakeholders for alignment and acceptance
4. **Architecture Review**: [If applicable] Architecture board review for standards compliance
5. **Security Review**: [If applicable] Security team review for security requirements
6. **Compliance Review**: [If applicable] Compliance review for regulatory requirements
7. **Legal Review**: [If applicable] Legal counsel review
8. **Final Approval**: Designated approver(s) provide formal sign-off

### Approval Requirements

**Required Approvers**:
- Primary Approver: [Define role - e.g., Program Manager, Architecture Lead, CISO]
- Secondary Approver: [For high-risk or cross-functional artifacts]
- Governance Approval: [If requires board or committee approval]

**Approval Evidence**:
- Document approval in artifact metadata
- Capture approver name, role, date, and any conditional approvals
- Store approval records per records management requirements

## Maintenance & Lifecycle

### Update Frequency

**Regular Reviews**: [Define cadence - e.g., Quarterly, Annually]

**Event-Triggered Updates**: Update immediately when:
- Significant organizational changes occur
- Regulatory requirements change
- Major incidents reveal deficiencies
- Stakeholder requests identify needed updates
- Related artifacts are substantially updated

### Version Control Standards

Use semantic versioning: **MAJOR.MINOR.PATCH**

- **MAJOR**: Significant restructuring, scope changes, or approach changes
- **MINOR**: New sections, substantial additions, or enhancements
- **PATCH**: Corrections, clarifications, minor updates

### Change Log Requirements

Maintain change log with:
- Version number and date
- Author(s) of changes
- Summary of what changed and why
- Impact assessment (who/what is affected)
- Approver of changes

### Archival & Retention

**Retention Period**: [Define based on regulatory and business requirements]

**Archival Process**:
- Move superseded versions to archive repository
- Maintain access for historical reference and audit
- Follow records management policy for eventual destruction

### Ownership & Accountability

**Document Owner**: [Define role responsible for maintenance]

**Responsibilities**:
- Ensure artifact remains current and accurate
- Coordinate required updates
- Manage review and approval process
- Respond to stakeholder questions
- Archive superseded versions

## Templates & Examples

### Template Access

**Primary Template**: `templates/{artifact_name}-template.{format_type.lower()}`

**Alternative Formats**: [If multiple formats supported]

**Template Version**: Use latest approved template version from repository

### Example Artifacts

**Reference Examples**: `examples/{artifact_name}-example-*.{format_type.lower()}`

**Annotated Guidance**: See annotated examples showing best practices and common approaches

### Quick-Start Checklist

Before starting this artifact, ensure:

- [ ] Reviewed template and understand all sections
- [ ] Identified and engaged all required stakeholders
- [ ] Gathered prerequisite information and inputs
- [ ] Obtained access to necessary systems and data
- [ ] Allocated sufficient time for quality completion
- [ ] Identified reviewers and approvers
- [ ] Understood applicable standards and requirements

While creating this artifact:

- [ ] Following approved template structure
- [ ] Documenting sources and references
- [ ] Writing clearly for intended audience
- [ ] Including visual aids where helpful
- [ ] Self-reviewing against quality criteria
- [ ] Seeking input from stakeholders

Before submitting for approval:

- [ ] Completed all required sections
- [ ] Verified accuracy of all information
- [ ] Obtained peer review feedback
- [ ] Addressed all review comments
- [ ] Spell-checked and proofread
- [ ] Completed all metadata fields
- [ ] Verified compliance with standards
- [ ] Ready for formal approval process

## Governance & Compliance

### Regulatory Considerations

[Define any regulatory requirements applicable to this artifact type, such as:]

- SOC 2: [If artifact supports SOC 2 controls]
- ISO 27001: [If part of ISMS documentation]
- GDPR/Privacy: [If contains or references personal data]
- Industry-Specific: [Healthcare, Financial Services, etc.]

### Audit Requirements

This artifact may be subject to:

- Internal audits by IA team
- External audits by third-party auditors
- Regulatory examinations
- Customer security assessments

**Audit Preparation**:
- Maintain complete version history
- Document all approvals with evidence
- Keep change log current
- Ensure accessibility for auditors

### Policy Alignment

This artifact must align with:

- [Relevant organizational policies]
- [Industry regulations and standards]
- [Contractual obligations]
- [Governance framework requirements]

## Metrics & Success Criteria

### Artifact Quality Metrics

- **Completeness Score**: Percentage of template sections completed
- **Review Cycle Time**: Days from draft to approval
- **Defect Rate**: Number of errors found post-approval
- **Stakeholder Satisfaction**: Survey rating from artifact consumers

### Usage Metrics

- **Access Frequency**: How often artifact is accessed/referenced
- **Update Frequency**: How often artifact requires updates
- **Downstream Impact**: How many artifacts/processes depend on this

### Continuous Improvement

- Gather feedback from users and reviewers
- Track common questions or confusion points
- Identify recurring issues or challenges
- Update template and guidance based on lessons learned
- Share best practices across organization

## Metadata Tags

**Phase**: {phase}

**Category**: {category}

**Typical Producers**: [Roles/teams that typically create this artifact]

**Typical Consumers**: [Roles/teams that typically use this artifact]

**Effort Estimate**: [Typical hours/days required to complete]

**Complexity Level**: [Low | Medium | High | Very High]

**Business Criticality**: [Low | Medium | High | Mission Critical]

**Change Frequency**: [Static | Infrequent | Regular | Frequent]

---

*This artifact definition follows Big Five consulting methodology standards and incorporates industry best practices. Tailor to your organization's specific requirements and context.*

*Last Updated: {phase} - Version 2.0*
