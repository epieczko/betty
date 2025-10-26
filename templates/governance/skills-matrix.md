# Skills Matrix

**Document Version**: 1.0.0
**Last Updated**: 2025-01-15
**Document Owner**: Engineering Leadership & People Team
**Classification**: Confidential

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | SKL-MTX-2025-Q1 |
| **Status** | Active |
| **Created Date** | 2025-01-15 |
| **Next Review** | 2025-04-15 (Quarterly) |
| **Primary Author** | Engineering Manager |
| **Approvers** | VP Engineering, Director of People Operations |
| **Assessment Period** | Q1 2025 |

## Executive Summary

This Skills Matrix provides a comprehensive assessment of individual and team competencies across technical skills, domain knowledge, and soft skills using the Dreyfus Model of Skill Acquisition (Novice → Competent → Proficient → Expert → Master). This artifact enables data-driven decisions on hiring priorities, training investments, team composition, and succession planning.

**Purpose**: Map organizational capabilities, identify skill gaps, guide talent development, and ensure business continuity through appropriate skill coverage and redundancy.

**Strategic Value**: Enables T-shaped skill development, reveals single points of failure, informs $2.5M annual L&D budget allocation, and supports strategic hiring prioritization for Q1-Q2 2025.

---

## 1. Proficiency Level Definitions (Dreyfus Model)

| Level | Definition | Behavioral Indicators | Typical Experience |
|-------|------------|----------------------|-------------------|
| **1 - Novice** | Learning fundamentals; requires supervision and step-by-step guidance | • Follows rules rigidly<br>• Limited situational judgment<br>• Needs explicit instructions<br>• Cannot troubleshoot independently | 0-6 months exposure |
| **2 - Competent** | Working knowledge; can complete tasks independently with occasional guidance | • Applies learned concepts<br>• Handles routine situations<br>• Seeks guidance for edge cases<br>• Growing pattern recognition | 6 months - 2 years |
| **3 - Proficient** | Deep understanding; handles complex scenarios; recognized as team resource | • Solves complex problems<br>• Mentors others<br>• Adapts to new situations<br>• Strong pattern recognition | 2-5 years |
| **4 - Expert** | Authority in domain; drives architecture/strategy; creates new approaches | • Defines best practices<br>• Leads major initiatives<br>• Innovates solutions<br>• Thought leader internally | 5-10 years |
| **5 - Master** | Industry-recognized authority; shapes organizational/industry standards | • Publishes research/talks<br>• Influences industry trends<br>• Creates frameworks/methodologies<br>• External thought leader | 10+ years |

**Self-Assessment Calibration**: Team members self-assess, then managers validate and calibrate across the team to ensure consistency and avoid grade inflation.

---

## 2. T-Shaped Skills Framework

### Model Definition

```
         Deep Expertise (I-shaped → T-shaped)
               |
               |  Master (5)
               |  Expert (4)
         Depth |  Proficient (3)
               |  Competent (2)
               |  Novice (1)
               |
─────────────────────────────────────────────
   Skill A  Skill B  Skill C  Skill D  Skill E

         Breadth (Working Knowledge)
```

**Target Profile by Level**:
- **Junior Engineer**: I-shaped (deep in 1 skill, developing breadth)
- **Mid Engineer**: T-shaped (expert in 1, competent in 2-3)
- **Senior Engineer**: T-shaped (expert in 1-2, proficient in 3-4)
- **Staff+ Engineer**: Pi-shaped (expert in 2+, proficient in 5+)

---

## 3. Engineering Team Skills Matrix (Example)

### Team: Platform Engineering (8 members)

#### Technical Skills Assessment

| Team Member | Backend (Go/Java) | Frontend (React) | Cloud (AWS/K8s) | Databases (SQL/NoSQL) | Observability | Security | CI/CD | Architecture | Status |
|-------------|------------------|------------------|-----------------|----------------------|---------------|----------|-------|--------------|--------|
| **Alice Chen** (Staff) | 5 (Master) | 2 | 4 (Expert) | 4 | 4 | 3 | 4 | 5 | 🟢 T-shaped |
| **Bob Martinez** (Senior) | 4 (Expert) | 1 | 3 | 3 | 3 | 3 | 4 | 3 | 🟢 T-shaped |
| **Carol Wu** (Senior) | 3 | 4 (Expert) | 3 | 3 | 3 | 2 | 3 | 3 | 🟢 T-shaped |
| **David Kim** (Mid) | 3 | 2 | 3 (Proficient) | 2 | 3 | 2 | 3 | 2 | 🟡 I → T transition |
| **Emma Johnson** (Mid) | 2 | 3 (Proficient) | 2 | 2 | 2 | 3 | 2 | 2 | 🟡 I → T transition |
| **Frank Lee** (Mid) | 3 | 1 | 2 | 4 (Expert) | 2 | 2 | 2 | 2 | 🟡 I-shaped |
| **Grace Park** (Junior) | 2 | 2 | 2 | 2 (Competent) | 1 | 1 | 2 | 1 | 🟡 Developing |
| **Henry Zhang** (Junior) | 2 (Competent) | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 🟡 Developing |

**Legend**:
- 🟢 **T-shaped**: Expert (4+) in 1+ area, Proficient (3+) in 2+ areas
- 🟡 **I-shaped / Developing**: Expert in 1 area, limited breadth
- 🔴 **Gap**: No expert coverage in critical skill

#### Skill Coverage Heatmap

| Skill Domain | Novice (1) | Competent (2) | Proficient (3) | Expert (4) | Master (5) | **Gap Risk** |
|-------------|-----------|--------------|---------------|-----------|-----------|--------------|
| **Backend Development** | 0 | 3 | 3 | 1 | 1 | 🟢 Strong |
| **Frontend Development** | 2 | 3 | 1 | 1 | 0 | 🟡 Moderate |
| **Cloud Infrastructure** | 0 | 3 | 3 | 1 | 0 | 🟢 Strong |
| **Databases** | 1 | 3 | 2 | 2 | 0 | 🟢 Strong |
| **Observability** | 1 | 3 | 4 | 0 | 0 | 🟡 No Expert |
| **Security** | 2 | 4 | 2 | 0 | 0 | 🔴 **Critical Gap** |
| **CI/CD Pipelines** | 1 | 3 | 2 | 2 | 0 | 🟢 Strong |
| **Architecture** | 3 | 3 | 1 | 0 | 1 | 🟡 Moderate |

**Analysis**:
- **Strengths**: Backend development (Alice master-level), Cloud infrastructure (strong depth)
- **Moderate Gaps**: Observability (no expert), Architecture (single expert - succession risk)
- **Critical Gap**: Security (no expert-level capability) → Priority hire or training
- **Bus Factor Risk**: Alice is single Master-level engineer → succession planning needed

---

## 4. Domain Knowledge & Business Skills

### Team: Product Engineering

| Team Member | E-Commerce Domain | Payment Processing | Inventory Mgmt | Marketing Tech | Customer Data | Analytics | Status |
|-------------|------------------|-------------------|---------------|---------------|--------------|----------|--------|
| **Sarah Johnson** (PM) | 4 | 3 | 4 | 3 | 3 | 2 | 🟢 Domain Expert |
| **Mike Davis** (Eng Lead) | 3 | 4 | 2 | 2 | 3 | 3 | 🟢 T-shaped |
| **Lisa Wang** (Senior Eng) | 3 | 2 | 3 | 2 | 2 | 2 | 🟢 Balanced |
| **Tom Brown** (Mid Eng) | 2 | 1 | 2 | 1 | 2 | 2 | 🟡 Developing |
| **Nina Patel** (Junior Eng) | 1 | 1 | 1 | 1 | 1 | 1 | 🟡 Ramping |

**Domain Expertise Assessment**:
- **Payment Processing**: Mike (Expert) - single point of expertise
- **Inventory Management**: Sarah (Expert) - knowledge transfer to Lisa in progress
- **Overall**: Strong domain coverage in e-commerce, growing expertise in newer members

---

## 5. Soft Skills & Leadership Capabilities

### Team: Engineering Leadership

| Team Member | Communication | Mentoring | Stakeholder Mgmt | Conflict Resolution | Strategic Thinking | Team Building | Influence | Status |
|-------------|--------------|-----------|------------------|--------------------|--------------------|---------------|-----------|--------|
| **VP Engineering** | 5 | 4 | 5 | 4 | 5 | 4 | 5 | 🟢 Executive |
| **Director - Platform** | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 🟢 Leader |
| **Director - Product Eng** | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 🟢 Leader |
| **Staff Eng (Alice)** | 3 | 4 | 3 | 3 | 4 | 2 | 3 | 🟢 Tech Lead |
| **Staff Eng (Mike)** | 4 | 3 | 3 | 3 | 3 | 3 | 3 | 🟢 Tech Lead |
| **Senior Eng (Bob)** | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 🟡 Developing |
| **Senior Eng (Carol)** | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 🟡 Developing |

**Leadership Development**:
- Alice and Mike are ready for Director-level roles (4+ in most leadership competencies)
- Bob and Carol need mentoring development before promotion to Staff (target: 6-12 months)
- Succession pipeline: 2 Staff engineers ready for Director promotion within 12 months

---

## 6. Skill Gap Analysis & Hiring Priorities

### Critical Skill Gaps (Q1 2025)

| Skill Gap | Current Coverage | Minimum Need | Gap | Impact | Priority | Action Plan |
|-----------|-----------------|--------------|-----|--------|----------|-------------|
| **Security Engineering** | 0 Experts, 2 Proficient | 2 Experts | -2 | High (compliance risk) | P0 | **Hire:** Senior Security Eng (Q1) |
| **Observability** | 0 Experts, 4 Proficient | 1 Expert | -1 | Medium | P1 | **Train:** Send Bob to Observability Summit |
| **Frontend (React)** | 1 Expert, 1 Proficient | 2 Experts | -1 | Medium | P2 | **Hire:** Senior Frontend Eng (Q2) |
| **Machine Learning** | 0 capability | 1 Proficient | -1 | Medium (roadmap) | P2 | **Hire:** ML Engineer (Q2) |
| **iOS Development** | 0 capability | 2 Proficient | -2 | High (mobile roadmap) | P0 | **Hire:** 2 iOS Engineers (Q1) |

**Total Headcount Needs**: 5 hires in Q1-Q2
**Budget Impact**: $750K (fully loaded, annual)

### Succession Risk Analysis (Bus Factor)

| Critical Knowledge Area | Single Point of Expertise | Risk Level | Mitigation Plan |
|------------------------|---------------------------|------------|-----------------|
| **Backend Architecture** | Alice Chen (Master) | 🔴 High | Cross-train Bob (6mo plan), document architecture decisions |
| **AWS Infrastructure** | Alice Chen (Expert) | 🟡 Medium | Bob at Proficient, assign co-ownership of infra projects |
| **Payment Integration** | Mike Davis (Expert) | 🟡 Medium | Lisa shadowing, planned knowledge transfer sessions |
| **Database Performance** | Frank Lee (Expert) | 🟡 Medium | Share on-call rotation with David, document tuning procedures |

**Recommendation**: Implement knowledge sharing sessions (2hrs/week) and pair programming for high-risk areas.

---

## 7. Training & Development Plan (Q1-Q2 2025)

### Planned Investments

| Initiative | Target Audience | Skill Gap Addressed | Format | Cost | Expected Outcome |
|-----------|----------------|---------------------|--------|------|------------------|
| **AWS Solutions Architect Certification** | Bob, David, Emma | Cloud Infrastructure | Self-paced + exam | $4,500 | 3 AWS certified engineers |
| **Security Champions Program** | All engineers | Security fundamentals | Internal training | $15K | Every team has security advocate |
| **React Advanced Patterns Workshop** | Carol, Emma, Grace | Frontend depth | 2-day workshop | $8K | Improve React expertise |
| **Observability Summit 2025** | Bob, David | Observability expert development | Conference | $6K | Bob → Expert level |
| **Leadership Coaching** | Alice, Mike | Executive presence | 1:1 coaching (6mo) | $24K | Prepare for Director roles |
| **Internal Mentorship Program** | Juniors + Seniors | Accelerated growth | Structured pairing | $0 | Faster junior → mid progression |

**Total L&D Budget (Q1-Q2)**: $57,500
**ROI**: Projected 30% faster skill development vs. self-directed learning

### Individual Development Plans (IDPs)

**Example: David Kim (Mid-Level Engineer)**

| Current State | Target State (6 months) | Development Activities | Success Metrics |
|--------------|------------------------|----------------------|-----------------|
| Cloud (3 - Proficient) | Cloud (4 - Expert) | • AWS SA Certification<br>• Lead infrastructure migration project<br>• Pair with Alice on architecture | • Certification obtained<br>• Independently design AWS architecture<br>• Mentor junior on cloud |
| Architecture (2 - Competent) | Architecture (3 - Proficient) | • Attend architecture reviews<br>• Read "Building Microservices"<br>• Design 2 major features end-to-end | • Present architecture proposals<br>• Receive positive peer review<br>• Document 2 architecture decisions |
| Leadership (1 - Novice) | Leadership (2 - Competent) | • Lead sprint planning<br>• Mentor Grace (Junior)<br>• Present tech talks internally | • Successfully run 3 sprint plans<br>• Grace shows measurable progress<br>• Deliver 2 tech talks |

**Manager Assessment**: On track for Senior promotion in 9-12 months if targets achieved.

---

## 8. Team Composition Analysis

### Platform Engineering Team - Skill Balance

**Current State**:
```
Seniority Distribution:
  Staff:   1 (12.5%)  ████
  Senior:  2 (25%)    ████████
  Mid:     3 (37.5%)  ████████████
  Junior:  2 (25%)    ████████

T-shaped Profile:
  T-shaped:      3 (37.5%)
  I → T:         3 (37.5%)
  I-shaped:      2 (25%)
```

**Target State** (Healthy distribution):
```
Seniority Distribution:
  Staff:   2 (20%)    ████████
  Senior:  3 (30%)    ████████████
  Mid:     4 (40%)    ████████████████
  Junior:  1 (10%)    ████

T-shaped Profile:
  T-shaped:      7 (70%)
  Developing:    3 (30%)
```

**Recommendations**:
1. Promote Alice to Director within 6 months (succession planning)
2. Hire 1 Staff+ engineer externally for immediate expertise infusion
3. Promote Bob and David to Senior (conditional on development plan completion)
4. Reduce junior hiring; focus on mid-senior for faster impact

---

## 9. Certification & Credential Tracking

### Current Certifications

| Team Member | Certifications | Expiration | Renewal Required |
|------------|---------------|-----------|------------------|
| Alice Chen | • AWS Solutions Architect Professional<br>• Kubernetes CKA<br>• TOGAF 9 | 2025-08, 2025-11, Lifetime | Renew AWS by Q3 |
| Bob Martinez | • AWS Developer Associate | 2026-03 | None |
| Carol Wu | • Google Professional Cloud Architect | 2025-06 | Renew by Q2 |
| Mike Davis | • PCI-DSS QSA<br>• CISSP | 2026-01, 2027-05 | None |

### Certification ROI Analysis

| Certification | Cost | Time Investment | Business Value | Priority |
|--------------|------|----------------|----------------|----------|
| AWS Solutions Architect (Associate) | $150 | 40 hours | High (cloud strategy) | Recommended for all senior+ |
| Kubernetes CKA | $395 | 60 hours | High (infrastructure) | Recommended for platform team |
| React Developer Certification | $200 | 30 hours | Medium | Optional for frontend specialists |
| Security+ / CISSP | $400-700 | 80-120 hours | High (compliance) | Required for security team |

---

## 10. Skill Development Velocity Tracking

### Quarterly Skill Progression (Q4 2024 → Q1 2025)

| Team Member | Skill Improved | Q4 Level | Q1 Level | Change | Notes |
|------------|---------------|---------|---------|--------|-------|
| David Kim | Cloud Infrastructure | 2 | 3 | ↑ +1 | Led AWS migration, earned certification |
| Emma Johnson | Frontend (React) | 2 | 3 | ↑ +1 | Completed advanced React course, shipped major feature |
| Grace Park | Backend (Go) | 1 | 2 | ↑ +1 | Completed onboarding bootcamp, solo contributions |
| Henry Zhang | CI/CD | 1 | 1 | → 0 | Needs focused development plan |

**Team Skill Development Velocity**: 3.5 skills improved per quarter (average)
**Target**: 5 skills per quarter with structured IDP process

---

## 11. Cross-Team Skills Matrix (Organization-Wide)

### Engineering Organization (40 engineers across 5 teams)

| Skill Domain | # Experts (4+) | # Proficient (3) | # Competent (2) | # Novice (1) | Org Coverage |
|-------------|---------------|-----------------|----------------|-------------|--------------|
| Backend Development | 8 | 15 | 12 | 5 | 🟢 Strong (57% at 3+) |
| Frontend Development | 5 | 10 | 18 | 7 | 🟡 Moderate (37% at 3+) |
| Mobile (iOS/Android) | 0 | 2 | 3 | 0 | 🔴 **Critical Gap** |
| DevOps/SRE | 6 | 12 | 15 | 7 | 🟢 Strong (45% at 3+) |
| Data Engineering | 3 | 8 | 10 | 5 | 🟡 Moderate (42% at 3+) |
| Security Engineering | 1 | 4 | 8 | 10 | 🔴 **Critical Gap** |
| Machine Learning | 0 | 1 | 2 | 0 | 🔴 **Critical Gap** |

**Organization-Level Priorities**:
1. **Immediate**: Hire 3 mobile engineers (iOS & Android)
2. **High**: Hire 2 security engineers, establish security champions program
3. **Medium**: Hire 1 ML engineer, build ML capability from ground up
4. **Low**: Continue growing frontend depth organically

---

## 12. Skills Matrix Maintenance & Governance

### Update Cadence

| Activity | Frequency | Owner | Process |
|---------|-----------|-------|---------|
| Individual self-assessment | Quarterly | Each engineer | Use standardized assessment form |
| Manager validation & calibration | Quarterly | Engineering managers | 1:1 review + team calibration meeting |
| Team-level aggregation | Quarterly | Engineering manager | Roll up to team heatmap |
| Org-level reporting | Quarterly | VP Engineering | Report to executive team & board |
| Skill gap analysis & hiring plan | Semi-annually | VP Eng + People Ops | Align with annual planning cycle |
| Individual development plan review | Quarterly | Manager + Individual | Progress tracking against IDP goals |

### Data Privacy & Access Controls

| Data View | Access Level | Purpose |
|----------|-------------|---------|
| **Individual Detailed Assessments** | Self + Manager only | Performance discussions, career development |
| **Team Aggregated Heatmaps** | Team + Leadership | Team composition, skill gap identification |
| **Organization Summary Stats** | Leadership + HR | Strategic workforce planning, hiring priorities |
| **De-identified Trends** | All employees | Transparency on org capability maturity |

**Privacy Policy**: Individual skill data is confidential. Only aggregated, anonymized data shared beyond manager level.

---

## 13. Related Artifacts

| Artifact Type | Relationship | Location |
|--------------|--------------|----------|
| **Individual Development Plans (IDPs)** | Contains personalized skill growth targets | HR System / Lattice |
| **Team Topology Map** | Defines team structure and mission alignment | `/architecture/team-topology-map.md` |
| **Hiring Plan** | Prioritizes recruitment based on skill gaps | `/governance/staffing-plan.md` |
| **Training Budget** | Allocates L&D spend by skill development priority | `/governance/resource-plan.md` |
| **Performance Reviews** | Incorporates skill progression as evaluation criteria | HR System |
| **Succession Planning** | Identifies high-potential talent and leadership pipeline | `/governance/succession-plan.md` |

---

## 14. Change History

| Version | Date | Author | Changes | Assessment Period |
|---------|------|--------|---------|-------------------|
| 1.0.0 | 2025-01-15 | Engineering Manager | Q1 2025 assessment | Q1 2025 |
| 0.9.0 | 2024-10-15 | Engineering Manager | Q4 2024 assessment | Q4 2024 |
| 0.8.0 | 2024-07-15 | Engineering Manager | Q3 2024 assessment | Q3 2024 |

---

## Appendix A: Skill Assessment Self-Service Form

### Technical Skills Self-Assessment Template

**Name**: ___________________ **Date**: ___________
**Team**: ___________________ **Role**: ___________

For each skill, rate yourself using the Dreyfus Model (1-5):

| Skill | Level (1-5) | Evidence / Justification |
|-------|------------|-------------------------|
| [Skill 1] | ___ | ________________________________ |
| [Skill 2] | ___ | ________________________________ |
| [Skill 3] | ___ | ________________________________ |

**Dreyfus Reference**:
- **1 (Novice)**: Learning basics, need step-by-step guidance
- **2 (Competent)**: Work independently on routine tasks
- **3 (Proficient)**: Handle complex scenarios, mentor others
- **4 (Expert)**: Drive strategy, recognized authority
- **5 (Master)**: Industry thought leader, published work

**Development Goals** (next 6 months):
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

---

## Appendix B: Manager Calibration Guidelines

### Calibration Meeting Agenda

1. **Review Self-Assessments** (30 min)
   - Identify discrepancies between self-ratings and manager observation
   - Discuss evidence for each rating

2. **Cross-Team Calibration** (45 min)
   - Compare ratings across teams for consistency
   - Align on what "Expert" vs "Proficient" means for each skill
   - Adjust ratings to ensure fairness

3. **Gap Analysis** (30 min)
   - Identify team-level skill gaps
   - Prioritize hiring and training needs

4. **Succession Planning** (15 min)
   - Identify high-potential individuals
   - Flag single points of failure

**Calibration Principles**:
- **Evidence-Based**: Require concrete examples for 4+ ratings
- **Avoid Inflation**: "Expert" should be rare (top 10-15% of team)
- **Growth Mindset**: Focus on development trajectory, not just current state
- **Fairness**: Apply same standards across all team members

---

**Document Approval**:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| VP Engineering | [Name] | _____________ | ______ |
| Director of People Operations | [Name] | _____________ | ______ |

---

*This Skills Matrix follows Dreyfus Model competency framework and T-shaped skills development principles. Data confidentiality governed by organizational privacy policy. For questions, contact Engineering Leadership.*
