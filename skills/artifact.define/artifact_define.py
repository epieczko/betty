#!/usr/bin/env python3
"""
artifact_define.py - Define artifact metadata for Betty Framework skills

Helps create artifact_metadata blocks that declare what artifacts a skill
produces and consumes, enabling interoperability.
"""

import os
import sys
import json
import yaml
from typing import Dict, Any, List, Optional
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.config import BASE_DIR
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)

# Known artifact types and their metadata
KNOWN_ARTIFACT_TYPES = {
    "openapi-spec": {
        "schema": "schemas/openapi-spec.json",
        "file_pattern": "*.openapi.yaml",
        "content_type": "application/yaml",
        "description": "OpenAPI 3.0+ specification"
    },
    "validation-report": {
        "schema": "schemas/validation-report.json",
        "file_pattern": "*.validation.json",
        "content_type": "application/json",
        "description": "Structured validation results"
    },
    "workflow-definition": {
        "schema": "schemas/workflow-definition.json",
        "file_pattern": "*.workflow.yaml",
        "content_type": "application/yaml",
        "description": "Betty workflow definition"
    },
    "hook-config": {
        "schema": "schemas/hook-config.json",
        "file_pattern": "hooks.yaml",
        "content_type": "application/yaml",
        "description": "Claude Code hook configuration"
    },
    "api-models": {
        "file_pattern": "*.{py,ts,go}",
        "description": "Generated API data models"
    },
    "agent-description": {
        "schema": "schemas/agent-description.json",
        "file_pattern": "**/agent_description.md",
        "content_type": "text/markdown",
        "description": "Natural language description of agent purpose and requirements"
    },
    "agent-definition": {
        "schema": "schemas/agent-definition.json",
        "file_pattern": "agents/*/agent.yaml",
        "content_type": "application/yaml",
        "description": "Complete agent configuration with skills and metadata"
    },
    "agent-documentation": {
        "file_pattern": "agents/*/README.md",
        "content_type": "text/markdown",
        "description": "Human-readable agent documentation"
    },
    "optimization-report": {
        "schema": "schemas/optimization-report.json",
        "file_pattern": "*.optimization.json",
        "content_type": "application/json",
        "description": "Performance and security optimization recommendations for APIs and workflows. Contains actionable suggestions for improving efficiency, security posture, and adherence to best practices."
    },
    "compatibility-graph": {
        "schema": "schemas/compatibility-graph.json",
        "file_pattern": "*.compatibility.json",
        "content_type": "application/json",
        "description": "Agent relationship graph showing which agents can work together based on artifact flows. Maps producers to consumers, enabling intelligent multi-agent orchestration."
    },
    "pipeline-suggestion": {
        "schema": "schemas/pipeline-suggestion.json",
        "file_pattern": "*.pipeline.json",
        "content_type": "application/json",
        "description": "Suggested multi-agent workflow with step-by-step execution plan. Ensures artifact compatibility and provides rationale for agent selection."
    },
    "suggestion-report": {
        "schema": "schemas/suggestion-report.json",
        "file_pattern": "*.suggestions.json",
        "content_type": "application/json",
        "description": "Context-aware recommendations for what to do next after an agent completes. Includes ranked suggestions with rationale, required artifacts, and expected outcomes."
    },
    "skill-description": {
        "schema": "schemas/skill-description.json",
        "file_pattern": "**/skill_description.md",
        "content_type": "text/markdown",
        "description": "Natural language description of a skill's requirements, inputs, outputs, and implementation details. Used by meta.skill to generate complete skill implementations."
    },
    "agile-epic": {
        "file_pattern": "*.epic.md",
        "content_type": "text/markdown",
        "description": "Agile Epic document with structured fields including title, summary, background, acceptance criteria, stakeholders, and next steps. Created by epic.write skill."
    },
    "user-stories-list": {
        "file_pattern": "*.stories.json",
        "content_type": "application/json",
        "description": "Structured JSON list of user story summaries with persona, goal, benefit, and acceptance criteria. Created by epic.decompose skill."
    },
    "user-story": {
        "file_pattern": "story_*.md",
        "content_type": "text/markdown",
        "description": "Fully formatted user story document following standard format (As a/I want/So that) with acceptance criteria, INVEST validation, and metadata. Created by story.write skill."
    },
    "skill-definition": {
        "schema": "schemas/skill-definition.json",
        "file_pattern": "skills/*/skill.yaml",
        "content_type": "application/yaml",
        "description": "Complete skill configuration in YAML format. Defines skill metadata, inputs, outputs, artifact metadata, permissions, and entrypoints."
    },
    "hook-description": {
        "schema": "schemas/hook-description.json",
        "file_pattern": "**/hook_description.md",
        "content_type": "text/markdown",
        "description": "Natural language description of a Claude Code hook's purpose, trigger event, and command to execute. Used by meta.hook to generate hook configurations."
    },
    "acceptable-use-policy": {
        "file_pattern": "*.acceptable-use-policy.md",
        "content_type": "text/markdown",
        "description": "Acceptable Use Policy for Public-Facing and Legal. Part of Legal & External documentation and deliverables."
    },
    "acceptance-criteria": {
        "file_pattern": "*.acceptance-criteria.md",
        "content_type": "text/markdown",
        "description": "Acceptance criteria for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "access-recertification-plan": {
        "file_pattern": "*.access-recertification-plan.md",
        "content_type": "text/markdown",
        "description": "Access recertification plan for Architecture. Part of Security Architecture documentation and deliverables."
    },
    "access-review-logs": {
        "file_pattern": "*.access-review-logs.md",
        "content_type": "text/markdown",
        "description": "Access review logs for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables."
    },
    "accessibility-audits": {
        "file_pattern": "*.accessibility-audits.md",
        "content_type": "text/markdown",
        "description": "Accessibility audits for Design. Part of Design & UX documentation and deliverables."
    },
    "accessibility-requirements": {
        "file_pattern": "*.accessibility-requirements.md",
        "content_type": "text/markdown",
        "description": "Accessibility requirements for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "admin-guides": {
        "file_pattern": "*.admin-guides.md",
        "content_type": "text/markdown",
        "description": "Admin guides for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables."
    },
    "adr-index": {
        "file_pattern": "*.adr-index.md",
        "content_type": "text/markdown",
        "description": "ADR index for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "adversary-emulation-documents": {
        "file_pattern": "*.adversary-emulation-documents.md",
        "content_type": "text/markdown",
        "description": "Adversary emulation documents for Architecture. Part of Security Architecture documentation and deliverables."
    },
    "ai-ethics-and-bias-assessment": {
        "file_pattern": "*.ai-ethics-and-bias-assessment.md",
        "content_type": "text/markdown",
        "description": "AI ethics and bias assessment for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables."
    },
    "ai-use-case-inventory": {
        "file_pattern": "*.ai-use-case-inventory.md",
        "content_type": "text/markdown",
        "description": "AI use-case inventory for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables."
    },
    "alert-catalogs": {
        "file_pattern": "*.alert-catalogs.md",
        "content_type": "text/markdown",
        "description": "Alert catalogs for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "analytics-model-documentation": {
        "file_pattern": "*.analytics-model-documentation.md",
        "content_type": "text/markdown",
        "description": "Analytics model documentation for Data Engineering and Analytics. Part of Data Platform documentation and deliverables."
    },
    "api-catalogs": {
        "file_pattern": "*.api-catalogs.md",
        "content_type": "text/markdown",
        "description": "API catalogs for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables."
    },
    "api-versioning-policy": {
        "file_pattern": "*.api-versioning-policy.md",
        "content_type": "text/markdown",
        "description": "API versioning policy for Architecture. Part of Application and Integration documentation and deliverables."
    },
    "app-store-metadata": {
        "file_pattern": "*.app-store-metadata.md",
        "content_type": "text/markdown",
        "description": "App store metadata for Mobile, Desktop, and Distribution. Part of Client Distribution documentation and deliverables."
    },
    "approval-evidence": {
        "file_pattern": "*.approval-evidence.md",
        "content_type": "text/markdown",
        "description": "Approval evidence for HR, Access, and Lifecycle. Part of Access & Identity documentation and deliverables."
    },
    "architecture-approvals": {
        "file_pattern": "*.architecture-approvals.md",
        "content_type": "text/markdown",
        "description": "Architecture approvals for Architecture. Part of High-Level and Platform documentation and deliverables."
    },
    "architecture-overview": {
        "file_pattern": "*.architecture-overview.md",
        "content_type": "text/markdown",
        "description": "Architecture overview for Architecture. Part of High-Level and Platform documentation and deliverables."
    },
    "architecture-review-board-minutes": {
        "file_pattern": "*.architecture-review-board-minutes.md",
        "content_type": "text/markdown",
        "description": "Architecture review board minutes for Architecture. Part of High-Level and Platform documentation and deliverables."
    },
    "architecture-vision": {
        "file_pattern": "*.architecture-vision.md",
        "content_type": "text/markdown",
        "description": "Architecture vision for Architecture. Part of High-Level and Platform documentation and deliverables."
    },
    "architecture-waivers": {
        "file_pattern": "*.architecture-waivers.md",
        "content_type": "text/markdown",
        "description": "Architecture waivers for Architecture. Part of High-Level and Platform documentation and deliverables."
    },
    "archival-plan": {
        "file_pattern": "*.archival-plan.md",
        "content_type": "text/markdown",
        "description": "Archival plan for Closure and Archival. Part of Project Closure documentation and deliverables."
    },
    "artifact-registry-policies": {
        "file_pattern": "*.artifact-registry-policies.md",
        "content_type": "text/markdown",
        "description": "Artifact registry policies for Deployment and Release. Part of Release Management documentation and deliverables."
    },
    "artifact-store-policies": {
        "file_pattern": "*.artifact-store-policies.md",
        "content_type": "text/markdown",
        "description": "Artifact store policies for CI/CD, Build, and Provenance. Part of Build & Release Automation documentation and deliverables."
    },
    "asyncapi-specification": {
        "file_pattern": "*.asyncapi-specification.md",
        "content_type": "text/markdown",
        "description": "AsyncAPI specification for Architecture. Part of Application and Integration documentation and deliverables."
    },
    "attribution-files": {
        "file_pattern": "*.attribution-files.md",
        "content_type": "text/markdown",
        "description": "Attribution files for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables."
    },
    "audit-readiness-workbook": {
        "file_pattern": "*.audit-readiness-workbook.md",
        "content_type": "text/markdown",
        "description": "Audit readiness workbook for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables."
    },
    "auto-update-policies": {
        "file_pattern": "*.auto-update-policies.md",
        "content_type": "text/markdown",
        "description": "Auto-update policies for Mobile, Desktop, and Distribution. Part of Client Distribution documentation and deliverables."
    },
    "automated-quality-gates": {
        "file_pattern": "*.automated-quality-gates.md",
        "content_type": "text/markdown",
        "description": "Automated quality gates for CI/CD, Build, and Provenance. Part of Build & Release Automation documentation and deliverables."
    },
    "automated-test-scripts": {
        "file_pattern": "*.automated-test-scripts.txt",
        "content_type": "text/plain",
        "description": "Automated test scripts for Testing. Part of Quality Assurance documentation and deliverables."
    },
    "backup-and-recovery-plan": {
        "file_pattern": "*.backup-and-recovery-plan.md",
        "content_type": "text/markdown",
        "description": "Backup and recovery plan for Architecture. Part of Data and Information documentation and deliverables."
    },
    "backup-verification-logs": {
        "file_pattern": "*.backup-verification-logs.md",
        "content_type": "text/markdown",
        "description": "Backup verification logs for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "baseline-hardening-guides": {
        "file_pattern": "*.baseline-hardening-guides.md",
        "content_type": "text/markdown",
        "description": "Baseline hardening guides for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables."
    },
    "battlecards": {
        "file_pattern": "*.battlecards.md",
        "content_type": "text/markdown",
        "description": "Battlecards for Product Management and GTM. Part of Product & Market documentation and deliverables."
    },
    "benefits-realization-plan": {
        "file_pattern": "*.benefits-realization-plan.md",
        "content_type": "text/markdown",
        "description": "Benefits realization plan for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "benefits-realization-report": {
        "file_pattern": "*.benefits-realization-report.md",
        "content_type": "text/markdown",
        "description": "Benefits realization report for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "bias-and-fairness-reports": {
        "file_pattern": "*.bias-and-fairness-reports.md",
        "content_type": "text/markdown",
        "description": "Bias and fairness reports for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables."
    },
    "bounded-context-map": {
        "file_pattern": "*.bounded-context-map.*",
        "description": "Bounded context map for Architecture. Part of High-Level and Platform documentation and deliverables."
    },
    "budget-forecast": {
        "file_pattern": "*.budget-forecast.md",
        "content_type": "text/markdown",
        "description": "Budget forecast for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "bug-bounty-brief": {
        "file_pattern": "*.bug-bounty-brief.md",
        "content_type": "text/markdown",
        "description": "Bug bounty brief for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables."
    },
    "build-reproducibility-notes": {
        "file_pattern": "*.build-reproducibility-notes.md",
        "content_type": "text/markdown",
        "description": "Build reproducibility notes for CI/CD, Build, and Provenance. Part of Build & Release Automation documentation and deliverables."
    },
    "build-scripts": {
        "file_pattern": "*.build-scripts.txt",
        "content_type": "text/plain",
        "description": "Build scripts for Implementation. Part of Development documentation and deliverables."
    },
    "business-associate-agreement": {
        "file_pattern": "*.business-associate-agreement.md",
        "content_type": "text/markdown",
        "description": "Business Associate Agreement (BAA) for Public-Facing and Legal. Part of Legal & External documentation and deliverables."
    },
    "business-case": {
        "file_pattern": "*.business-case.md",
        "content_type": "text/markdown",
        "description": "Business case for Inception / Strategy. Part of Business & Strategy documentation and deliverables."
    },
    "business-process-models": {
        "file_pattern": "*.business-process-models.*",
        "description": "Business process models (BPMN, flowcharts) for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "business-rules-catalog": {
        "file_pattern": "*.business-rules-catalog.md",
        "content_type": "text/markdown",
        "description": "Business rules catalog for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "cab-approvals": {
        "file_pattern": "*.cab-approvals.md",
        "content_type": "text/markdown",
        "description": "CAB approvals for Deployment and Release. Part of Release Management documentation and deliverables."
    },
    "caching-strategy": {
        "file_pattern": "*.caching-strategy.md",
        "content_type": "text/markdown",
        "description": "Caching strategy for Design. Part of Design & UX documentation and deliverables."
    },
    "caching-tiers": {
        "file_pattern": "*.caching-tiers.md",
        "content_type": "text/markdown",
        "description": "Caching tiers for Performance, Capacity, and Cost. Part of Performance & Optimization documentation and deliverables."
    },
    "capability-model": {
        "file_pattern": "*.capability-model.md",
        "content_type": "text/markdown",
        "description": "Capability model for Architecture. Part of High-Level and Platform documentation and deliverables."
    },
    "capacity-models": {
        "file_pattern": "*.capacity-models.md",
        "content_type": "text/markdown",
        "description": "Capacity models for Performance, Capacity, and Cost. Part of Performance & Optimization documentation and deliverables."
    },
    "capacity-plan": {
        "file_pattern": "*.capacity-plan.md",
        "content_type": "text/markdown",
        "description": "Capacity plan for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "capitalization-policy": {
        "file_pattern": "*.capitalization-policy.md",
        "content_type": "text/markdown",
        "description": "Capitalization policy for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "carbon-footprint-analysis": {
        "file_pattern": "*.carbon-footprint-analysis.md",
        "content_type": "text/markdown",
        "description": "Carbon footprint analysis for Performance, Capacity, and Cost. Part of Performance & Optimization documentation and deliverables."
    },
    "cdn-and-waf-configs": {
        "file_pattern": "*.cdn-and-waf-configs.md",
        "content_type": "text/markdown",
        "description": "CDN and WAF configs for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables."
    },
    "certificate-policy": {
        "file_pattern": "*.certificate-policy.md",
        "content_type": "text/markdown",
        "description": "Certificate policy for Architecture. Part of Security Architecture documentation and deliverables."
    },
    "certification-exams": {
        "file_pattern": "*.certification-exams.md",
        "content_type": "text/markdown",
        "description": "Certification exams for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables."
    },
    "change-control-plan": {
        "file_pattern": "*.change-control-plan.md",
        "content_type": "text/markdown",
        "description": "Change control plan for Inception / Strategy. Part of Business & Strategy documentation and deliverables."
    },
    "change-log": {
        "file_pattern": "*.change-log.md",
        "content_type": "text/markdown",
        "description": "Change log for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "changelogs": {
        "file_pattern": "*.changelogs.md",
        "content_type": "text/markdown",
        "description": "Changelogs for Implementation. Part of Development documentation and deliverables."
    },
    "chaos-engineering-experiments": {
        "file_pattern": "*.chaos-engineering-experiments.md",
        "content_type": "text/markdown",
        "description": "Chaos engineering experiments for Testing. Part of Quality Assurance documentation and deliverables."
    },
    "ci-cd-pipeline-definitions": {
        "file_pattern": "*.ci-cd-pipeline-definitions.md",
        "content_type": "text/markdown",
        "description": "CI/CD pipeline definitions for Deployment and Release. Part of Release Management documentation and deliverables."
    },
    "circuit-breaker-configurations": {
        "file_pattern": "*.circuit-breaker-configurations.md",
        "content_type": "text/markdown",
        "description": "Circuit breaker configurations for Implementation. Part of Development documentation and deliverables."
    },
    "class-diagrams": {
        "file_pattern": "*.class-diagrams.*",
        "description": "Class diagrams for Design. Part of Design & UX documentation and deliverables."
    },
    "cloud-cost-optimization-reports": {
        "file_pattern": "*.cloud-cost-optimization-reports.md",
        "content_type": "text/markdown",
        "description": "Cloud cost optimization reports for Performance, Capacity, and Cost. Part of Performance & Optimization documentation and deliverables."
    },
    "cloud-landing-zone-design": {
        "file_pattern": "*.cloud-landing-zone-design.md",
        "content_type": "text/markdown",
        "description": "Cloud landing zone design for Architecture. Part of High-Level and Platform documentation and deliverables."
    },
    "cmp-configurations": {
        "file_pattern": "*.cmp-configurations.md",
        "content_type": "text/markdown",
        "description": "CMP configurations for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "code-coverage-reports": {
        "file_pattern": "*.code-coverage-reports.md",
        "content_type": "text/markdown",
        "description": "Code coverage reports for Implementation. Part of Development documentation and deliverables."
    },
    "code-review-records": {
        "file_pattern": "*.code-review-records.md",
        "content_type": "text/markdown",
        "description": "Code review records for Implementation. Part of Development documentation and deliverables."
    },
    "code-signing-records": {
        "file_pattern": "*.code-signing-records.md",
        "content_type": "text/markdown",
        "description": "Code signing records for Mobile, Desktop, and Distribution. Part of Client Distribution documentation and deliverables."
    },
    "coding-standards-and-style-guides": {
        "file_pattern": "*.coding-standards-and-style-guides.md",
        "content_type": "text/markdown",
        "description": "Coding standards and style guides for Implementation. Part of Development documentation and deliverables."
    },
    "commit-logs": {
        "file_pattern": "*.commit-logs.md",
        "content_type": "text/markdown",
        "description": "Commit logs for Implementation. Part of Development documentation and deliverables."
    },
    "communication-plan": {
        "file_pattern": "*.communication-plan.md",
        "content_type": "text/markdown",
        "description": "Communication plan for Inception / Strategy. Part of Business & Strategy documentation and deliverables."
    },
    "competitive-analysis": {
        "file_pattern": "*.competitive-analysis.md",
        "content_type": "text/markdown",
        "description": "Competitive analysis for Inception / Strategy. Part of Business & Strategy documentation and deliverables."
    },
    "component-diagrams": {
        "file_pattern": "*.component-diagrams.*",
        "description": "Component diagrams for Design. Part of Design & UX documentation and deliverables."
    },
    "component-model": {
        "file_pattern": "*.component-model.md",
        "content_type": "text/markdown",
        "description": "Component model for Architecture. Part of Application and Integration documentation and deliverables."
    },
    "configuration-design": {
        "file_pattern": "*.configuration-design.md",
        "content_type": "text/markdown",
        "description": "Configuration design for Design. Part of Design & UX documentation and deliverables."
    },
    "configuration-drift-reports": {
        "file_pattern": "*.configuration-drift-reports.md",
        "content_type": "text/markdown",
        "description": "Configuration drift reports for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "consent-models": {
        "file_pattern": "*.consent-models.md",
        "content_type": "text/markdown",
        "description": "Consent models for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "consent-receipts": {
        "file_pattern": "*.consent-receipts.md",
        "content_type": "text/markdown",
        "description": "Consent receipts for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "content-strategy": {
        "file_pattern": "*.content-strategy.md",
        "content_type": "text/markdown",
        "description": "Content strategy for Design. Part of Design & UX documentation and deliverables."
    },
    "context-diagrams": {
        "file_pattern": "*.context-diagrams.*",
        "description": "Context diagrams for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "continuous-improvement-plan": {
        "file_pattern": "*.continuous-improvement-plan.md",
        "content_type": "text/markdown",
        "description": "Continuous improvement plan for Closure and Archival. Part of Project Closure documentation and deliverables."
    },
    "contributing-guide": {
        "file_pattern": "CONTRIBUTING.md",
        "content_type": "text/markdown",
        "description": "CONTRIBUTING guide for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables."
    },
    "contributor-license-agreements": {
        "file_pattern": "*.contributor-license-agreements.md",
        "content_type": "text/markdown",
        "description": "Contributor License Agreements (CLAs) for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables."
    },
    "control-test-evidence-packs": {
        "file_pattern": "*.control-test-evidence-packs.md",
        "content_type": "text/markdown",
        "description": "Control test evidence packs for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables."
    },
    "cookie-policy-inventory": {
        "file_pattern": "*.cookie-policy-inventory.md",
        "content_type": "text/markdown",
        "description": "Cookie policy inventory for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "cookie-policy": {
        "file_pattern": "*.cookie-policy.md",
        "content_type": "text/markdown",
        "description": "Cookie Policy for Public-Facing and Legal. Part of Legal & External documentation and deliverables."
    },
    "cosign-signatures": {
        "file_pattern": "*.cosign-signatures.md",
        "content_type": "text/markdown",
        "description": "Cosign signatures for Implementation. Part of Development documentation and deliverables."
    },
    "cost-anomaly-alerts": {
        "file_pattern": "*.cost-anomaly-alerts.md",
        "content_type": "text/markdown",
        "description": "Cost anomaly alerts for Performance, Capacity, and Cost. Part of Performance & Optimization documentation and deliverables."
    },
    "cost-tagging-policy": {
        "file_pattern": "*.cost-tagging-policy.md",
        "content_type": "text/markdown",
        "description": "Cost tagging policy for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables."
    },
    "crash-reporting-taxonomy": {
        "file_pattern": "*.crash-reporting-taxonomy.md",
        "content_type": "text/markdown",
        "description": "Crash reporting taxonomy for Mobile, Desktop, and Distribution. Part of Client Distribution documentation and deliverables."
    },
    "crash-triage-playbooks": {
        "file_pattern": "*.crash-triage-playbooks.md",
        "content_type": "text/markdown",
        "description": "Crash triage playbooks for Mobile, Desktop, and Distribution. Part of Client Distribution documentation and deliverables."
    },
    "customer-communication-templates": {
        "file_pattern": "*.customer-communication-templates.md",
        "content_type": "text/markdown",
        "description": "Customer communication templates for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables."
    },
    "customer-data-return-procedures": {
        "file_pattern": "*.customer-data-return-procedures.md",
        "content_type": "text/markdown",
        "description": "Customer data return procedures for Closure and Archival. Part of Project Closure documentation and deliverables."
    },
    "customer-onboarding-plan": {
        "file_pattern": "*.customer-onboarding-plan.md",
        "content_type": "text/markdown",
        "description": "Customer onboarding plan for Product Management and GTM. Part of Product & Market documentation and deliverables."
    },
    "cutover-checklist": {
        "file_pattern": "*.cutover-checklist.md",
        "content_type": "text/markdown",
        "description": "Cutover checklist for Deployment and Release. Part of Release Management documentation and deliverables."
    },
    "dag-definitions": {
        "file_pattern": "*.dag-definitions.md",
        "content_type": "text/markdown",
        "description": "DAG definitions for Data Engineering and Analytics. Part of Data Platform documentation and deliverables."
    },
    "data-contracts": {
        "file_pattern": "*.data-contracts.md",
        "content_type": "text/markdown",
        "description": "Data contracts for Architecture. Part of Application and Integration documentation and deliverables."
    },
    "data-dictionaries": {
        "file_pattern": "*.data-dictionaries.md",
        "content_type": "text/markdown",
        "description": "Data dictionaries for Architecture. Part of Data and Information documentation and deliverables."
    },
    "data-export-procedures": {
        "file_pattern": "*.data-export-procedures.md",
        "content_type": "text/markdown",
        "description": "Data export procedures for Closure and Archival. Part of Project Closure documentation and deliverables."
    },
    "data-flow-diagrams": {
        "file_pattern": "*.data-flow-diagrams.*",
        "description": "Data flow diagrams (DFDs) for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "data-freshness-slas": {
        "file_pattern": "*.data-freshness-slas.md",
        "content_type": "text/markdown",
        "description": "Data freshness SLAs for Architecture. Part of Data and Information documentation and deliverables."
    },
    "data-lineage-maps": {
        "file_pattern": "*.data-lineage-maps.*",
        "description": "Data lineage maps for Architecture. Part of Data and Information documentation and deliverables."
    },
    "data-lineage-tracking": {
        "file_pattern": "*.data-lineage-tracking.md",
        "content_type": "text/markdown",
        "description": "Data lineage tracking for Data Engineering and Analytics. Part of Data Platform documentation and deliverables."
    },
    "data-map": {
        "file_pattern": "*.data-map.*",
        "description": "Data map for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "data-processing-addendum": {
        "file_pattern": "*.data-processing-addendum.md",
        "content_type": "text/markdown",
        "description": "Data Processing Addendum (DPA) for Public-Facing and Legal. Part of Legal & External documentation and deliverables."
    },
    "data-product-specification": {
        "file_pattern": "*.data-product-specification.md",
        "content_type": "text/markdown",
        "description": "Data product specification for Data Engineering and Analytics. Part of Data Platform documentation and deliverables."
    },
    "data-protection-impact-assessment": {
        "file_pattern": "*.data-protection-impact-assessment.md",
        "content_type": "text/markdown",
        "description": "Data Protection Impact Assessment (DPIA) for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "data-quality-rules": {
        "file_pattern": "*.data-quality-rules.md",
        "content_type": "text/markdown",
        "description": "Data quality rules for Architecture. Part of Data and Information documentation and deliverables."
    },
    "data-residency-plan": {
        "file_pattern": "*.data-residency-plan.md",
        "content_type": "text/markdown",
        "description": "Data residency plan for Architecture. Part of Data and Information documentation and deliverables."
    },
    "data-retention-plan": {
        "file_pattern": "*.data-retention-plan.md",
        "content_type": "text/markdown",
        "description": "Data retention plan for Architecture. Part of Data and Information documentation and deliverables."
    },
    "database-schema-ddl": {
        "file_pattern": "*.database-schema-ddl.txt",
        "content_type": "text/plain",
        "description": "Database schema DDL for Architecture. Part of Data and Information documentation and deliverables."
    },
    "dataset-documentation": {
        "file_pattern": "*.dataset-documentation.md",
        "content_type": "text/markdown",
        "description": "Dataset documentation for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables."
    },
    "ddos-posture-assessments": {
        "file_pattern": "*.ddos-posture-assessments.md",
        "content_type": "text/markdown",
        "description": "DDoS posture assessments for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables."
    },
    "decision-log": {
        "file_pattern": "*.decision-log.md",
        "content_type": "text/markdown",
        "description": "Decision log for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "decommissioning-plan": {
        "file_pattern": "*.decommissioning-plan.md",
        "content_type": "text/markdown",
        "description": "Decommissioning plan for Closure and Archival. Part of Project Closure documentation and deliverables."
    },
    "defect-log": {
        "file_pattern": "*.defect-log.md",
        "content_type": "text/markdown",
        "description": "Defect log for Testing. Part of Quality Assurance documentation and deliverables."
    },
    "demo-scripts": {
        "file_pattern": "*.demo-scripts.txt",
        "content_type": "text/plain",
        "description": "Demo scripts for Product Management and GTM. Part of Product & Market documentation and deliverables."
    },
    "dependency-graph": {
        "file_pattern": "*.dependency-graph.*",
        "description": "Dependency graph for Implementation. Part of Development documentation and deliverables."
    },
    "deployment-diagram": {
        "file_pattern": "*.deployment-diagram.*",
        "description": "Deployment diagram for Design. Part of Design & UX documentation and deliverables."
    },
    "deployment-plan": {
        "file_pattern": "*.deployment-plan.md",
        "content_type": "text/markdown",
        "description": "Deployment plan (blue-green, canary, rolling) for Deployment and Release. Part of Release Management documentation and deliverables."
    },
    "deployment-topology-diagram": {
        "file_pattern": "*.deployment-topology-diagram.*",
        "description": "Deployment topology diagram for Architecture. Part of High-Level and Platform documentation and deliverables."
    },
    "deprecation-policy": {
        "file_pattern": "*.deprecation-policy.md",
        "content_type": "text/markdown",
        "description": "Deprecation policy for Architecture. Part of Application and Integration documentation and deliverables."
    },
    "developer-handbook": {
        "file_pattern": "*.developer-handbook.md",
        "content_type": "text/markdown",
        "description": "Developer handbook for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables."
    },
    "disaster-recovery-runbooks": {
        "file_pattern": "*.disaster-recovery-runbooks.md",
        "content_type": "text/markdown",
        "description": "Disaster recovery runbooks for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "discount-guardrails": {
        "file_pattern": "*.discount-guardrails.md",
        "content_type": "text/markdown",
        "description": "Discount guardrails for Product Management and GTM. Part of Product & Market documentation and deliverables."
    },
    "dns-configurations": {
        "file_pattern": "*.dns-configurations.md",
        "content_type": "text/markdown",
        "description": "DNS configurations for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables."
    },
    "docker-compose-manifests": {
        "schema": "schemas/docker-compose-manifests.json",
        "file_pattern": "*.docker-compose-manifests.yaml",
        "content_type": "application/yaml",
        "description": "Docker Compose manifests for Implementation. Part of Development documentation and deliverables."
    },
    "dockerfiles": {
        "file_pattern": "*.dockerfiles.txt",
        "content_type": "text/plain",
        "description": "Dockerfiles for Implementation. Part of Development documentation and deliverables."
    },
    "domain-model": {
        "file_pattern": "*.domain-model.md",
        "content_type": "text/markdown",
        "description": "Domain model for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "dr-test-reports": {
        "file_pattern": "*.dr-test-reports.md",
        "content_type": "text/markdown",
        "description": "DR test reports for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "drift-detection-reports": {
        "file_pattern": "*.drift-detection-reports.md",
        "content_type": "text/markdown",
        "description": "Drift detection reports for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables."
    },
    "dsar-playbooks": {
        "file_pattern": "*.dsar-playbooks.md",
        "content_type": "text/markdown",
        "description": "DSAR playbooks for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "eccn-classification": {
        "file_pattern": "*.eccn-classification.md",
        "content_type": "text/markdown",
        "description": "ECCN classification for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables."
    },
    "encryption-and-key-management-design": {
        "file_pattern": "*.encryption-and-key-management-design.md",
        "content_type": "text/markdown",
        "description": "Encryption and key management design for Architecture. Part of Security Architecture documentation and deliverables."
    },
    "engagement-plan": {
        "file_pattern": "*.engagement-plan.md",
        "content_type": "text/markdown",
        "description": "Engagement plan for Inception / Strategy. Part of Business & Strategy documentation and deliverables."
    },
    "enterprise-data-model": {
        "file_pattern": "*.enterprise-data-model.md",
        "content_type": "text/markdown",
        "description": "Enterprise data model for Architecture. Part of Data and Information documentation and deliverables."
    },
    "enterprise-risk-register": {
        "file_pattern": "*.enterprise-risk-register.md",
        "content_type": "text/markdown",
        "description": "Enterprise risk register for Inception / Strategy. Part of Business & Strategy documentation and deliverables."
    },
    "environment-matrix": {
        "file_pattern": "*.environment-matrix.md",
        "content_type": "text/markdown",
        "description": "Environment matrix for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables."
    },
    "environment-promotion-rules": {
        "file_pattern": "*.environment-promotion-rules.md",
        "content_type": "text/markdown",
        "description": "Environment promotion rules for CI/CD, Build, and Provenance. Part of Build & Release Automation documentation and deliverables."
    },
    "epic-charter": {
        "file_pattern": "*.epic-charter.md",
        "content_type": "text/markdown",
        "description": "Epic charter for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "er-diagrams": {
        "file_pattern": "*.er-diagrams.*",
        "description": "ER diagrams for Architecture. Part of Data and Information documentation and deliverables."
    },
    "error-budget-policy": {
        "file_pattern": "*.error-budget-policy.md",
        "content_type": "text/markdown",
        "description": "Error budget policy for Design. Part of Design & UX documentation and deliverables."
    },
    "error-taxonomy": {
        "file_pattern": "*.error-taxonomy.md",
        "content_type": "text/markdown",
        "description": "Error taxonomy for Architecture. Part of Application and Integration documentation and deliverables."
    },
    "escalation-matrix": {
        "file_pattern": "*.escalation-matrix.md",
        "content_type": "text/markdown",
        "description": "Escalation matrix for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "etl-elt-specifications": {
        "file_pattern": "*.etl-elt-specifications.md",
        "content_type": "text/markdown",
        "description": "ETL/ELT specifications for Data Engineering and Analytics. Part of Data Platform documentation and deliverables."
    },
    "evaluation-protocols": {
        "file_pattern": "*.evaluation-protocols.txt",
        "content_type": "text/plain",
        "description": "Evaluation protocols for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables."
    },
    "event-schemas": {
        "schema": "schemas/event-schemas.json",
        "file_pattern": "*.event-schemas.json",
        "content_type": "application/json",
        "description": "Event schemas (Avro, JSON, Protobuf) for Architecture. Part of Application and Integration documentation and deliverables."
    },
    "eviction-policies": {
        "file_pattern": "*.eviction-policies.md",
        "content_type": "text/markdown",
        "description": "Eviction policies for Performance, Capacity, and Cost. Part of Performance & Optimization documentation and deliverables."
    },
    "exception-log": {
        "file_pattern": "*.exception-log.md",
        "content_type": "text/markdown",
        "description": "Exception log for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "exception-register": {
        "file_pattern": "*.exception-register.md",
        "content_type": "text/markdown",
        "description": "Exception register for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "experiment-tracking-logs": {
        "file_pattern": "*.experiment-tracking-logs.md",
        "content_type": "text/markdown",
        "description": "Experiment tracking logs for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables."
    },
    "explainability-reports": {
        "file_pattern": "*.explainability-reports.md",
        "content_type": "text/markdown",
        "description": "Explainability reports (SHAP, LIME) for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables."
    },
    "export-control-screening": {
        "file_pattern": "*.export-control-screening.md",
        "content_type": "text/markdown",
        "description": "Export control screening for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables."
    },
    "faq": {
        "file_pattern": "*.faq.md",
        "content_type": "text/markdown",
        "description": "FAQ for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables."
    },
    "feasibility-study": {
        "file_pattern": "*.feasibility-study.md",
        "content_type": "text/markdown",
        "description": "Feasibility study for Inception / Strategy. Part of Business & Strategy documentation and deliverables."
    },
    "feature-flag-registry": {
        "file_pattern": "*.feature-flag-registry.md",
        "content_type": "text/markdown",
        "description": "Feature flag registry for Implementation. Part of Development documentation and deliverables."
    },
    "feature-rollback-playbooks": {
        "file_pattern": "*.feature-rollback-playbooks.md",
        "content_type": "text/markdown",
        "description": "Feature rollback playbooks for Deployment and Release. Part of Release Management documentation and deliverables."
    },
    "feature-store-contracts": {
        "file_pattern": "*.feature-store-contracts.md",
        "content_type": "text/markdown",
        "description": "Feature store contracts for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables."
    },
    "finops-dashboards": {
        "file_pattern": "*.finops-dashboards.md",
        "content_type": "text/markdown",
        "description": "FinOps dashboards for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables."
    },
    "firewall-rules": {
        "file_pattern": "*.firewall-rules.md",
        "content_type": "text/markdown",
        "description": "Firewall rules for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables."
    },
    "functional-requirements-specification": {
        "file_pattern": "*.functional-requirements-specification.md",
        "content_type": "text/markdown",
        "description": "Functional Requirements Specification (FRS) for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "genai-safety-evaluations": {
        "file_pattern": "*.genai-safety-evaluations.md",
        "content_type": "text/markdown",
        "description": "GenAI safety evaluations for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables."
    },
    "glossary-and-taxonomy-index": {
        "file_pattern": "*.glossary-and-taxonomy-index.md",
        "content_type": "text/markdown",
        "description": "Glossary and taxonomy index for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables."
    },
    "go-no-go-minutes": {
        "file_pattern": "*.go-no-go-minutes.md",
        "content_type": "text/markdown",
        "description": "Go/no-go minutes for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "golden-path-guide": {
        "file_pattern": "*.golden-path-guide.md",
        "content_type": "text/markdown",
        "description": "Golden path guide for Architecture. Part of High-Level and Platform documentation and deliverables."
    },
    "governance-charter": {
        "file_pattern": "*.governance-charter.md",
        "content_type": "text/markdown",
        "description": "Governance charter for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "graphql-schema": {
        "file_pattern": "*.graphql-schema.*",
        "description": "GraphQL schema for Architecture. Part of Application and Integration documentation and deliverables."
    },
    "great-expectations-suites": {
        "file_pattern": "*.great-expectations-suites.md",
        "content_type": "text/markdown",
        "description": "Great Expectations suites for Architecture. Part of Data and Information documentation and deliverables."
    },
    "grpc-proto-files": {
        "file_pattern": "*.grpc-proto-files.txt",
        "content_type": "text/plain",
        "description": "gRPC proto files for Architecture. Part of Application and Integration documentation and deliverables."
    },
    "gtm-checklist": {
        "file_pattern": "*.gtm-checklist.md",
        "content_type": "text/markdown",
        "description": "GTM checklist for Product Management and GTM. Part of Product & Market documentation and deliverables."
    },
    "helm-charts": {
        "schema": "schemas/helm-charts.json",
        "file_pattern": "*/Chart.yaml",
        "content_type": "application/yaml",
        "description": "Helm charts for Implementation. Part of Development documentation and deliverables."
    },
    "high-fidelity-mockups": {
        "file_pattern": "*.high-fidelity-mockups.*",
        "description": "High-fidelity mockups for Design. Part of Design & UX documentation and deliverables."
    },
    "hsm-procedures": {
        "file_pattern": "*.hsm-procedures.md",
        "content_type": "text/markdown",
        "description": "HSM procedures for Architecture. Part of Security Architecture documentation and deliverables."
    },
    "hyperparameter-configurations": {
        "file_pattern": "*.hyperparameter-configurations.md",
        "content_type": "text/markdown",
        "description": "Hyperparameter configurations for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables."
    },
    "iac-module-registry": {
        "file_pattern": "*.iac-module-registry.md",
        "content_type": "text/markdown",
        "description": "IaC module registry for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables."
    },
    "iam-design": {
        "file_pattern": "*.iam-design.md",
        "content_type": "text/markdown",
        "description": "IAM design for Architecture. Part of Security Architecture documentation and deliverables."
    },
    "idempotency-and-replay-protection-policy": {
        "file_pattern": "*.idempotency-and-replay-protection-policy.md",
        "content_type": "text/markdown",
        "description": "Idempotency and replay protection policy for Architecture. Part of Application and Integration documentation and deliverables."
    },
    "incident-management-plan": {
        "file_pattern": "*.incident-management-plan.md",
        "content_type": "text/markdown",
        "description": "Incident management plan for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "incident-reports": {
        "file_pattern": "*.incident-reports.md",
        "content_type": "text/markdown",
        "description": "Incident reports for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "information-architecture": {
        "file_pattern": "*.information-architecture.md",
        "content_type": "text/markdown",
        "description": "Information architecture for Design. Part of Design & UX documentation and deliverables."
    },
    "initiative-charter": {
        "file_pattern": "*.initiative-charter.md",
        "content_type": "text/markdown",
        "description": "Initiative charter for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "installation-guides": {
        "file_pattern": "*.installation-guides.md",
        "content_type": "text/markdown",
        "description": "Installation guides for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables."
    },
    "installer-manifests": {
        "file_pattern": "*.installer-manifests.md",
        "content_type": "text/markdown",
        "description": "Installer manifests for Mobile, Desktop, and Distribution. Part of Client Distribution documentation and deliverables."
    },
    "interactive-prototypes": {
        "file_pattern": "*.interactive-prototypes.*",
        "description": "Interactive prototypes for Design. Part of Design & UX documentation and deliverables."
    },
    "interface-control-document": {
        "file_pattern": "*.interface-control-document.md",
        "content_type": "text/markdown",
        "description": "Interface Control Document (ICD) for Architecture. Part of Application and Integration documentation and deliverables."
    },
    "ip-register": {
        "file_pattern": "*.ip-register.md",
        "content_type": "text/markdown",
        "description": "IP register for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables."
    },
    "iso-27001-mapping": {
        "file_pattern": "*.iso-27001-mapping.*",
        "description": "ISO 27001 mapping for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables."
    },
    "joiner-mover-leaver-workflows": {
        "file_pattern": "*.joiner-mover-leaver-workflows.md",
        "content_type": "text/markdown",
        "description": "Joiner-Mover-Leaver workflows for HR, Access, and Lifecycle. Part of Access & Identity documentation and deliverables."
    },
    "key-ceremony-records": {
        "file_pattern": "*.key-ceremony-records.md",
        "content_type": "text/markdown",
        "description": "Key ceremony records for Architecture. Part of Security Architecture documentation and deliverables."
    },
    "kill-switch-designs": {
        "file_pattern": "*.kill-switch-designs.md",
        "content_type": "text/markdown",
        "description": "Kill-switch designs for Implementation. Part of Development documentation and deliverables."
    },
    "knowledge-base-articles": {
        "file_pattern": "*.knowledge-base-articles.md",
        "content_type": "text/markdown",
        "description": "Knowledge base articles for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables."
    },
    "kpi-framework": {
        "file_pattern": "*.kpi-framework.md",
        "content_type": "text/markdown",
        "description": "KPI framework for Inception / Strategy. Part of Business & Strategy documentation and deliverables."
    },
    "kustomize-manifests": {
        "schema": "schemas/kustomize-manifests.json",
        "file_pattern": "*.kustomize-manifests.yaml",
        "content_type": "application/yaml",
        "description": "Kustomize manifests for Implementation. Part of Development documentation and deliverables."
    },
    "labs-and-workshops": {
        "file_pattern": "*.labs-and-workshops.md",
        "content_type": "text/markdown",
        "description": "Labs and workshops for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables."
    },
    "legal-hold-procedures": {
        "file_pattern": "*.legal-hold-procedures.md",
        "content_type": "text/markdown",
        "description": "Legal hold procedures for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "lessons-learned-document": {
        "file_pattern": "*.lessons-learned-document.md",
        "content_type": "text/markdown",
        "description": "Lessons learned document for Closure and Archival. Part of Project Closure documentation and deliverables."
    },
    "load-balancer-configurations": {
        "file_pattern": "*.load-balancer-configurations.md",
        "content_type": "text/markdown",
        "description": "Load balancer configurations for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables."
    },
    "load-profiles": {
        "file_pattern": "*.load-profiles.md",
        "content_type": "text/markdown",
        "description": "Load profiles for Performance, Capacity, and Cost. Part of Performance & Optimization documentation and deliverables."
    },
    "load-test-report": {
        "file_pattern": "*.load-test-report.md",
        "content_type": "text/markdown",
        "description": "Load test report for Testing. Part of Quality Assurance documentation and deliverables."
    },
    "locale-files": {
        "file_pattern": "*.locale-files.md",
        "content_type": "text/markdown",
        "description": "Locale files for Design. Part of Design & UX documentation and deliverables."
    },
    "localization-plan": {
        "file_pattern": "*.localization-plan.md",
        "content_type": "text/markdown",
        "description": "Localization plan for Design. Part of Design & UX documentation and deliverables."
    },
    "logging-taxonomy": {
        "file_pattern": "*.logging-taxonomy.md",
        "content_type": "text/markdown",
        "description": "Logging taxonomy for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "logical-architecture-diagram": {
        "file_pattern": "*.logical-architecture-diagram.*",
        "description": "Logical architecture diagram for Architecture. Part of High-Level and Platform documentation and deliverables."
    },
    "logical-data-model": {
        "file_pattern": "*.logical-data-model.md",
        "content_type": "text/markdown",
        "description": "Logical data model for Architecture. Part of Data and Information documentation and deliverables."
    },
    "market-analysis": {
        "file_pattern": "*.market-analysis.md",
        "content_type": "text/markdown",
        "description": "Market analysis for Inception / Strategy. Part of Business & Strategy documentation and deliverables."
    },
    "messaging-frameworks": {
        "file_pattern": "*.messaging-frameworks.md",
        "content_type": "text/markdown",
        "description": "Messaging frameworks for Product Management and GTM. Part of Product & Market documentation and deliverables."
    },
    "metadata-catalogs": {
        "file_pattern": "*.metadata-catalogs.md",
        "content_type": "text/markdown",
        "description": "Metadata catalogs for Architecture. Part of Data and Information documentation and deliverables."
    },
    "metric-catalog": {
        "file_pattern": "*.metric-catalog.md",
        "content_type": "text/markdown",
        "description": "Metric catalog for Data Engineering and Analytics. Part of Data Platform documentation and deliverables."
    },
    "microcopy-guides": {
        "file_pattern": "*.microcopy-guides.md",
        "content_type": "text/markdown",
        "description": "Microcopy guides for Design. Part of Design & UX documentation and deliverables."
    },
    "migration-scripts": {
        "file_pattern": "*.migration-scripts.txt",
        "content_type": "text/plain",
        "description": "Migration scripts (Liquibase/Flyway) for Architecture. Part of Data and Information documentation and deliverables."
    },
    "mission-statement": {
        "file_pattern": "*.mission-statement.md",
        "content_type": "text/markdown",
        "description": "Mission statement for Inception / Strategy. Part of Business & Strategy documentation and deliverables."
    },
    "model-cards": {
        "file_pattern": "*.model-cards.md",
        "content_type": "text/markdown",
        "description": "Model cards for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables."
    },
    "model-governance-policy": {
        "file_pattern": "*.model-governance-policy.md",
        "content_type": "text/markdown",
        "description": "Model governance policy for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables."
    },
    "model-registry-entries": {
        "file_pattern": "*.model-registry-entries.md",
        "content_type": "text/markdown",
        "description": "Model registry entries for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables."
    },
    "model-risk-assessments": {
        "file_pattern": "*.model-risk-assessments.md",
        "content_type": "text/markdown",
        "description": "Model risk assessments for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables."
    },
    "monitoring-and-observability-design": {
        "file_pattern": "*.monitoring-and-observability-design.md",
        "content_type": "text/markdown",
        "description": "Monitoring and observability design for Design. Part of Design & UX documentation and deliverables."
    },
    "monitoring-dashboards": {
        "file_pattern": "*.monitoring-dashboards.md",
        "content_type": "text/markdown",
        "description": "Monitoring dashboards for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "multi-region-active-active-plan": {
        "file_pattern": "*.multi-region-active-active-plan.md",
        "content_type": "text/markdown",
        "description": "Multi-region active-active plan for Architecture. Part of High-Level and Platform documentation and deliverables."
    },
    "network-policies": {
        "file_pattern": "*.network-policies.md",
        "content_type": "text/markdown",
        "description": "Network policies for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables."
    },
    "network-topology-diagram": {
        "file_pattern": "*.network-topology-diagram.*",
        "description": "Network topology diagram for Architecture. Part of High-Level and Platform documentation and deliverables."
    },
    "non-functional-requirements-matrix": {
        "file_pattern": "*.non-functional-requirements-matrix.md",
        "content_type": "text/markdown",
        "description": "Non-Functional Requirements (NFR) matrix for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "notarization-records": {
        "file_pattern": "*.notarization-records.md",
        "content_type": "text/markdown",
        "description": "Notarization records for Mobile, Desktop, and Distribution. Part of Client Distribution documentation and deliverables."
    },
    "offboarding-checklist": {
        "file_pattern": "*.offboarding-checklist.md",
        "content_type": "text/markdown",
        "description": "Offboarding checklist for HR, Access, and Lifecycle. Part of Access & Identity documentation and deliverables."
    },
    "okr-definitions": {
        "file_pattern": "*.okr-definitions.md",
        "content_type": "text/markdown",
        "description": "OKR definitions for Inception / Strategy. Part of Business & Strategy documentation and deliverables."
    },
    "on-call-handbook": {
        "file_pattern": "*.on-call-handbook.md",
        "content_type": "text/markdown",
        "description": "On-call handbook for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "onboarding-checklist": {
        "file_pattern": "*.onboarding-checklist.md",
        "content_type": "text/markdown",
        "description": "Onboarding checklist for HR, Access, and Lifecycle. Part of Access & Identity documentation and deliverables."
    },
    "onboarding-guide": {
        "file_pattern": "*.onboarding-guide.md",
        "content_type": "text/markdown",
        "description": "Onboarding guide for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables."
    },
    "open-source-license-bom": {
        "file_pattern": "*.open-source-license-bom.md",
        "content_type": "text/markdown",
        "description": "Open source license BoM for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables."
    },
    "openapi-specification": {
        "file_pattern": "*.openapi-specification.md",
        "content_type": "text/markdown",
        "description": "OpenAPI specification for Architecture. Part of Application and Integration documentation and deliverables."
    },
    "operational-acceptance-certificate": {
        "file_pattern": "*.operational-acceptance-certificate.md",
        "content_type": "text/markdown",
        "description": "Operational acceptance certificate for Closure and Archival. Part of Project Closure documentation and deliverables."
    },
    "operations-manual": {
        "file_pattern": "*.operations-manual.md",
        "content_type": "text/markdown",
        "description": "Operations manual for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "ownership-charters": {
        "file_pattern": "*.ownership-charters.md",
        "content_type": "text/markdown",
        "description": "Ownership charters for Data Engineering and Analytics. Part of Data Platform documentation and deliverables."
    },
    "patterns-and-anti-patterns-library": {
        "file_pattern": "*.patterns-and-anti-patterns-library.md",
        "content_type": "text/markdown",
        "description": "Patterns and anti-patterns library for Architecture. Part of High-Level and Platform documentation and deliverables."
    },
    "penetration-testing-report": {
        "file_pattern": "*.penetration-testing-report.md",
        "content_type": "text/markdown",
        "description": "Penetration testing report for Testing. Part of Quality Assurance documentation and deliverables."
    },
    "performance-strategy": {
        "file_pattern": "*.performance-strategy.md",
        "content_type": "text/markdown",
        "description": "Performance strategy for Design. Part of Design & UX documentation and deliverables."
    },
    "performance-test-plan": {
        "file_pattern": "*.performance-test-plan.md",
        "content_type": "text/markdown",
        "description": "Performance test plan for Testing. Part of Quality Assurance documentation and deliverables."
    },
    "performance-test-results": {
        "file_pattern": "*.performance-test-results.md",
        "content_type": "text/markdown",
        "description": "Performance test results for Performance, Capacity, and Cost. Part of Performance & Optimization documentation and deliverables."
    },
    "physical-architecture-diagram": {
        "file_pattern": "*.physical-architecture-diagram.*",
        "description": "Physical architecture diagram for Architecture. Part of High-Level and Platform documentation and deliverables."
    },
    "physical-data-model": {
        "file_pattern": "*.physical-data-model.md",
        "content_type": "text/markdown",
        "description": "Physical data model for Architecture. Part of Data and Information documentation and deliverables."
    },
    "pipeline-architecture-diagram": {
        "file_pattern": "*.pipeline-architecture-diagram.*",
        "description": "Pipeline architecture diagram for CI/CD, Build, and Provenance. Part of Build & Release Automation documentation and deliverables."
    },
    "pipeline-definitions": {
        "file_pattern": "*.pipeline-definitions.md",
        "content_type": "text/markdown",
        "description": "Pipeline definitions for CI/CD, Build, and Provenance. Part of Build & Release Automation documentation and deliverables."
    },
    "platform-services-catalog": {
        "file_pattern": "*.platform-services-catalog.md",
        "content_type": "text/markdown",
        "description": "Platform services catalog for Architecture. Part of High-Level and Platform documentation and deliverables."
    },
    "playbooks": {
        "file_pattern": "*.playbooks.md",
        "content_type": "text/markdown",
        "description": "Playbooks for Deployment and Release. Part of Release Management documentation and deliverables."
    },
    "portfolio-roadmap": {
        "file_pattern": "*.portfolio-roadmap.*",
        "description": "Portfolio roadmap for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "positioning-documents": {
        "file_pattern": "*.positioning-documents.md",
        "content_type": "text/markdown",
        "description": "Positioning documents for Product Management and GTM. Part of Product & Market documentation and deliverables."
    },
    "post-implementation-review": {
        "file_pattern": "*.post-implementation-review.md",
        "content_type": "text/markdown",
        "description": "Post-implementation review for Deployment and Release. Part of Release Management documentation and deliverables."
    },
    "post-mortem-report": {
        "file_pattern": "*.post-mortem-report.md",
        "content_type": "text/markdown",
        "description": "Post-mortem report for Closure and Archival. Part of Project Closure documentation and deliverables."
    },
    "price-books": {
        "file_pattern": "*.price-books.md",
        "content_type": "text/markdown",
        "description": "Price books for Product Management and GTM. Part of Product & Market documentation and deliverables."
    },
    "pricing-and-packaging-strategy": {
        "file_pattern": "*.pricing-and-packaging-strategy.md",
        "content_type": "text/markdown",
        "description": "Pricing and packaging strategy for Product Management and GTM. Part of Product & Market documentation and deliverables."
    },
    "privacy-impact-assessment": {
        "file_pattern": "*.privacy-impact-assessment.md",
        "content_type": "text/markdown",
        "description": "Privacy Impact Assessment (PIA) for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "privacy-labels": {
        "file_pattern": "*.privacy-labels.md",
        "content_type": "text/markdown",
        "description": "Privacy labels for Mobile, Desktop, and Distribution. Part of Client Distribution documentation and deliverables."
    },
    "privacy-policy": {
        "file_pattern": "*.privacy-policy.md",
        "content_type": "text/markdown",
        "description": "Privacy Policy for Public-Facing and Legal. Part of Legal & External documentation and deliverables."
    },
    "product-launch-plan": {
        "file_pattern": "*.product-launch-plan.md",
        "content_type": "text/markdown",
        "description": "Product launch plan for Product Management and GTM. Part of Product & Market documentation and deliverables."
    },
    "product-requirements-document": {
        "file_pattern": "*.product-requirements-document.md",
        "content_type": "text/markdown",
        "description": "Product Requirements Document (PRD) for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "product-strategy": {
        "file_pattern": "*.product-strategy.md",
        "content_type": "text/markdown",
        "description": "Product strategy for Inception / Strategy. Part of Business & Strategy documentation and deliverables."
    },
    "production-hygiene-checklist": {
        "file_pattern": "*.production-hygiene-checklist.md",
        "content_type": "text/markdown",
        "description": "Production hygiene checklist for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "program-increment-plan": {
        "file_pattern": "*.program-increment-plan.md",
        "content_type": "text/markdown",
        "description": "Program increment plan for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "promotion-rules": {
        "file_pattern": "*.promotion-rules.md",
        "content_type": "text/markdown",
        "description": "Promotion rules for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables."
    },
    "promotion-workflows": {
        "file_pattern": "*.promotion-workflows.md",
        "content_type": "text/markdown",
        "description": "Promotion workflows for Deployment and Release. Part of Release Management documentation and deliverables."
    },
    "prompt-engineering-policy": {
        "file_pattern": "*.prompt-engineering-policy.md",
        "content_type": "text/markdown",
        "description": "Prompt engineering policy for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables."
    },
    "provenance-attestations": {
        "file_pattern": "*.provenance-attestations.md",
        "content_type": "text/markdown",
        "description": "Provenance attestations (in-toto) for Implementation. Part of Development documentation and deliverables."
    },
    "provenance-chain-documentation": {
        "file_pattern": "*.provenance-chain-documentation.md",
        "content_type": "text/markdown",
        "description": "Provenance chain documentation (SLSA) for CI/CD, Build, and Provenance. Part of Build & Release Automation documentation and deliverables."
    },
    "pseudo-localization-reports": {
        "file_pattern": "*.pseudo-localization-reports.md",
        "content_type": "text/markdown",
        "description": "Pseudo-localization reports for Design. Part of Design & UX documentation and deliverables."
    },
    "pull-request-summaries": {
        "file_pattern": "*.pull-request-summaries.md",
        "content_type": "text/markdown",
        "description": "Pull request summaries for Implementation. Part of Development documentation and deliverables."
    },
    "purple-team-reports": {
        "file_pattern": "*.purple-team-reports.md",
        "content_type": "text/markdown",
        "description": "Purple team reports for Architecture. Part of Security Architecture documentation and deliverables."
    },
    "qbr-templates": {
        "file_pattern": "*.qbr-templates.md",
        "content_type": "text/markdown",
        "description": "QBR templates for Product Management and GTM. Part of Product & Market documentation and deliverables."
    },
    "quarterly-access-reviews": {
        "file_pattern": "*.quarterly-access-reviews.md",
        "content_type": "text/markdown",
        "description": "Quarterly access reviews for HR, Access, and Lifecycle. Part of Access & Identity documentation and deliverables."
    },
    "raci-per-workstream": {
        "file_pattern": "*.raci-per-workstream.md",
        "content_type": "text/markdown",
        "description": "RACI per workstream for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "raid-log": {
        "file_pattern": "*.raid-log.md",
        "content_type": "text/markdown",
        "description": "RAID log for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "rate-limiting-policy": {
        "file_pattern": "*.rate-limiting-policy.md",
        "content_type": "text/markdown",
        "description": "Rate limiting policy for Architecture. Part of Application and Integration documentation and deliverables."
    },
    "rbac-abac-matrix": {
        "file_pattern": "*.rbac-abac-matrix.md",
        "content_type": "text/markdown",
        "description": "RBAC/ABAC matrix for Architecture. Part of Security Architecture documentation and deliverables."
    },
    "rbac-abac-policy": {
        "file_pattern": "*.rbac-abac-policy.md",
        "content_type": "text/markdown",
        "description": "RBAC/ABAC policy for HR, Access, and Lifecycle. Part of Access & Identity documentation and deliverables."
    },
    "readme": {
        "file_pattern": "README.md",
        "content_type": "text/markdown",
        "description": "README for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables."
    },
    "records-of-processing-activities": {
        "file_pattern": "*.records-of-processing-activities.md",
        "content_type": "text/markdown",
        "description": "Records of Processing Activities (RoPA) for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "red-team-reports": {
        "file_pattern": "*.red-team-reports.md",
        "content_type": "text/markdown",
        "description": "Red team reports for Architecture. Part of Security Architecture documentation and deliverables."
    },
    "red-teaming-reports": {
        "file_pattern": "*.red-teaming-reports.md",
        "content_type": "text/markdown",
        "description": "Red-teaming reports for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables."
    },
    "reference-architectures": {
        "file_pattern": "*.reference-architectures.md",
        "content_type": "text/markdown",
        "description": "Reference architectures for Product Management and GTM. Part of Product & Market documentation and deliverables."
    },
    "regression-test-suite": {
        "file_pattern": "*.regression-test-suite.md",
        "content_type": "text/markdown",
        "description": "Regression test suite for Testing. Part of Quality Assurance documentation and deliverables."
    },
    "regulatory-mapping": {
        "file_pattern": "*.regulatory-mapping.*",
        "description": "Regulatory mapping (SOC2, ISO, NIST, HIPAA, PCI, FedRAMP) for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "release-certification": {
        "file_pattern": "*.release-certification.md",
        "content_type": "text/markdown",
        "description": "Release certification for Deployment and Release. Part of Release Management documentation and deliverables."
    },
    "release-notes": {
        "file_pattern": "*.release-notes.md",
        "content_type": "text/markdown",
        "description": "Release notes for Implementation. Part of Development documentation and deliverables."
    },
    "release-plan": {
        "file_pattern": "*.release-plan.md",
        "content_type": "text/markdown",
        "description": "Release plan for Deployment and Release. Part of Release Management documentation and deliverables."
    },
    "release-risk-assessment": {
        "file_pattern": "*.release-risk-assessment.md",
        "content_type": "text/markdown",
        "description": "Release risk assessment for Deployment and Release. Part of Release Management documentation and deliverables."
    },
    "remediation-tracker": {
        "file_pattern": "*.remediation-tracker.md",
        "content_type": "text/markdown",
        "description": "Remediation tracker for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables."
    },
    "renewal-playbooks": {
        "file_pattern": "*.renewal-playbooks.md",
        "content_type": "text/markdown",
        "description": "Renewal playbooks for Product Management and GTM. Part of Product & Market documentation and deliverables."
    },
    "reproducibility-checklists": {
        "file_pattern": "*.reproducibility-checklists.md",
        "content_type": "text/markdown",
        "description": "Reproducibility checklists for Data Engineering and Analytics. Part of Data Platform documentation and deliverables."
    },
    "requirements-traceability-matrix": {
        "file_pattern": "*.requirements-traceability-matrix.md",
        "content_type": "text/markdown",
        "description": "Requirements traceability matrix for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "resource-plan": {
        "file_pattern": "*.resource-plan.md",
        "content_type": "text/markdown",
        "description": "Resource plan for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "retention-schedule": {
        "file_pattern": "*.retention-schedule.md",
        "content_type": "text/markdown",
        "description": "Retention schedule for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "reverse-etl-playbooks": {
        "file_pattern": "*.reverse-etl-playbooks.md",
        "content_type": "text/markdown",
        "description": "Reverse ETL playbooks for Data Engineering and Analytics. Part of Data Platform documentation and deliverables."
    },
    "risk-appetite-statement": {
        "file_pattern": "*.risk-appetite-statement.md",
        "content_type": "text/markdown",
        "description": "Risk appetite statement for Inception / Strategy. Part of Business & Strategy documentation and deliverables."
    },
    "roi-model": {
        "file_pattern": "*.roi-model.md",
        "content_type": "text/markdown",
        "description": "ROI model for Inception / Strategy. Part of Business & Strategy documentation and deliverables."
    },
    "roi-tco-calculators": {
        "file_pattern": "*.roi-tco-calculators.md",
        "content_type": "text/markdown",
        "description": "ROI/TCO calculators for Product Management and GTM. Part of Product & Market documentation and deliverables."
    },
    "role-catalog": {
        "file_pattern": "*.role-catalog.md",
        "content_type": "text/markdown",
        "description": "Role catalog for HR, Access, and Lifecycle. Part of Access & Identity documentation and deliverables."
    },
    "rollback-plan": {
        "file_pattern": "*.rollback-plan.md",
        "content_type": "text/markdown",
        "description": "Rollback plan for Deployment and Release. Part of Release Management documentation and deliverables."
    },
    "root-cause-analyses": {
        "file_pattern": "*.root-cause-analyses.md",
        "content_type": "text/markdown",
        "description": "Root cause analyses (RCA) for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "runbooks": {
        "file_pattern": "*.runbooks.md",
        "content_type": "text/markdown",
        "description": "Runbooks for Deployment and Release. Part of Release Management documentation and deliverables."
    },
    "safety-filter-configurations": {
        "file_pattern": "*.safety-filter-configurations.md",
        "content_type": "text/markdown",
        "description": "Safety filter configurations for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables."
    },
    "sales-enablement-kits": {
        "file_pattern": "*.sales-enablement-kits.md",
        "content_type": "text/markdown",
        "description": "Sales enablement kits for Product Management and GTM. Part of Product & Market documentation and deliverables."
    },
    "sbom-policy": {
        "schema": "schemas/sbom-policy.json",
        "file_pattern": "*.sbom-policy.json",
        "content_type": "application/json",
        "description": "SBOM policy for CI/CD, Build, and Provenance. Part of Build & Release Automation documentation and deliverables."
    },
    "sbom-verification-reports": {
        "schema": "schemas/sbom-verification-reports.json",
        "file_pattern": "*.sbom-verification-reports.json",
        "content_type": "application/json",
        "description": "SBOM verification reports for Deployment and Release. Part of Release Management documentation and deliverables."
    },
    "scaling-policies": {
        "file_pattern": "*.scaling-policies.md",
        "content_type": "text/markdown",
        "description": "Scaling policies for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "scheduling-slas": {
        "file_pattern": "*.scheduling-slas.md",
        "content_type": "text/markdown",
        "description": "Scheduling SLAs for Data Engineering and Analytics. Part of Data Platform documentation and deliverables."
    },
    "schema-evolution-policy": {
        "file_pattern": "*.schema-evolution-policy.md",
        "content_type": "text/markdown",
        "description": "Schema evolution policy for Architecture. Part of Application and Integration documentation and deliverables."
    },
    "secret-rotation-schedule": {
        "file_pattern": "*.secret-rotation-schedule.md",
        "content_type": "text/markdown",
        "description": "Secret rotation schedule for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables."
    },
    "secrets-management-policy": {
        "file_pattern": "*.secrets-management-policy.md",
        "content_type": "text/markdown",
        "description": "Secrets management policy for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables."
    },
    "secure-coding-checklist": {
        "file_pattern": "*.secure-coding-checklist.md",
        "content_type": "text/markdown",
        "description": "Secure coding checklist for Implementation. Part of Development documentation and deliverables."
    },
    "secure-coding-policy": {
        "file_pattern": "*.secure-coding-policy.md",
        "content_type": "text/markdown",
        "description": "Secure coding policy for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables."
    },
    "security-architecture-diagram": {
        "file_pattern": "*.security-architecture-diagram.*",
        "description": "Security architecture diagram for Architecture. Part of Security Architecture documentation and deliverables."
    },
    "security-detections-catalog": {
        "file_pattern": "*.security-detections-catalog.md",
        "content_type": "text/markdown",
        "description": "Security detections catalog (MITRE ATT&CK) for Architecture. Part of Security Architecture documentation and deliverables."
    },
    "security-policy-library": {
        "file_pattern": "*.security-policy-library.md",
        "content_type": "text/markdown",
        "description": "Security policy library for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables."
    },
    "security-test-results": {
        "file_pattern": "*.security-test-results.md",
        "content_type": "text/markdown",
        "description": "Security test results (SAST, DAST, IAST) for Testing. Part of Quality Assurance documentation and deliverables."
    },
    "semantic-layer-definitions": {
        "file_pattern": "*.semantic-layer-definitions.md",
        "content_type": "text/markdown",
        "description": "Semantic layer definitions (dbt, LookML) for Architecture. Part of Data and Information documentation and deliverables."
    },
    "sequence-diagrams": {
        "file_pattern": "*.sequence-diagrams.*",
        "description": "Sequence diagrams for Design. Part of Design & UX documentation and deliverables."
    },
    "service-configuration-files": {
        "file_pattern": "*.service-configuration-files.md",
        "content_type": "text/markdown",
        "description": "Service configuration files for Implementation. Part of Development documentation and deliverables."
    },
    "service-decomposition": {
        "file_pattern": "*.service-decomposition.md",
        "content_type": "text/markdown",
        "description": "Service decomposition for Architecture. Part of Application and Integration documentation and deliverables."
    },
    "service-dependency-graph": {
        "file_pattern": "*.service-dependency-graph.*",
        "description": "Service dependency graph for Architecture. Part of Application and Integration documentation and deliverables."
    },
    "service-level-objectives": {
        "file_pattern": "*.service-level-objectives.md",
        "content_type": "text/markdown",
        "description": "Service-level objectives (SLOs) for Design. Part of Design & UX documentation and deliverables."
    },
    "service-mesh-configurations": {
        "file_pattern": "*.service-mesh-configurations.md",
        "content_type": "text/markdown",
        "description": "Service mesh configurations for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables."
    },
    "shadow-canary-deployment-scorecards": {
        "file_pattern": "*.shadow-canary-deployment-scorecards.md",
        "content_type": "text/markdown",
        "description": "Shadow/canary deployment scorecards for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables."
    },
    "showback-and-chargeback-reports": {
        "file_pattern": "*.showback-and-chargeback-reports.md",
        "content_type": "text/markdown",
        "description": "Showback and chargeback reports for Infrastructure and Platform Engineering. Part of Platform Engineering documentation and deliverables."
    },
    "sig-questionnaires": {
        "file_pattern": "*.sig-questionnaires.md",
        "content_type": "text/markdown",
        "description": "SIG questionnaires for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "skills-matrix": {
        "file_pattern": "*.skills-matrix.md",
        "content_type": "text/markdown",
        "description": "Skills matrix for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "sla-slo-schedules": {
        "file_pattern": "*.sla-slo-schedules.md",
        "content_type": "text/markdown",
        "description": "SLA/SLO schedules for Public-Facing and Legal. Part of Legal & External documentation and deliverables."
    },
    "soc-2-control-implementation-matrix": {
        "file_pattern": "*.soc-2-control-implementation-matrix.md",
        "content_type": "text/markdown",
        "description": "SOC 2 control implementation matrix for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables."
    },
    "sod-conflict-matrices": {
        "file_pattern": "*.sod-conflict-matrices.md",
        "content_type": "text/markdown",
        "description": "SoD conflict matrices for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables."
    },
    "sod-matrix": {
        "file_pattern": "*.sod-matrix.md",
        "content_type": "text/markdown",
        "description": "SoD matrix for Architecture. Part of Security Architecture documentation and deliverables."
    },
    "software-bill-of-materials": {
        "schema": "schemas/software-bill-of-materials.json",
        "file_pattern": "*.software-bill-of-materials.json",
        "content_type": "application/json",
        "description": "Software Bill of Materials (SBOM) for Implementation. Part of Development documentation and deliverables."
    },
    "solution-briefs": {
        "file_pattern": "*.solution-briefs.md",
        "content_type": "text/markdown",
        "description": "Solution briefs for Product Management and GTM. Part of Product & Market documentation and deliverables."
    },
    "source-code-repositories": {
        "file_pattern": "*.source-code-repositories.md",
        "content_type": "text/markdown",
        "description": "Source code repositories for Implementation. Part of Development documentation and deliverables."
    },
    "sprint-goals": {
        "file_pattern": "*.sprint-goals.md",
        "content_type": "text/markdown",
        "description": "Sprint goals for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "staffing-plan": {
        "file_pattern": "*.staffing-plan.md",
        "content_type": "text/markdown",
        "description": "Staffing plan for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "stakeholder-map": {
        "file_pattern": "*.stakeholder-map.*",
        "description": "Stakeholder map for Inception / Strategy. Part of Business & Strategy documentation and deliverables."
    },
    "standard-contractual-clauses": {
        "file_pattern": "*.standard-contractual-clauses.md",
        "content_type": "text/markdown",
        "description": "Standard Contractual Clauses (SCCs) for Public-Facing and Legal. Part of Legal & External documentation and deliverables."
    },
    "standard-operating-procedures": {
        "file_pattern": "*.standard-operating-procedures.md",
        "content_type": "text/markdown",
        "description": "Standard operating procedures (SOPs) for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "state-diagrams": {
        "file_pattern": "*.state-diagrams.*",
        "description": "State diagrams for Design. Part of Design & UX documentation and deliverables."
    },
    "static-analysis-reports": {
        "file_pattern": "*.static-analysis-reports.md",
        "content_type": "text/markdown",
        "description": "Static analysis reports for Implementation. Part of Development documentation and deliverables."
    },
    "status-page-communication-templates": {
        "file_pattern": "*.status-page-communication-templates.md",
        "content_type": "text/markdown",
        "description": "Status page communication templates for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "steering-committee-minutes": {
        "file_pattern": "*.steering-committee-minutes.md",
        "content_type": "text/markdown",
        "description": "Steering committee minutes for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "storyboards": {
        "file_pattern": "*.storyboards.*",
        "description": "Storyboards for Design. Part of Design & UX documentation and deliverables."
    },
    "subprocessor-notifications": {
        "file_pattern": "*.subprocessor-notifications.md",
        "content_type": "text/markdown",
        "description": "Subprocessor notifications for Public-Facing and Legal. Part of Legal & External documentation and deliverables."
    },
    "success-plan-templates": {
        "file_pattern": "*.success-plan-templates.md",
        "content_type": "text/markdown",
        "description": "Success plan templates for Product Management and GTM. Part of Product & Market documentation and deliverables."
    },
    "sustainability-reports": {
        "file_pattern": "*.sustainability-reports.md",
        "content_type": "text/markdown",
        "description": "Sustainability reports for Performance, Capacity, and Cost. Part of Performance & Optimization documentation and deliverables."
    },
    "sync-contracts": {
        "file_pattern": "*.sync-contracts.md",
        "content_type": "text/markdown",
        "description": "Sync contracts for Data Engineering and Analytics. Part of Data Platform documentation and deliverables."
    },
    "synthetic-data-generation-plan": {
        "file_pattern": "*.synthetic-data-generation-plan.md",
        "content_type": "text/markdown",
        "description": "Synthetic data generation plan for Testing. Part of Quality Assurance documentation and deliverables."
    },
    "system-requirements-specification": {
        "file_pattern": "*.system-requirements-specification.md",
        "content_type": "text/markdown",
        "description": "System Requirements Specification (SRS) for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "target-state-evolution-map": {
        "file_pattern": "*.target-state-evolution-map.*",
        "description": "Target-state evolution map for Architecture. Part of High-Level and Platform documentation and deliverables."
    },
    "team-topology-map": {
        "file_pattern": "*.team-topology-map.*",
        "description": "Team topology map for Architecture. Part of High-Level and Platform documentation and deliverables."
    },
    "technology-standards-catalog": {
        "file_pattern": "*.technology-standards-catalog.md",
        "content_type": "text/markdown",
        "description": "Technology standards catalog for Architecture. Part of High-Level and Platform documentation and deliverables."
    },
    "telemetry-schema": {
        "file_pattern": "*.telemetry-schema.txt",
        "content_type": "text/plain",
        "description": "Telemetry schema for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "tenancy-and-isolation-model": {
        "file_pattern": "*.tenancy-and-isolation-model.md",
        "content_type": "text/markdown",
        "description": "Tenancy and isolation model for Architecture. Part of High-Level and Platform documentation and deliverables."
    },
    "terms-of-service": {
        "file_pattern": "*.terms-of-service.md",
        "content_type": "text/markdown",
        "description": "Terms of Service for Public-Facing and Legal. Part of Legal & External documentation and deliverables."
    },
    "test-case-specifications": {
        "file_pattern": "*.test-case-specifications.md",
        "content_type": "text/markdown",
        "description": "Test case specifications for Testing. Part of Quality Assurance documentation and deliverables."
    },
    "test-data-specification": {
        "file_pattern": "*.test-data-specification.md",
        "content_type": "text/markdown",
        "description": "Test data specification for Testing. Part of Quality Assurance documentation and deliverables."
    },
    "test-plan": {
        "file_pattern": "*.test-plan.md",
        "content_type": "text/markdown",
        "description": "Test plan for Testing. Part of Quality Assurance documentation and deliverables."
    },
    "test-strategy": {
        "file_pattern": "*.test-strategy.md",
        "content_type": "text/markdown",
        "description": "Test strategy for Testing. Part of Quality Assurance documentation and deliverables."
    },
    "third-party-risk-assessments": {
        "file_pattern": "*.third-party-risk-assessments.md",
        "content_type": "text/markdown",
        "description": "Third-party risk assessments for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "threat-model": {
        "file_pattern": "*.threat-model.md",
        "content_type": "text/markdown",
        "description": "Threat model (STRIDE, attack trees) for Architecture. Part of Security Architecture documentation and deliverables."
    },
    "time-allocation-worksheets": {
        "file_pattern": "*.time-allocation-worksheets.md",
        "content_type": "text/markdown",
        "description": "Time allocation worksheets for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "toil-reduction-plan": {
        "file_pattern": "*.toil-reduction-plan.md",
        "content_type": "text/markdown",
        "description": "Toil reduction plan for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "topic-and-queue-catalog": {
        "file_pattern": "*.topic-and-queue-catalog.md",
        "content_type": "text/markdown",
        "description": "Topic and queue catalog for Architecture. Part of Application and Integration documentation and deliverables."
    },
    "traceability-matrix": {
        "file_pattern": "*.traceability-matrix.md",
        "content_type": "text/markdown",
        "description": "Traceability matrix for Testing. Part of Quality Assurance documentation and deliverables."
    },
    "trademark-guidance": {
        "file_pattern": "*.trademark-guidance.md",
        "content_type": "text/markdown",
        "description": "Trademark guidance for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables."
    },
    "training-curriculum": {
        "file_pattern": "*.training-curriculum.md",
        "content_type": "text/markdown",
        "description": "Training curriculum for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables."
    },
    "training-data-cards": {
        "file_pattern": "*.training-data-cards.md",
        "content_type": "text/markdown",
        "description": "Training data cards for AI/ML and Model Ops. Part of Model Development & Governance documentation and deliverables."
    },
    "triage-rules": {
        "file_pattern": "*.triage-rules.md",
        "content_type": "text/markdown",
        "description": "Triage rules for Testing. Part of Quality Assurance documentation and deliverables."
    },
    "troubleshooting-trees": {
        "file_pattern": "*.troubleshooting-trees.md",
        "content_type": "text/markdown",
        "description": "Troubleshooting trees for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables."
    },
    "trust-center-content-plan": {
        "file_pattern": "*.trust-center-content-plan.md",
        "content_type": "text/markdown",
        "description": "Trust center content plan for Product Management and GTM. Part of Product & Market documentation and deliverables."
    },
    "trust-center-evidence-summaries": {
        "file_pattern": "*.trust-center-evidence-summaries.md",
        "content_type": "text/markdown",
        "description": "Trust center evidence summaries for Public-Facing and Legal. Part of Legal & External documentation and deliverables."
    },
    "uat-plan": {
        "file_pattern": "*.uat-plan.md",
        "content_type": "text/markdown",
        "description": "UAT plan for Testing. Part of Quality Assurance documentation and deliverables."
    },
    "uat-sign-off-document": {
        "file_pattern": "*.uat-sign-off-document.md",
        "content_type": "text/markdown",
        "description": "UAT sign-off document for Testing. Part of Quality Assurance documentation and deliverables."
    },
    "upgrade-guides": {
        "file_pattern": "*.upgrade-guides.md",
        "content_type": "text/markdown",
        "description": "Upgrade guides for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables."
    },
    "uptime-methodology": {
        "file_pattern": "*.uptime-methodology.md",
        "content_type": "text/markdown",
        "description": "Uptime methodology for Public-Facing and Legal. Part of Legal & External documentation and deliverables."
    },
    "use-case-diagrams": {
        "file_pattern": "*.use-case-diagrams.*",
        "description": "Use-case diagrams for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "use-case-models": {
        "file_pattern": "*.use-case-models.md",
        "content_type": "text/markdown",
        "description": "Use-case models for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "user-journeys": {
        "file_pattern": "*.user-journeys.md",
        "content_type": "text/markdown",
        "description": "User journeys for Design. Part of Design & UX documentation and deliverables."
    },
    "user-manuals": {
        "file_pattern": "*.user-manuals.md",
        "content_type": "text/markdown",
        "description": "User manuals for Documentation, Support, and Training. Part of Knowledge & Enablement documentation and deliverables."
    },
    "user-stories": {
        "file_pattern": "*.user-stories.md",
        "content_type": "text/markdown",
        "description": "User stories for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "velocity-and-burndown-reports": {
        "file_pattern": "*.velocity-and-burndown-reports.md",
        "content_type": "text/markdown",
        "description": "Velocity and burndown reports for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "vendor-management-pack": {
        "file_pattern": "*.vendor-management-pack.md",
        "content_type": "text/markdown",
        "description": "Vendor management pack for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "vendor-scorecards": {
        "file_pattern": "*.vendor-scorecards.md",
        "content_type": "text/markdown",
        "description": "Vendor scorecards for Portfolio, Governance, and Delivery Ops. Part of Governance & Planning documentation and deliverables."
    },
    "version-tags": {
        "file_pattern": "*.version-tags.md",
        "content_type": "text/markdown",
        "description": "Version tags for Implementation. Part of Development documentation and deliverables."
    },
    "vision-statement": {
        "file_pattern": "*.vision-statement.md",
        "content_type": "text/markdown",
        "description": "Vision statement for Inception / Strategy. Part of Business & Strategy documentation and deliverables."
    },
    "vpat-acr-results": {
        "file_pattern": "*.vpat-acr-results.md",
        "content_type": "text/markdown",
        "description": "VPAT/ACR results for Requirements and Analysis. Part of Requirements & Analysis documentation and deliverables."
    },
    "vulnerability-disclosure-policy": {
        "file_pattern": "*.vulnerability-disclosure-policy.md",
        "content_type": "text/markdown",
        "description": "Vulnerability disclosure policy for Security, Privacy, Audit, and Compliance. Part of Governance, Risk & Compliance documentation and deliverables."
    },
    "vulnerability-management-plan": {
        "file_pattern": "*.vulnerability-management-plan.md",
        "content_type": "text/markdown",
        "description": "Vulnerability management plan for Operations, SRE, and Maintenance. Part of Operations & Reliability documentation and deliverables."
    },
    "wireframes": {
        "file_pattern": "*.wireframes.*",
        "description": "Wireframes for Design. Part of Design & UX documentation and deliverables."
    },
    "zero-trust-design": {
        "file_pattern": "*.zero-trust-design.md",
        "content_type": "text/markdown",
        "description": "Zero trust design for Architecture. Part of Security Architecture documentation and deliverables."
    },

}


def get_artifact_definition(artifact_type: str) -> Optional[Dict[str, Any]]:
    """
    Get the definition for a known artifact type.

    Args:
        artifact_type: Artifact type identifier

    Returns:
        Artifact definition dictionary with schema, file_pattern, etc., or None if unknown
    """
    if artifact_type in KNOWN_ARTIFACT_TYPES:
        definition = {"type": artifact_type}
        definition.update(KNOWN_ARTIFACT_TYPES[artifact_type])
        return definition
    return None


def validate_artifact_type(artifact_type: str) -> tuple[bool, Optional[str]]:
    """
    Validate that an artifact type is known or suggest registering it.

    Args:
        artifact_type: Artifact type identifier

    Returns:
        Tuple of (is_valid, warning_message)
    """
    if artifact_type in KNOWN_ARTIFACT_TYPES:
        return True, None

    warning = f"Artifact type '{artifact_type}' is not in the known registry. "
    warning += "Consider documenting it in docs/ARTIFACT_STANDARDS.md and creating a schema."
    return False, warning


def generate_artifact_metadata(
    skill_name: str,
    produces: Optional[List[str]] = None,
    consumes: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Generate artifact metadata structure.

    Args:
        skill_name: Name of the skill
        produces: List of artifact types produced
        consumes: List of artifact types consumed

    Returns:
        Artifact metadata dictionary
    """
    metadata = {}
    warnings = []

    # Build produces section
    if produces:
        produces_list = []
        for artifact_type in produces:
            is_known, warning = validate_artifact_type(artifact_type)
            if warning:
                warnings.append(warning)

            artifact_def = {"type": artifact_type}

            # Add known metadata if available
            if artifact_type in KNOWN_ARTIFACT_TYPES:
                known = KNOWN_ARTIFACT_TYPES[artifact_type]
                if "schema" in known:
                    artifact_def["schema"] = known["schema"]
                if "file_pattern" in known:
                    artifact_def["file_pattern"] = known["file_pattern"]
                if "content_type" in known:
                    artifact_def["content_type"] = known["content_type"]
                if "description" in known:
                    artifact_def["description"] = known["description"]

            produces_list.append(artifact_def)

        metadata["produces"] = produces_list

    # Build consumes section
    if consumes:
        consumes_list = []
        for artifact_type in consumes:
            is_known, warning = validate_artifact_type(artifact_type)
            if warning:
                warnings.append(warning)

            artifact_def = {
                "type": artifact_type,
                "required": True  # Default to required
            }

            # Add description if known
            if artifact_type in KNOWN_ARTIFACT_TYPES:
                known = KNOWN_ARTIFACT_TYPES[artifact_type]
                if "description" in known:
                    artifact_def["description"] = known["description"]

            consumes_list.append(artifact_def)

        metadata["consumes"] = consumes_list

    return metadata, warnings


def format_as_yaml(metadata: Dict[str, Any]) -> str:
    """
    Format artifact metadata as YAML for inclusion in skill.yaml.

    Args:
        metadata: Artifact metadata dictionary

    Returns:
        Formatted YAML string
    """
    yaml_str = "artifact_metadata:\n"
    yaml_str += yaml.dump(metadata, default_flow_style=False, indent=2, sort_keys=False)
    return yaml_str


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Define artifact metadata for Betty Framework skills"
    )
    parser.add_argument(
        "skill_name",
        help="Name of the skill (e.g., api.define)"
    )
    parser.add_argument(
        "--produces",
        nargs="+",
        help="Artifact types this skill produces"
    )
    parser.add_argument(
        "--consumes",
        nargs="+",
        help="Artifact types this skill consumes"
    )
    parser.add_argument(
        "--output-file",
        default="artifact_metadata.yaml",
        help="Output file path"
    )

    args = parser.parse_args()

    logger.info(f"Generating artifact metadata for skill: {args.skill_name}")

    try:
        # Generate metadata
        metadata, warnings = generate_artifact_metadata(
            args.skill_name,
            produces=args.produces,
            consumes=args.consumes
        )

        # Format as YAML
        yaml_content = format_as_yaml(metadata)

        # Save to file
        output_path = args.output_file
        with open(output_path, 'w') as f:
            f.write(yaml_content)

        logger.info(f"✅ Generated artifact metadata: {output_path}")

        # Print to stdout
        print("\n# Add this to your skill.yaml:\n")
        print(yaml_content)

        # Show warnings
        if warnings:
            logger.warning("\n⚠️  Warnings:")
            for warning in warnings:
                logger.warning(f"  - {warning}")

        # Print summary
        logger.info("\n📋 Summary:")
        if metadata.get("produces"):
            logger.info(f"  Produces: {', '.join(a['type'] for a in metadata['produces'])}")
        if metadata.get("consumes"):
            logger.info(f"  Consumes: {', '.join(a['type'] for a in metadata['consumes'])}")

        # Success result
        result = {
            "ok": True,
            "status": "success",
            "skill_name": args.skill_name,
            "metadata": metadata,
            "output_file": output_path,
            "warnings": warnings
        }

        print("\n" + json.dumps(result, indent=2))
        sys.exit(0)

    except Exception as e:
        logger.error(f"Failed to generate artifact metadata: {e}")
        result = {
            "ok": False,
            "status": "failed",
            "error": str(e)
        }
        print(json.dumps(result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
