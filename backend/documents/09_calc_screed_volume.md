---
title: "Screed and Repair Volume Calculator"
document_type: "calculator"
calculator_id: "CALC_SCREED_VOLUME"
priority: 95
retrieval_aliases:
  - screed volume
  - cubic metres of screed
  - litres of screed
  - screed thickness
  - falls
  - ramp screed
  - sand cement quantity
last_reviewed: "2026-07-08"
---

# Screed and Repair Volume Calculator

## Required Inputs

Ask for:

- area in m²
- minimum and maximum thickness, or verified average thickness, in mm
- whether the thickness is uniform
- wastage percentage; default 10%
- specified mix or proprietary product, if material quantities are required

## Uniform Thickness Formula

`volume_m3 = area_m2 × thickness_mm ÷ 1000`

`volume_with_allowance_m3 = volume_m3 × 1.10`

`volume_litres = volume_m3 × 1000`

## Linear Fall Formula

Where the screed changes reasonably evenly from a minimum to a maximum:

`average_thickness_mm = (minimum_mm + maximum_mm) ÷ 2`

Then use the uniform-thickness formula with the average.

## Worked Example

Inputs:

- area: 25 m²
- uniform thickness: 40 mm
- wastage: 10%

Calculation:

- volume = 25 × 40 ÷ 1000 = 1.00 m³
- with allowance = 1.00 × 1.10 = 1.10 m³

Answer:

> “The planning volume is **1.10 m³**, including 10% allowance.”

## Important Limitation

Do not convert screed volume into cement and sand quantities unless the mix design, material densities, moisture condition, batching method and specified yield are known.

A nominal mix ratio alone is not enough for a guaranteed material order.

## Irregular Floors

For irregular floors:

1. measure a grid of levels
2. estimate average thickness for each zone
3. calculate each zone separately
4. add the zone volumes
5. add 10%

## Contractor Warnings

- Confirm bonded, unbonded or floating screed design.
- Confirm minimum thickness for the specified system.
- Falls to drains must be designed and checked on site.
- Screed must not bridge structural movement joints.
- Cracks, deflection and moisture require assessment before covering.
- Proprietary repair products have their own thickness and yield limits.
