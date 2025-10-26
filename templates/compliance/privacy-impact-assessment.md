# Privacy Impact Assessment (PIA)

> **Note for GDPR Compliance:** Under GDPR Article 35, Privacy Impact Assessments (PIAs) are referred to as Data Protection Impact Assessments (DPIAs). For EU/EEA processing activities, use the comprehensive **[Data Protection Impact Assessment (DPIA) template](./data-protection-impact-assessment.md)** which includes all GDPR Article 35 requirements.
>
> This PIA template is designed for:
> - Non-GDPR jurisdictions (US, Canada PIPEDA, Australia, etc.)
> - Internal privacy risk assessments
> - CCPA/CPRA privacy risk evaluations
> - Organizational privacy due diligence

**Document ID:** PIA-[PROJECT-NAME]-[YYYY-MM]
**Version:** 1.0.0
**Assessment Date:** [YYYY-MM-DD]
**Status:** Draft | In Review | Approved | Superseded

---

## Document Control

| Field | Value |
|-------|-------|
| **Organization** | [Organization Legal Name] |
| **Processing Activity/Project** | [Name of Processing Activity or Project] |
| **System/Application** | [System or Application Name] |
| **Privacy Lead** | [Privacy Officer/Lead Name & Email] |
| **Assessment Owner** | [Product Manager/Business Owner] |
| **Business Unit** | [Business Unit/Department] |
| **Classification** | Confidential |
| **Review Frequency** | Annually or upon significant change |
| **Next Review Date** | [YYYY-MM-DD] |

### Version History

| Version | Date | Author | Changes | Approver |
|---------|------|--------|---------|----------|
| 1.0.0 | YYYY-MM-DD | [Name] | Initial PIA | [Privacy Lead] |

### Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Privacy Officer/DPO** | [Name] | [Electronic Signature] | YYYY-MM-DD |
| **Business Owner** | [Name] | [Electronic Signature] | YYYY-MM-DD |
| **Information Security** | [Name] | [Electronic Signature] | YYYY-MM-DD |
| **Legal Counsel** | [Name] | [Electronic Signature] | YYYY-MM-DD |

---

## Executive Summary

### Purpose of Assessment
[2-3 sentences describing the project/system/processing activity being assessed and why this PIA is being conducted]

### Privacy Risk Level Assessment
**Overall Privacy Risk:** Critical | High | Medium | Low

**Key Privacy Concerns:**
- [Concern 1]
- [Concern 2]
- [Concern 3]

**Recommendation:** Proceed | Proceed with Conditions | Do Not Proceed | Requires Further Assessment

---

## 1. Project/System Description

### 1.1 Overview

**Project/System Name:** [Name]

**Business Purpose:**
[Detailed description of the business purpose and why this project/system is being implemented]

**Project Sponsor:** [Name/Role]

**Project Team:**
- Product Manager: [Name]
- Technical Lead: [Name]
- Privacy Lead: [Name]
- Security Lead: [Name]

**Project Timeline:**
- **Start Date:** [YYYY-MM-DD]
- **Go-Live Date:** [YYYY-MM-DD]
- **Current Phase:** Planning | Design | Development | Testing | Deployment

### 1.2 System Architecture

**System Type:**
- [ ] Web application
- [ ] Mobile application (iOS, Android)
- [ ] Desktop application
- [ ] Backend/API service
- [ ] Data analytics platform
- [ ] AI/ML system
- [ ] IoT/Connected devices
- [ ] Database/Data warehouse
- [ ] Other: [Specify]

**Hosting Environment:**
- [ ] On-premises data center
- [ ] Public cloud ([AWS/Azure/GCP] - [Region(s)])
- [ ] Private cloud
- [ ] Hybrid cloud
- [ ] Third-party SaaS

**Technologies Used:**
- [ ] Artificial Intelligence/Machine Learning
- [ ] Automated decision-making
- [ ] Biometric processing (fingerprint, facial recognition, etc.)
- [ ] Video surveillance/CCTV
- [ ] Geolocation tracking
- [ ] Cookies and online tracking
- [ ] Big data analytics
- [ ] Blockchain
- Other: [Specify]

---

## 2. Personal Information Assessment

### 2.1 Information Collection

**Personal Information Categories:**

| Category | Specific Data Elements | Sensitivity | Collection Method | Volume |
|----------|------------------------|-------------|-------------------|---------|
| **Identifiers** | Name, email, phone, address, SSN | Medium | Web form | [Estimated #] |
| **Demographics** | Age, gender, race, ethnicity | Medium | User profile | [Estimated #] |
| **Financial** | Credit card, bank account, transaction history | High | Payment processor | [Estimated #] |
| **Health** | Medical records, health status, prescriptions | **Critical** | Health form | [Estimated #] |
| **Biometric** | Fingerprints, facial images, voice prints | **Critical** | Biometric scanner | [Estimated #] |
| **Location** | GPS coordinates, IP address, address history | Medium | Mobile app | [Estimated #] |
| **Online Activity** | Browsing history, search queries, clicks | Low-Medium | Cookies/tracking | [Estimated #] |
| **Government IDs** | Passport, driver's license, SSN, national ID | High | ID verification | [Estimated #] |
| **Employment** | Job title, employer, salary, performance | Medium | HR system | [Estimated #] |
| **Children's Data** | Any data about individuals under 16/13 | **Critical** | Age gate | [Estimated #] |

**Sensitivity Assessment:**
- **Critical:** Biometric, health, children's data, government IDs
- **High:** Financial, precise geolocation, full SSN
- **Medium:** Employment, contact information, demographics
- **Low:** Anonymous usage statistics

### 2.2 Data Subjects

**Affected Individuals:**

| Category | Description | Estimated Volume | Vulnerable? |
|----------|-------------|------------------|-------------|
| Customers/Users | [Description] | [Number] | No |
| Employees | [Description] | [Number] | Yes (power imbalance) |
| Children (<16 yrs) | [Description] | [Number] | **Yes** |
| Job Applicants | [Description] | [Number] | Yes (power imbalance) |
| Website Visitors | [Description] | [Number] | No |
| Other: [Specify] | [Description] | [Number] | [Yes/No] |

**Vulnerable Populations:**
- [ ] Children or minors
- [ ] Employees (power imbalance)
- [ ] Elderly individuals
- [ ] Individuals with disabilities
- [ ] Economically disadvantaged individuals
- [ ] Asylum seekers or immigrants
- [ ] Individuals in healthcare settings

### 2.3 Information Use

**Primary Purposes:**
1. [Purpose 1 - be specific, e.g., "Process customer orders and payments"]
2. [Purpose 2]
3. [Purpose 3]

**Secondary Purposes (if any):**
1. [Purpose 1 - e.g., "Marketing and promotional communications"]
2. [Purpose 2]

**Legal Basis for Processing:**
- [ ] **Consent** - Individual provides opt-in consent
- [ ] **Contract** - Necessary to perform a contract with the individual
- [ ] **Legal Obligation** - Required by law
- [ ] **Vital Interests** - Protecting life or health
- [ ] **Legitimate Interest** - Balancing organizational needs vs. individual rights
- [ ] **Public Interest** - Public sector/government function

**Justification:** [Explain why this legal basis applies]

### 2.4 Information Sharing and Disclosure

**Third-Party Recipients:**

| Recipient | Type | Purpose | Location | Safeguards |
|-----------|------|---------|----------|------------|
| [Company Name] | Service Provider | [Purpose] | [Country] | [DPA, Contract, Encryption] |
| [Company Name] | Business Partner | [Purpose] | [Country] | [Agreement terms] |
| [Government Agency] | Legal Requirement | [Purpose] | [Country] | [Legal basis] |

**Data Processors:**
- [ ] Cloud hosting provider
- [ ] Payment processor
- [ ] Email/communication service
- [ ] Analytics provider
- [ ] Customer support platform
- [ ] Marketing automation
- [ ] Background check provider
- Other: [Specify]

**International Transfers:**
- [ ] No cross-border transfers
- [ ] Transfers within same country
- [ ] Transfers to [Country/Region]

**Transfer Safeguards (if applicable):**
- [ ] Standard Contractual Clauses (SCCs)
- [ ] Binding Corporate Rules (BCRs)
- [ ] Adequacy decision by regulatory authority
- [ ] Privacy Shield or Data Privacy Framework (if applicable)
- [ ] Explicit consent from individuals
- [ ] Other: [Specify]

### 2.5 Data Retention and Disposal

**Retention Schedule:**

| Data Type | Retention Period | Legal/Business Justification | Disposal Method |
|-----------|------------------|------------------------------|-----------------|
| [Data category 1] | [e.g., 7 years] | [Legal requirement/business need] | [Secure deletion/shredding] |
| [Data category 2] | [e.g., Account life + 3 years] | [Justification] | [Method] |

**Automated Deletion:**
- [ ] Yes - Automated processes in place to delete data after retention period
- [ ] No - Manual deletion process
- [ ] Partial - Some data types automated, others manual

---

## 3. Privacy Risk Assessment

### 3.1 Risk Evaluation Methodology

**Risk Scoring:**
- **Likelihood:** Rare (1) | Unlikely (2) | Possible (3) | Likely (4) | Almost Certain (5)
- **Impact:** Negligible (1) | Minor (2) | Moderate (3) | Major (4) | Catastrophic (5)
- **Risk Score:** Likelihood × Impact (1-25)

**Risk Levels:**
- **Low (1-5):** Acceptable risk with standard controls
- **Medium (6-12):** Manageable risk with enhanced controls
- **High (13-20):** Significant risk requiring extensive mitigation
- **Critical (21-25):** Unacceptable risk, may require project redesign or cancellation

### 3.2 Privacy Risks and Harms

#### Risk 1: [Risk Title - e.g., Unauthorized Access to Sensitive Personal Data]

**Risk Description:**
[Detailed description of what could go wrong and how]

**Affected Data Subjects:** [Which categories]

**Potential Harms to Individuals:**
- [ ] Identity theft
- [ ] Financial loss
- [ ] Discrimination or bias
- [ ] Reputational damage
- [ ] Physical safety risk
- [ ] Emotional distress
- [ ] Loss of privacy/confidentiality
- [ ] Loss of control over personal information
- [ ] Stalking or harassment
- [ ] Unwanted contact/spam
- Other: [Specify]

**Likelihood:** [1-5] - **Justification:** [Why this likelihood]

**Impact:** [1-5] - **Justification:** [Based on sensitivity, volume, vulnerability of data subjects]

**Inherent Risk Score:** [1-25]

**Current Controls:**
1. [Control 1 - e.g., "Encryption of data at rest using AES-256"]
2. [Control 2 - e.g., "Multi-factor authentication required"]
3. [Control 3]

**Residual Risk (with current controls):** [1-25]

**Risk Owner:** [Name/Role]

**Additional Mitigations Recommended:**
- [ ] [Mitigation 1] - **Priority:** Critical | High | Medium | Low - **Due:** [Date]
- [ ] [Mitigation 2] - **Priority:** Critical | High | Medium | Low - **Due:** [Date]

**Final Residual Risk (after all mitigations):** [1-25]

---

#### Risk 2: [Risk Title - e.g., Function Creep/Secondary Uses Without Consent]

[Repeat structure from Risk 1]

---

#### Risk 3: [Risk Title - e.g., Discriminatory Algorithmic Decision-Making]

[Repeat structure from Risk 1]

---

### 3.3 Risk Summary Matrix

| Risk ID | Risk Title | Inherent Risk | Current Residual Risk | Target Residual Risk | Status |
|---------|------------|---------------|-----------------------|----------------------|--------|
| R1 | [Risk 1] | High (16) | Medium (9) | Low (4) | Mitigations in progress |
| R2 | [Risk 2] | Critical (20) | High (15) | Medium (8) | Open |
| R3 | [Risk 3] | Medium (12) | Low (6) | Low (6) | Closed |

**Overall Residual Risk:** Critical | High | Medium | Low

---

## 4. Fair Information Practice Principles (FIPPs) Compliance

### 4.1 Notice/Transparency

- [ ] **Privacy notice provided** at point of collection
- [ ] **Clear and conspicuous** notice, not buried in terms
- [ ] **Plain language** written for average consumer, avoiding legalese
- [ ] **Layered notice** approach (short form + detailed notice)
- [ ] **Just-in-time notice** provided at point of data collection

**Privacy Notice Includes:**
- [ ] Identity and contact information of organization
- [ ] Categories of personal information collected
- [ ] Purposes of collection and use
- [ ] Categories of third parties with whom data is shared
- [ ] Individual rights (access, deletion, opt-out, etc.)
- [ ] How to exercise rights
- [ ] Data retention periods
- [ ] Security measures
- [ ] How to contact privacy officer/DPO

**Notice Delivery Method:**
- [ ] Privacy policy on website
- [ ] Point-of-collection notice
- [ ] Email notification
- [ ] In-app notification
- [ ] Physical notice

### 4.2 Choice/Consent

- [ ] **Opt-in consent** obtained for sensitive data or non-essential uses
- [ ] **Opt-out mechanism** provided for marketing communications
- [ ] **Granular choices** (not bundled consent for unrelated purposes)
- [ ] **Easy to withdraw** consent at any time
- [ ] **No negative consequences** for declining non-essential processing

**Consent Mechanism:**
- [ ] Affirmative action required (checkbox, button click)
- [ ] Pre-checked boxes NOT used
- [ ] Consent separate from terms of service
- [ ] Consent recorded with timestamp and method

### 4.3 Access/Participation

**Individual Rights Supported:**
- [ ] **Right to access** - Individuals can view their personal information
- [ ] **Right to rectification** - Individuals can correct inaccurate data
- [ ] **Right to deletion** - Individuals can request deletion (with exceptions)
- [ ] **Right to data portability** - Export data in machine-readable format
- [ ] **Right to opt-out** of sale or sharing (CCPA)
- [ ] **Right to object** to processing
- [ ] **Right to restrict** processing

**Implementation:**
- [ ] Self-service portal for access and updates
- [ ] Manual request process via email/form
- [ ] Identity verification for privacy requests
- [ ] Response within [X] days
- [ ] No fee for requests (or reasonable fee for excessive requests)

### 4.4 Data Minimization

**Minimization Practices:**
- [ ] Only **necessary data** collected for stated purposes
- [ ] **No excessive collection** beyond what's needed
- [ ] **Optional fields** clearly distinguished from mandatory
- [ ] Regular review to **eliminate unused data**
- [ ] **Anonymization or aggregation** where identifiable data not needed

**Data Minimization Assessment:**
| Data Element | Necessary? | Justification | Alternative |
|--------------|------------|---------------|-------------|
| [Field 1] | Yes/No | [Reason] | [If No, what instead?] |
| [Field 2] | Yes/No | [Reason] | [Alternative] |

### 4.5 Use Limitation

- [ ] Data used **only for stated purposes**
- [ ] **No secondary uses** without additional consent
- [ ] **Purpose specification** documented and communicated
- [ ] **Compatible use** assessment for new purposes
- [ ] **No sale** of personal information without consent

### 4.6 Data Quality/Integrity

- [ ] **Accuracy** measures to ensure data is correct and current
- [ ] **Completeness** checks for missing critical data
- [ ] **Timeliness** - outdated data removed or updated
- [ ] **Individuals can correct** inaccurate data
- [ ] **Validation** at point of collection

### 4.7 Security/Safeguards

**Technical Controls:**
- [ ] **Encryption** at rest (AES-256 or equivalent)
- [ ] **Encryption** in transit (TLS 1.2+)
- [ ] **Access controls** - role-based access with least privilege
- [ ] **Multi-factor authentication** for systems with personal data
- [ ] **Logging and monitoring** of access to personal data
- [ ] **Intrusion detection/prevention**
- [ ] **Regular security testing** (penetration testing, vulnerability scans)
- [ ] **Secure development practices** (OWASP, secure code review)

**Organizational Controls:**
- [ ] **Privacy policies and procedures**
- [ ] **Employee training** on privacy and security
- [ ] **Confidentiality agreements** for staff and contractors
- [ ] **Background checks** for personnel with access to sensitive data
- [ ] **Incident response plan** for data breaches
- [ ] **Business continuity/disaster recovery**
- [ ] **Vendor management** and third-party due diligence
- [ ] **Privacy by design** practices

### 4.8 Accountability

- [ ] **Designated privacy officer** or DPO
- [ ] **Privacy governance** structure and oversight
- [ ] **Privacy training** for employees
- [ ] **Vendor contracts** with privacy obligations
- [ ] **Privacy impact assessments** for new projects
- [ ] **Audit and monitoring** of privacy practices
- [ ] **Breach notification procedures**
- [ ] **Regular privacy program assessments**

---

## 5. Legal and Regulatory Compliance

### 5.1 Applicable Privacy Laws

**Jurisdiction-Specific Requirements:**

- [ ] **GDPR** (EU/EEA residents)
  - Special category data provisions (Article 9)
  - Automated decision-making (Article 22)
  - Cross-border transfer requirements

- [ ] **CCPA/CPRA** (California residents)
  - Consumer rights (access, deletion, opt-out of sale)
  - Do Not Sell or Share My Personal Information
  - Sensitive personal information limitations

- [ ] **PIPEDA** (Canada)
  - Consent requirements
  - Breach notification obligations

- [ ] **Privacy Act 1988** (Australia)
  - Australian Privacy Principles (APPs)

- [ ] **LGPD** (Brazil)
  - Data subject rights
  - International transfer restrictions

- [ ] **Other:** [Specify applicable state, national, or sector-specific laws]

**Sector-Specific Requirements:**
- [ ] **HIPAA** (Healthcare - Protected Health Information)
- [ ] **FERPA** (Education - Student records)
- [ ] **COPPA** (Children's Online Privacy Protection Act)
- [ ] **GLBA** (Financial services - Customer financial information)
- [ ] **FCRA** (Fair Credit Reporting Act)
- [ ] **TCPA** (Telephone Consumer Protection Act - marketing calls/texts)

### 5.2 Compliance Assessment

| Requirement | Compliant? | Gap/Notes | Remediation |
|-------------|------------|-----------|-------------|
| [Specific legal requirement 1] | Yes/No/Partial | [Description] | [Action needed] |
| [Specific legal requirement 2] | Yes/No/Partial | [Description] | [Action needed] |

---

## 6. Mitigation Plan and Recommendations

### 6.1 Privacy Enhancements

**Recommended Mitigations:**

| Mitigation | Priority | Responsible Party | Target Date | Status | Cost Estimate |
|------------|----------|-------------------|-------------|--------|---------------|
| [Mitigation 1] | Critical | [Name] | YYYY-MM-DD | Not Started | $[Amount] |
| [Mitigation 2] | High | [Name] | YYYY-MM-DD | In Progress | $[Amount] |
| [Mitigation 3] | Medium | [Name] | YYYY-MM-DD | Completed | $[Amount] |

### 6.2 Alternatives Considered

**Option 1: [Alternative Approach]**
- **Description:** [How this differs from current approach]
- **Privacy Benefits:** [How this reduces privacy risk]
- **Privacy Drawbacks:** [Any privacy concerns]
- **Cost/Feasibility:** [Implementation considerations]

**Option 2: [Alternative Approach]**
- **Description:**
- **Privacy Benefits:**
- **Privacy Drawbacks:**
- **Cost/Feasibility:**

**Selected Approach and Justification:**
[Explain which option was chosen and why, from a privacy perspective]

---

## 7. Stakeholder Consultation

### 7.1 Internal Stakeholders

| Stakeholder | Role | Consulted? | Date | Key Input/Concerns |
|-------------|------|------------|------|---------------------|
| Privacy Officer/DPO | Privacy oversight | Yes | YYYY-MM-DD | [Input provided] |
| Information Security | Security controls | Yes | YYYY-MM-DD | [Input provided] |
| Legal Counsel | Legal compliance | Yes | YYYY-MM-DD | [Input provided] |
| IT/Engineering | Technical implementation | Yes | YYYY-MM-DD | [Input provided] |
| Business Owner | Business requirements | Yes | YYYY-MM-DD | [Input provided] |

### 7.2 External Stakeholder Consultation (if applicable)

- [ ] **Customer/user feedback** sought on privacy practices
- [ ] **Privacy advocacy groups** consulted
- [ ] **Regulatory guidance** obtained
- [ ] **Industry associations** consulted

**Summary of External Input:**
[Summarize any external stakeholder feedback and how it was incorporated]

---

## 8. Conclusion and Recommendation

### 8.1 Overall Privacy Assessment

**Privacy Principles Compliance:**
- **Notice/Transparency:** Compliant | Issues Identified
- **Choice/Consent:** Compliant | Issues Identified
- **Access/Participation:** Compliant | Issues Identified
- **Data Minimization:** Compliant | Issues Identified
- **Use Limitation:** Compliant | Issues Identified
- **Data Quality:** Compliant | Issues Identified
- **Security:** Compliant | Issues Identified
- **Accountability:** Compliant | Issues Identified

**Summary:**
[1-2 paragraph summary of PIA findings, key risks, mitigations, and overall privacy posture]

### 8.2 Recommendation

**Decision:** ☐ Proceed | ☐ Proceed with Conditions | ☐ Do Not Proceed | ☐ Defer

**Justification:**
[Explain recommendation based on risk assessment, mitigation effectiveness, and legal compliance]

**Conditions for Proceeding (if applicable):**
1. [Condition 1 - must be implemented before/during deployment]
2. [Condition 2]
3. [Condition 3]

**Privacy Officer Signature:**

_______________________________
[Name], [Title]
Date: ______________

**Business Owner Acknowledgment:**

_______________________________
[Name], [Title]
Date: ______________

---

## 9. Monitoring and Review

### 9.1 Ongoing Monitoring

**Monitoring Activities:**
- [ ] Quarterly privacy risk review
- [ ] Annual PIA refresh
- [ ] Post-implementation privacy review
- [ ] Breach and incident tracking
- [ ] Consumer complaint monitoring
- [ ] Regulatory guidance monitoring

**Review Triggers:**
- [ ] Significant change in processing activities
- [ ] New technologies introduced
- [ ] Change in applicable laws or regulations
- [ ] Privacy incident or breach
- [ ] Consumer complaints
- [ ] Regulatory inquiry or investigation
- [ ] Annual scheduled review

### 9.2 PIA Register

**Recorded in Privacy Assessment Register:**
- [ ] Yes - Register ID: [ID]
- Assessment summary logged
- Risk level documented
- Review schedule established

**Next Scheduled Review:** [YYYY-MM-DD]

---

## Appendices

### Appendix A: Data Flow Diagram
[Diagram showing how personal information flows through systems]

### Appendix B: Privacy Notice
[Copy of or link to privacy notice]

### Appendix C: Consent Forms
[Copies of consent forms or mechanisms]

### Appendix D: Vendor Contracts/DPAs
[List of data processing agreements with third parties]

### Appendix E: Supporting Documentation
[Any additional relevant documents]

---

## References

### Regulatory Guidance
- **FTC Fair Information Practice Principles:** https://www.ftc.gov/reports/privacy-online-fair-information-practices-electronic-marketplace-federal-trade-commission
- **NIST Privacy Framework:** https://www.nist.gov/privacy-framework
- **ISO 29134 Privacy Impact Assessment:** https://www.iso.org/standard/62289.html
- **OECD Privacy Guidelines:** https://www.oecd.org/sti/ieconomy/privacy-guidelines.htm

### Internal References
- [Data Privacy Policy]
- [Information Security Policy]
- [Data Retention Schedule]
- [Incident Response Plan]
- [Records of Processing Activities]

---

**PIA Completion Date:** [YYYY-MM-DD]
**Document Control:** PIA-[PROJECT-NAME]-[VERSION]

---

*This Privacy Impact Assessment template follows Fair Information Practice Principles (FIPPs), NIST Privacy Framework, and ISO 29134 guidance. For GDPR compliance, use the Data Protection Impact Assessment (DPIA) template.*
