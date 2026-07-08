---
title: "Grout Quantity Calculator"
document_type: "calculator"
calculator_id: "CALC_GROUT"
priority: 100
retrieval_aliases:
  - how much grout
  - grout kg per square metre
  - grout bags
  - joint width
  - grout formula
  - grout coverage
last_reviewed: "2026-07-08"
---

# Grout Quantity Calculator

## Required Inputs

Ask for:

- tile length in mm
- tile width in mm
- tile thickness in mm
- joint width in mm
- tiled area in m²
- grout specific gravity, SG, from the product data
- grout pack size

## Formula

`kg_per_m2 = ((L + W) × T × J × SG) ÷ (L × W)`

Where:

- `L` = tile length in mm
- `W` = tile width in mm
- `T` = tile thickness in mm
- `J` = joint width in mm
- `SG` = grout specific gravity

Then:

`total_kg = kg_per_m2 × area_m2 × 1.10`

`packs = ceiling(total_kg ÷ pack_size_kg)`

## Important SG Rule

Do not invent SG.

The verified TAL Industrial Epoxy Grout formula uses `SG = 1.8`. That value must not automatically be applied to another grout.

## Worked Example

Inputs:

- tile: 600 × 600 mm
- thickness: 9 mm
- joint: 3 mm
- area: 50 m²
- SG: 1.8
- pack: 5 kg
- wastage: 10%

Calculation:

- kg/m² = ((600 + 600) × 9 × 3 × 1.8) ÷ (600 × 600)
- kg/m² = 0.162
- total = 0.162 × 50 × 1.10 = 8.91 kg
- packs = ceiling(8.91 ÷ 5) = 2 packs

Answer:

> “You need **2 × 5 kg packs**, based on the stated SG of 1.8 and full-depth 3 mm joints.”

## Formula Limitations

The formula assumes:

- consistent tile size
- consistent joint width
- joint depth approximately equal to tile thickness
- joints are properly cleaned and filled
- normal site wastage

Actual use changes if adhesive remains high in the joint, tile edges are irregular, joints vary, or grout is wasted during cleaning.

## Verified Joint Ranges for Selected TAL Products

- TAL Wall & Floor Grout: 2–8 mm joints
- TAL Quarrygrout: 5–25 mm joints

Do not use these ranges for another brand or product without checking its data sheet.

## Contractor Warnings

- Never butt-joint tiles.
- Confirm that the chosen grout suits the joint width, environment and cleaning exposure.
- Cement grout is not a replacement for movement-joint sealant.
- Waterproofing sits behind the tile system; grout alone does not make a shower watertight.
- Test grout on absorbent, textured or stain-sensitive tiles before full use.
