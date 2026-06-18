# Addon README — 95 Percent Coverage Map

**Version:** 2026-06-18  
**Market:** South Africa / Southern Africa  
**Business:** Tiletoria customer and staff RAG knowledge base  

## Purpose
Explain what this add-on pack adds to the first Tori brain pack and how to ingest it.

## Retrieval triggers
- readme
- manifest
- coverage
- 95%
- brain pack
- ingestion

## How to use this add-on
Load these Markdown files into the same GitHub knowledge folder as the first Tori brain pack. Do not delete the first pack. This pack expands operational and edge-case coverage.

Recommended folder structure:

```text
/backend/knowledge/tori_brain/
  00_README_INGESTION_MANIFEST.md
  ... first pack files ...
  24_ADDON_README_95_PERCENT_COVERAGE_MAP.md
  ... add-on files ...
```

## What the first pack covered
The first pack established the core operating system: Tori personality, intent routing, persona routing, product basics, calculators, installation preparation, LVT, large-format tiles, wet areas, cleaning, complaints, staff training and starter FAQs.

## What this add-on covers
This add-on closes the main gaps normally seen in a flooring, sanitaryware and renovation business:

- South African and Southern African market language.
- Returns, exchanges, CPA-sensitive behaviour and warranty triage.
- Quote workflows for retail, trade, project, designer, architect, QS and insurer personas.
- Deliveries, collections, lead times, branch routing, stock availability and substitutions.
- Batch, shade, calibre, box, pallet and UOM logic.
- Room-by-room measurement guidance and project budgeting.
- Persona-specific operating playbooks.
- Outdoor, balcony, patio, pool, ramp, commercial, hospitality and body-corporate scenarios.
- Failure diagnostics for lippage, hollow-sounding tiles, cracking, tenting, efflorescence and moisture.
- Response templates, form schemas, escalation rules and RAG QA tests.

## RAG ingestion principles
Keep files as separate Markdown documents. Each document should answer one business theme. The headings are deliberately retrieval-friendly. Do not merge everything into one large file unless the backend cannot ingest folder structures.

## Chunking recommendation
Suggested chunk size: 500 to 900 words with 80 to 150 word overlap. Keep headings in chunks. Preserve file names in metadata if your loader supports metadata.

## Priority order
When documents conflict, use this priority:

1. Live system data: ERP, website, branch stock, branch price, account status.
2. Tiletoria management-approved policy.
3. This RAG brain pack.
4. Manufacturer datasheets and installation instructions.
5. General industry guidance.

## Best-bot behaviour
Tori should be more useful than a brochure. A strong answer normally includes:

1. A direct answer.
2. One or two important warnings.
3. A practical next step.
4. A quote or lead-capture offer when purchase intent is clear.

## Files in this add-on
Files 24 to 60 are the coverage-expansion layer. They are intended to sit next to files 00 to 23 from the first pack.

---

## Universal Tori rule for this file
Tori must be helpful, practical and commercially safe. Tori may guide, calculate and explain, but must not invent live stock, live prices, delivery availability, technical certifications, warranties, legal outcomes or product suitability where site conditions are unknown. When the question depends on site inspection, current branch stock, quoted pricing, account status or formal compliance, Tori must capture the correct details and route to the correct Tiletoria team.
