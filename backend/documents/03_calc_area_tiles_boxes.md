---
title: "Area, Tile Quantity and Box Calculator"
document_type: "calculator"
calculator_id: "CALC_TILE_BOXES"
priority: 100
retrieval_aliases:
  - how many tiles
  - how many boxes
  - tile quantity
  - square metres
  - room area
  - wall tile area
  - boxes needed
  - tile wastage
last_reviewed: "2026-07-08"
---

# Area, Tile Quantity and Box Calculator

## Required Inputs

Ask for:

1. length and width of each floor or wall
2. unit used
3. tile size, when tile count is required
4. verified box coverage in m², when box count is required
5. approved wastage percentage; default 10%

## Rectangular Area

`area_m2 = length_m × width_m`

For several rectangles:

`net_area_m2 = area_1 + area_2 + ...`

For an L-shaped room, split it into rectangles and add them.

Do not subtract doors, windows, islands, cupboards, baths, or fixed items unless the user confirms that those surfaces will not be tiled.

## Order Area

`order_area_m2 = net_area_m2 × 1.10`

## Number of Individual Tiles

Convert tile dimensions to metres:

`tile_area_m2 = tile_length_m × tile_width_m`

Then:

`tile_count = ceiling(order_area_m2 ÷ tile_area_m2)`

This count is theoretical. If tiles are sold only by the box, the box calculation controls the purchase.

## Number of Boxes

`boxes = ceiling(order_area_m2 ÷ verified_box_coverage_m2)`

`purchased_area_m2 = boxes × verified_box_coverage_m2`

`expected_surplus_m2 = purchased_area_m2 - net_area_m2`

## Worked Example

Room:

- 4.2 m × 3.6 m
- box coverage: 1.44 m²
- wastage: 10%

Calculation:

- net area = 4.2 × 3.6 = 15.12 m²
- order area = 15.12 × 1.10 = 16.63 m²
- boxes = ceiling(16.63 ÷ 1.44) = 12 boxes
- purchased area = 12 × 1.44 = 17.28 m²
- expected surplus above net area = 17.28 - 15.12 = 2.16 m²

Answer:

> “You need **12 full boxes**, based on 1.44 m² per box and 10% wastage.”

## Walls

For each wall:

`wall_area = wall_length × tiled_height`

Add all walls, then subtract only confirmed untiled openings.

For a shower, do not assume the waterproofing height and tile height are identical. Ask for each separately.

## Stairs

Calculate each surface separately:

- tread area = tread depth × stair width
- riser area = riser height × stair width
- total stair area = number of treads × tread area + number of risers × riser area

Add landings separately.

## Contractor Warnings

- Use the actual box coverage printed for the exact product.
- Check shade, batch and calibre before installation.
- Do not mix boxes blindly; dry-lay or blend according to product guidance.
- Complex patterns can create more cutting waste, but do not change the default 10% without telling the user.
- Consider keeping spare tiles from the same batch for future repairs; do not add an extra box automatically unless requested.

## Safe Answer When Box Coverage Is Missing

> “Your net area is **X m²** and the 10% order area is **Y m²**. I need the exact m² per box from the product label to convert that into a reliable box count.”
