# Strategy.Architect Agent

## Purpose

Create comprehensive business strategy and planning artifacts including business cases, portfolio roadmaps, market analyses, competitive assessments, and strategic planning documents. Leverages financial modeling (NPV, IRR, ROI) and industry frameworks (PMBOK, SAFe, BCG Matrix) to produce executive-ready strategic deliverables.

## Skills

This agent uses the following skills:


## Artifact Flow

### Consumes

- `Initiative or project description`
- `Problem statement or opportunity`
- `Target business outcomes`
- `Budget range or financial constraints`
- `Market research data`
- `Competitive intelligence`
- `Stakeholder requirements`

### Produces

- `business-case: Comprehensive business justification with financial analysis, ROI model, risk assessment, and recommendation`
- `portfolio-roadmap: Strategic multi-initiative roadmap with timeline, dependencies, and resource allocation`
- `market-analysis: Market opportunity assessment with sizing, trends, and target segments`
- `competitive-analysis: Competitive landscape analysis with positioning and differentiation`
- `feasibility-study: Technical and business feasibility assessment`
- `strategic-plan: Multi-year strategic planning document with objectives and key results`
- `value-proposition-canvas: Customer value proposition and fit analysis`
- `roi-model: Financial return on investment model with multi-year projections`

## Example Use Cases

- Executive summary for C-suite
- Problem statement with impact analysis
- Proposed solution with scope
- Financial analysis (costs $500K, benefits $300K annually, 18mo payback)
- Risk assessment with mitigation
- Implementation timeline
- Recommendation and next steps
- Strategic alignment to business objectives
- Three major initiatives with phases
- Timeline with milestones and dependencies
- Resource allocation across initiatives
- Budget distribution ($5M across 18 months)
- Risk and dependency management
- Success metrics and KPIs
- market-analysis.yaml with market sizing, growth trends, target segments
- competitive-analysis.yaml with competitor positioning, SWOT analysis
- value-proposition-canvas.yaml with customer jobs, pains, gains

## Usage

```bash
# Activate the agent
/agent strategy.architect

# Or invoke directly
betty agent run strategy.architect --input <path>
```

## Created By

This agent was created by **meta.agent**, the meta-agent for creating agents.

---

*Part of the Betty Framework*
