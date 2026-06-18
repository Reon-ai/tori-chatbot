# Monthly RAG Quality Scorecard

**Version:** 2026-06-18  
**Market:** South Africa / Southern Africa  
**Business:** Tiletoria / Tori RAG brain  
**Layer:** Phase 3 Control Layer  

## Purpose
Provide a monthly scorecard for measuring whether Tori is becoming more accurate, useful, safe and commercially valuable.

## Retrieval triggers
- scorecard
- monthly review
- RAG quality
- bot performance
- metrics
- KPI
- accuracy
- faithfulness
- customer satisfaction
- conversion

## Purpose
Tori should be measured like a business system, not judged by vibes. The scorecard should show quality, risk, sales support and staff learning value.

## Monthly scorecard sections
### 1. Answer quality
Measure:

- answer helpfulness
- factual accuracy
- faithfulness to retrieved knowledge
- clarity
- customer tone
- persona fit

Suggested target: 90 percent plus on reviewed sample answers.

### 2. Retrieval quality
Measure:

- correct file retrieved
- correct chunk retrieved
- no irrelevant/conflicting chunks
- missing synonyms identified

Suggested target: high retrieval accuracy for top 100 customer questions.

### 3. Hallucination control
Measure:

- stock/price guesses
- legal/warranty guesses
- technical overclaims
- unsupported product suitability claims

Target: zero high-risk hallucinations.

### 4. Lead capture performance
Measure:

- quote form trigger rate
- completed quote requests
- abandoned quote requests
- handover completeness
- branch response success

### 5. Escalation performance
Measure:

- red flags detected
- complaints routed correctly
- safety/legal issues escalated
- false escalations
- missed escalations

### 6. Customer experience
Measure:

- thumbs up/down
- customer comments
- repeated questions in same chat
- frustration signals
- handover satisfaction

### 7. Staff learning usage
Measure:

- staff training prompts
- quiz completions
- common staff questions
- reduced repeated mistakes

### 8. Knowledge maintenance
Measure:

- new files added
- files updated
- outdated files removed
- failed answer fixes completed
- approval backlog

## Monthly scorecard template
```text
Month:
Total chats:
Quote leads captured:
Completed quote forms:
Abandoned quote forms:
Top 10 intents:
Top 10 failed questions:
High-risk hallucinations:
Missed escalations:
New knowledge files added:
Files updated:
Frontend fixes needed:
API/live-data fixes needed:
Staff training insights:
Overall Tori score: /100
```

## Suggested scoring
- Answer quality: 25
- Retrieval quality: 20
- Hallucination control: 20
- Lead capture: 15
- Escalation safety: 10
- Staff learning value: 5
- Knowledge maintenance: 5

## Management review questions
Ask monthly:

- What are customers asking that Tori cannot answer?
- Where is Tori costing us sales?
- Where is Tori protecting us from risk?
- Which branch is getting poor handovers?
- Which products need better datasheets?
- What frontend change would improve conversion most?
- What live data integration is now worth building?

---

## Universal Tori rule for this file
Tori must be helpful, practical and commercially safe. Tori may guide, calculate, explain, collect details and prepare a handover, but must not invent live stock, live prices, delivery availability, technical certifications, warranties, legal outcomes, account status, branch decisions or product suitability where site conditions are unknown. When the answer depends on current branch systems, ERP data, site inspection, supplier confirmation or management approval, Tori must clearly say so and route the customer to the correct Tiletoria team.
