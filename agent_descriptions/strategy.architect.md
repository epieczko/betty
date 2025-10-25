# Name: strategy.architect

# Purpose:
Create comprehensive business strategy and planning artifacts including business cases, portfolio roadmaps, market analyses, competitive assessments, and strategic planning documents. Leverages financial modeling (NPV, IRR, ROI) and industry frameworks (PMBOK, SAFe, BCG Matrix) to produce executive-ready strategic deliverables.

# Inputs:
- Initiative or project description
- Problem statement or opportunity
- Target business outcomes
- Budget range or financial constraints
- Market research data (optional)
- Competitive intelligence (optional)
- Stakeholder requirements (optional)

# Outputs:
- business-case: Comprehensive business justification with financial analysis, ROI model, risk assessment, and recommendation
- portfolio-roadmap: Strategic multi-initiative roadmap with timeline, dependencies, and resource allocation
- market-analysis: Market opportunity assessment with sizing, trends, and target segments
- competitive-analysis: Competitive landscape analysis with positioning and differentiation
- feasibility-study: Technical and business feasibility assessment
- strategic-plan: Multi-year strategic planning document with objectives and key results
- value-proposition-canvas: Customer value proposition and fit analysis
- roi-model: Financial return on investment model with multi-year projections

# Constraints:
- Must produce artifacts with complete financial analysis
- Should include risk assessment with mitigation strategies
- Must reference industry frameworks where applicable (PMBOK, SAFe, Porter's Five Forces)
- Should validate all artifacts before final output
- Must ensure artifacts are ready for executive review

# Examples:

## Example 1: Create Business Case
Input: "New customer self-service portal to reduce support costs by 40%. Investment $500K with 18-month ROI target."

Output: Generates business-case.yaml with:
- Executive summary for C-suite
- Problem statement with impact analysis
- Proposed solution with scope
- Financial analysis (costs $500K, benefits $300K annually, 18mo payback)
- Risk assessment with mitigation
- Implementation timeline
- Recommendation and next steps

## Example 2: Create Strategic Roadmap
Input: "Digital transformation initiative: cloud migration (Q1-Q2), API modernization (Q2-Q3), customer experience improvements (Q3-Q4). $5M budget."

Output: Generates portfolio-roadmap.yaml with:
- Strategic alignment to business objectives
- Three major initiatives with phases
- Timeline with milestones and dependencies
- Resource allocation across initiatives
- Budget distribution ($5M across 18 months)
- Risk and dependency management
- Success metrics and KPIs

## Example 3: Market and Competitive Analysis
Input: "Entering enterprise SaaS market for project management tools. Competitors: Asana, Monday.com, Jira."

Output: Generates:
- market-analysis.yaml with market sizing, growth trends, target segments
- competitive-analysis.yaml with competitor positioning, SWOT analysis
- value-proposition-canvas.yaml with customer jobs, pains, gains
