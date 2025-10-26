# Escalation Matrix

**Document Version**: 1.0.0
**Last Updated**: 2025-01-15
**Document Owner**: SRE Leadership & Operations
**Classification**: Internal

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ESC-MTX-2025-001 |
| **Status** | Active |
| **Created Date** | 2025-01-15 |
| **Next Review** | 2025-02-15 (Monthly) |
| **Primary Author** | SRE Manager |
| **Approvers** | VP Engineering, Director of Operations |
| **Effective Date** | 2025-01-15 |

## Executive Summary

This Escalation Matrix defines support tier responsibilities (L1/L2/L3), escalation paths, contact information, and SLA response times for incident management. Aligned with ITIL 4 and Google SRE practices, this matrix ensures rapid, appropriate escalation of production incidents to minimize MTTR (Mean Time To Resolution) and customer impact.

**Purpose**: Provide authoritative reference for incident escalation paths, eliminating confusion about who to contact for specific incident types or severity levels.

**Strategic Value**: Reduces incident resolution time by 50-70% through predefined escalation paths, ensures SLA compliance, maintains 24/7 coverage through follow-the-sun support model.

---

## 1. Support Tier Definitions

| Tier | Responsibility | Skill Level | Escalation Trigger | Response Time Target |
|------|---------------|-------------|-------------------|----------------------|
| **L1 (First Responder)** | • Triage and initial assessment<br>• Basic troubleshooting (restart, clear cache)<br>• Gather incident context<br>• Follow runbooks/playbooks<br>• Escalate complex issues | Generalist, working knowledge | Unable to resolve in 30 min (P0) or 2 hrs (P1-P2) | P0: 5 min<br>P1: 15 min<br>P2: 1 hr |
| **L2 (Specialist)** | • Deep diagnosis and troubleshooting<br>• System-specific expertise<br>• Log analysis, query optimization<br>• Coordinate cross-team efforts<br>• Escalate architectural issues | Expert in 2-3 systems | Unable to resolve in 1 hr (P0) or 4 hrs (P1) | P0: 15 min<br>P1: 30 min<br>P2: 2 hrs |
| **L3 (Expert/Architect)** | • Architectural decisions<br>• Code-level debugging<br>• Complex system interactions<br>• Emergency patches/hotfixes<br>• Escalate to management if needed | Architect/Staff+ engineer | Business-critical decision needed or resolution >4 hrs | P0: 30 min<br>P1: 1 hr |
| **Management** | • Executive escalation<br>• Customer communication<br>• Resource mobilization<br>• Crisis management<br>• Post-incident accountability | Director+, VP, CTO, CEO | Major customer impact, legal/PR risk, SLA breach imminent | P0: 1 hr<br>P1: 2 hrs |

---

## 2. Severity Level Definitions & SLAs

| Severity | Definition | Examples | Response Time | Resolution Target | Escalation Time |
|----------|-----------|----------|--------------|------------------|----------------|
| **P0 / SEV0<br>(Critical)** | Complete system outage; all customers affected; revenue impact | • Website down<br>• Payment processing failure<br>• Data breach<br>• Complete AWS region failure | **5 minutes** | 4 hours | Escalate to L2 if unresolved in 30 min<br>Escalate to L3 if unresolved in 1 hr<br>Escalate to VP if unresolved in 2 hrs |
| **P1 / SEV1<br>(High)** | Major degradation; significant customer subset affected; partial revenue impact | • 50%+ API error rate<br>• Critical feature unavailable<br>• Database performance degraded<br>• Key integration down | **15 minutes** | 8 hours | Escalate to L2 if unresolved in 2 hrs<br>Escalate to L3 if unresolved in 4 hrs |
| **P2 / SEV2<br>(Medium)** | Limited functionality impaired; workaround available; minor customer impact | • Non-critical feature broken<br>• Performance slowdown <20%<br>• Intermittent errors<br>• Monitoring alerts | **1 hour** | 24 hours | Escalate to L2 if unresolved in 4 hrs |
| **P3 / SEV3<br>(Low)** | Minor issues; cosmetic; no customer impact; internal tooling | • Typo in UI<br>• Internal dashboard issue<br>• Enhancement requests<br>• Documentation updates | **4 hours** | 72 hours | No automatic escalation |

**SLA Compliance Target**: 95% of incidents resolved within target timeframe

---

## 3. Escalation Paths by Incident Type

### 3.1 Application Incidents

| Incident Type | L1 Contact | L2 Contact | L3 Contact | SME / Architect | Notes |
|--------------|-----------|-----------|-----------|----------------|-------|
| **Frontend (Web App)** | On-Call SRE | Frontend Team Lead | Staff Frontend Eng | Alice Johnson (Architect) | Check CDN, browser console errors |
| **Backend API** | On-Call SRE | Backend Team Lead | Staff Backend Eng | Bob Martinez (Tech Lead) | Review API logs, DB queries |
| **Mobile App (iOS/Android)** | On-Call SRE | Mobile Team Lead | Staff Mobile Eng | Carol Wu (iOS Lead) | Check crash reports, API responses |
| **Authentication / SSO** | On-Call SRE | Identity Team | Security Engineer | David Kim (Security) | Critical - potential security issue |
| **Search / Recommendations** | On-Call SRE | Data Engineering | ML Engineer | Emma Davis (ML Lead) | Check Elasticsearch, model performance |

### 3.2 Infrastructure Incidents

| Incident Type | L1 Contact | L2 Contact | L3 Contact | SME / Architect | Notes |
|--------------|-----------|-----------|-----------|----------------|-------|
| **AWS / Cloud Platform** | On-Call SRE | Platform Team | Staff SRE | Frank Lee (Cloud Architect) | Check AWS Health Dashboard first |
| **Kubernetes Cluster** | On-Call SRE | Platform Team | K8s Specialist | Frank Lee | Review pod status, resource limits |
| **Database (PostgreSQL)** | On-Call SRE | Database Team | DBA | Grace Park (DBA) | Check query performance, locks |
| **Redis / Caching** | On-Call SRE | Platform Team | Staff SRE | Frank Lee | Check hit rates, memory usage |
| **Network / CDN** | On-Call SRE | Network Engineer | Senior Network Eng | Henry Zhang (Network) | Check Cloudflare, DNS, routing |
| **CI/CD Pipeline** | On-Call SRE | DevOps Team | Staff DevOps Eng | Ian Roberts | Review build logs, deployments |

### 3.3 Data & Integration Incidents

| Incident Type | L1 Contact | L2 Contact | L3 Contact | SME / Architect | Notes |
|--------------|-----------|-----------|-----------|----------------|-------|
| **ETL / Data Pipeline** | On-Call SRE | Data Engineering | Staff Data Eng | Julia Chen (Data Arch) | Check Airflow, data quality |
| **Third-Party Integration** | On-Call SRE | Integration Team | Staff Backend Eng | Bob Martinez | Review API logs, credentials |
| **Payment Processor** | On-Call SRE (Priority) | Payments Team | Senior Payments Eng | Kevin Patel (Payments) | **Critical** - revenue impact |
| **Analytics / Reporting** | On-Call SRE | Data Engineering | Analytics Engineer | Julia Chen | Non-critical unless customer-facing |

### 3.4 Security Incidents

| Incident Type | L1 Contact | L2 Contact | L3 Contact | Management | Notes |
|--------------|-----------|-----------|-----------|-----------|-------|
| **Security Breach / Intrusion** | On-Call SRE | Security Engineer | CISO | VP Eng + Legal | **Immediate P0** - follow security playbook |
| **DDoS Attack** | On-Call SRE | Network Team | Security Engineer | CISO | Engage Cloudflare, AWS Shield |
| **Credential Leak** | On-Call SRE | Security Engineer | CISO | VP Eng | Rotate credentials immediately |
| **Vulnerability Exploit** | On-Call SRE | Security Engineer | Staff SRE | CISO | Assess impact, patch priority |

---

## 4. Contact Directory (24/7 Coverage)

### On-Call Rotations

| Role | Primary | Secondary | Tertiary | Contact Methods | Timezone |
|------|---------|-----------|----------|----------------|----------|
| **L1 SRE (24/7)** | Rotation (PagerDuty) | Rotation (PagerDuty) | SRE Manager | PagerDuty, Slack: #incidents, Phone | Follow-the-sun |
| **L2 Backend** | Mike Davis | Sarah Johnson | Tom Brown | PagerDuty, Slack: @backend-oncall | UTC-8 (PST) |
| **L2 Frontend** | Alice Johnson | Lisa Wang | Nina Patel | PagerDuty, Slack: @frontend-oncall | UTC-5 (EST) |
| **L2 Platform/SRE** | Frank Lee | Bob Martinez | David Kim | PagerDuty, Slack: @sre-oncall | UTC+0 (UTC) |
| **L2 Database** | Grace Park | Emma Davis | Henry Zhang | PagerDuty, Slack: @dba-oncall | UTC+8 (SGT) |
| **L3 Security** | David Kim (CISO) | Security Team | - | Phone (direct), Slack: #security-incidents | UTC-8 (PST) |
| **Management** | See Management Escalation | - | - | Phone (direct), Slack: #exec-alerts | Various |

### Key Contacts (Direct)

| Name | Role | Phone | Email | Slack | Timezone | Backup |
|------|------|-------|-------|-------|----------|--------|
| **Alice Johnson** | VP Engineering | +1-555-0101 | alice.j@company.com | @alice | UTC-8 (PST) | Bob Martinez |
| **Bob Martinez** | Director - Platform | +1-555-0102 | bob.m@company.com | @bob | UTC-8 (PST) | Frank Lee |
| **Carol Wu** | Director - Product Eng | +1-555-0103 | carol.w@company.com | @carol | UTC-5 (EST) | Mike Davis |
| **David Kim** | CISO | +1-555-0104 | david.k@company.com | @davidk | UTC-8 (PST) | Security Team |
| **Emma Davis** | Staff SRE | +1-555-0105 | emma.d@company.com | @emmad | UTC+0 (UTC) | Frank Lee |
| **Frank Lee** | Staff Platform Eng | +1-555-0106 | frank.l@company.com | @frankl | UTC+0 (UTC) | Emma Davis |

**Note**: All phone numbers connect to PagerDuty. Use Slack for non-urgent communication.

---

## 5. Escalation Decision Tree

### P0 (Critical) Incident Escalation Flow

```
┌─────────────────┐
│  Incident       │
│  Detected       │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│ L1: Initial Triage      │  ← Response: 5 min
│ - Create incident       │    Resolve: 30 min
│ - Assess severity       │
│ - Follow runbook        │
└────────┬────────────────┘
         │
         │ [Unresolved after 30 min]
         ▼
┌─────────────────────────┐
│ L2: Specialist Engaged  │  ← Response: 15 min
│ - Deep diagnosis        │    Resolve: 1 hr
│ - Cross-team coord      │
│ - Update status         │
└────────┬────────────────┘
         │
         │ [Unresolved after 1 hr]
         ▼
┌─────────────────────────┐
│ L3: Expert/Architect    │  ← Response: 30 min
│ - Code-level debug      │    Resolve: 2 hrs
│ - Emergency patch       │
│ - Architecture decision │
└────────┬────────────────┘
         │
         │ [Unresolved after 2 hrs OR major customer impact]
         ▼
┌─────────────────────────┐
│ Management Escalation   │  ← Response: 1 hr
│ - VP Engineering        │    - Customer communication
│ - CTO (if needed)       │    - Resource mobilization
│ - CEO (if major)        │    - Crisis management
└─────────────────────────┘
```

**Parallel Actions for P0**:
1. Update #incidents Slack channel every 15 minutes
2. Notify Customer Success if customer-facing
3. Prepare status page update
4. Document timeline and actions in incident ticket

---

## 6. Follow-the-Sun Handoff Procedures

### Regional Coverage

| Region | Timezone | Coverage Hours (Local) | Primary Team | Handoff To |
|--------|----------|----------------------|-------------|-----------|
| **Americas** | UTC-8 to UTC-5 | 6am - 10pm | US/Canada SRE Team | EMEA |
| **EMEA** | UTC+0 to UTC+2 | 6am - 10pm | Europe SRE Team | APAC |
| **APAC** | UTC+8 to UTC+10 | 6am - 10pm | Singapore/Sydney SRE Team | Americas |

### Handoff Protocol

**15 Minutes Before Handoff**:
1. Review all open incidents in #incidents channel
2. Prepare handoff notes in incident ticket
3. Join #handoff Slack channel
4. Post summary of ongoing incidents

**Handoff Template**:
```
🔄 HANDOFF: [REGION] → [REGION]  |  [Date] [Time]

🔴 P0 Incidents (CRITICAL):
  - [INC-12345] API outage - investigating database locks (L2 engaged)

🟠 P1 Incidents (HIGH):
  - [INC-12346] Payment processing delays - monitoring after cache flush

🟡 P2 Incidents (MEDIUM):
  - [INC-12347] Dashboard performance - patch in review

📊 System Status:
  - All core services: operational
  - Known issue: Intermittent CDN latency in EU region (monitoring)

🎯 Watch Items:
  - Monitor API error rates (currently 2.1%, threshold 5%)
  - Deployment scheduled for 2am UTC (low-risk, auto-rollback enabled)

✅ Ready for handoff. Questions?
```

---

## 7. Escalation Triggers & Criteria

### Automatic Escalation Triggers

| Condition | Action | Notification |
|-----------|--------|-------------|
| P0 incident open >30 min | Auto-page L2 specialist | PagerDuty + Slack |
| P0 incident open >1 hr | Auto-page L3 architect | PagerDuty + Slack + SMS |
| P0 incident open >2 hrs | Auto-notify VP Engineering | Phone + Slack |
| P1 incident open >4 hrs | Auto-notify Director | PagerDuty + Slack |
| SLA breach imminent (80% of target time) | Notify Incident Commander | Slack alert |
| Multiple related incidents (3+) | Create master incident, escalate | Auto-group in PagerDuty |
| Customer escalation received | Tag Customer Success, escalate to L2 | Slack + email |

### Manual Escalation Criteria

**Escalate to L2 when**:
- Incident complexity exceeds L1 runbook coverage
- Multiple systems involved requiring specialist coordination
- Root cause unclear after initial triage
- Customer VIP affected (enterprise accounts)

**Escalate to L3 when**:
- Architectural decision needed (e.g., failover to DR region)
- Code change required (emergency patch/hotfix)
- Multiple L2 specialists unable to resolve
- Complex system interaction analysis needed

**Escalate to Management when**:
- Major customer churn risk
- Legal or PR implications
- Data breach or security incident
- SLA credits will be issued
- Resolution requires cross-organizational coordination

---

## 8. Communication Channels & Protocols

### Primary Channels

| Channel | Purpose | Participants | Urgency |
|---------|---------|-------------|---------|
| **#incidents** (Slack) | Real-time incident coordination | All engineering, on-call | P0-P2 incidents |
| **#sev0** (Slack) | Critical incidents only | Leadership, incident team, CS | P0 only |
| **PagerDuty** | Alerting and on-call routing | On-call engineers | All severities |
| **Incident.io** | Incident documentation and timeline | Incident responders | All incidents |
| **Status Page** | External customer communication | Public | P0-P1 customer-facing |
| **Zoom War Room** | Live coordination for major incidents | Incident team | P0, complex P1 |

### Status Update Cadence

| Severity | Internal Update Frequency | External Update Frequency | Update Owner |
|----------|--------------------------|---------------------------|--------------|
| **P0** | Every 15 minutes | Every 30 minutes | Incident Commander |
| **P1** | Every 30 minutes | Every 2 hours | Incident Commander |
| **P2** | Hourly | Not required (unless customer-facing) | On-call engineer |
| **P3** | No fixed cadence | Not required | Assigned engineer |

**Update Template**:
```
[P0] [INC-12345] API Outage - Update #3  |  [Time]

STATUS: Investigating
IMPACT: All API requests failing (100% error rate)
CUSTOMERS AFFECTED: ~15,000 active users
DURATION: 45 minutes
ROOT CAUSE: Database connection pool exhausted (investigating why)
ACTIONS TAKEN:
  - Restarted API servers (no effect)
  - Increased DB connection pool size
  - Investigating slow queries causing connection leak
NEXT STEPS:
  - Kill long-running queries (in progress)
  - Apply emergency connection timeout patch
  - Consider read replica failover if unresolved in 15 min
ETA: 30 minutes to resolution (confidence: medium)
INCIDENT COMMANDER: Frank Lee
RESPONDERS: Emma (DBA), Bob (Backend), Alice (Architect on standby)
```

---

## 9. Cross-Functional Escalation

### Product & Customer-Facing Teams

| Incident Impact | Notify | When | Contact |
|----------------|--------|------|---------|
| **Customer-facing P0** | Customer Success Leadership | Immediately | cs-leadership@company.com, #customer-success |
| **Payment/Billing issue** | Finance + CS | Immediately | finance-ops@company.com |
| **Data accuracy issue** | Product + Data | Within 1 hour | product-oncall@company.com |
| **Security/Privacy issue** | Legal + Compliance | Immediately | legal@company.com, privacy@company.com |
| **PR risk (media attention)** | Communications/PR | Immediately | pr@company.com |

### External Vendor Escalation

| Vendor | Incident Type | Support Contact | Escalation Path | SLA |
|--------|--------------|----------------|----------------|-----|
| **AWS** | Cloud infrastructure | AWS Support (Premium) | TAM → Service Team → Principal Engineer | 15 min (P0) |
| **Datadog** | Monitoring | support@datadoghq.com | Support → Solutions Arch → Account Manager | 1 hr (P1) |
| **Stripe** | Payment processing | support@stripe.com | Support → Integration Eng → Account Manager | 30 min (P0) |
| **Cloudflare** | CDN/DDoS | support@cloudflare.com | Support → Solutions Eng → CSM | 15 min (P0) |

---

## 10. Escalation Matrix Summary (Quick Reference)

### One-Page Quick Reference

| If incident is... | And... | Then escalate to... | Within... |
|------------------|--------|-------------------|-----------|
| **P0** | Just detected | L1 SRE (PagerDuty) | 5 min |
| **P0** | Unresolved after 30 min | L2 Specialist | 15 min |
| **P0** | Unresolved after 1 hr | L3 Architect | 30 min |
| **P0** | Unresolved after 2 hrs OR major customer impact | VP Engineering | 1 hr |
| **P1** | Unresolved after 2 hrs | L2 Specialist | 30 min |
| **P1** | Unresolved after 4 hrs | L3 Architect | 1 hr |
| **P2** | Unresolved after 4 hrs | L2 Specialist | 2 hrs |
| **Security incident** | Any severity | CISO + Security Team | Immediately |
| **Payment issue** | Any severity | Payments Team + Finance | Immediately |
| **Data breach suspected** | Any severity | CISO + Legal + CEO | Immediately |

**Always**:
- Post in #incidents Slack channel
- Create incident ticket in Incident.io
- Update status every 15-30 min (P0), hourly (P1-P2)
- Document all actions and timeline

---

## 11. Related Artifacts

| Artifact Type | Relationship | Location |
|--------------|--------------|----------|
| **Incident Response Playbooks** | Detailed troubleshooting procedures | `/operations/playbooks.md` |
| **Runbooks** | Step-by-step operational procedures | `/operations/runbooks.yaml` |
| **On-Call Handbook** | On-call rotation schedule and expectations | `/documentation/on-call-handbook.md` |
| **Service Level Objectives** | SLA targets and error budgets | `/operations/service-level-objectives.md` |
| **Post-Mortem Template** | Incident retrospective format | `/governance/post-mortem-report.md` |
| **Root Cause Analysis** | Investigation methodology | `/operations/root-cause-analyses.md` |

---

## 12. Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-01-15 | SRE Manager | Initial escalation matrix |
| 0.9.0 | 2025-01-01 | SRE Manager | Draft for review |

**Next Review**: 2025-02-15 (monthly review of contact info and on-call rotations)

---

**Document Approval**:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| VP Engineering | Alice Johnson | _____________ | ______ |
| Director of Operations | Bob Martinez | _____________ | ______ |
| CISO | David Kim | _____________ | ______ |

---

*This Escalation Matrix follows ITIL 4 and Google SRE incident management best practices. Contact information must be reviewed monthly. For questions, contact SRE Leadership.*
