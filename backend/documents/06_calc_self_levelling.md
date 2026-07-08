---
title: "Self-Levelling Compound Calculator"
document_type: "calculator"
calculator_id: "CALC_SELF_LEVELLING"
priority: 100
retrieval_aliases:
  - self leveller
  - self leveling
  - floor levelling
  - screedmaster
  - bags per millimetre
  - uneven floor
  - average thickness
last_reviewed: "2026-07-08"
---

# Self-Levelling Compound Calculator

## Required Inputs

Ask for:

1. floor area in m²
2. average application thickness in mm
3. exact product consumption in kg/m²/mm
4. bag size
5. permitted product thickness range
6. primer system

## Formula

`required_kg = area_m2 × average_thickness_mm × consumption_kg_per_m2_per_mm × 1.10`

`bags = ceiling(required_kg ÷ bag_size_kg)`

## Verified TAL Screedmaster Constants

- approximate consumption: 1.8 kg/m²/mm
- bag size: 22 kg
- application thickness: 3–16 mm

These constants are product-specific and may change. The current packaging and technical data sheet override this file.

## Worked Example

Inputs:

- area: 40 m²
- average thickness: 4 mm
- consumption: 1.8 kg/m²/mm
- bag size: 22 kg
- wastage: 10%

Calculation:

- base mass = 40 × 4 × 1.8 = 288 kg
- with allowance = 288 × 1.10 = 316.8 kg
- bags = ceiling(316.8 ÷ 22) = 15 bags

Answer:

> “You need **15 × 22 kg bags** at a true average thickness of 4 mm.”

## Average Thickness Is Critical

Do not use the deepest point for the entire floor.

For a simple floor plane with a roughly linear change:

`average_thickness = (minimum_thickness + maximum_thickness) ÷ 2`

A level survey or grid of measurements gives a better average for irregular floors.

## Example of a Sloping Plane

- minimum: 3 mm
- maximum: 9 mm
- average: (3 + 9) ÷ 2 = 6 mm

Use 6 mm only when the slope is reasonably uniform.

## Contractor Warnings

- Confirm the product's minimum and maximum application thickness.
- Very deep areas may require repair mortar, screed, aggregate extension, or multiple stages according to the product system.
- Prime with the correct system for porous or dense substrates.
- Remove contamination and weak material.
- Seal gaps and penetrations before pouring.
- Do not calculate from room area alone; thickness drives the quantity.
- Follow the stated water ratio. Extra water can damage performance.
