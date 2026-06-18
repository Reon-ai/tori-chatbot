# Failed Answer Logging Categories

**Version:** 2026-06-18  
**Market:** South Africa / Southern Africa  
**Business:** Tiletoria / Tori RAG brain  
**Layer:** Phase 3 Control Layer  

## Purpose
Provide categories for tagging and analysing Tori failures so the team can fix root causes rather than only individual answers.

## Retrieval triggers
- failed answer
- logging
- analytics
- wrong answer
- no answer
- hallucination
- bad retrieval
- bot failure
- quality tag

## Purpose
Every failed answer should be categorised. The category tells Tiletoria whether the fix is content, retrieval, frontend, integration, training or policy.

## Failure category list
### F01 Missing knowledge
The answer is not in the Markdown brain.

Fix: create/update file.

### F02 Outdated knowledge
The answer exists but is old or conflicts with current business rules.

Fix: update source and remove old content.

### F03 Retrieval miss
Knowledge exists but Tori did not find it.

Fix: improve headings, triggers, synonyms, chunking and metadata.

### F04 Ambiguous customer wording
Customer phrasing was unclear or misspelled.

Fix: add synonym/misspelling mapping.

### F05 Hallucination risk
Tori guessed stock, price, suitability, policy, warranty or legal outcome.

Fix: strengthen boundary rules and system prompt.

### F06 Live-data needed
Question required ERP/API/live data.

Fix: route to live lookup or branch handover.

### F07 Form flow failure
Tori needed structured fields but the frontend did not trigger the right form.

Fix: adjust frontend trigger logic.

### F08 Escalation failure
Tori should have escalated but continued answering.

Fix: improve red-flag engine.

### F09 Tone failure
Answer was technically correct but too cold, too vague, too salesy or too legalistic.

Fix: update response templates.

### F10 Persona mismatch
Tori answered a contractor like a homeowner, or an architect like a retail customer.

Fix: improve persona routing.

### F11 Calculation failure
Tori misunderstood m², boxes, waste, grout, adhesive or unit conversion.

Fix: calculator logic and examples.

### F12 Policy approval needed
The answer depends on a Tiletoria management decision.

Fix: add to approval list.

## Failure log template
```text
Failure ID:
Date/time:
Customer question:
Tori answer:
Expected answer:
Category code:
Persona:
Intent:
Product/category:
Branch/region:
Risk level:
Root cause:
Fix required:
Owner:
Status:
```

## Priority rules
Fix first:

1. safety/legal/public liability risks
2. stock/price hallucinations
3. quote form failures causing lost sales
4. complaint escalation failures
5. high-volume repeated questions
6. staff training errors

## Weekly summary metrics
Track:

- total failed answers
- failures by category
- repeat failures
- time to fix
- number of new/updated Markdown files
- top missing topics
- top frontend issues

---

## Universal Tori rule for this file
Tori must be helpful, practical and commercially safe. Tori may guide, calculate, explain, collect details and prepare a handover, but must not invent live stock, live prices, delivery availability, technical certifications, warranties, legal outcomes, account status, branch decisions or product suitability where site conditions are unknown. When the answer depends on current branch systems, ERP data, site inspection, supplier confirmation or management approval, Tori must clearly say so and route the customer to the correct Tiletoria team.
