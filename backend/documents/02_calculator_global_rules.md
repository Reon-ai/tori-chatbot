---
title: "Global Rules for All Tori Calculators"
document_type: "calculator_policy"
priority: 95
market: "South Africa"
units: "metric"
default_waste_percent: 10
last_reviewed: "2026-07-08"
---

# Global Rules for All Tori Calculators

## Unit Rules

Use:

- length: millimetres or metres
- area: square metres, m²
- volume: litres or cubic metres, m³
- mass: kilograms, kg
- linear products: running metres, lm
- prices: South African rand only when the user supplies a price or a verified live price source exists

Conversions:

- millimetres to metres: divide by 1,000
- centimetres to metres: divide by 100
- square millimetres to square metres: divide by 1,000,000
- litres to cubic metres: divide by 1,000
- 1 m³ = 1,000 litres

## Wastage Rule

Default wastage for planning is **10%**.

Formula:

`quantity_with_waste = net_quantity × 1.10`

Do not silently change the wastage. If the user or approved project specification requires another percentage, repeat it before calculating.

## Rounding Rule

Always round **up** to the next purchasable unit.

- tiles and LVT: full boxes or packs
- adhesive, grout, screed and self-leveller: full bags
- primer: full containers
- waterproofing: full kits or buckets
- trims and movement profiles: full lengths
- membrane: full rolls
- silicone or sealant: full cartridges
- spacers, clips and wedges: full packs

Mathematical rule:

`buying_units = ceiling(required_quantity ÷ pack_quantity)`

Never round down.

## Truth Labels

Tori must separate:

- **Known input:** supplied by the user or verified product data
- **Calculated result:** arithmetic from known inputs
- **Planning assumption:** such as 10% wastage
- **Unknown:** stock, price, exact site consumption, product suitability, or pack coverage not supplied

## Product-Coverage Rule

Exact coverage must come from:

1. current product packaging
2. current manufacturer technical data sheet
3. verified product data in `18_verified_product_constants.md`

Do not invent coverage from tile size alone.

## Calculation Response Template

> **Result:** [rounded buying quantity]  
> **Inputs:** [repeat measurements and product data]  
> **Calculation:** [show concise formula]  
> **Allowance:** 10% wastage  
> **Important:** [one relevant site or product warning]  
> **Confirm:** [unknown product, stock, batch, price, or technical detail]

## Missing Input Rule

Ask for the smallest number of missing inputs.

Example for adhesive:

> “What adhesive are you using, what is its stated coverage per bag, and is the substrate smooth or being levelled first?”

## No False Precision

Do not show more than:

- two decimal places for areas and litres
- one decimal place for kilograms before pack rounding
- whole numbers for boxes, bags, kits, rolls, lengths, cartridges, and packs

## Safety and Escalation

Do not finalise system design for:

- structural cracks
- suspended slabs with movement or deflection
- pools
- balconies and exposed decks
- ramps and public wet areas
- unusual substrates
- heavy stone or large-format wall cladding
- active moisture or water ingress

Give the planning quantity, identify the limitation, and request technical confirmation.
