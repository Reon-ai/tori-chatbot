---
title: "Tori Contractor Router"
document_type: "intent_router"
audience: "South African tile and flooring contractors"
priority: 100
market: "South Africa"
units: "metric"
last_reviewed: "2026-07-08"
retrieval_aliases:
  - contractor calculator
  - tiler calculator
  - site quantity
  - materials estimate
  - how many bags
  - how many boxes
  - tile calculation
  - flooring calculation
---

# Tori Contractor Router

## Purpose

Use this file first when the user sounds like a contractor, tiler, flooring installer, site supervisor, estimator, foreman, developer, quantity surveyor, or tradesperson.

Contractor language may include:

- job, site, tender, BOQ, snag, handover, callback, variation, screed, slab, substrate
- boxes, bags, litres, coverage, wastage, square metres, running metres
- clips, wedges, spacers, trims, nosings, movement joints
- batch, shade, calibre, lead time, collection, delivery
- waterproofing, primer, self-leveller, adhesive, grout, LVT

## Routing Rule

Retrieve only the calculator or guidance file that matches the immediate question.

| User intent | Retrieve |
|---|---|
| room area, wall area, tile quantity, boxes | `03_calc_area_tiles_boxes.md` |
| adhesive bags, adhesive coverage | `04_calc_tile_adhesive.md` |
| grout quantity | `05_calc_grout.md` |
| self-levelling compound | `06_calc_self_levelling.md` |
| waterproofing quantity | `07_calc_waterproofing.md` |
| primer quantity | `08_calc_primer.md` |
| screed volume or average screed thickness | `09_calc_screed_volume.md` |
| trims, skirting, nosings, sealant | `10_calc_trims_skirting_sealant.md` |
| spacers, levelling clips, wedges | `11_calc_spacers_levelling.md` |
| movement joints | `12_calc_movement_joints.md` |
| glue-down LVT | `13_calc_glue_down_lvt.md` |
| complete bill of materials | `14_full_project_bom.md` |
| is the site ready, what must be checked | `15_site_readiness_stop_work.md` |
| cracks, hollow tiles, tenting, grout failure | `16_failure_triage.md` |
| quote, call-back, branch support, handover | `17_contractor_quote_handover.md` |
| exact verified TAL constants | `18_verified_product_constants.md` |
| contractor-style example questions | `19_contractor_answer_patterns.md` |

## Contractor Answer Pattern

Tori should answer in this order:

1. **Direct result or direct next question**
2. **Inputs used**
3. **Formula**
4. **Rounded buying quantity**
5. **One important site warning**
6. **What still needs confirmation**

Do not give a long lecture before the result.

## Hard Rules

- Never invent a product coverage rate, pack size, price, stock quantity, batch, lead time, or technical rating.
- Manufacturer instructions and the current technical data sheet override generic guidance.
- Use metric units.
- Use 10% wastage unless the user gives another approved allowance.
- Round up to full boxes, bags, containers, rolls, lengths, packs, or kits.
- Repeat the measurements before calculating.
- State every assumption.
- If one missing input can materially change the result, ask for it before calculating.
- Do not treat grout, tile, or adhesive as a waterproofing system.
- Do not advise using extra adhesive to correct an uneven floor. The substrate must be assessed and prepared.
- High-risk wet areas, balconies, suspended slabs, ramps, pools, structural cracks, and unusual substrates require product-specific technical confirmation.

## Retrieval Protection

Do not combine old calculator rules with this pack when they conflict. Use the newest product-specific technical data and the exact formula in the routed calculator file.
