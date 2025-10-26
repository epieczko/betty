# Business Process Models

**Document Version**: 1.0.0
**Last Updated**: 2025-01-15
**Document Owner**: Business Process Excellence Team
**Classification**: Internal

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | BPM-2025-001 |
| **Status** | Draft |
| **Created Date** | 2025-01-15 |
| **Next Review** | 2025-04-15 |
| **Primary Author** | [Process Analyst Name] |
| **Approvers** | Process Owner, Operations Director |

## Executive Summary

This document provides comprehensive visual and structured documentation of business processes using BPMN 2.0 (Business Process Model and Notation) standard, swimlane diagrams, value stream maps, and SIPOC analysis. These models enable process optimization through Lean Six Sigma methodologies, process mining, and workflow automation while supporting regulatory compliance (SOX, ISO 9001, ISO 27001).

**Purpose**: Document current-state (As-Is) and future-state (To-Be) business processes to identify inefficiencies, bottlenecks, and automation opportunities.

**Strategic Value**: Standardizes processes across the organization, reduces cycle time by 20-40%, improves quality through error reduction, and provides foundation for RPA and BPM system implementation.

---

## 1. Process Overview

### Process Hierarchy

```
Level 0: Enterprise Process Map
  └─ Level 1: Core Process Groups
      └─ Level 2: Detailed Process Flows
          └─ Level 3: Procedure-Level Activities
```

### Process Metadata

| Attribute | Details |
|-----------|---------|
| **Process Name** | [e.g., Order-to-Cash, Procure-to-Pay, Hire-to-Retire] |
| **Process ID** | [Unique identifier, e.g., P-FIN-001] |
| **Process Owner** | [Role and department] |
| **Process Type** | Core Business | Support | Management |
| **Scope** | [Boundaries: start event to end event] |
| **Frequency** | Continuous | Daily | Weekly | Monthly | Quarterly |
| **Volume** | [Number of process instances per period] |
| **Systems Involved** | [List of applications and platforms] |

---

## 2. BPMN 2.0 Process Diagrams

### BPMN Notation Legend

**Events**:
- ○ **Start Event**: Process initiation
- ◎ **Intermediate Event**: Event during process flow
- ⊗ **End Event**: Process completion
- ⌚ **Timer Event**: Time-based trigger
- ✉ **Message Event**: Message receipt or send

**Activities**:
- ▭ **Task**: Single unit of work
- ⊟ **Subprocess**: Collapsed process detail
- ⊕ **Call Activity**: Reusable subprocess reference

**Gateways** (Decision Points):
- ◇ **Exclusive Gateway (XOR)**: One path chosen
- ⬥ **Parallel Gateway (AND)**: All paths executed
- ⬦ **Inclusive Gateway (OR)**: One or more paths

**Flows**:
- → **Sequence Flow**: Process order
- ⇢ **Message Flow**: Communication between participants
- ⋯→ **Association**: Data or artifact linkage

### Example 1: Order-to-Cash Process (L2)

```
[Customer Order Request] ○──→ [Validate Customer Credit] ──→ ◇
                                                               ├─(Approved)──→ [Create Sales Order]
                                                               │
                                                               └─(Rejected)──→ [Notify Sales Team] ──→ ⊗

[Create Sales Order] ──→ [Check Inventory] ──→ ◇
                                                 ├─(In Stock)──→ [Reserve Inventory]
                                                 │
                                                 └─(Out of Stock)──→ [Create Backorder] ──→ ⌚ (Wait for Stock)

[Reserve Inventory] ──→ [Pick & Pack Order] ──→ [Generate Invoice] ──→ [Ship Order] ──→ ✉ (Shipping Notification)

[Ship Order] ──→ [Update Order Status] ──→ ◇
                                             ├─→ [Collect Payment] ──→ [Apply Payment to AR]
                                             │
                                             └─→ ⌚ (Payment Due Reminder)

[Apply Payment to AR] ──→ [Close Order] ──→ ⊗ (Order Complete)
```

**Process Metrics**:
- **Cycle Time**: 5.2 days (average from order to delivery)
- **Touch Time**: 4.8 hours (actual work time)
- **Wait Time**: 4.7 days (queuing, approvals, handoffs)
- **Throughput**: 850 orders/week
- **Error Rate**: 3.2% (orders requiring correction)
- **Cost per Transaction**: $47.50

---

## 3. Swimlane Diagrams (Cross-Functional Workflows)

### Example 2: Employee Onboarding Process

**Participants**: HR, IT, Facilities, Manager, New Hire

| Participant | Activities |
|-------------|------------|
| **HR** | ![Start] Receive Signed Offer → Create Employee Record → Schedule Orientation → Conduct Benefits Enrollment → ![End] Close Onboarding Case |
| **Manager** | Assign Buddy → Prepare Workspace Plan → Conduct First Day Welcome → Set 30-60-90 Day Goals |
| **IT** | Provision User Account → Configure Email → Assign Hardware → Install Software → Grant System Access |
| **Facilities** | Assign Desk/Office → Provide Building Access Badge → Setup Phone Extension |
| **New Hire** | Complete I-9 Forms → Attend Orientation → Review Policies → Complete Compliance Training → Meet Team |

**Cross-Functional Handoffs** (Pain Points):
1. HR → IT: Employee data transfer (24-hour delay)
2. IT → Facilities: Badge activation coordination (12-hour delay)
3. Manager → New Hire: Equipment delivery timing (variable)

**Process Improvements Identified**:
- Integrate HRIS with IT provisioning system (reduce delay from 24hrs to 2hrs)
- Automate badge creation from employee record (eliminate 12-hour delay)
- Pre-stage equipment based on start date (improve Day 1 readiness)

**Metrics**:
- **Current Cycle Time**: 8.5 days (offer acceptance to full productivity)
- **Target Cycle Time**: 5 days (37% reduction)
- **Employee Satisfaction**: 7.2/10 (onboarding experience)

---

## 4. Value Stream Map (VSM)

### Example 3: Incident Management Process (As-Is)

```
┌─────────────┐    ┌──────────────┐    ┌──────────────┐    ┌─────────────┐    ┌──────────────┐
│   Customer  │ →  │  L1 Support  │ →  │  L2 Support  │ →  │ Engineering │ →  │  Resolution  │
│   Reports   │    │   Triage     │    │  Diagnosis   │    │     Fix     │    │   Deploy     │
│   Incident  │    │              │    │              │    │             │    │              │
└─────────────┘    └──────────────┘    └──────────────┘    └─────────────┘    └──────────────┘
                          ↓                   ↓                   ↓                   ↓
Process Time:            8 min              45 min             180 min             30 min
Wait Time:               15 min             120 min            480 min             60 min
% C&A (First Time):      100%               65%                40%                 85%
```

**Value Stream Metrics**:

| Stage | Process Time | Wait Time | Lead Time | % Complete & Accurate |
|-------|--------------|-----------|-----------|----------------------|
| Customer Report | 8 min | 15 min | 23 min | 100% |
| L1 Triage | 45 min | 120 min | 165 min | 65% (35% escalated) |
| L2 Diagnosis | 180 min | 480 min | 660 min | 40% (60% escalated) |
| Engineering Fix | 180 min | 60 min | 240 min | 85% |
| Deploy Resolution | 30 min | 0 min | 30 min | 100% |
| **TOTALS** | **443 min (7.4 hrs)** | **675 min (11.3 hrs)** | **1,118 min (18.6 hrs)** | **Process Efficiency: 39.6%** |

**7 Wastes Identified** (Lean Analysis):
1. **Waiting**: 11.3 hours of queue time between stages
2. **Defects**: 35% of L1 triage requires rework/escalation
3. **Overprocessing**: Manual data entry across 4 different systems
4. **Transportation**: Incident ticket handed off 4 times
5. **Motion**: Engineers searching for incident context in multiple tools
6. **Inventory**: 120 incidents queued in L2 backlog at any time
7. **Underutilized Talent**: L2 engineers spending 40% time on L1-level issues

**To-Be Improvements**:
- Implement AI-powered triage to improve L1 accuracy from 65% to 85%
- Integrate incident management platform with monitoring tools (eliminate 60 min wait)
- Create automated runbooks for top 20 incident types (reduce engineering time by 50%)
- **Target Lead Time**: 6.5 hours (65% reduction)
- **Target Process Efficiency**: 75%

---

## 5. SIPOC Analysis

### Example: IT Service Request Fulfillment

| SIPOC Element | Details |
|---------------|---------|
| **Suppliers** | • Employees (requestors)<br>• Service Catalog (request definitions)<br>• Vendor Partners (software licenses, hardware)<br>• IT Asset Management (inventory) |
| **Inputs** | • Service Request Form<br>• User Information (name, department, manager approval)<br>• Request Type (software, hardware, access, other)<br>• Business Justification<br>• Priority Level (P1-P4) |
| **Process** | 1. **Submit Request** → Employee submits via service portal<br>2. **Auto-Route** → Workflow assigns to appropriate IT team<br>3. **Manager Approval** → Manager approves/rejects via email<br>4. **Fulfillment** → IT team provisions resource<br>5. **Verification** → Requester confirms completion<br>6. **Close** → Ticket closed and satisfaction survey sent |
| **Outputs** | • Provisioned Software/Hardware/Access<br>• Updated CMDB records<br>• Asset assignment in inventory<br>• Service metrics (completion time, satisfaction)<br>• License consumption data |
| **Customers** | • Employees (end users)<br>• Managers (approval and visibility)<br>• Finance (budget tracking)<br>• Compliance (audit trail) |

**Process Boundaries**:
- **Start**: Employee submits service request in portal
- **End**: Request fulfilled and ticket closed

**Process Metrics**:
- **Volume**: 1,200 requests/month
- **SLA**: 90% resolved within 2 business days
- **Current Performance**: 78% on-time resolution
- **Customer Satisfaction**: 4.1/5.0

---

## 6. Process Performance Metrics

### Key Performance Indicators (KPIs)

| Metric Category | KPI | Current | Target | Status |
|-----------------|-----|---------|--------|--------|
| **Efficiency** | Cycle Time | 5.2 days | 3.5 days | 🔴 Behind |
| **Efficiency** | Process Cost | $47.50/transaction | $35/transaction | 🔴 Behind |
| **Efficiency** | Automation Rate | 32% | 60% | 🟡 In Progress |
| **Quality** | Error Rate | 3.2% | <1.5% | 🔴 Behind |
| **Quality** | First-Time-Right | 82% | 95% | 🟡 In Progress |
| **Quality** | Rework Rate | 12% | <5% | 🔴 Behind |
| **Throughput** | Volume Processed | 850/week | 1,200/week | 🔴 Behind |
| **Throughput** | Capacity Utilization | 71% | 85% | 🟡 In Progress |
| **Customer** | CSAT Score | 7.2/10 | 8.5/10 | 🟡 In Progress |
| **Customer** | NPS | +15 | +40 | 🔴 Behind |

**Performance Trends**:
- Cycle time increased 15% year-over-year due to volume growth
- Automation initiatives expected to improve efficiency by 35% in next quarter
- Quality improvements from Six Sigma project showing early positive results

---

## 7. Process Improvement Opportunities

### Bottleneck Analysis

| Bottleneck | Impact | Root Cause | Recommended Action | Expected Benefit |
|------------|--------|------------|-------------------|------------------|
| Credit approval queue | 1.5 day delay | Manual review by single approver | Implement tiered approval thresholds + auto-approval rules | -60% approval time |
| Inventory check | 45 min | Batch processing (hourly) | Real-time inventory integration via API | -95% wait time |
| Invoice generation | Manual errors | Rekeying data from order system | Direct system integration | -80% errors |
| Payment application | 2-day delay | Batch import from bank (daily) | Real-time payment posting | -75% payment cycle |

### Automation Candidates (RPA Assessment)

| Process Step | Automation Potential | Complexity | ROI | Priority |
|-------------|---------------------|-----------|-----|----------|
| Data entry from PDFs | High (95% suitable) | Medium | $125K/year savings | P0 |
| Invoice generation | High (100% suitable) | Low | $85K/year savings | P0 |
| Credit score lookup | High (100% suitable) | Low | $45K/year savings | P1 |
| Shipping label creation | High (98% suitable) | Low | $32K/year savings | P1 |
| Payment reminder emails | High (100% suitable) | Low | $18K/year savings | P2 |

---

## 8. Process Documentation Standards

### BPMN 2.0 Modeling Guidelines

1. **Naming Conventions**:
   - Tasks: Verb + Noun (e.g., "Validate Credit Score", "Generate Invoice")
   - Gateways: Question format (e.g., "Credit Approved?", "In Stock?")
   - Events: Noun + past tense (e.g., "Order Received", "Payment Confirmed")

2. **Complexity Limits**:
   - Level 2 diagrams: Maximum 25 elements
   - Level 3 diagrams: Maximum 15 elements
   - Subprocesses for complex sections

3. **Exception Handling**:
   - Document error paths and exception flows
   - Include escalation procedures
   - Show compensation activities for rollback scenarios

4. **Tool Standards**:
   - Lucidchart (preferred): Shared team workspace
   - Bizagi Modeler: For process simulation
   - BPMN.io: For lightweight web-based modeling

### Process Documentation Checklist

- [ ] Process name follows naming convention (VERB-NOUN format)
- [ ] Process owner identified and documented
- [ ] BPMN 2.0 notation used correctly and consistently
- [ ] Swimlanes clearly labeled with role/system names
- [ ] All decision points have defined criteria
- [ ] Exception and error paths documented
- [ ] Integration points with systems identified
- [ ] Process metrics (cycle time, cost, volume) documented
- [ ] As-Is process validated by process performers
- [ ] To-Be process approved by process owner
- [ ] Gap analysis completed (As-Is vs To-Be)
- [ ] Implementation roadmap defined
- [ ] Change impact assessment completed

---

## 9. Related Artifacts

| Artifact Type | Relationship | Location |
|--------------|--------------|----------|
| **Business Rules Catalog** | Defines decision logic referenced in gateways | `/governance/business-rules-catalog.md` |
| **System Requirements** | Technical implementation of process automation | `/requirements/system-requirements-specification.yaml` |
| **RACI Matrix** | Defines roles and responsibilities per process step | `/governance/raci-per-workstream.md` |
| **Runbooks** | Operational procedures for executing process steps | `/operations/runbooks.yaml` |
| **SOX Controls** | Control points mapped to process steps | `/compliance/soc-2-control-implementation-matrix.yaml` |

---

## 10. Compliance & Governance

### SOX Controls Mapping

| Process Step | SOX Control | Control Type | Testing Frequency |
|-------------|------------|--------------|-------------------|
| Credit Approval | Segregation of duties | Preventive | Quarterly |
| Inventory Reserve | Authorization limits | Detective | Monthly |
| Invoice Generation | System-generated (no manual override) | Preventive | Automated |
| Payment Application | Dual authorization for >$50K | Preventive | Per transaction |
| AR Reconciliation | Monthly review and sign-off | Detective | Monthly |

### ISO 9001 Quality Management

- Process capability analysis (Cp, Cpk) performed quarterly
- Control charts monitored for special cause variation
- Continuous improvement initiatives tracked via DMAIC methodology
- Process audits conducted semi-annually

---

## 11. Change History

| Version | Date | Author | Changes | Approver |
|---------|------|--------|---------|----------|
| 1.0.0 | 2025-01-15 | Process Analyst | Initial As-Is documentation | Process Owner |
| 1.1.0 | TBD | Process Analyst | To-Be process design | Operations Director |
| 2.0.0 | TBD | Process Analyst | Post-automation update | Process Owner |

---

## Appendix A: Process Notation Reference

### BPMN 2.0 Quick Reference

| Symbol | Name | Usage |
|--------|------|-------|
| ○ | Start Event | Beginning of process |
| ⊗ | End Event | Process completion |
| ▭ | Task | Single unit of work |
| ⊟ | Subprocess | Collapsible detail |
| ◇ | Exclusive Gateway (XOR) | One path of many |
| ⬥ | Parallel Gateway (AND) | All paths simultaneously |
| ⬦ | Inclusive Gateway (OR) | One or more paths |
| ✉ | Message Event | Send/receive message |
| ⌚ | Timer Event | Time-based trigger |
| ⚠ | Error Event | Exception handling |

### Swimlane Roles Definition

| Role/System | Responsibilities | Access Level |
|------------|------------------|--------------|
| Customer Service | Order intake, customer communication | Read/Write orders |
| Finance | Credit approval, AR management | Read/Write financial data |
| Warehouse | Inventory management, fulfillment | Read/Write inventory |
| Shipping | Logistics, tracking | Read orders, Write shipping data |
| ERP System | Order processing automation | System integration |

---

**Document Approval**:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Process Owner | [Name] | _____________ | ______ |
| Operations Director | [Name] | _____________ | ______ |
| Quality Manager | [Name] | _____________ | ______ |

---

*This document follows BPMN 2.0 OMG standards and Lean Six Sigma best practices. For questions, contact the Business Process Excellence team.*
