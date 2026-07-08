---
title: "Spacers, Levelling Clips and Wedges Calculator"
document_type: "calculator"
calculator_id: "CALC_SPACERS_CLIPS"
priority: 95
retrieval_aliases:
  - how many clips
  - levelling clips
  - leveling clips
  - wedges
  - tile spacers
  - spacer quantity
  - clip spacing
  - clips per tile
last_reviewed: "2026-07-08"
---

# Spacers, Levelling Clips and Wedges Calculator

## Truth First

There is no universal clips-per-tile number.

The result changes with:

- tile dimensions
- room dimensions
- layout and stagger
- clip type
- manufacturer spacing
- number of clips along each edge
- cuts and perimeter conditions
- installer pace and working section

Use the exact levelling-system instructions.

## Simple Grid Input

Ask for:

- room length and width
- tile length and width
- joint direction
- manufacturer-approved clip spacing
- straight grid or staggered layout
- clip pack size
- wedge pack size
- maximum area installed before the clips are broken out

## Simple Rectangular Grid

Approximate tile rows and columns:

`columns = ceiling(room_width ÷ tile_width)`

`rows = ceiling(room_length ÷ tile_length)`

Internal vertical seam count:

`vertical_seams = columns - 1`

Internal horizontal seam count:

`horizontal_seams = rows - 1`

Clips per vertical seam:

`clips_vertical = ceiling(room_length ÷ clip_spacing) + 1`

Clips per horizontal seam:

`clips_horizontal = ceiling(room_width ÷ clip_spacing) + 1`

Total:

`clips = (vertical_seams × clips_vertical) + (horizontal_seams × clips_horizontal)`

Apply 10% and round to full packs.

## Why This Is an Estimate

Cuts, staggered joints, T-junctions, edge support and installer technique alter the count. Herringbone and complex patterns should be planned from the actual layout, not this grid formula.

## Wedges

A wedge is normally reusable; a clip is normally sacrificial.

During setting, every active clip needs a wedge.

Therefore:

- if the whole job is installed before any wedges are released, wedges required = total active clips
- if work is completed in sections, wedges required = maximum clips active in one section
- do not use a fixed clips-to-wedges ratio without the installer pace and section size

## Simple X-Spacer Estimate

For a full rectangular grid:

`grid_intersections = (columns + 1) × (rows + 1)`

Apply 10% and round to full packs.

This is only a planning estimate. T-spacers, horseshoe spacers, perimeter conditions and staggered layouts need a different count.

## Contractor Warning

Levelling clips help control lippage while adhesive cures. They do not flatten a bad substrate and do not replace correct trowelling, adhesive coverage, joint width, movement joints or tile-quality checks.
