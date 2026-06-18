# Boxes, UOM, Packaging and Pallet Logic

**Version:** 2026-06-18  
**Market:** South Africa / Southern Africa  
**Business:** Tiletoria customer and staff RAG knowledge base  

## Purpose
Teach Tori how to explain tile quantities, boxes, square metres, eaches, packs and pallet-related questions.

## Retrieval triggers
- box
- boxes
- m2 per box
- 2 tiles per box
- UOM
- pallet
- how many boxes
- coverage
- pack
- each

## Core unit logic
Tiles are normally sold by m² but physically supplied in boxes. Some accessories are sold each, per bag, per length, per kit or per box.

## Tile box calculation
Formula:

```text
Boxes required = ceiling(required m² ÷ m² per box)
Actual supplied m² = boxes required × m² per box
```

## 700 mm x 1400 mm example
One tile area:

```text
0.7 m × 1.4 m = 0.98 m² per tile
```

If there are 2 tiles per box:

```text
0.98 m² × 2 = 1.96 m² per box
```

## 600 mm x 600 mm common example
One tile:

```text
0.6 m × 0.6 m = 0.36 m²
```

If 4 tiles per box:

```text
0.36 m² × 4 = 1.44 m² per box
```

## 600 mm x 1200 mm common example
One tile:

```text
0.6 m × 1.2 m = 0.72 m²
```

If 2 tiles per box:

```text
0.72 m² × 2 = 1.44 m² per box
```

## Rounding rule
Always round boxes up. You cannot usually buy part of a sealed tile box unless branch policy/product allows it.

## Waste allowance reminder
After calculating room area, add waste before converting to boxes.

Typical guidance:
- Simple open floor: 10% waste.
- Complex cuts/diagonal patterns: 12% to 15%.
- Large-format tiles: often 10% to 15%, depending on layout.
- Repair stock: suggest an extra box where practical.

## Product UOM examples
- Tiles: m²/box.
- Mosaics: sheet or m².
- Adhesive: bag/kg.
- Grout: bag/kg.
- Trims: length/each.
- Spacers/clips/wedges: pack/each.
- Toilets/basins/taps: each.
- LVT: m²/box or pack.

## Pallet logic
Tori may explain that large orders may be palletised, but must not invent pallet quantity or weight. Branch must confirm.

## Customer-safe answer
"I can calculate the estimated boxes if you give me the tile size, m² per box and the area to cover. The branch will confirm the final sellable box quantity and stock."

---

## Universal Tori rule for this file
Tori must be helpful, practical and commercially safe. Tori may guide, calculate and explain, but must not invent live stock, live prices, delivery availability, technical certifications, warranties, legal outcomes or product suitability where site conditions are unknown. When the question depends on site inspection, current branch stock, quoted pricing, account status or formal compliance, Tori must capture the correct details and route to the correct Tiletoria team.
