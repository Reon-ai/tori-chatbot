# Phase 3 Control Layer README

**Version:** 2026-06-18  
**Market:** South Africa / Southern Africa  
**Business:** Tiletoria / Tori RAG brain  
**File range:** 71 to 100  

## Purpose
This pack completes the Tori knowledge base with the operating control layer. The earlier files teach Tori what to know. These files teach Tori when to answer, when to ask for details, when to hand over, when to stop, and how Tiletoria should improve the bot over time.

## Why this layer matters
A customer support chatbot becomes risky when it sounds confident about things it cannot verify. Tori must not behave like a live ERP, legal adviser, engineer, waterproofing inspector or complaints manager unless the correct system and authorised team have confirmed the facts.

This layer makes Tori commercially useful and risk-aware by adding:

- live-data boundaries
- stock and price handover rules
- ERP/K8 escalation logic
- quote-to-branch SOPs
- lead scoring
- POPIA-safe contact handling
- product datasheet and specification handling
- image/photo diagnostic workflows
- staff learning paths and quizzes
- South African customer language mapping
- red-flag escalation
- legal/technical/safety boundaries
- weekly and monthly RAG quality improvement loops
- gold-standard response examples

## Recommended ingestion order
Load these files after the original brain files 01 to 70.

Preferred folder:

```text
/backend/knowledge/tori_brain/phase_3_control_layer/
```

If your backend loads all Markdown files from one folder, you may place these files in the same knowledge folder as the first 70 files. The numbering is intentional so the theme sequence remains clear.

## RAG style used
Each file is deliberately focused around one operational theme. The headings are designed to create useful retrieval chunks. Customer phrasing and professional terminology are both included so Tori can match messy retail questions and trade/specifier questions.

## What this pack does not replace
This pack does not replace:

- live stock data
- live price data
- ERP/K8 information
- supplier datasheets
- formal warranties
- signed policy documents
- legal advice
- engineering inspections
- waterproofing inspections
- professional tiler/plumber responsibility
- branch management decisions

## Highest priority behaviour
When Tori is uncertain, she must still be useful. The correct pattern is:

1. Acknowledge the customer need.
2. Explain the general principle.
3. Ask only for the missing details that matter.
4. Give a safe next step.
5. Route to the correct Tiletoria branch/team where live confirmation is required.

## Example of correct control-layer behaviour
Customer: Do you have 80 m² of this tile in Cape Town and what is the price?

Tori should answer:

> I can help with that. I cannot confirm live stock or final pricing from the knowledge base alone, because stock and price can change by branch and batch. Please share the tile name/code if you have it, the m² required, whether you need adhesive/grout/trims included, and your preferred branch. I will prepare the request for the Cape Town team to confirm availability, batch and price.

## Management note
After this phase, the next important discussion is frontend and backend behaviour: form triggers, live ERP lookup, CRM/lead routing, upload handling, escalation queues, staff mode, analytics and QA reporting.
