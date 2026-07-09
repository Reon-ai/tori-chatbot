---
title: Tori Knowledge Base Master Index
category: Governance
customer_types: [All]
intent: navigation
related_products: []
standards_or_references: []
source_keys: [openai_vector_stores]
risk_level: low
market: South Africa
last_reviewed: 2026-07-09
owner: Tiletoria Knowledge Base
---

# Tori Knowledge Base Master Index

This knowledge base is designed for Tiletoria's RAG chatbot in South Africa. It is split into focused Markdown files so retrieval can find the right small answer quickly.

## Folder map

- `00-start-here`: bot behaviour, safety, escalation, persona routing and knowledge rules.
- `01-personas`: guidance by customer type: contractor, homeowner, architect/designer, insurer, internal consultant and developer.
- `02-tiles`: porcelain, ceramic, decorative tiles, mosaics, formats, finishes and selection.
- `03-installation-systems`: adhesives, grouts, primers, waterproofing, self-levelling, spacers, clips, trims and site failures.
- `04-flooring`: laminate, LVT, SPC/rigid vinyl, floor preparation and maintenance.
- `05-bathroom-sanitaryware`: baths, basins, toilets, taps, showers, wastes, traps, accessories and plumbing-safe boundaries.
- `06-calculators`: deterministic calculation rules and example answer formats.
- `07-sales-service`: showroom, quotations, stock, samples, complaints, warranties and handover.
- `08-project-specification`: architect, developer, body corporate, insurance and commercial project guidance.
- `09-trend-design`: design guidance and South African trend language.
- `10-quality-tests`: regression tests to check whether Tori answers safely and usefully.

## Retrieval rules

Tori should use the most specific file first.

- Use adhesive calculator files for quantities.
- Use waterproofing files for showers, balconies and wet rooms.
- Use live ERP/API tools for price, stock, batch, shade and lead time.
- Use escalation rules when the customer asks for warranty, formal sign-off, failed installations or compliance.

## Non-negotiable rule

Tori must never invent stock, prices, batch/shade availability, formal specifications, warranties, compliance certificates or product approvals.
