# Data Protection Impact Assessment (DPIA)
## GDPR Article 35 Compliance Assessment

**Document ID:** DPIA-[PROJECT-NAME]-[YYYY-MM]
**Version:** 1.0.0
**Assessment Date:** [YYYY-MM-DD]
**Status:** Draft | In Review | Approved | Superseded

---

## Document Control

| Field | Value |
|-------|-------|
| **Organization** | [Organization Legal Name] |
| **Processing Activity** | [Name of Data Processing Activity] |
| **Project/System** | [Project or System Name] |
| **DPO Contact** | [Data Protection Officer Name & Email] |
| **Assessment Owner** | [Privacy Lead/Product Manager] |
| **Business Owner** | [Business Unit/Department] |
| **Classification** | Confidential |
| **Review Frequency** | Annually or upon significant change |
| **Next Review Date** | [YYYY-MM-DD] |
| **Retention Period** | 7 years after processing cessation |

### Version History

| Version | Date | Author | Changes | Approver |
|---------|------|--------|---------|----------|
| 1.0.0 | YYYY-MM-DD | [Name] | Initial DPIA | [DPO Name] |

### Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Data Protection Officer** | [Name] | [Electronic Signature] | YYYY-MM-DD |
| **Business Owner** | [Name] | [Electronic Signature] | YYYY-MM-DD |
| **CISO/Security Lead** | [Name] | [Electronic Signature] | YYYY-MM-DD |
| **Executive Sponsor** | [Name] | [Electronic Signature] | YYYY-MM-DD |

---

## Executive Summary

### Purpose of DPIA
[2-3 sentence summary of why this DPIA is being conducted and what processing activity it covers]

### High-Risk Processing Determination
- [ ] **Systematic and extensive profiling** with significant effects on individuals
- [ ] **Large-scale processing of special category data** (Article 9) or criminal conviction data (Article 10)
- [ ] **Systematic monitoring of publicly accessible areas** on a large scale
- [ ] **Automated decision-making with legal or similarly significant effect** (Article 22)
- [ ] **Processing on a large scale**
- [ ] **Matching or combining datasets** from different sources
- [ ] **Processing data concerning vulnerable data subjects** (children, employees, asylum seekers)
- [ ] **Innovative use of technology** (AI/ML, biometrics, geolocation)
- [ ] **Processing prevents data subjects from exercising rights** or using services
- [ ] **Cross-border data transfers** outside EEA

**DPIA Required:** Yes | No
**Justification:** [Explain which criteria trigger DPIA requirement per EDPB Guidelines 3/2019]

### Overall Risk Assessment

**Inherent Risk Level:** Critical | High | Medium | Low
**Residual Risk Level (after mitigations):** Critical | High | Medium | Low

**Key Findings:**
- [Summary point 1]
- [Summary point 2]
- [Summary point 3]

**Supervisory Authority Consultation Required:** Yes | No
**Justification:** [If high residual risk remains despite mitigations, consultation required per GDPR Article 36]

---

## 1. Processing Activity Description

### 1.1 Nature of Processing

**Processing Activity Name:** [Descriptive name]

**Business Purpose/Objective:**
[Detailed description of why this processing is necessary for the organization]

**Legal Entity Responsible:**
- **Data Controller:** [Legal entity name and contact details]
- **Joint Controllers:** [If applicable, list and describe arrangement per Article 26]
- **Data Processors:** [List processors and describe their processing activities]

**Processing Start Date:** [YYYY-MM-DD]
**Expected Processing Duration:** Ongoing | Fixed term until [YYYY-MM-DD]

**Processing Operations:**
- [ ] Collection (from data subjects, third parties, public sources)
- [ ] Recording/Storage
- [ ] Organization/Structuring
- [ ] Adaptation/Alteration
- [ ] Retrieval/Consultation
- [ ] Use for [specify purpose]
- [ ] Disclosure to [specify recipients]
- [ ] Combination with other datasets
- [ ] Restriction of processing
- [ ] Erasure/Destruction
- [ ] Transfer to third countries or international organizations
- [ ] Automated decision-making/Profiling

**Technologies Used:**
- [ ] Cloud computing ([Provider name] - [Location])
- [ ] Artificial Intelligence/Machine Learning
- [ ] Biometric recognition systems
- [ ] Video surveillance/CCTV
- [ ] Geolocation tracking
- [ ] Cookies and tracking technologies
- [ ] Big data analytics
- [ ] Internet of Things (IoT) devices
- [ ] Blockchain
- Other: [Specify]

### 1.2 Scope of Processing

**Data Subjects:**
| Category | Description | Estimated Volume |
|----------|-------------|------------------|
| Customers | [Description] | [Number/range] |
| Employees | [Description] | [Number/range] |
| Job Applicants | [Description] | [Number/range] |
| Website Visitors | [Description] | [Number/range] |
| Children (<16 years) | [Description] | [Number/range] |
| Vulnerable Individuals | [Description] | [Number/range] |
| Other: [Specify] | [Description] | [Number/range] |

**Personal Data Categories:**
| Data Category | Specific Data Elements | Special Category? | Retention Period |
|---------------|------------------------|-------------------|------------------|
| **Identification** | Name, email, phone, address | No | [Period] |
| **Demographic** | Age, gender, nationality | No | [Period] |
| **Financial** | Payment card, bank account | No | [Period] |
| **Professional** | Job title, employer, salary | No | [Period] |
| **Online** | IP address, cookies, device ID | No | [Period] |
| **Location** | GPS coordinates, address history | No | [Period] |
| **Behavioral** | Browsing history, purchase history | No | [Period] |
| **Special Category - Health** | Medical records, health status | **Yes (Art. 9)** | [Period] |
| **Special Category - Biometric** | Fingerprints, facial recognition | **Yes (Art. 9)** | [Period] |
| **Special Category - Genetic** | DNA, genetic test results | **Yes (Art. 9)** | [Period] |
| **Special Category - Racial/Ethnic** | Race, ethnicity | **Yes (Art. 9)** | [Period] |
| **Special Category - Political** | Political opinions, memberships | **Yes (Art. 9)** | [Period] |
| **Special Category - Religious** | Religious beliefs | **Yes (Art. 9)** | [Period] |
| **Special Category - Philosophical** | Philosophical beliefs | **Yes (Art. 9)** | [Period] |
| **Special Category - Trade Union** | Trade union membership | **Yes (Art. 9)** | [Period] |
| **Special Category - Sexual** | Sexual orientation, sex life | **Yes (Art. 9)** | [Period] |
| **Criminal Conviction Data** | Criminal history, offenses | **Yes (Art. 10)** | [Period] |

**Processing Scale:**
- **Volume of data subjects:** [Number]
- **Geographic scope:** Local | National | EEA-wide | Global
- **Processing frequency:** Continuous | Daily | Weekly | Monthly | One-time
- **Processing duration:** [Timeframe]

### 1.3 Context of Processing

**Relationship with Data Subjects:**
- [ ] Customers/Clients
- [ ] Employees
- [ ] Business partners
- [ ] Website visitors
- [ ] No direct relationship (publicly available data)

**Data Subject Expectations:**
[Describe what data subjects would reasonably expect regarding the processing of their data]

**Power Imbalance:**
- [ ] Employer-employee relationship
- [ ] Public authority processing
- [ ] Children's data
- [ ] Vulnerable individuals
- [ ] No significant power imbalance

**Level of Control:**
- [ ] Data subjects can easily opt-out
- [ ] Data subjects can access and modify their data
- [ ] Data subjects have limited control
- [ ] Data subjects cannot easily withdraw consent

---

## 2. Necessity and Proportionality Assessment

### 2.1 Legal Basis (GDPR Article 6)

**Primary Legal Basis:**
- [ ] **Consent** (Article 6(1)(a)) - Freely given, specific, informed, unambiguous indication
- [ ] **Contract** (Article 6(1)(b)) - Necessary for contract performance or pre-contractual steps
- [ ] **Legal Obligation** (Article 6(1)(c)) - Compliance with legal obligation
- [ ] **Vital Interests** (Article 6(1)(d)) - Protection of life or physical integrity
- [ ] **Public Task** (Article 6(1)(e)) - Performance of task in public interest or official authority
- [ ] **Legitimate Interests** (Article 6(1)(f)) - Pursuit of legitimate interests (requires LIA)

**Legal Basis Justification:**
[Detailed explanation of why this legal basis applies and how it is satisfied]

**Special Category Data - Additional Legal Basis (Article 9(2)):**
If processing special category data, select additional condition:
- [ ] **Explicit consent** (Article 9(2)(a))
- [ ] **Employment law** (Article 9(2)(b))
- [ ] **Vital interests** (Article 9(2)(c))
- [ ] **Legitimate activities of foundation/association** (Article 9(2)(d))
- [ ] **Data manifestly made public** (Article 9(2)(e))
- [ ] **Legal claims** (Article 9(2)(f))
- [ ] **Substantial public interest** (Article 9(2)(g))
- [ ] **Health/social care** (Article 9(2)(h))
- [ ] **Public health** (Article 9(2)(i))
- [ ] **Archiving/research/statistics** (Article 9(2)(j))

### 2.2 Legitimate Interests Assessment (if applicable)

**Legitimate Interest Pursued:**
[Describe the legitimate interest - must be lawful, clearly articulated, and real/present]

**Necessity Test:**
- Is the processing necessary to achieve the legitimate interest? **Yes | No**
- Are there less intrusive means to achieve the same objective? **Yes | No**
- [Explanation]

**Balancing Test:**
| Factor | Controller Interest | Data Subject Impact | Assessment |
|--------|---------------------|---------------------|------------|
| Strength of interest | [High/Medium/Low] | [High/Medium/Low] | [Analysis] |
| Nature of data | [Sensitivity] | [Risk level] | [Analysis] |
| Reasonable expectations | [Controller view] | [Subject view] | [Analysis] |
| Mitigations available | [Measures] | [Effectiveness] | [Analysis] |

**Conclusion:** Legitimate interests override | Do not override data subject rights

### 2.3 Purpose Limitation (Article 5(1)(b))

**Specified, Explicit, Legitimate Purposes:**
1. [Purpose 1 - be specific and granular]
2. [Purpose 2]
3. [Purpose 3]

**Compatible Processing Assessment:**
If processing for purposes other than original collection:
- Relationship between original and new purposes: [Analysis]
- Context of collection: [Analysis]
- Nature of data and potential impact: [Analysis]
- Safeguards applied: [Analysis]
- **Conclusion:** Compatible | Not compatible | Additional legal basis required

### 2.4 Data Minimization (Article 5(1)(c))

**Minimization Analysis:**
| Data Element | Necessary? | Justification | Alternative Considered |
|--------------|------------|---------------|------------------------|
| [Data 1] | Yes/No | [Reason] | [Alternative if No] |
| [Data 2] | Yes/No | [Reason] | [Alternative if No] |

**Data Collection Limits:**
- [ ] Only personal data adequate and relevant to purposes is collected
- [ ] Excessive data collection has been eliminated
- [ ] Optional vs. mandatory data clearly distinguished
- [ ] Privacy-enhancing technologies considered (pseudonymization, anonymization)

### 2.5 Storage Limitation (Article 5(1)(e))

**Retention Schedule:**
| Data Category | Retention Period | Legal/Business Justification | Deletion Method |
|---------------|------------------|------------------------------|-----------------|
| [Category 1] | [Period] | [Justification] | [Secure deletion/anonymization] |
| [Category 2] | [Period] | [Justification] | [Secure deletion/anonymization] |

**Retention Review:**
- [ ] Retention periods based on legal requirements, contractual obligations, or business needs
- [ ] Automated deletion processes implemented
- [ ] Regular reviews scheduled to delete outdated data
- [ ] Archiving for compliance purposes (GDPR does not apply to anonymized archives)

---

## 3. Data Subject Rights Assessment

### 3.1 Rights Implementation

| Right (GDPR Article) | Implemented? | How? | Limitations/Exceptions |
|----------------------|--------------|------|------------------------|
| **Right to be informed** (13-14) | Yes/No/Partial | [Privacy notice, layered approach] | [None/Exceptions] |
| **Right of access** (15) | Yes/No/Partial | [Self-service portal, request process] | [None/Exceptions] |
| **Right to rectification** (16) | Yes/No/Partial | [Profile update, data correction process] | [None/Exceptions] |
| **Right to erasure** (17) | Yes/No/Partial | [Account deletion, right to be forgotten] | [Legal obligations, legitimate interests] |
| **Right to restrict processing** (18) | Yes/No/Partial | [Restriction flag in systems] | [None/Exceptions] |
| **Right to data portability** (20) | Yes/No/Partial | [Export in machine-readable format] | [Only applies to automated processing] |
| **Right to object** (21) | Yes/No/Partial | [Opt-out mechanism, stop profiling] | [Compelling legitimate grounds] |
| **Rights re: automated decision-making** (22) | Yes/No/Partial/N/A | [Human intervention, explanation] | [Necessary for contract, legal basis] |

### 3.2 Transparency Measures

**Privacy Notice/Policy:**
- [ ] Accessible, concise, transparent, intelligible privacy notice provided
- [ ] Identity and contact details of controller and DPO
- [ ] Purposes of processing and legal basis
- [ ] Legitimate interests (if applicable)
- [ ] Recipients or categories of recipients
- [ ] International transfers and safeguards
- [ ] Retention periods or criteria
- [ ] Data subject rights and how to exercise them
- [ ] Right to lodge complaint with supervisory authority
- [ ] Source of data (if not collected from data subject)
- [ ] Existence of automated decision-making/profiling and logic involved

**Notice Delivery Method:**
- [ ] Website privacy policy
- [ ] Point-of-collection notice
- [ ] Email notification
- [ ] In-app notification
- [ ] Just-in-time notice

**Language and Accessibility:**
- [ ] Plain language, avoiding legal/technical jargon
- [ ] Layered approach (summary + detailed notice)
- [ ] Accessible to persons with disabilities (WCAG 2.1 AA compliance)
- [ ] Translated to languages of data subjects

---

## 4. Privacy Risk Identification and Assessment

### 4.1 Risk Assessment Methodology

**Risk Criteria:**
- **Likelihood:** Negligible (1) | Low (2) | Medium (3) | High (4) | Very High (5)
- **Severity of Impact:** Negligible (1) | Limited (2) | Significant (3) | Severe (4) | Critical (5)
- **Risk Score:** Likelihood × Severity (1-25 scale)

**Risk Levels:**
- **Low (1-5):** Minimal risk, standard controls sufficient
- **Medium (6-12):** Moderate risk, enhanced controls required
- **High (13-20):** Significant risk, extensive mitigation needed
- **Critical (21-25):** Severe risk, may require supervisory authority consultation

### 4.2 Privacy Risks to Data Subjects

#### Risk 1: [Risk Title - e.g., Unauthorized Access to Sensitive Personal Data]

**Risk Description:**
[Detailed description of the privacy risk and how it could occur]

**Affected Data Subjects:** [Which categories]

**Potential Harms:**
- [ ] Physical harm
- [ ] Financial loss
- [ ] Reputational damage
- [ ] Discrimination
- [ ] Identity theft
- [ ] Loss of confidentiality
- [ ] Loss of control over personal data
- [ ] Limitation of rights or freedoms
- [ ] Psychological harm
- Other: [Specify]

**Likelihood:** [1-5] - [Justification]

**Severity:** [1-5] - [Justification based on:]
- Number of affected data subjects: [High/Medium/Low]
- Sensitivity of data: [High/Medium/Low]
- Ease of identification: [High/Medium/Low]
- Vulnerability of data subjects: [High/Medium/Low]

**Inherent Risk Score:** [1-25]

**Existing Controls/Mitigations:**
1. [Control 1 - e.g., Encryption at rest and in transit (AES-256)]
2. [Control 2 - e.g., Role-based access controls with least privilege]
3. [Control 3 - e.g., Multi-factor authentication for system access]

**Residual Risk Score (after controls):** [1-25]

**Risk Owner:** [Name/Role]

**Additional Mitigations Required:**
- [ ] [Mitigation 1] - Priority: Critical | High | Medium | Low - Due: [Date]
- [ ] [Mitigation 2] - Priority: Critical | High | Medium | Low - Due: [Date]

**Final Residual Risk:** [1-25] after additional mitigations

---

#### Risk 2: [Risk Title - e.g., Profiling Leading to Discriminatory Decisions]

[Repeat structure from Risk 1]

---

#### Risk 3: [Risk Title - e.g., Data Breach Due to Vendor Security Failure]

[Repeat structure from Risk 1]

---

[Continue for all identified risks]

### 4.3 Risk Summary Matrix

| Risk ID | Risk Title | Inherent Risk | Residual Risk (Current) | Residual Risk (After Mitigations) | Status |
|---------|------------|---------------|-------------------------|-----------------------------------|--------|
| R1 | [Risk title] | High (16) | Medium (9) | Low (4) | Mitigations in progress |
| R2 | [Risk title] | Critical (20) | High (15) | Medium (8) | Open |
| R3 | [Risk title] | Medium (12) | Low (6) | Low (6) | Closed |

**Overall Residual Risk Assessment:** Critical | High | Medium | Low

---

## 5. Technical and Organizational Measures

### 5.1 Security Measures (Article 32)

#### 5.1.1 Technical Measures

**Encryption:**
- [ ] **Data at rest:** AES-256 encryption for databases and file storage
- [ ] **Data in transit:** TLS 1.2+ for all network communications
- [ ] **End-to-end encryption:** [Where applicable]
- [ ] **Key management:** Hardware Security Module (HSM) or KMS with key rotation

**Access Controls:**
- [ ] **Authentication:** Multi-factor authentication (MFA) required for all users
- [ ] **Authorization:** Role-based access control (RBAC) with least privilege
- [ ] **Privileged Access Management:** PAM solution for admin access with session recording
- [ ] **Access reviews:** Quarterly access recertification

**Network Security:**
- [ ] **Firewalls:** Next-generation firewalls with application awareness
- [ ] **Network segmentation:** DMZ, production, and data zones separated
- [ ] **Intrusion detection/prevention:** SIEM with real-time alerting
- [ ] **DDoS protection:** Cloud-based DDoS mitigation

**Data Protection:**
- [ ] **Pseudonymization:** [Describe implementation]
- [ ] **Anonymization:** [Describe techniques - k-anonymity, differential privacy]
- [ ] **Data masking:** Production data masked in non-production environments
- [ ] **Data loss prevention (DLP):** DLP rules for sensitive data exfiltration prevention

**Logging and Monitoring:**
- [ ] **Audit logging:** Comprehensive logs of all access to personal data
- [ ] **Log retention:** Logs retained for [period] in tamper-proof storage
- [ ] **SIEM monitoring:** 24/7 security operations center (SOC) monitoring
- [ ] **Anomaly detection:** ML-based user behavior analytics (UBA)

**Vulnerability Management:**
- [ ] **Patch management:** Critical patches within 7 days, high within 30 days
- [ ] **Vulnerability scanning:** Weekly automated scans
- [ ] **Penetration testing:** Annual third-party penetration testing
- [ ] **Secure SDLC:** Security integrated into development lifecycle

#### 5.1.2 Organizational Measures

**Policies and Procedures:**
- [ ] Data Protection Policy
- [ ] Information Security Policy
- [ ] Access Control Policy
- [ ] Data Retention and Disposal Policy
- [ ] Incident Response Plan
- [ ] Business Continuity/Disaster Recovery Plan
- [ ] Vendor Management Policy
- [ ] Privacy by Design and Default Policy

**Governance:**
- [ ] Data Protection Officer (DPO) appointed and empowered
- [ ] Privacy governance committee established
- [ ] Regular privacy impact assessments
- [ ] Privacy program maturity assessment

**Training and Awareness:**
- [ ] **Privacy training:** Mandatory annual privacy training for all employees
- [ ] **Role-based training:** Specialized training for developers, IT, customer service
- [ ] **Security awareness:** Monthly phishing simulations and security tips
- [ ] **Training completion:** 98%+ completion rate tracked

**Physical Security:**
- [ ] Badge-controlled access to facilities
- [ ] Visitor management and escort requirements
- [ ] Clean desk policy
- [ ] Secure disposal (shredding, degaussing)
- [ ] CCTV monitoring of sensitive areas

**Business Continuity:**
- [ ] **Backups:** Daily incremental, weekly full backups with 3-2-1 strategy
- [ ] **Disaster recovery:** RTO [time], RPO [time]
- [ ] **High availability:** Multi-region deployment with automatic failover
- [ ] **DR testing:** Quarterly disaster recovery exercises

### 5.2 Privacy by Design and Default (Article 25)

**Privacy by Design:**
- [ ] Privacy integrated into system design from the outset
- [ ] Privacy risk assessments conducted during design phase
- [ ] Privacy-enhancing technologies (PETs) evaluated and implemented
- [ ] Data minimization embedded in system architecture
- [ ] Purpose limitation enforced through system controls

**Privacy by Default:**
- [ ] Default settings provide highest privacy protection
- [ ] Opt-in (not opt-out) for non-essential processing
- [ ] Minimal data collected by default
- [ ] Shortest retention period by default
- [ ] Access restricted by default (least privilege)

### 5.3 Data Processor Safeguards (Article 28)

**Processor Due Diligence:**
- [ ] Vendor privacy and security assessment completed
- [ ] SOC 2 Type II or ISO 27001 certification verified
- [ ] Data Processing Agreement (DPA) executed
- [ ] Sub-processor notification and approval process

**Data Processing Agreements:**
| Processor | Processing Activity | DPA Executed | Security Assessment | Audit Rights |
|-----------|---------------------|--------------|---------------------|--------------|
| [Vendor 1] | [Activity] | Yes - [Date] | Completed - [Date] | Annual |
| [Vendor 2] | [Activity] | Yes - [Date] | Completed - [Date] | Annual |

**DPA Terms Include:**
- [ ] Processing only on documented instructions
- [ ] Confidentiality obligations for personnel
- [ ] Security measures (Article 32)
- [ ] Sub-processor requirements
- [ ] Data subject rights assistance
- [ ] Breach notification obligations
- [ ] Deletion or return of data at contract end
- [ ] Audit and inspection rights

### 5.4 International Data Transfers

**Transfer Mechanisms:**
| Recipient | Country | Transfer Mechanism | Adequacy | Additional Safeguards |
|-----------|---------|--------------------|-----------|-----------------------|
| [Entity 1] | [Country] | Standard Contractual Clauses (SCCs) | Not adequate | SCCs + encryption + access controls |
| [Entity 2] | [Country] | Adequacy Decision | Adequate | None required |
| [Entity 3] | USA | Data Privacy Framework | Adequate (if certified) | DPF certification verified |

**Transfer Impact Assessment (Schrems II Compliance):**
- [ ] **Legal framework analysis:** Assessment of third country laws (surveillance, data access)
- [ ] **Practical effectiveness:** Verification that safeguards are effective in practice
- [ ] **Supplementary measures:** Encryption, pseudonymization, contractual obligations
- [ ] **Continuous monitoring:** Ongoing monitoring of third country legal changes

**Safeguards for Non-Adequate Countries:**
- [ ] Standard Contractual Clauses (2021 SCCs)
- [ ] Binding Corporate Rules (BCRs)
- [ ] Technical measures: Encryption with EU-held keys
- [ ] Contractual measures: Enhanced data protection obligations
- [ ] Organizational measures: Limited access, audit rights

---

## 6. Consultation and Sign-Off

### 6.1 Stakeholder Consultation

| Stakeholder | Role | Consulted? | Date | Key Input |
|-------------|------|------------|------|-----------|
| Data Protection Officer | Privacy oversight | Yes | YYYY-MM-DD | [Input provided] |
| Information Security | Security controls | Yes | YYYY-MM-DD | [Input provided] |
| Legal Counsel | Legal compliance | Yes | YYYY-MM-DD | [Input provided] |
| IT/Engineering | Technical implementation | Yes | YYYY-MM-DD | [Input provided] |
| Business Unit Owner | Business requirements | Yes | YYYY-MM-DD | [Input provided] |
| Data Subjects (if applicable) | User perspective | Yes/No | YYYY-MM-DD | [Input provided] |

### 6.2 Data Protection Officer Opinion

**DPO Assessment:**
[DPO provides formal opinion on whether the processing complies with GDPR, whether risks are adequately mitigated, and whether supervisory authority consultation is required]

**DPO Recommendation:**
- [ ] **Approve** - Processing may proceed as described
- [ ] **Approve with conditions** - Processing may proceed if [conditions] implemented
- [ ] **Reject** - Processing should not proceed due to [reasons]
- [ ] **Defer** - Additional mitigations required before decision

**DPO Signature:** ________________________ **Date:** __________

### 6.3 Supervisory Authority Prior Consultation (Article 36)

**Consultation Required?** Yes | No

**Determination:**
If residual risk remains high despite mitigations, consult supervisory authority before processing.

**Consultation Details (if applicable):**
- **Supervisory Authority:** [ICO, CNIL, etc.]
- **Consultation Date:** [YYYY-MM-DD]
- **Reference Number:** [SA reference]
- **Authority Response:** [Summary of guidance/decision]
- **Conditions Imposed:** [Any requirements from SA]

---

## 7. Implementation Plan and Monitoring

### 7.1 Mitigation Implementation Plan

| Mitigation | Priority | Owner | Due Date | Status | Verification Method |
|------------|----------|-------|----------|--------|---------------------|
| [Mitigation 1] | Critical | [Name] | YYYY-MM-DD | Not Started / In Progress / Complete | [Testing, audit, review] |
| [Mitigation 2] | High | [Name] | YYYY-MM-DD | In Progress | [Testing, audit, review] |
| [Mitigation 3] | Medium | [Name] | YYYY-MM-DD | Complete | [Testing, audit, review] |

### 7.2 Ongoing Monitoring

**Review Triggers:**
- [ ] Annually (scheduled review)
- [ ] Significant change in processing activities
- [ ] New technologies introduced
- [ ] Data breach or security incident
- [ ] Regulatory changes (new laws, supervisory authority guidance)
- [ ] Changes in risks (new vulnerabilities, threats)
- [ ] Complaints from data subjects
- [ ] Audit findings

**Monitoring Activities:**
- [ ] Quarterly risk review meetings
- [ ] Annual DPIA refresh
- [ ] Continuous control effectiveness monitoring
- [ ] Vendor security assessment reviews
- [ ] Incident and breach analysis

### 7.3 DPIA Register Entry

**DPIA recorded in organizational DPIA register:**
- [ ] Yes - Register ID: [ID]
- Processing activity summary recorded
- Risk level documented
- Review schedule established

---

## 8. Conclusion and Decision

### 8.1 Summary of Findings

**Compliance with GDPR Principles:**
- [ ] **Lawfulness, fairness, transparency** - [Compliant/Issues identified]
- [ ] **Purpose limitation** - [Compliant/Issues identified]
- [ ] **Data minimization** - [Compliant/Issues identified]
- [ ] **Accuracy** - [Compliant/Issues identified]
- [ ] **Storage limitation** - [Compliant/Issues identified]
- [ ] **Integrity and confidentiality** - [Compliant/Issues identified]
- [ ] **Accountability** - [Compliant/Issues identified]

**Overall Assessment:**
[Summary paragraph of DPIA conclusions, key risks, mitigations, and compliance status]

### 8.2 Processing Decision

**Decision:** Proceed | Proceed with Conditions | Do Not Proceed | Defer

**Justification:**
[Explanation of decision based on DPIA findings, risk assessment, and mitigation effectiveness]

**Conditions (if applicable):**
1. [Condition 1 - must be met before/during processing]
2. [Condition 2]
3. [Condition 3]

**Responsible Executive Signature:**

_______________________________
[Name], [Title]
Date: ______________

---

## Appendices

### Appendix A: Data Flow Diagram
[Visual diagram showing how personal data flows through systems, including collection, storage, processing, sharing, and deletion]

### Appendix B: Privacy Notice
[Copy of or link to privacy notice provided to data subjects]

### Appendix C: Data Processing Agreements
[List of all DPAs with processors, or links to executed agreements]

### Appendix D: Legitimate Interests Assessment (LIA)
[Detailed LIA if Article 6(1)(f) is legal basis - separate from main DPIA]

### Appendix E: Transfer Impact Assessment
[Detailed assessment per Schrems II for international transfers to non-adequate countries]

### Appendix F: Consultation Records
[Meeting notes, emails, and documentation of stakeholder consultation process]

### Appendix G: Risk Assessment Details
[Extended risk analysis, threat modeling, attack scenarios]

---

## Document References

### Regulatory References
- **GDPR:** Articles 5, 6, 9, 13-14, 25, 32, 35, 36
- **EDPB Guidelines 3/2019:** Guidelines on processing of personal data through video devices
- **EDPB Guidelines 4/2019:** Article 25 Data Protection by Design and by Default
- **ICO DPIA Guidance:** https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/accountability-and-governance/data-protection-impact-assessments/
- **CNIL PIA Methodology:** https://www.cnil.fr/en/privacy-impact-assessment-pia

### Internal References
- Data Protection Policy [Link/Reference]
- Privacy by Design Standard [Link/Reference]
- Data Retention Schedule [Link/Reference]
- Incident Response Plan [Link/Reference]
- Records of Processing Activities (Article 30) [Link/Reference]

---

**DPIA Completion Date:** [YYYY-MM-DD]
**Next Scheduled Review:** [YYYY-MM-DD]
**Document Control:** DPIA-[PROJECT-NAME]-[VERSION]

---

*This DPIA template complies with GDPR Article 35 requirements and incorporates guidance from ICO, CNIL, EDPB, and ISO/IEC 29134. Customize all bracketed fields and sections based on your specific processing activity.*
