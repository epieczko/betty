# Name: idempotency-and-replay-protection-policy

## Executive Summary

The Idempotency And Replay Protection Policy defines strategies and implementation patterns for ensuring operations are executed exactly once, even in the presence of retries, network failures, or duplicate requests. This artifact establishes idempotency key patterns (Stripe-style Idempotency-Key headers), deduplication mechanisms, exactly-once semantics, and event replay protection that prevent duplicate charges, double processing, and data corruption in distributed systems.

Distributed systems face inevitable challenges from network partitions, timeouts, and client retries. Without proper idempotency guarantees, a timeout on a payment request could result in double-charging a customer, a failed API call retry could create duplicate records, or event replay could process the same message multiple times. This artifact specifies idempotency key generation and validation, database-level uniqueness constraints, exactly-once delivery guarantees in messaging systems (Kafka, AWS SQS, Azure Service Bus), deduplication windows, and replay prevention mechanisms that ensure operations are safe to retry.

### Strategic Importance

- **Risk Management**: Mitigates organizational risk through standardized requirements
- **Compliance Assurance**: Ensures adherence to regulatory and legal obligations
- **Consistency**: Drives uniform approach across business units and geographies
- **Accountability**: Establishes clear expectations and consequences
- **Efficiency**: Reduces redundant decision-making through established standards

## Purpose & Scope

### Primary Purpose

This artifact establishes policies and implementation patterns that ensure operations are idempotent (producing the same result when executed multiple times) and protected from replay attacks. It prevents duplicate processing, data corruption, and financial losses that occur when operations are unintentionally executed multiple times due to retries, network issues, or malicious replay attacks.

### Scope

**In Scope**:
- Idempotency key patterns (Idempotency-Key header, request fingerprinting)
- Client-generated vs. server-generated idempotency keys
- Idempotency key storage, lifecycle, and expiration (typically 24 hours)
- Database uniqueness constraints for deduplication
- Exactly-once delivery semantics in messaging systems
- Kafka exactly-once processing (idempotent producers, transactional consumers)
- AWS SQS deduplication (FIFO queues, content-based deduplication)
- Azure Service Bus duplicate detection
- Event sourcing deduplication patterns
- Distributed transaction idempotency (saga pattern, 2PC)
- API retry safety (safe retries vs. unsafe retries)
- Deduplication windows and time-based expiration
- Replay attack prevention (nonce, timestamps, sequence numbers)

**Out of Scope**:
- General API rate limiting (covered by API gateway policies)
- Authentication and authorization mechanisms
- Business logic for transaction processing
- Database transaction isolation levels (separate database policy)

### Target Audience

**Primary Audience**:
- Backend Engineers implementing idempotent APIs
- Platform Engineers building distributed systems infrastructure
- Site Reliability Engineers ensuring system reliability
- Payment Engineers preventing duplicate charges

**Secondary Audience**:
- Security Engineers preventing replay attacks
- API Architects designing resilient APIs
- QA Engineers testing retry behavior
- Product Managers understanding reliability guarantees

## Document Information

**Format**: Markdown

**File Pattern**: `*.idempotency-and-replay-protection-policy.md`

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

**Always Require Idempotency Keys**: Require Idempotency-Key header for all mutating operations (POST, PATCH, non-idempotent PUT)
**Client-Generated Keys**: Prefer client-generated UUIDs for idempotency keys to survive client crashes
**UUID V4 Standard**: Use UUID v4 for idempotency keys to ensure global uniqueness
**24-Hour Window**: Store idempotency keys for 24 hours to handle delayed retries
**Store Original Response**: Cache the full response for idempotent replay, not just success/failure
**Validate Before Processing**: Check idempotency key before starting any state-changing operations
**Atomic Key Insertion**: Use database unique constraints or atomic cache operations (SETNX) to prevent race conditions
**Return Same Response**: For duplicate requests with same key, return cached response with 200 OK (not 409)
**Different Parameters Error**: If request with same key has different parameters, return 422 Unprocessable Entity
**Fail Safe on Storage Failures**: If idempotency key storage fails, reject request (fail safe, not fail open)
**Database Unique Constraints**: Always add unique constraints on business entity IDs to prevent database-level duplicates
**Kafka Exactly-Once Config**: Enable enable.idempotence=true for Kafka producers; use transactions for consumers
**SQS FIFO Queues**: Use FIFO queues with MessageDeduplicationId for operations requiring exactly-once processing
**Event Sourcing IDs**: Always include unique event IDs in event sourcing; check for duplicates before processing
**Saga Compensation Idempotency**: Design saga compensation transactions to be idempotent (safe to retry)
**Exponential Backoff**: Implement exponential backoff with jitter for retries (avoid retry storms)
**Document Retry Safety**: Clearly document which API endpoints are safe to retry and which require idempotency keys
**Monitor Duplicate Rate**: Track and alert on duplicate request rate to detect client retry issues
**Test Retry Scenarios**: Include retry and duplicate request scenarios in integration tests
**Nonce for Replay Protection**: Use nonces (numbers used once) for security-sensitive operations like authentication
**Timestamp Validation**: Validate request timestamps; reject requests older than 5 minutes to prevent replay
**Cleanup Old Keys**: Implement automated cleanup of expired idempotency keys to prevent storage bloat
**Circuit Breaker Integration**: Integrate idempotency checking with circuit breakers for resilience

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

**Idempotency Key Patterns**:
- Idempotency-Key HTTP header (Stripe API pattern)
- Client-generated UUIDs (UUID v4 for uniqueness)
- Request fingerprinting (hash of request body + metadata)
- Composite keys (user_id + operation_id + timestamp)
- Server-generated idempotency tokens
- Idempotency key validation and rejection of reused keys

**Storage & Lifecycle**:
- Idempotency key storage (Redis, database table)
- Key expiration policies (typically 24-hour TTL)
- Response caching (store original response for replay)
- Key cleanup and garbage collection
- Distributed key storage for high availability

**Database Deduplication**:
- Unique constraints (UNIQUE index on idempotency key)
- Upsert operations (INSERT ON CONFLICT, MERGE)
- Check-then-set patterns with locking
- Optimistic concurrency control (version numbers)
- Database-level deduplication (PostgreSQL, MySQL)

**Messaging System Patterns**:
- Kafka exactly-once semantics (idempotent producer config)
- Kafka transactional processing (isolation.level=read_committed)
- AWS SQS FIFO queues (deduplication ID, content-based deduplication)
- AWS SQS visibility timeout for safe retries
- Azure Service Bus duplicate detection (requires duplicate detection)
- Google Pub/Sub deduplication (custom implementation)
- RabbitMQ message deduplication patterns
- Message fingerprinting for deduplication

**Kafka Exactly-Once Configuration**:
- enable.idempotence=true (producer-level idempotency)
- transactional.id configuration
- isolation.level=read_committed (consumer-level)
- exactly_once processing topology
- Checkpointing and offset management

**AWS SQS Deduplication**:
- MessageDeduplicationId parameter
- Content-based deduplication (SHA-256 hash of message body)
- 5-minute deduplication window for FIFO queues
- ReceiptHandle for at-least-once delivery
- Visibility timeout for processing guarantees

**Event Sourcing Patterns**:
- Event ID uniqueness constraints
- Sequence number validation
- Idempotent event handlers
- Snapshot-based replay prevention
- Command deduplication before event generation

**Distributed Transaction Patterns**:
- Saga pattern with idempotent compensating transactions
- Two-phase commit (2PC) with transaction IDs
- Three-phase commit (3PC)
- Outbox pattern for reliable message publishing
- Transaction log tailing for consistency

**API Retry Safety**:
- Safe HTTP methods (GET, HEAD, OPTIONS, TRACE)
- Idempotent HTTP methods (PUT, DELETE)
- Non-idempotent methods requiring protection (POST, PATCH)
- Retry-After header for rate limit backoff
- Exponential backoff with jitter
- Circuit breaker patterns

**Replay Attack Prevention**:
- Nonce (number used once) validation
- Timestamp validation with clock skew tolerance
- Sequence number enforcement
- HMAC signatures with replay window
- JWT jti claim for one-time use tokens
- Request expiration timestamps

**Deduplication Windows**:
- Short-term deduplication (5-15 minutes for retries)
- Long-term deduplication (24 hours for operations)
- Sliding window vs. fixed window
- Trade-offs between window size and storage

**Stripe-Style Idempotency**:
- Idempotency-Key header (client-provided UUID)
- 24-hour idempotency window
- Response replay for duplicate requests
- 409 Conflict for mismatched parameters
- Automatic cleanup after expiration

**Implementation Libraries**:
- idempotency-rs (Rust idempotency library)
- django-idempotency-key (Django middleware)
- express-idempotency (Node.js middleware)
- Stripe API clients (built-in idempotency support)
- Spring Idempotency (Java/Spring Boot)

**Testing Strategies**:
- Chaos engineering for retry storms
- Duplicate request injection testing
- Network partition simulation
- Timeout and retry behavior validation
- Idempotency key collision testing

**Monitoring & Metrics**:
- Idempotency key cache hit rate
- Duplicate request rate
- Replay prevention trigger rate
- Deduplication storage size
- Failed idempotency validation rate

**Standards & Specifications**:
- RFC 5789 (PATCH method idempotency)
- RFC 7231 (HTTP semantics and safe/idempotent methods)
- IETF draft on Idempotency-Key header
- Event-driven architecture patterns (Martin Fowler)

**Reference**: Consult organizational architecture and standards team for detailed guidance on framework application

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
