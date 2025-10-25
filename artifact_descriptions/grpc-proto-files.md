# Name: grpc-proto-files

## Executive Summary

gRPC Proto Files define service contracts for gRPC APIs using Protocol Buffers (Protobuf) Interface Definition Language (IDL). These .proto files specify service methods, message types, field definitions, and streaming patterns that enable high-performance, type-safe, bidirectional communication between microservices using HTTP/2 transport.

Built using Protocol Buffers v3 syntax, proto files leverage protoc compiler for code generation across 10+ languages (Java, Go, Python, C++, C#, Node.js, Ruby, PHP), support four streaming modes (unary, server-streaming, client-streaming, bidirectional streaming), and enable features like backward/forward compatibility, efficient binary serialization, automatic API documentation, and strongly-typed contracts for polyglot microservices architectures running on Kubernetes, service meshes (Istio, Linkerd), and cloud platforms.

### Strategic Importance

- **Strategic Alignment**: Ensures activities and decisions support organizational objectives
- **Standardization**: Promotes consistent approach and quality across teams and projects
- **Risk Management**: Identifies and mitigates risks through structured analysis
- **Stakeholder Communication**: Facilitates clear, consistent communication among diverse audiences
- **Knowledge Management**: Captures and disseminates institutional knowledge and best practices
- **Compliance**: Supports adherence to regulatory, policy, and contractual requirements
- **Continuous Improvement**: Enables measurement, learning, and process refinement

## Purpose & Scope

### Primary Purpose

This artifact defines gRPC service contracts using Protocol Buffers IDL, specifying service interfaces, RPC methods, request/response message types, streaming patterns, and data structures. It enables contract-first API development, cross-language code generation, type-safe communication, and efficient binary serialization for high-performance microservices.

### Scope

**In Scope**:
- Protocol Buffers v3 syntax (.proto files)
- Service definitions with RPC methods
- Message types and field definitions
- Streaming modes: unary, server-streaming, client-streaming, bidirectional
- Scalar types (int32, int64, float, double, bool, string, bytes)
- Complex types (message, enum, oneof, map, repeated)
- Package namespacing and imports
- Field numbering and reserved fields
- Options and custom options
- Well-known types (Timestamp, Duration, Empty, Any, Struct)

**Out of Scope**:
- gRPC server/client implementation code
- Interceptors and middleware logic
- Service deployment and infrastructure
- Load balancing and service discovery
- TLS/SSL certificate configuration
- Monitoring and tracing implementation

### Target Audience

**Primary Audience**:
- API Engineers designing gRPC services
- Backend Engineers implementing microservices
- Platform Engineers managing service contracts
- Polyglot teams using multiple programming languages

**Secondary Audience**:
- Software Architects reviewing API design
- DevOps Engineers deploying gRPC services
- QA Engineers testing service contracts
- Mobile Engineers consuming gRPC APIs

## Document Information

**Format**: Text

**File Pattern**: `*.grpc-proto-files.txt`

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

**Proto3 Syntax**:
- **Always Use Proto3**: Use `syntax = "proto3";` at top of file
- **Package Naming**: Use reverse domain notation (com.company.service.v1)
- **File Organization**: One service per .proto file; separate messages into logical files
- **Imports**: Use well-known types from google/protobuf when appropriate

**Field Numbering**:
- **Never Change Field Numbers**: Field numbers are part of wire format; changing breaks compatibility
- **Reserve Deleted Fields**: Use `reserved` keyword to prevent number reuse
- **Number Ranges**: Use 1-15 for frequently used fields (1-byte encoding)
- **Sequential Numbering**: Number fields sequentially; don't leave gaps
- **Reserved Ranges**: Reserve ranges for future extensions (e.g., 1000-2000)

**Schema Evolution**:
- **Backward Compatibility**: New clients can read old messages
- **Forward Compatibility**: Old clients can read new messages
- **Safe Changes**: Add new fields, delete optional fields, change field names
- **Breaking Changes**: Never change field numbers or types
- **Deprecation**: Mark deprecated fields with `[deprecated = true]`

**Message Design**:
- **Meaningful Names**: Use clear, descriptive message names (CreateUserRequest, not Req)
- **Request/Response Pattern**: Suffix with Request/Response (GetOrderRequest, GetOrderResponse)
- **Nested Messages**: Use nested messages for closely related types
- **Avoid Deep Nesting**: Keep message nesting shallow (2-3 levels max)
- **Empty Messages**: Use google.protobuf.Empty for empty requests/responses

**Field Design**:
- **Optional Fields**: All fields in proto3 are optional by default
- **Required Data**: Use validation, not proto2 required keyword
- **Repeated Fields**: Use `repeated` for arrays/lists
- **Maps**: Use `map<key_type, value_type>` for key-value pairs
- **Oneof**: Use `oneof` for mutually exclusive fields

**Service Design**:
- **Unary RPCs**: Use for simple request-response (GetUser, CreateOrder)
- **Server Streaming**: Use for large result sets (ListUsers returns stream)
- **Client Streaming**: Use for uploading data (UploadFile sends stream)
- **Bidirectional Streaming**: Use for real-time communication (Chat)

**Naming Conventions**:
- **Services**: PascalCase (UserService, OrderService)
- **Methods**: PascalCase (GetUser, CreateOrder, DeleteProduct)
- **Messages**: PascalCase (User, Order, Product)
- **Fields**: snake_case (user_id, created_at, first_name)
- **Enums**: UPPER_SNAKE_CASE (USER_STATUS_ACTIVE, ORDER_TYPE_RETAIL)

**Enum Design**:
- **Zero Value**: First enum value must be zero (UNKNOWN or UNSPECIFIED)
- **Explicit Values**: Assign explicit values to all enum constants
- **Prefix Enums**: Prefix enum values with enum name to avoid conflicts
- **Deprecation**: Mark deprecated enum values clearly

**Well-Known Types**:
- **Timestamp**: Use google.protobuf.Timestamp for date-time
- **Duration**: Use google.protobuf.Duration for time spans
- **Empty**: Use google.protobuf.Empty for void/null
- **Any**: Use google.protobuf.Any for dynamic types (sparingly)
- **Wrappers**: Use wrappers for nullable primitives (Int32Value, StringValue)

**API Versioning**:
- **Package Versioning**: Include version in package (com.company.service.v1)
- **Major Versions**: Create new package for breaking changes (v1 -> v2)
- **Multiple Versions**: Support multiple API versions simultaneously
- **Deprecation Period**: Maintain old versions during transition

**Error Handling**:
- **Status Codes**: Use standard gRPC status codes
- **Rich Errors**: Use google.rpc.Status for detailed error information
- **Error Details**: Include ErrorInfo, DebugInfo, RetryInfo
- **Client Errors**: 4xx-equivalent for client errors (INVALID_ARGUMENT, NOT_FOUND)
- **Server Errors**: 5xx-equivalent for server errors (INTERNAL, UNAVAILABLE)

**Documentation**:
- **Comments**: Add comments to all services, methods, messages, fields
- **Method Description**: Explain what method does, when to use it
- **Field Description**: Document field purpose, format, constraints
- **Examples**: Provide usage examples in comments

**Code Generation**:
- **Buf**: Use Buf for modern protobuf workflow (linting, generation, breaking change detection)
- **Multi-Language**: Generate code for all target languages
- **Version Control**: Check in .proto files; optionally generated code
- **CI/CD Integration**: Auto-generate code in build pipeline

**Linting & Validation**:
- **Buf Lint**: Use Buf linting rules for consistency
- **Breaking Changes**: Detect breaking changes in CI/CD
- **Style Guide**: Follow Google's Protocol Buffers Style Guide
- **Automated Checks**: Validate proto files in pull requests

**Performance**:
- **Message Size**: Keep messages small; avoid large nested structures
- **Field Ordering**: Place frequently used fields in 1-15 range
- **Streaming**: Use streaming for large data transfers
- **Compression**: Enable gRPC compression for large payloads

**Security**:
- **TLS**: Always use TLS in production
- **Authentication**: Use JWT or OAuth2 tokens in metadata
- **Authorization**: Implement field-level authorization
- **Input Validation**: Validate all inputs on server side
- **Sensitive Data**: Avoid logging sensitive fields

**Testing**:
- **Contract Testing**: Test that implementations match proto definitions
- **Backward Compatibility**: Test old clients with new servers
- **Forward Compatibility**: Test new clients with old servers
- **Load Testing**: Use ghz or similar for gRPC load testing

**Dependency Management**:
- **Buf Registry**: Use Buf Schema Registry for proto dependencies
- **Versioned Dependencies**: Pin proto dependency versions
- **Shared Protos**: Extract common types to shared proto modules
- **Import Paths**: Use consistent import paths across projects

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

**Protocol Buffers**:
- Protocol Buffers v3 (proto3 syntax)
- Language-neutral, platform-neutral serialization
- Binary wire format (efficient, compact)
- Text format (for debugging, human-readable)
- JSON mapping for interoperability

**gRPC Framework**:
- gRPC Core (C-based implementation)
- HTTP/2 transport protocol
- Multiplexing (multiple RPCs over single connection)
- Flow control and bidirectional streaming
- Deadline/timeout propagation
- Metadata (headers) support

**Streaming Patterns**:
- Unary RPC: Single request, single response
- Server streaming: Single request, stream of responses
- Client streaming: Stream of requests, single response
- Bidirectional streaming: Stream of requests and responses

**Scalar Types**:
- Integer types: int32, int64, uint32, uint64, sint32, sint64, fixed32, fixed64, sfixed32, sfixed64
- Floating point: float, double
- Boolean: bool
- String: string (UTF-8 or 7-bit ASCII)
- Bytes: bytes (arbitrary byte sequence)

**Complex Types**:
- message (composite types, nested messages)
- enum (enumerated values)
- oneof (one field active at a time)
- map (key-value pairs: map<key_type, value_type>)
- repeated (array/list of values)

**Well-Known Types**:
- google.protobuf.Timestamp (date-time)
- google.protobuf.Duration (time span)
- google.protobuf.Empty (no data)
- google.protobuf.Any (arbitrary message type)
- google.protobuf.Struct (JSON-like structures)
- google.protobuf.FieldMask (field selection)
- google.protobuf.Wrappers (nullable primitives)

**Code Generation**:
- protoc compiler (official Protocol Buffers compiler)
- Language plugins: protoc-gen-go, protoc-gen-java, protoc-gen-python, protoc-gen-grpc-web
- Buf (modern protoc alternative with enhanced features)
- grpc-gateway (gRPC to REST/JSON transcoding)

**Compatibility Rules**:
- Never change field numbers of existing fields
- Can add new fields (will be ignored by old clients)
- Can delete optional fields (use reserved to prevent reuse)
- Can change field names (wire format uses numbers)
- Can't change field types (breaking change)

**Service Definition**:
- Service keyword defines RPC service
- rpc keyword defines methods
- Request/response message types
- Streaming keywords: stream

**gRPC Implementations**:
- gRPC-Go (official Go implementation)
- grpc-java (official Java implementation)
- grpc-node (Node.js)
- grpc-python
- grpc-dotnet (C#/.NET)
- grpc-web (browser support)
- grpc-swift (iOS/macOS)
- grpc-kotlin

**Service Mesh Integration**:
- Istio (traffic management, observability)
- Linkerd (lightweight service mesh)
- Envoy proxy (gRPC load balancing)
- Consul Connect
- AWS App Mesh

**Error Handling**:
- gRPC status codes (OK, CANCELLED, UNKNOWN, INVALID_ARGUMENT, DEADLINE_EXCEEDED, NOT_FOUND, etc.)
- google.rpc.Status for rich error details
- Error details with google.rpc.ErrorInfo, DebugInfo, RetryInfo

**Interceptors & Middleware**:
- Unary interceptors (before/after RPC)
- Streaming interceptors (stream lifecycle)
- Authentication interceptors
- Logging and metrics interceptors
- Retry and circuit breaker logic

**Load Balancing**:
- Client-side load balancing
- Round-robin, least-request algorithms
- Subchannel management
- Health checking protocol

**Security**:
- TLS/SSL encryption (transport security)
- OAuth2 token authentication
- JWT (JSON Web Tokens)
- mTLS (mutual TLS)
- Application-level authentication

**Reflection & Introspection**:
- gRPC Server Reflection Protocol
- grpcurl (curl for gRPC)
- grpcui (web UI for gRPC services)
- BloomRPC, Postman (gRPC clients)

**Tooling**:
- buf (linting, breaking change detection, dependency management)
- grpcurl (command-line gRPC client)
- ghz (gRPC benchmarking tool)
- grpc-ecosystem (gateway, health checking, middleware)
- Evans (gRPC CLI client)

**API Design Patterns**:
- Pagination (page tokens, limit)
- Filtering and sorting
- Field masks (partial responses)
- Long-running operations (google.longrunning.Operation)
- Batch operations

**Cloud Platform Support**:
- Google Cloud (Cloud Run, GKE, Endpoints)
- AWS (App Runner, ECS, EKS, App Mesh)
- Azure (AKS, Container Apps)
- gRPC native support in all major clouds

**Reference**: Consult organizational architecture and standards team for detailed guidance on framework application. Refer to grpc.io and developers.google.com/protocol-buffers.

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
