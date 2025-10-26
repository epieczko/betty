# Name: skills-matrix

## Executive Summary

The Skills Matrix is a comprehensive talent assessment and planning tool that maps individual and team competencies across technical skills, domain knowledge, and soft skills using standardized proficiency levels. This strategic HR and engineering management artifact visualizes skill distribution, identifies critical skill gaps, guides hiring and development priorities, and supports succession planning by making organizational capabilities transparent and measurable.

Built on competency frameworks like the Dreyfus Model of Skill Acquisition (Novice, Competent, Proficient, Expert, Master) and the T-shaped skills concept (depth in one area, breadth across many), this matrix enables Engineering Managers, Team Leads, and HR partners to assess current capabilities, forecast future needs, plan training investments, and build resilient teams with appropriate skill coverage and redundancy for business continuity.

### Strategic Importance

- **Skill Gap Identification**: Reveals critical capability gaps requiring hiring, training, or contractors
- **T-Shaped Skills Development**: Balances specialists (I-shaped) with generalists (T-shaped) for team resilience
- **Succession Planning**: Identifies single points of failure and develops backup expertise
- **Hiring Prioritization**: Guides recruitment based on documented skill gaps and strategic needs
- **Training Investment**: Focuses L&D budget on highest-impact skill development opportunities
- **Team Formation**: Enables balanced team composition with complementary skill sets
- **Career Pathing**: Supports individual development plans aligned with organizational needs

## Purpose & Scope

### Primary Purpose

This artifact assesses and visualizes individual and team competencies across technical skills, domain knowledge, and soft skills to enable data-driven decisions on hiring, training, team composition, and succession planning. It transforms subjective skill assessments into structured, comparable data for strategic workforce planning.

### Scope

**In Scope**:
- Competency levels: Novice, Competent, Proficient, Expert, Master (Dreyfus Model)
- Technical skills: programming languages, frameworks, tools, platforms, architectures
- Domain knowledge: business domain expertise, industry knowledge, product understanding
- Soft skills: communication, leadership, mentoring, facilitation, stakeholder management
- T-shaped skills assessment: depth (expertise) vs. breadth (working knowledge)
- Skill gap analysis: comparing current state vs. required capabilities
- Team-level skill distribution: coverage, redundancy, single points of failure
- Career development paths: skill progression roadmaps per role/level
- Hiring needs: prioritized skill gaps requiring recruitment
- Training plans: L&D investments aligned with capability needs

**Out of Scope**:
- Performance reviews and compensation decisions (separate HR process)
- Team organizational structure and topologies (see team-topology-map)
- Service ownership and operational responsibilities (see ownership-charters)
- RACI for project execution (see raci-per-workstream)
- Time allocation and capacity planning (see time-allocation-worksheets)
- Initiative-level governance (see initiative-charter)

### Target Audience

**Primary Audience**:
- Engineering Managers assessing team capabilities and planning hiring/training
- Team Leads identifying skill development needs for their team members
- HR/People Teams supporting talent acquisition, L&D, and succession planning
- Organizational Designers ensuring teams have necessary skills for their mission

**Secondary Audience**:
- Individual Contributors understanding their skill development opportunities
- Product Leaders ensuring teams have domain expertise for their product areas
- CTOs and VPs assessing organizational capability maturity
- Recruiting teams prioritizing technical hiring based on documented gaps

## Document Information

**Format**: Markdown

**File Pattern**: `*.skills-matrix.md`

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

**Version Control**: Store in centralized version control system (Git, SharePoint with versioning, etc.) to maintain complete history and enable rollback
**Naming Conventions**: Follow organization's document naming standards for consistency and discoverability
**Template Usage**: Use approved templates to ensure completeness and consistency across teams
**Peer Review**: Have at least one qualified peer review before submitting for approval
**Metadata Completion**: Fully complete all metadata fields to enable search, classification, and lifecycle management
**Stakeholder Validation**: Review draft with key stakeholders before finalizing to ensure alignment and buy-in
**Plain Language**: Write in clear, concise language appropriate for the intended audience; avoid unnecessary jargon
**Visual Communication**: Include diagrams, charts, and tables to communicate complex information more effectively
**Traceability**: Reference source materials, related documents, and dependencies to provide context and enable navigation
**Regular Updates**: Review and update on scheduled cadence or when triggered by significant changes
**Approval Evidence**: Maintain clear record of who approved, when, and any conditions or caveats
**Distribution Management**: Clearly communicate where artifact is published and notify stakeholders of updates
**Retention Compliance**: Follow organizational retention policies for how long to maintain and when to archive/destroy
**Skill Assessment Best Practices**:
- **Consistent Rubrics**: Use standardized Dreyfus levels (Novice/Competent/Proficient/Expert/Master) with clear definitions
- **Self-Assessment Plus Validation**: Employees self-assess; managers validate for calibration
- **Behavioral Anchors**: Define concrete behaviors for each proficiency level per skill
- **Regular Updates**: Refresh skills matrix quarterly or semi-annually as skills evolve
- **Avoid Inflation**: Resist pressure to overstate capabilities; accuracy enables better planning
- **Privacy Considerations**: Limit visibility of individual assessments; share aggregated team views
- **Focus on Critical Skills**: Don't try to assess everything; prioritize strategically important capabilities

**T-Shaped Skills Development**:
- **Depth First**: Ensure each person has at least one area of deep expertise (Expert or Master)
- **Breadth Second**: Encourage working knowledge (Competent) across adjacent areas
- **Team Complementarity**: Compose teams with overlapping T's for knowledge sharing
- **Career Pathing**: Provide paths for I-shaped specialists to broaden into T-shapes
- **Cross-Training**: Facilitate learning opportunities in adjacent domains
- **Pair Programming**: Effective for knowledge transfer and skill development

**Gap Analysis and Planning**:
- **Critical vs. Nice-to-Have**: Prioritize gaps that block strategic initiatives or create risk
- **Build vs. Buy**: Decide whether to train existing staff or hire for gaps
- **Succession Risk**: Identify skills with only one expert (bus factor analysis)
- **Future Needs**: Anticipate skill requirements from technology roadmap
- **Skill Adjacency**: Leverage transferable skills (e.g., Java to Kotlin, React to Vue)
- **Quick Wins**: Identify where small training investments yield high impact

**Hiring and Recruiting**:
- **Prioritized Job Reqs**: Use skills matrix to justify and prioritize open roles
- **Skill-Based Interviewing**: Assess for documented capability gaps
- **Balanced Hiring**: Mix senior hires (immediate impact) with junior hires (long-term investment)
- **Diversity Sourcing**: Build diverse skill perspectives through inclusive recruiting
- **Realistic Job Previews**: Share skill requirements honestly to set expectations

**Learning and Development Investment**:
- **Training Budget Allocation**: Prioritize L&D for highest-impact skill gaps
- **Certification Support**: Fund relevant certifications (AWS, Kubernetes, etc.)
- **Conference Attendance**: Send people to conferences aligned with development goals
- **Internal Training**: Experts mentor others to spread knowledge
- **Learning Time**: Allocate dedicated time for skill development (e.g., 10% time for learning)
- **Cohort-Based Learning**: Group training for teams developing same skills

**Team Composition and Formation**:
- **Skill Coverage**: Ensure teams have necessary skills for their mission
- **Redundancy Planning**: Avoid single points of failure for critical skills
- **Junior-Senior Mix**: Balance experienced engineers with developing talent
- **Cross-Functional**: Include necessary domain, technical, and soft skills
- **Platform Expertise**: Embed platform skills in stream-aligned teams

**Career Development Integration**:
- **Individual Development Plans**: Align skill growth with career goals
- **Skill Targets by Level**: Define expected skills for Junior, Mid, Senior, Staff, etc.
- **Promotion Criteria**: Link promotions to demonstrated skill progression
- **Mentorship Matching**: Pair learners with experts in target skill areas
- **Stretch Assignments**: Provide opportunities to develop new capabilities

**Tools and Visualization**:
- **Heatmaps**: Color-code skill levels for quick visual assessment (red=gap, green=strong)
- **Radar Charts**: Visualize individual skill profiles across dimensions
- **Team Aggregation**: Roll up to show team-level capability coverage
- **Trend Tracking**: Show skill development progress over time
- **Gap Dashboards**: Highlight critical gaps requiring attention

**Governance Alignment**: Align skills matrix with talent strategy and workforce planning
**Metric-Driven**: Track skill development velocity, gap closure rate, training ROI
**Privacy and Ethics**: Handle individual skill data with confidentiality; aggregate for reporting
**Regular Review**: Quarterly skills assessment and semi-annual strategic planning
**Transparency**: Share team-level capabilities to enable informed staffing decisions

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

**Competency Assessment Models**:
- Dreyfus Model of Skill Acquisition: Novice → Competent → Proficient → Expert → Master
- Bloom's Taxonomy: Knowledge → Comprehension → Application → Analysis → Synthesis → Evaluation
- SFIA (Skills Framework for the Information Age): 7-level competency framework for IT professionals
- European e-Competence Framework (e-CF): 40 competencies across 5 proficiency levels
- IEEE Software Engineering Competency Model (SWECOM)
- ACM/IEEE Computer Science Curricula competency frameworks

**Skill Shape Models**:
- T-shaped skills: Deep expertise in one area, broad knowledge across many
- Pi-shaped skills: Deep expertise in two complementary areas
- M-shaped skills: Multiple areas of deep expertise
- Comb-shaped skills: Multiple areas of varying depth
- I-shaped skills: Deep specialist with narrow focus (less desirable for resilience)
- Dash-shaped skills: Broad generalist without deep expertise

**Technical Skill Taxonomies**:
- Programming languages: Python, Java, JavaScript, TypeScript, Go, Rust, C++, etc.
- Frontend frameworks: React, Vue, Angular, Svelte
- Backend frameworks: Spring, Django, Flask, Node.js/Express, .NET
- Cloud platforms: AWS, Azure, GCP certifications and services
- DevOps tools: Docker, Kubernetes, Terraform, Ansible, Jenkins, GitLab CI
- Databases: PostgreSQL, MySQL, MongoDB, Redis, Elasticsearch
- Architecture patterns: Microservices, event-driven, serverless, domain-driven design

**Leadership and Soft Skills Frameworks**:
- Emotional Intelligence (EQ): Self-awareness, self-regulation, motivation, empathy, social skills
- Situational Leadership: adapting leadership style to team maturity
- Communication skills: technical writing, presentations, facilitation, stakeholder management
- Mentoring and coaching: developing others' capabilities
- Conflict resolution and negotiation
- Influence without authority

**Career Laddering and Levels**:
- Engineering career ladders: Junior → Mid → Senior → Staff → Principal → Distinguished
- Individual Contributor (IC) vs. Management tracks
- Dual ladder systems: technical and management career paths
- Competency progression by level: expectations at each career stage
- Promotion criteria and skill requirements

**Skills Gap Analysis**:
- Current state vs. desired state mapping
- Critical vs. nice-to-have skills prioritization
- Make vs. buy analysis: train existing staff vs. hire external talent
- Skills inventory: comprehensive list of current organizational capabilities
- Succession risk analysis: single points of failure, bus factor
- Future skills forecasting: anticipating technology shifts

**Learning and Development (L&D)**:
- 70-20-10 model: 70% on-the-job learning, 20% coaching/mentoring, 10% formal training
- Competency-based training programs
- Certification programs: AWS, Azure, GCP, Kubernetes (CKA/CKAD), Scrum, etc.
- Internal training academies and bootcamps
- Mentorship programs and pair programming
- Conference and workshop attendance
- Book clubs and learning communities

**Talent Management Frameworks**:
- 9-box grid: performance vs. potential talent assessment
- Succession planning: identifying and developing high-potentials
- Talent pipeline: building bench strength for key roles
- Skills-based hiring: assessing competencies in recruitment
- Competency-based interviews: behavioral and technical assessments
- Onboarding programs: ramping new hires to productivity

**Workforce Planning**:
- Strategic workforce planning: aligning talent with business strategy
- Capability heatmaps: visualizing organizational strengths and weaknesses
- Skills forecasting: anticipating future needs based on roadmap
- Hiring plans: prioritizing recruitment by skill gap criticality
- Contractor vs. FTE decisions: temporary vs. permanent skill acquisition
- Skill adjacency analysis: leveraging transferable skills

**Team Composition Models**:
- Cross-functional teams: diverse skill sets for autonomy
- Skill coverage: ensuring redundancy for critical capabilities
- Junior-Senior ratios: balancing experience levels for sustainability
- Specialist vs. generalist mix: team resilience considerations
- Domain expert allocation: distributing business knowledge
- Platform expertise: embedded skills for platform adoption

**HR Technology and Tools**:
- Skills management platforms: Degreed, Workday Skills Cloud, LinkedIn Learning
- Competency assessment tools: 360-degree feedback, peer reviews
- Learning Management Systems (LMS): Cornerstone, SAP SuccessFactors
- Skills matrix templates: Excel, Google Sheets, Miro, specialized tools
- Talent marketplace platforms: internal mobility and project staffing
- Skills analytics and reporting dashboards

**Performance Management Integration**:
- OKRs aligned with skill development goals
- Individual Development Plans (IDPs): personalized learning paths
- Skill development as performance metric
- Continuous feedback and coaching
- Quarterly skill assessment reviews
- Career conversations and growth planning

**Industry Standards and Certifications**:
- Cloud certifications: AWS Solutions Architect, Azure Administrator, GCP Professional
- Kubernetes: CKA (Certified Kubernetes Administrator), CKAD (Developer)
- Agile/Scrum: Certified Scrum Master (CSM), SAFe certifications
- Security: CISSP, CEH, Security+
- Project Management: PMP, PRINCE2
- ITIL: IT Service Management certifications

**Organizational Capability Maturity**:
- Capability Maturity Model Integration (CMMI)
- DevOps maturity assessments
- Agile maturity models
- Platform engineering maturity
- Engineering effectiveness benchmarks

**Diversity, Equity, Inclusion (DEI)**:
- Bias reduction in skill assessments
- Equal access to development opportunities
- Diverse hiring to build varied skill perspectives
- Inclusive mentorship and sponsorship programs
- Skills-based evaluation reducing demographic bias

**Related Standards**:
- ISO 30414: Human Capital Reporting guidelines
- ISO 9001: Quality management competence requirements
- ANSI/SHRM: Society for HR Management standards
- PMI Talent Triangle: Technical, Leadership, Strategic skills

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
