# Tori Feedback Loop and Weekly Review

**Version:** 2026-06-18  
**Market:** South Africa / Southern Africa  
**Business:** Tiletoria / Tori RAG brain  
**Layer:** Phase 3 Control Layer  

## Purpose
Define a weekly process for improving Tori based on failed answers, missing knowledge, customer friction and staff feedback.

## Retrieval triggers
- feedback loop
- weekly review
- improve Tori
- bot quality
- failed answer
- customer feedback
- staff feedback
- continuous improvement

## Why weekly review matters
A RAG chatbot improves when real questions are reviewed and converted into better knowledge files, routing rules or frontend flows. Tori should not be static.

## Weekly review owner
Tiletoria should assign an owner or small team to review Tori performance weekly. Ideal panel:

- customer service/sales manager
- technical/product expert
- branch representative
- chatbot/backend owner
- marketing/UX owner

## Weekly review inputs
Collect:

- unanswered questions
- low-confidence answers
- hallucination attempts
- customer complaints about the bot
- staff corrections
- repeated questions
- quote form drop-offs
- live-data handover failures
- red-flag escalations
- product knowledge gaps

## Weekly review categories
### Knowledge gap
Tori did not have the information.

Action: add or update Markdown.

### Retrieval failure
The information existed but Tori did not retrieve it.

Action: improve headings, triggers, synonyms, chunking.

### Frontend gap
Tori needed a form, photo upload, branch selector or live lookup.

Action: coding/frontend backlog.

### Policy gap
Tori needed an approved business rule.

Action: management approval.

### Live-data gap
Tori needed ERP/API data.

Action: integration backlog.

### Staff process gap
Customer issue failed because handover route was unclear.

Action: SOP update.

## Weekly meeting agenda
1. Top 10 failed/unclear questions.
2. Top 10 repeated questions.
3. Quote conversion issues.
4. Complaint/risk escalations.
5. Product/data gaps.
6. New Markdown updates required.
7. Frontend/backend fixes required.
8. Owner and due date per action.

## Feedback capture format
```text
Date:
Question/customer phrase:
Tori answer:
Problem category:
Correct answer:
Source of truth:
Action required:
Owner:
Due date:
```

## Staff feedback prompt
Staff can submit:

> Tori got this wrong: [question]. Correct Tiletoria answer should be: [answer]. Source/approval: [person/document].

## Success metric
Tori should become better every week in:

- answer accuracy
- lead capture
- escalation safety
- customer satisfaction
- staff learning usefulness
- reduced repetitive staff questions

---

## Universal Tori rule for this file
Tori must be helpful, practical and commercially safe. Tori may guide, calculate, explain, collect details and prepare a handover, but must not invent live stock, live prices, delivery availability, technical certifications, warranties, legal outcomes, account status, branch decisions or product suitability where site conditions are unknown. When the answer depends on current branch systems, ERP data, site inspection, supplier confirmation or management approval, Tori must clearly say so and route the customer to the correct Tiletoria team.
