# RAG Chunking and Style Guide for Future Tori Files

**Version:** 2026-06-18  
**Market:** South Africa / Southern Africa  
**Business:** Tiletoria customer and staff RAG knowledge base  

## Purpose
Give Tiletoria a repeatable standard for creating future Markdown knowledge files that ingest well.

## Retrieval triggers
- RAG
- chunking
- markdown
- knowledge base
- new file
- format
- ingestion
- GitHub

## File size principle
Create many focused Markdown files rather than one giant file. Each file should answer one theme.

## Ideal structure
Use this structure:

```markdown
# Main Topic

## Purpose
What this file helps Tori answer.

## Retrieval triggers
Words and phrases customers use.

## Key rules
The must-follow logic.

## Questions to ask
Fields Tori should capture.

## Safe response templates
Reusable wording.

## Escalation rules
When to hand over.
```

## Chunk size
Aim for sections that are 300 to 900 words. Avoid huge tables unless the retrieval system handles tables well.

## Write in customer language
Include the words customers actually use:
- "How many boxes?"
- "Can I use this outside?"
- "My tiles are lifting."
- "I need a quote."
- "Do you deliver?"
- "Can I tile over tiles?"

## Include professional language too
Also include terms professionals use:
- substrate
- movement joints
- waterproofing membrane
- adhesive coverage
- BOQ
- specification
- slip resistance
- batch/shade/calibre

## Avoid in RAG files
- Long legal clauses without plain-English summaries.
- Unverified live prices.
- Old promotions.
- Supplier-specific claims without datasheets.
- Conflicting advice.

## Update discipline
When adding product-specific files, include:
- Product name/code.
- Size.
- Finish.
- Indoor/outdoor/wet suitability if verified.
- Box m².
- Branch availability only if connected to live source.
- Datasheet date if available.

## Retrieval test
After adding a file, test with customer-style questions and professional-style questions.

---

## Universal Tori rule for this file
Tori must be helpful, practical and commercially safe. Tori may guide, calculate and explain, but must not invent live stock, live prices, delivery availability, technical certifications, warranties, legal outcomes or product suitability where site conditions are unknown. When the question depends on site inspection, current branch stock, quoted pricing, account status or formal compliance, Tori must capture the correct details and route to the correct Tiletoria team.
