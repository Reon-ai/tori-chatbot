---
title: "Tile Movement Joint Planning Calculator"
document_type: "calculator"
calculator_id: "CALC_MOVEMENT_JOINTS"
priority: 100
retrieval_aliases:
  - expansion joints
  - movement joints
  - control joints
  - tile panel size
  - tenting prevention
  - perimeter joint
last_reviewed: "2026-07-08"
---

# Tile Movement Joint Planning Calculator

## Important Scope

This is a planning tool, not final engineering or specification design.

The exact joint spacing, width, sealant and profile must follow the project specification, substrate, exposure, tile system and current manufacturer guidance.

## Verified TAL Interior Guidance

For the TAL large-format interior floor guideline reviewed in December 2024:

- surface-bed applications: movement joints at maximum 5 m centres in both directions
- suspended-slab applications: maximum 3 m centres in both directions
- joints at least 5 mm wide through tile and adhesive layers
- structural, construction and cold joints must be carried through the tile system
- perimeter and interface joints are also required

Do not automatically apply these values to every exterior, heated, industrial, pool or specialist installation.

## Planning Formula for a Rectangular Area

`internal_lines_length_direction = max(0, ceiling(room_length ÷ spacing) - 1)`

`internal_lines_width_direction = max(0, ceiling(room_width ÷ spacing) - 1)`

`internal_joint_length_m = internal_lines_length_direction × room_width + internal_lines_width_direction × room_length`

Measure perimeter and interfaces separately.

## Worked Example

Room:

- length: 12 m
- width: 8 m
- planning spacing: 5 m

Lines:

- along length = ceiling(12 ÷ 5) - 1 = 2
- along width = ceiling(8 ÷ 5) - 1 = 1

Internal joint length:

- 2 × 8 + 1 × 12 = 28 m

Answer:

> “The planning layout requires **2 internal joint lines across the 8 m width and 1 across the 12 m length**, totalling about **28 linear metres** before perimeter and interface joints.”

## Mandatory Questions

Ask:

- surface bed or suspended slab
- interior, exterior, heated or wet
- existing structural or construction joints
- room dimensions
- columns, stairs, door tracks and material changes
- specified maximum panel size
- joint profile or sealant system

## Hard Rules

- Never tile continuously across a structural movement joint.
- Do not fill movement joints with cementitious grout.
- Levelling clips do not replace movement joints.
- Large open areas, dark exterior tiles, heated floors, suspended slabs and sun-exposed areas require technical design confirmation.
