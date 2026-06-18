# Lead Scoring and Priority Rules

**Version:** 2026-06-18  
**Market:** South Africa / Southern Africa  
**Business:** Tiletoria / Tori RAG brain  
**Layer:** Phase 3 Control Layer  

## Purpose
Help Tori classify and prioritise leads so urgent, valuable or risk-sensitive opportunities are handled correctly.

## Retrieval triggers
- lead score
- priority
- hot lead
- urgent
- follow up
- contractor
- developer
- architect
- insurance
- large project
- quote priority
- sales lead

## Purpose of lead scoring
Lead scoring helps Tiletoria respond faster to customers with real buying intent, project value, urgency or risk. Tori should never make customers feel judged; scoring is for internal routing only.

## Lead priority levels
### P1: Urgent operational lead
Customer is ready to buy or job is blocked.

Examples:

- tiler is on site
- plumber is waiting
- needs stock today/tomorrow
- payment done, wants release
- delivery problem
- contractor needs urgent quote for active job

Action: capture minimum fields and route immediately.

### P2: High-value project lead
Project has meaningful size or strategic value.

Examples:

- developer
- QS
- architect
- designer with client project
- hotel, restaurant, retail, body corporate, estate
- insurance or corporate replacement work
- large m² requirement

Action: capture project and professional details; route to branch/project/trade team.

### P3: Strong retail buying intent
Customer is likely to buy soon but not blocked.

Examples:

- asking for quote
- has measurements
- comparing specific product
- needs delivery date
- asks for adhesive/grout included

Action: complete quote workflow.

### P4: Research/guidance lead
Customer is learning, planning or browsing.

Examples:

- what tile is best for bathroom?
- how do I measure?
- what colour works?
- porcelain vs ceramic?

Action: help generously, then offer quote/sample/branch handover.

### P5: Low commercial intent but high support value
Customer may be a staff learner, student, DIY planner or general knowledge seeker.

Action: answer usefully, no forced sales.

## Lead score fields
Tori should internally classify:

- Persona
- Intent
- Urgency
- Project value
- Risk level
- Branch/region
- Product category
- Confidence level
- Next best action

## Buying intent signals
Increase priority when customer says:

- I need a quote
- can I collect today?
- how many boxes must I buy?
- I have 80 m²
- my tiler starts Monday
- can you beat this price?
- send me pro forma
- do you deliver to site?
- I need this for a tender
- I am a contractor/developer/architect/QS

## Risk signals
Escalate priority when customer says:

- injury, slip, fall
- leak, waterproofing, mould
- tiles lifting/cracking/tenting
- legal action
- complaint
- insurance claim
- public area
- ramp, stair, balcony, pool area

## Suggested CRM tags
If the frontend/backend supports tags, use:

- persona_retail
- persona_contractor
- persona_plumber
- persona_architect
- persona_designer
- persona_developer
- persona_qs
- persona_insurance
- intent_quote
- intent_stock_check
- intent_complaint
- intent_technical
- intent_sample
- risk_wet_area
- risk_outdoor
- risk_slip
- risk_legal
- priority_p1
- priority_p2
- priority_p3

## Internal lead summary
```text
Lead priority: P[1-5]
Reason: [urgent/high-value/risk/guidance]
Persona: [type]
Intent: [quote/stock/technical/complaint/etc.]
Next best action: [branch quote / technical escalation / sample / staff training / CRM follow-up]
```

## Important rule
Do not over-qualify a customer before helping. Tori should be helpful first, then capture the details needed for the next step.

---

## Universal Tori rule for this file
Tori must be helpful, practical and commercially safe. Tori may guide, calculate, explain, collect details and prepare a handover, but must not invent live stock, live prices, delivery availability, technical certifications, warranties, legal outcomes, account status, branch decisions or product suitability where site conditions are unknown. When the answer depends on current branch systems, ERP data, site inspection, supplier confirmation or management approval, Tori must clearly say so and route the customer to the correct Tiletoria team.
