---
title: Tori Calculation Knowledge Base
business: Tiletoria / Spec Lab
purpose: RAG-ready calculator brain for Tori chatbot
market: South Africa
units: metric, m², mm, kg, litres, ZAR
source: Tiletoria_SpecLab_20_SA_Tiling_Calculators.docx
created_for: Tori AI chatbot
---

# Tori Calculation Knowledge Base

This markdown file is optimised for a RAG chatbot. It contains practical South African tiling and flooring calculators, formula references, lookup tables, worked examples, and chatbot response instructions.

## How Tori Must Use This Knowledge Base

- Use this file first when a user asks for a calculation, estimate, quantity, coverage, wastage, labour, cost, or project budget.
- Ask for missing inputs before calculating where the answer depends on dimensions, tile size, pattern, substrate, or product type.
- Use metric units by default: metres, millimetres, square metres, kilograms, litres, and South African Rand.
- Always round material quantities up to full boxes, full bags, full containers, or full lengths.
- For tiles, always include wastage and recommend at least one spare box for future repairs when appropriate.
- For adhesives, grout, waterproofing, screed, self-levelling and primers, remind customers that brand coverage rates vary and manufacturer instructions override generic calculator estimates.
- For bathrooms, showers, balconies, ramps, commercial areas, high-risk wet areas and structural questions, calculate the estimate but recommend confirmation by a Tiletoria consultant or qualified installer.
- Do not invent exact Tiletoria pricing or stock availability. If pricing is requested, explain that the calculation is an estimate and trigger quote/handover.
- For exact stock, branch availability, complaints, product defects, large commercial quantities, or risky technical applications, trigger the popup form or human handover.

## Available Calculators Index

- CALCULATOR 1: FLOOR AREA CALCULATOR
- CALCULATOR 2: TILE QUANTITY CALCULATOR
- CALCULATOR 3: TOTAL PROJECT COST ESTIMATOR
- CALCULATOR 4: TILE ADHESIVE QUANTITY CALCULATOR
- CALCULATOR 5: GROUT QUANTITY CALCULATOR
- CALCULATOR 6: SCREED VOLUME CALCULATOR
- CALCULATOR 7: SELF-LEVELLING COMPOUND CALCULATOR
- CALCULATOR 8: WATERPROOFING CALCULATOR
- CALCULATOR 9: PATTERN LAYOUT WASTAGE CALCULATOR
- CALCULATOR 10: LABOUR COST ESTIMATOR
- CALCULATOR 11: STAIR TILING CALCULATOR
- CALCULATOR 12: SKIRTING AND TRIM LENGTH CALCULATOR
- CALCULATOR 13: UNDERFLOOR HEATING AREA CALCULATOR
- CALCULATOR 14: MOVEMENT JOINT SPACING CALCULATOR
- CALCULATOR 15: STRUCTURAL LOAD CALCULATOR
- CALCULATOR 16: FLOOR REMOVAL AND DISPOSAL COST CALCULATOR
- CALCULATOR 17: PRIMER AND PREPARATION CALCULATOR
- CALCULATOR 18: LVT AND LAMINATE PLANK QUANTITY CALCULATOR
- CALCULATOR 19: DECORATIVE FEATURE AND MOSAIC CALCULATOR
- CALCULATOR 20: COMPLETE PROJECT BUDGET CALCULATOR

## Quick Intent Mapping for Tori

| Customer asks... | Use calculator |
|---|---|
| How many square metres is my room? | Calculator 1: Floor Area Calculator |
| How many tiles or boxes do I need? | Calculator 2: Tile Quantity Calculator |
| What will my whole project cost? | Calculator 3 or 20 |
| How many bags of adhesive? | Calculator 4 |
| How much grout? | Calculator 5 |
| How much screed, cement and sand? | Calculator 6 |
| How many bags of self-levelling compound? | Calculator 7 |
| How much waterproofing? | Calculator 8 |
| How much wastage for herringbone / diagonal? | Calculator 9 |
| What will labour cost? | Calculator 10 |
| How many stair tiles? | Calculator 11 |
| How much trim or skirting? | Calculator 12 |
| How much underfloor heating? | Calculator 13 |
| Do I need movement joints? | Calculator 14 |
| Is the floor load too heavy? | Calculator 15 |
| What will tile removal and disposal cost? | Calculator 16 |
| How much primer and prep material? | Calculator 17 |
| How much LVT or laminate? | Calculator 18 |
| How much mosaic or feature tile? | Calculator 19 |
| Full budget with all components | Calculator 20 |

## Standard Tori Calculation Response Pattern

When answering a calculation question, use this structure:

1. Confirm the inputs used.
2. Show the calculation in simple steps.
3. Round up to practical buying units.
4. Add relevant wastage, safety buffer or spare allowance.
5. Mention any technical caution.
6. Give a next step: showroom, quote, consultant, branch stock check, or popup form where appropriate.

Example closing line:

> “This is a strong estimate for planning. For final buying, we at Tiletoria should confirm the exact product, box coverage, batch and stock before you place the order.”

---


20 Professional Estimation Tools for the SA Construction Market


## Document Overview

Document Version: 1.0 Date: June 2025 Target Market: South Africa (ZAR pricing, metric units) Standards Referenced: SANS 10109, SANS 10400, SANS 10107, SANS 1449, BS 5385 Intended Users: Homeowners, contractors, quantity surveyors, AI chatbots

How to Use This Document

Each calculator in this document is self-contained and follows a consistent structure:

| Section | Purpose |
| --- | --- |
| Name & Purpose | What the calculator does and who needs it |
| Formula | The mathematical equations (dimensionally consistent) |
| Lookup Tables | Quick-reference data for common scenarios |
| Step-by-Step Method | Numbered instructions anyone can follow |
| Worked Example | Realistic SA scenario with actual numbers |
| SANS / Regulatory Reference | Applicable South African standards |
| Chatbot Instruction Notes | How an AI should guide customers through this calculation |

Units Used Throughout This Document

| Quantity | Unit | Symbol |
| --- | --- | --- |
| Length | Millimetres / Metres | mm / m |
| Area | Square metres | m² |
| Volume | Cubic metres / Litres | m³ / L |
| Mass | Kilograms | kg |
| Time | Days | d |
| Temperature | Degrees Celsius | °C |
| Currency | South African Rand | R / ZAR |
| Power | Watts per square metre | W/m² |

Quick Conversion Reference

| From | To | Multiply By |
| --- | --- | --- |
| Millimetres (mm) | Metres (m) | 0.001 |
| Centimetres (cm) | Metres (m) | 0.01 |
| Square centimetres (cm²) | Square metres (m²) | 0.0001 |
| Litres (L) | Cubic metres (m³) | 0.001 |
| Kilograms (kg) | Tonnes (t) | 0.001 |


## Master Reference Tables


### Table A: Adhesive Coverage Rates (per m²)

| Tile Size | Trowel Notch | Coverage | Notes |
| --- | --- | --- | --- |
| Small wall (<=200x200mm) | 6mm | 3-4 kg/m² | Standard thinset |
| Medium wall/floor (200-400mm) | 8mm | 4-5 kg/m² | Common for floors |
| Large floor (400-600mm) | 10mm | 5-7 kg/m² | Needs thicker bed |
| Extra-large / textured (600-1200mm) | 12mm | 7-10 kg/m² | Full bed + back-butter |
| Mosaics on mesh | 4-6mm | 2-3 kg/m² | Light application |

Bag Coverage (20kg bag): - Standard tiles: ~5-6.5 m² per bag - Large format tiles: ~3-4 m² per bag

Adjustments: - Uneven surface: add 15-25% to standard coverage - Back-buttering large format: add 40-60% to standard coverage - Coverage formula: 1.2 kg/m² per mm of adhesive thickness after compression


### Table B: Grout Coverage Reference

Formula: Grout (kg/m²) = (Tile Length + Tile Width) / (Tile Length x Tile Width) x Joint Width x Joint Depth x SG

Where SG = Specific Gravity: - Cement grout: ~1.5 kg/L - Epoxy grout: ~1.6 kg/L

Typical range: 0.2-0.8 kg/m² depending on tile size and joint width 5kg bag coverage: ~10-25 m² depending on format


### Table C: Wastage Percentages (SANS 10109 / BS 5385 Aligned)

| Pattern | Wastage % | Notes |
| --- | --- | --- |
| Straight / stack bond | 10% | Standard baseline |
| Brick bond (50% offset) | 12% | More cuts, some reusable offcuts |
| Diagonal (45 degrees) | 15-18% | Triangular cuts, limited reuse |
| Herringbone | 18-22% | Complex angles, minimal offcut reuse |
| Chevron | 18-22% | Similar to herringbone |
| Versailles / modular | 15% | Multiple sizes in pattern |

Complication Additions: | Complication | Additional Wastage | |————-|——————-| | L-shaped room | +3% | | Pillars / pipes | +2% | | Many cuts required | +3% |


### Table D: Self-Levelling Compound Data

Coverage: 1.6 kg/m² per mm of thickness (standard)

25kg bag coverage:

At 1mm: ~15.6 m²

At 2mm: ~7.8 m²

At 3mm: ~5.2 m²

Primer: 0.2-0.3 L/m² (depends on substrate porosity)

Min thickness: 1mm (smooth surface), 2mm (prepared concrete)

Max thickness single pour: 10-20mm (product dependent)

Over 20mm: add 30% graded sand (0/4mm)


### Table E: Waterproofing Requirements

Liquid membrane: 1.0-1.5 L/m² per coat

Coats required: 2 minimum

Total: 2.0-3.0 L/m²

Shower floor: 2.5-3.0 L/m² (thicker application)

Sheet membrane: coverage = actual area (minimal overlap waste)

SANS 10400 Part P: wet areas must be waterproofed

Upstand requirement: 150mm minimum on walls

Primer for waterproofing: 0.2-0.4 L/m²


### Table F: Screed Data (SANS 10400-J)

Standard mix: 1 part cement : 3-4 parts sand (by volume)

Bonded screed: min 15mm thickness

Unbonded screed: min 35mm thickness

Floating screed: min 35mm thickness

Volume: Area (m²) x Thickness (m) = m³

1 m³ screed approx 1,800-2,000 kg dry mix

Cement: 350-400 kg per m³

Sand: 1,400-1,600 kg per m³

Water: 80-100 litres per m³

Drying time: 1 day per mm (up to 40mm), then 2 days per mm thereafter

50mm screed: ~50-65 days drying before tiling


### Table G: Labour Rates (South Africa 2025/2026)

| Service | Rate per m² | Notes |
| --- | --- | --- |
| Standard floor tiling | R150-250 | Ceramic/porcelain |
| Wall tiling | R180-300 | Higher precision |
| Large format (>600mm) | R250-400 | Two-person team |
| Mosaic installation | R250-400 | Time-consuming |
| Herringbone/diagonal | +30-50% surcharge | Complex patterns |
| Tiler day rate | R800-1,500 | Plus assistant if needed |
| Tile removal (floor) | R50-150 | Plus disposal |
| Tile removal (wall) | R60-180 | Plus disposal |
| Screeding | R100-200 | Labour + materials |
| Self-levelling | R80-150 | Per m² |
| Waterproofing | R150-300 | Membrane + labour |
| Primer application | R20-40 | Per m² |


### Table H: Tile Weights (Structural Load Calculation)

| Tile Type | Thickness | Weight per m² |
| --- | --- | --- |
| Ceramic wall tile | 6-8mm | 12-16 kg/m² |
| Ceramic floor tile | 9-10mm | 18-22 kg/m² |
| Porcelain tile | 9-11mm | 20-25 kg/m² |
| Large format porcelain | 11-14mm | 25-35 kg/m² |
| Extra-large/slab | 12-20mm | 30-50 kg/m² |
| Mosaic (with mesh) | 4-6mm | 8-12 kg/m² |
| Full adhesive bed (10mm) | - | 18-22 kg/m² |
| Screed (50mm) | - | 100-120 kg/m² |


### Table I: Movement Joint Requirements (SANS 10109 / BS 5385)

| Location | Max Spacing |
| --- | --- |
| Interior floors | 8m in each direction |
| Exterior floors | 3m in each direction |
| Suspended floors | 4.5m in each direction |

Perimeter joints: mandatory around all perimeters

Change in substrate/material junctions: joint required

Joint width: minimum 6mm for joints up to 3m, +2mm per additional metre

Formula: Joint Width (mm) = (Tile Coefficient x Temp Range x Distance) + 2mm safety

Typical tile coefficient of thermal expansion: 4-6 x 10^-6/°C


### Table J: Underfloor Heating Data

| Type | Wattage | Application |
| --- | --- | --- |
| Electric (primary) | 100-150 W/m² | Main heat source |
| Electric (comfort) | 60-80 W/m² | Secondary/comfort heating |
| Hydronic | 80-120 W/m² | Connected to geyser/boiler |

Heated area = Total area - (perimeter 100mm zone + fixed furniture areas)

Typical heated area = 60-85% of total floor area

Flexible adhesive mandatory

Minimum 6mm adhesive bed under tiles on heating

Maximum tile thermal resistance: 0.15 m²K/W


### Table K: Standard SA Tile Box Coverage

| Size | Tiles per Box | Coverage per Box |
| --- | --- | --- |
| 300x300mm | 17 | ~1.53 m² |
| 400x400mm | 10 | ~1.60 m² |
| 500x500mm | 7 | ~1.75 m² |
| 600x600mm | 4 | ~1.44 m² |
| 800x800mm | 3 | ~1.92 m² |
| 1200x600mm | 2 | ~1.44 m² |
| 1200x200mm (wood plank) | 6 | ~1.44 m² |
| 600x300mm | 8 | ~1.44 m² |
| 100x100mm mosaic sheet | 22 sheets | ~1.98 m² |
| 200x100mm subway | 34 | ~0.68 m² |



<!-- RAG_CHUNK: calculator -->

---

## CALCULATOR 1: FLOOR AREA CALCULATOR

**RAG search aliases:** area, m2, square metres, room size, measure room



### 1.1 Name and Purpose

Name: Floor Area Calculator Purpose: Calculates the total floor area of any room shape for tiling purposes, including rectangular rooms, L-shaped rooms, and irregular shapes. Also handles deductions for fixed items (built-in cupboards, island baths, fireplaces).

Who uses it: Homeowners measuring their own spaces, tilers doing initial estimates, quantity surveyors, contractors preparing quotes.


### 1.2 Formula

Basic Rectangle

Area (m²) = Length (m) x Width (m)

L-Shaped Room (Method: Split into two rectangles)

Area = (Length_A x Width_A) + (Length_B x Width_B)

Room with Cut-out (e.g., island bath, cupboard)

Net Area = Total Room Area - Area of Cut-out(s)

Irregular Room (Method: Divide into regular shapes)

Total Area = Sum of all regular shape areas

Right-Angled Triangle (for diagonal layouts or triangular nooks)

Area = 0.5 x Base (m) x Height (m)

Circular Area (for feature medallions, round rooms)

Area = pi x Radius² (m²)


### 1.3 Lookup Tables

Common Room Sizes (South African Homes)

| Room Type | Typical Size | Typical Area |
| --- | --- | --- |
| Small bathroom | 1.5m x 2.0m | 3.0 m² |
| Medium bathroom | 2.0m x 2.5m | 5.0 m² |
| Large bathroom | 2.5m x 3.0m | 7.5 m² |
| Small bedroom | 2.7m x 3.0m | 8.1 m² |
| Standard bedroom | 3.0m x 3.5m | 10.5 m² |
| Main bedroom | 4.0m x 4.5m | 18.0 m² |
| Small kitchen | 2.5m x 3.0m | 7.5 m² |
| Standard kitchen | 3.0m x 4.0m | 12.0 m² |
| Open-plan kitchen/living | 6.0m x 5.0m | 30.0 m² |
| Small lounge | 3.5m x 4.0m | 14.0 m² |
| Standard lounge | 4.5m x 5.0m | 22.5 m² |
| Double garage | 6.0m x 6.0m | 36.0 m² |
| Single garage | 3.0m x 6.0m | 18.0 m² |
| Standard patio | 4.0m x 5.0m | 20.0 m² |
| Entrance hall | 2.0m x 3.0m | 6.0 m² |
| Passage (standard width) | 1.2m x 5.0m | 6.0 m² |

Common Fixed Items to Deduct

| Item | Typical Dimensions | Area to Deduct |
| --- | --- | --- |
| Built-in cupboard (BIC) | 1.2m x 0.6m | 0.72 m² |
| Walk-in shower | 1.2m x 0.9m | 1.08 m² |
| Island bath | 1.8m x 0.8m | 1.44 m² |
| Built-in bath | 1.7m x 0.7m | 1.19 m² |
| Fireplace hearth | 1.5m x 0.5m | 0.75 m² |
| Toilet (WC) base | 0.7m x 0.4m | 0.28 m² |
| Vanity cabinet | 0.9m x 0.5m | 0.45 m² |


### 1.4 Step-by-Step Method

For a Rectangular Room:

Measure the length of the room in metres (wall to wall)

Measure the width of the room in metres (wall to wall)

Multiply length by width to get area in m²

Measure any fixed items (built-in cupboards, baths, etc.)

Calculate the area of each fixed item

Subtract fixed item areas from the total

Round to two decimal places for final tiling area

For an L-Shaped Room:

Draw a rough sketch of the room on paper

Identify where to split the L into two rectangles

Draw the dividing line (imaginary) that creates two clean rectangles

Measure Rectangle A: length and width

Measure Rectangle B: length and width

Calculate Area A = Length A x Width A

Calculate Area B = Length B x Width B

Total Area = Area A + Area B

Subtract any fixed items as above

For an Irregular Room:

Draw a detailed sketch with all measurements

Divide the room into the simplest possible regular shapes (rectangles, triangles)

Calculate the area of each shape

Add all shape areas together

Subtract any fixed items


### 1.5 Worked Example

Scenario: A homeowner in Randburg wants to tile their L-shaped kitchen/dining area.

Measurements: - Rectangle A (kitchen): 3.2m x 2.8m - Rectangle B (dining nook): 2.0m x 1.8m - Built-in kitchen cupboards: 2.4m x 0.6m (do NOT deduct - tiles go under cupboards) - Kitchen island: 1.2m x 0.9m (must deduct - tiles go around island)

Calculation: - Area A = 3.2 x 2.8 = 8.96 m² - Area B = 2.0 x 1.8 = 3.60 m² - Gross Area = 8.96 + 3.60 = 12.56 m² - Island deduction = 1.2 x 0.9 = 1.08 m² - Net Tiling Area = 12.56 - 1.08 = 11.48 m²


### 1.6 SANS / Regulatory Reference

SANS 10109: Code of Practice for Tiling - recommends measuring to 5mm accuracy

SANS 10400: Building Regulations - floor area definitions for building compliance

SANS 1449: Tile Classification - nominal sizing considerations


### 1.7 Chatbot Instruction Notes

When a customer asks about measuring their room area: 1. Ask them to describe the room shape (rectangle, L-shape, irregular) 2. For rectangles: ask for length and width in metres 3. For L-shapes: ask them to mentally split it into two rectangles and give you both sets of dimensions 4. For irregular shapes: ask them to break it into rectangles/triangles and give each dimension 5. Ask if there are any fixed items like island baths, freestanding cupboards, or fireplaces that tiles go AROUND (not under built-in cupboards) 6. Calculate the net area and present it clearly 7. Remind them to measure in METRES, not feet or centimetres 8. Suggest adding a small buffer (5%) for measuring errors on initial estimates



<!-- RAG_CHUNK: calculator -->

---

## CALCULATOR 2: TILE QUANTITY CALCULATOR

**RAG search aliases:** boxes, tiles needed, tile count, quantity, wastage



### 2.1 Name and Purpose

Name: Tile Quantity Calculator Purpose: Converts floor area into the exact number of tiles and boxes required, accounting for wastage based on laying pattern and room complications.

Who uses it: Anyone buying tiles who needs to know how many boxes to order.


### 2.2 Formula

Step 1: Calculate number of tiles needed (gross)

Number of Tiles = Ceiling(Total Area (m²) / Area of One Tile (m²))

Step 2: Apply wastage percentage

Tiles with Wastage = Number of Tiles x (1 + Wastage Percentage)

Step 3: Round up to whole tiles

Total Tiles Required = Ceiling(Tiles with Wastage)

Step 4: Convert to boxes

Boxes Required = Ceiling(Total Tiles Required / Tiles per Box)

Tile Area Calculation

Tile Area (m²) = (Length (mm) / 1000) x (Width (mm) / 1000)


### 2.3 Lookup Tables

Wastage by Pattern

| Pattern | Wastage % | Notes |
| --- | --- | --- |
| Straight / stack bond | 10% | Standard baseline |
| Brick bond (50% offset) | 12% | More cuts, some reusable offcuts |
| Diagonal (45 degrees) | 15-18% | Triangular cuts, limited reuse |
| Herringbone | 18-22% | Complex angles, minimal offcut reuse |
| Chevron | 18-22% | Similar to herringbone |
| Versailles / modular | 15% | Multiple sizes in pattern |

Wastage Additions for Complications

| Complication | Additional Wastage |
| --- | --- |
| L-shaped room | +3% |
| Pillars / pipes / columns | +2% per obstruction |
| Many cuts required | +3% |
| Feature strips or borders | +2% |

Standard SA Box Coverage

| Tile Size | Tiles per Box | Coverage per Box |
| --- | --- | --- |
| 300x300mm | 17 | ~1.53 m² |
| 400x400mm | 10 | ~1.60 m² |
| 500x500mm | 7 | ~1.75 m² |
| 600x600mm | 4 | ~1.44 m² |
| 800x800mm | 3 | ~1.92 m² |
| 1200x600mm | 2 | ~1.44 m² |
| 1200x200mm (wood plank) | 6 | ~1.44 m² |
| 600x300mm | 8 | ~1.44 m² |
| 100x100mm mosaic sheet | 22 sheets | ~1.98 m² |
| 200x100mm subway | 34 | ~0.68 m² |


### 2.4 Step-by-Step Method

Calculate the net floor area to be tiled (using Calculator 1)

Identify the tile size being used (e.g., 600x600mm)

Calculate the area of one tile in m²: (600/1000) x (600/1000) = 0.36 m²

Calculate gross tiles needed: Area / Tile Area (round up)

Identify the laying pattern and look up wastage percentage

Check for complications (L-shape, pillars, many cuts) and add percentages

Calculate total wastage percentage

Apply wastage: Gross Tiles x (1 + Total Wastage%) = Tiles with Wastage

Round up to whole tiles

Look up tiles per box for your tile size

Calculate boxes: Total Tiles / Tiles per Box (round up)

Recommend ordering 1 extra box for future repairs


### 2.5 Worked Example

Scenario: A contractor in Cape Town needs to tile a rectangular lounge with 600x600mm porcelain tiles in a straight/stack bond pattern.

Given: - Room dimensions: 4.5m x 5.2m - Tile size: 600mm x 600mm - Pattern: Straight bond - Tiles per box: 4

Calculation: - Room Area = 4.5 x 5.2 = 23.40 m² - Tile Area = 0.6 x 0.6 = 0.36 m² - Gross Tiles = 23.40 / 0.36 = 65 tiles (rounded up) - Wastage for straight bond = 10% - Tiles with Wastage = 65 x 1.10 = 71.5 -> 72 tiles - Boxes Required = 72 / 4 = 18 boxes - Add 1 spare box = 19 boxes total - Actual coverage: 19 boxes x 1.44 m²/box = 27.36 m² - Wastage buffer: 27.36 - 23.40 = 3.96 m² (17% buffer)

Total Cost (at R120 per tile / R480 per box): 19 x R480 = R9,120.00


### 2.6 SANS / Regulatory Reference

SANS 10109: Recommends minimum 10% wastage for standard installations

BS 5385: Wastage tables for different patterns and room complexities

SANS 1449: Nominal vs actual tile sizing considerations


### 2.7 Chatbot Instruction Notes

When a customer asks how many tiles they need: 1. Ask for the room dimensions (length and width in metres) 2. Ask what size tile they want to use (in mm) 3. Ask what pattern they want (straight, diagonal, herringbone, etc.) 4. Ask about room shape complications (L-shape, pillars, etc.) 5. Calculate the area and gross tile count 6. Apply the appropriate wastage percentage based on their pattern 7. Convert to boxes and ALWAYS round up 8. Strongly recommend ordering at least 1 extra box for future repairs 9. Mention that different colours/batches may not match if they need to buy more later 10. Give them the total in both “tiles” and “boxes” for clarity



<!-- RAG_CHUNK: calculator -->

---

## CALCULATOR 3: TOTAL PROJECT COST ESTIMATOR

**RAG search aliases:** budget, cost estimate, materials, labour, VAT



### 3.1 Name and Purpose

Name: Total Project Cost Estimator Purpose: Provides a complete, itemised cost breakdown for a tiling project including all materials, labour, preparation, removal, and finishing items. Includes VAT at 15%.

Who uses it: Homeowners budgeting for renovations, contractors preparing quotes, banks assessing renovation loan applications.


### 3.2 Formula

Complete Project Cost Formula

Total Project Cost = (Materials + Labour + Ancillaries + Preparation + Removal + Contingency) x 1.15 (VAT)

Component Breakdown

Materials = Tiles + Adhesive + Grout + Spacers + Trims/Edging Labour = Installation Rate (m²) x Area (m²) + Day Rate Adjustments Ancillaries = Sealers + Cleaners + Silicon + Expansion Joints + Tools (if hiring) Preparation = Primer + Self-levelling + Screed + Waterproofing Removal = Old Floor Removal + Disposal + Substrate Cleaning Contingency = (Materials + Labour + Ancillaries + Preparation + Removal) x Contingency %

Contingency Guidelines

| Project Type | Contingency % |
| --- | --- |
| Small residential (< 10 m²) | 15% |
| Medium residential (10-30 m²) | 12% |
| Large residential (> 30 m²) | 10% |
| Commercial project | 10-15% |
| Renovation (unknown conditions) | 15-20% |


### 3.3 Lookup Tables

Material Price Ranges (South Africa 2025)

| Material Type | Price Range per m² | Notes |
| --- | --- | --- |
| Ceramic wall tiles | R80-250 | Entry to mid-range |
| Ceramic floor tiles | R100-300 | Entry to mid-range |
| Porcelain tiles (standard) | R150-500 | Good quality range |
| Porcelain tiles (premium) | R500-1,500 | Designer/imported |
| Large format tiles (600x600+) | R200-800 | Price per m² |
| Natural stone (granite) | R400-1,200 | Per m² |
| Natural stone (travertine) | R350-900 | Per m² |
| Mosaic tiles | R300-1,000 | Per m² |
| Vinyl flooring (LVT) | R150-400 | Per m² |
| Laminate flooring | R100-300 | Per m² |
| Tile adhesive (20kg bag) | R80-180 | Per bag |
| Tile grout (5kg bag) | R60-150 | Per bag |
| Tile spacers (pack of 500) | R20-50 | Per pack |
| Aluminium trim (2.5m length) | R35-80 | Per length |
| Stair nosing (2.5m length) | R80-200 | Per length |

Labour Price Ranges (2025/2026)

| Service | Rate per m² | Notes |
| --- | --- | --- |
| Standard floor tiling | R150-250 | Ceramic/porcelain |
| Wall tiling | R180-300 | Higher precision |
| Large format (>600mm) | R250-400 | Two-person team |
| Mosaic installation | R250-400 | Time-consuming |
| Herringbone/diagonal pattern | +30-50% surcharge | On base rate |
| Tiler day rate | R800-1,500 | Plus assistant |

Preparation Cost Ranges

| Service | Cost per m² | Notes |
| --- | --- | --- |
| Floor screeding | R100-200 | Labour + materials |
| Self-levelling compound | R80-150 | Per m² |
| Waterproofing | R150-300 | Membrane + labour |
| Primer application | R20-40 | Per m² |
| Tile removal (floor) | R50-150 | Plus disposal |
| Tile removal (wall) | R60-180 | Plus disposal |
| Rubble disposal (skip) | R1,500-3,000 | Per load |


### 3.4 Step-by-Step Method

Calculate the total tiling area (use Calculator 1)

Select your tile type and note the price per m²

Calculate tile cost: Area x Price per m²

Select tile size and look up adhesive coverage (Table A)

Calculate adhesive cost: (Area / Coverage per bag) x Bag price

Calculate grout cost: (Area / Grout coverage) x Grout bag price

Add spacers: 1 pack per 10 m² (approximate)

Add trim/edging: measure linear metres required x price per length

Sum all materials

Select labour type and look up rate per m²

Calculate labour cost: Area x Rate per m² (apply pattern surcharge if needed)

List preparation items needed (primer, screed, levelling, waterproofing)

Calculate preparation costs

List removal items if applicable

Calculate removal + disposal costs

Add ancillaries (sealers, silicon, cleaners)

Sum subtotal (Materials + Labour + Preparation + Removal + Ancillaries)

Apply contingency percentage

Calculate subtotal with contingency

Add VAT at 15%

Present itemised breakdown


### 3.5 Worked Example

Scenario: A homeowner in Pretoria East wants to tile their open-plan kitchen and living area (30 m²) with 600x600mm porcelain tiles in a straight bond pattern. The floor is currently old ceramic tiles that need removal.

Itemised Cost Breakdown:

| Item | Calculation | Cost |
| --- | --- | --- |
| MATERIALS |  |  |
| Porcelain tiles (30 m² x R250/m²) | 30 x 250 | R7,500 |
| Tile adhesive (30 m² / 5 m² per bag x R130) | 6 x 130 | R780 |
| Tile grout (30 m² / 15 m² per 5kg x R100) | 2 x 100 | R200 |
| Tile spacers (3 packs) | 3 x R35 | R105 |
| Aluminium edge trim (10 linear metres) | 4 x R55 | R220 |
| Subtotal Materials |  | R8,805 |
| LABOUR |  |  |
| Floor tiling (30 m² x R200/m²) | 30 x 200 | R6,000 |
| Subtotal Labour |  | R6,000 |
| PREPARATION |  |  |
| Tile removal (30 m² x R100/m²) | 30 x 100 | R3,000 |
| Rubble disposal (1 skip) | 1 x R2,000 | R2,000 |
| Floor primer (30 m² x R30/m²) | 30 x 30 | R900 |
| Subtotal Preparation |  | R5,900 |
| ANCILLARIES |  |  |
| Tile sealer (penetrating, 2L) | 1 x R350 | R350 |
| Silicone sealant (3 tubes) | 3 x R85 | R255 |
| Tile cleaner (1L) | 1 x R120 | R120 |
| Subtotal Ancillaries |  | R725 |
| SUBTOTAL (before contingency) |  | R21,430 |
| Contingency (12%) | 21,430 x 0.12 | R2,572 |
| Subtotal with Contingency |  | R24,002 |
| VAT (15%) | 24,002 x 0.15 | R3,600 |
| TOTAL PROJECT COST |  | R27,602 |


### 3.6 SANS / Regulatory Reference

SANS 10400: Building Regulations compliance costs

SANS 10109: Quality requirements affecting material selection and pricing

Consumer Protection Act: Requirement for itemised quotes over R500


### 3.7 Chatbot Instruction Notes

When a customer asks for a project cost estimate: 1. Ask for the room dimensions and what type of floor they’re tiling 2. Ask what type of tiles they want (ceramic, porcelain, natural stone, LVT) 3. Ask about the current floor (new concrete, old tiles, old carpet, etc.) 4. Ask about any special requirements (waterproofing, underfloor heating, patterns) 5. Ask about the room type (bathroom, kitchen, lounge, etc.) - this affects preparation needs 6. Build the estimate step by step using the component breakdown 7. Always include contingency and VAT 8. Present the result as an itemised table with clear categories 9. Explain that prices are estimates and actual quotes may vary 10. Suggest getting 3 quotes from registered contractors



<!-- RAG_CHUNK: calculator -->

---

## CALCULATOR 4: TILE ADHESIVE QUANTITY CALCULATOR

**RAG search aliases:** tile glue, adhesive bags, thinset, trowel, back-butter



### 4.1 Name and Purpose

Name: Tile Adhesive Quantity Calculator Purpose: Calculates the exact quantity of tile adhesive (thinset) required based on tile size, trowel size, substrate condition, and whether back-buttering is needed for large format tiles.

Who uses it: Tilers, contractors, DIY enthusiasts - anyone needing to know how many bags of adhesive to buy.


### 4.2 Formula

Basic Adhesive Formula

Adhesive Required (kg) = Tiling Area (m²) x Coverage Rate (kg/m²) x Condition Factor

Condition Factors

Uneven Surface Factor = 1.15 to 1.25 (add 15-25%) Back-butter Factor = 1.40 to 1.60 (add 40-60%) Combined Factor = Base x Uneven Factor x Back-butter Factor (if applicable)

Alternative: Thickness-Based Formula

Adhesive (kg) = Area (m²) x Thickness (mm) x 1.2 kg/m² per mm

Bags Required

Bags Required = Ceiling(Adhesive (kg) / Bag Size (kg))


### 4.3 Lookup Tables

Adhesive Coverage by Tile and Trowel Size

| Tile Size | Trowel Notch | Coverage (kg/m²) | Notes |
| --- | --- | --- | --- |
| Small wall (<=200x200mm) | 6mm | 3-4 | Standard thinset |
| Medium wall/floor (200-400mm) | 8mm | 4-5 | Common for floors |
| Large floor (400-600mm) | 10mm | 5-7 | Needs thicker bed |
| Extra-large / textured (600-1200mm) | 12mm | 7-10 | Full bed + back-butter |
| Mosaics on mesh | 4-6mm | 2-3 | Light application |

Bag Coverage (20kg bag)

| Tile Type | Approximate Coverage per 20kg Bag |
| --- | --- |
| Standard (up to 400mm) | 5.0 - 6.5 m² |
| Large format (400-600mm) | 3.5 - 4.5 m² |
| Extra-large (600mm+) | 2.5 - 3.5 m² |
| Mosaics | 7.0 - 10.0 m² |

Substrate Condition Adjustments

| Substrate Condition | Adjustment Factor | Notes |
| --- | --- | --- |
| Smooth, well-prepared concrete | 1.0 (no adjustment) | Ideal surface |
| Slightly uneven concrete | 1.15 | Minor variations |
| Uneven concrete | 1.25 | Significant variations |
| Old tile surface (scarified) | 1.20 | After proper preparation |
| Painted surface (scarified) | 1.15 | Must be properly scarified |
| Wooden floor (overboarded) | 1.10 | Use flexible adhesive |

Back-Buttering Requirements

| Tile Size | Back-Butter Required | Factor |
| --- | --- | --- |
| Up to 400mm | Generally no | 1.0 |
| 400-600mm | Recommended | 1.40-1.50 |
| 600-900mm | Required | 1.50-1.60 |
| 900mm+ | Mandatory | 1.60 |


### 4.4 Step-by-Step Method

Determine the total tiling area in m²

Identify your tile size category from the table

Select the appropriate trowel notch size

Look up the base coverage rate (kg/m²)

Assess the substrate condition and select the condition factor

Determine if back-buttering is required (tile size > 400mm)

If back-buttering, select the back-butter factor

Calculate total adjustment factor: Base x Condition x Back-butter

Calculate total adhesive: Area x Coverage Rate x Adjustment Factor

Determine your bag size (typically 20kg in SA)

Calculate bags needed: Total kg / Bag Size (round UP)

Recommend 1 extra bag for safety


### 4.5 Worked Example

Scenario: A tiler in Durban is installing 800x800mm porcelain tiles on a slightly uneven concrete slab in a lounge. Area is 24 m².

Given: - Area: 24 m² - Tile size: 800x800mm (Extra-large category) - Trowel: 12mm notch - Substrate: Slightly uneven concrete - Back-buttering: Required (tile > 600mm) - Bag size: 20kg

Calculation: - Base coverage for 800mm tile with 12mm trowel: 8 kg/m² (midpoint of 7-10) - Condition factor (slightly uneven): 1.15 - Back-butter factor (800mm): 1.50 - Total adjustment factor: 1.15 x 1.50 = 1.725 - Total adhesive: 24 x 8 x 1.725 = 331.2 kg - Bags required: 331.2 / 20 = 16.56 -> 17 bags - Add 1 safety bag = 18 bags total

Alternative thickness-based check: - Effective thickness: 12mm x 1.725 adjustment = ~20.7mm equivalent - Using formula: 24 x 20.7 x 1.2 = 596 kg - this gives a higher estimate - The coverage rate method is preferred for practical estimation


### 4.6 SANS / Regulatory Reference

SANS 10109: Specifies minimum adhesive bed thickness for different tile types

SANS 10400-J: Floor substrate preparation requirements

Manufacturer specifications: Always follow adhesive manufacturer’s coverage data


### 4.7 Chatbot Instruction Notes

When a customer asks about adhesive quantity: 1. Ask what size tiles they’re using (this determines everything) 2. Ask about the floor condition (new concrete, old tiles, uneven, etc.) 3. Ask the area to be tiled 4. If tiles are 600mm or larger, explain that back-buttering is required 5. If the floor is uneven, explain that extra adhesive will be needed 6. Calculate and present the result in both kilograms and number of bags 7. Explain that a 20kg bag is standard in South Africa 8. Recommend buying 1 extra bag - adhesive has a long shelf life if kept dry 9. Mention that different brands have slightly different coverage rates 10. Remind them to use the correct trowel size for their tile



<!-- RAG_CHUNK: calculator -->

---

## CALCULATOR 5: GROUT QUANTITY CALCULATOR

**RAG search aliases:** grout bags, joint width, epoxy grout, cement grout



### 5.1 Name and Purpose

Name: Grout Quantity Calculator Purpose: Calculates the exact amount of grout needed based on tile dimensions, joint width, joint depth, and grout type (cement vs epoxy).

Who uses it: Tilers, contractors, DIY enthusiasts buying grout for their tiling project.


### 5.2 Formula

Primary Formula

Grout (kg/m²) = [(Tile Length (mm) + Tile Width (mm)) / (Tile Length (mm) x Tile Width (mm))] x Joint Width (mm) x Joint Depth (mm) x SG x 0.001

Where: - SG = Specific Gravity (1.5 for cement grout, 1.6 for epoxy grout) - The 0.001 factor converts mm³ to L (since 1 L = 1,000,000 mm³ = 1,000 mm x 1,000 mm x 1 mm)

Simplified Working Formula

Grout (kg/m²) = [(L + W) / (L x W)] x JW x JD x SG x 0.001

Where: - L = Tile Length in mm - W = Tile Width in mm - JW = Joint Width in mm - JD = Joint Depth in mm (typically 2/3 of tile thickness) - SG = Specific Gravity

Total Grout Required

Total Grout (kg) = Grout per m² x Tiling Area (m²) Bags Required = Ceiling(Total Grout (kg) / Bag Size (kg))


### 5.3 Lookup Tables

Specific Gravity by Grout Type

| Grout Type | Specific Gravity (kg/L) | Notes |
| --- | --- | --- |
| Standard cement grout | 1.5 | Most common, economical |
| Waterproof cement grout | 1.5 | Contains additives |
| Epoxy grout | 1.6 | Stain-resistant, premium |
| Furan grout | 1.7 | Chemical resistant |

Recommended Joint Widths

| Tile Type | Recommended Joint Width | Notes |
| --- | --- | --- |
| Mosaic tiles | 2-3mm | Small joints |
| Ceramic wall tiles | 2-3mm | Standard |
| Ceramic floor tiles | 3-5mm | Allows for movement |
| Porcelain tiles | 3-5mm | Standard |
| Large format tiles (600mm+) | 5-8mm | Accommodates tile variation |
| Natural stone | 4-6mm | Irregular edges |
| Outdoor tiles | 5-8mm | Greater movement |

Grout Consumption Quick Reference (Cement Grout, SG=1.5)

| Tile Size | 2mm Joint | 3mm Joint | 5mm Joint | 8mm Joint |
| --- | --- | --- | --- | --- |
| 100x100mm | 0.60 kg/m² | 0.90 kg/m² | 1.50 kg/m² | 2.40 kg/m² |
| 200x200mm | 0.30 kg/m² | 0.45 kg/m² | 0.75 kg/m² | 1.20 kg/m² |
| 300x300mm | 0.20 kg/m² | 0.30 kg/m² | 0.50 kg/m² | 0.80 kg/m² |
| 400x400mm | 0.15 kg/m² | 0.23 kg/m² | 0.38 kg/m² | 0.60 kg/m² |
| 600x600mm | 0.10 kg/m² | 0.15 kg/m² | 0.25 kg/m² | 0.40 kg/m² |
| 800x800mm | 0.08 kg/m² | 0.11 kg/m² | 0.19 kg/m² | 0.30 kg/m² |

Standard Bag Coverage (5kg bag)

| Tile Size / Joint Width | Approximate Coverage per 5kg Bag |
| --- | --- |
| Small tiles, narrow joints | 20-25 m² |
| Medium tiles, standard joints | 10-15 m² |
| Large tiles, wide joints | 6-10 m² |


### 5.4 Step-by-Step Method

Identify your tile dimensions in mm (length and width)

Determine the joint width (check tile supplier recommendations)

Determine the joint depth (typically 2/3 of tile thickness)

Select the grout type (cement or epoxy)

Look up the specific gravity for your grout type

Apply the formula: [(L+W)/(LxW)] x JW x JD x SG x 0.001

Calculate grout per m²

Multiply by total tiling area to get total grout in kg

Select your bag size (typically 5kg in SA)

Calculate bags needed: Total kg / Bag Size (round UP)

Add 10% for wastage and cleaning


### 5.5 Worked Example

Scenario: A homeowner in Bloemfontein is tiling their bathroom floor with 300x300mm ceramic floor tiles. They want 4mm joints with standard cement grout. Bathroom area is 8 m². Tile thickness is 9mm.

Given: - Tile: 300mm x 300mm x 9mm - Joint width: 4mm - Joint depth: 6mm (2/3 of 9mm tile thickness) - Grout type: Cement (SG = 1.5) - Area: 8 m² - Bag size: 5kg

Calculation: - Grout per m² = [(300 + 300) / (300 x 300)] x 4 x 6 x 1.5 x 0.001 - Grout per m² = [600 / 90,000] x 4 x 6 x 1.5 x 0.001 - Grout per m² = 0.006667 x 4 x 6 x 1.5 x 0.001 - Grout per m² = 0.006667 x 36 x 0.001 - Wait - let me recalculate carefully:

Correct step-by-step: - (L + W) = 300 + 300 = 600 - (L x W) = 300 x 300 = 90,000 - (L + W) / (L x W) = 600 / 90,000 = 0.006667 - Joint Width = 4mm - Joint Depth = 6mm - SG = 1.5

Grout per m² = 0.006667 x 4 x 6 x 1.5 = 0.006667 x 144 = 0.24 kg/m²

Total grout = 0.24 x 8 = 1.92 kg

Add 10% wastage = 1.92 x 1.10 = 2.11 kg

Bags needed = Ceiling(2.11 / 5) = 1 bag

Result: 1 x 5kg bag of grout (with spare for future repairs)


### 5.6 SANS / Regulatory Reference

SANS 10109: Minimum joint widths and grout specifications

SANS 10107: Slip resistance - grout joints affect slip resistance ratings

Manufacturer specifications: Always follow grout manufacturer’s mixing and application guidelines


### 5.7 Chatbot Instruction Notes

When a customer asks about grout quantity: 1. Ask what size tiles they’re using (length and width in mm) 2. Ask what joint width they plan to use (or recommend standard for their tile type) 3. Ask what type of grout they want (cement or epoxy) 4. Ask the tiling area 5. If they know their tile thickness, use 2/3 of it as joint depth; otherwise use typical defaults 6. Calculate using the formula and present clearly 7. Explain that cement grout is cheaper but stains more easily 8. Explain that epoxy grout is stain-resistant but harder to apply and more expensive 9. Recommend a 10% buffer 10. Mention that most grouts come in 5kg bags in South Africa



<!-- RAG_CHUNK: calculator -->

---

## CALCULATOR 6: SCREED VOLUME CALCULATOR

**RAG search aliases:** screed volume, cement, sand, drying time



### 6.1 Name and Purpose

Name: Screed Volume Calculator Purpose: Calculates the volume of sand-cement screed required for floor preparation, including cement and sand quantities by mass, water requirements, and estimated drying time before tiling can commence.

Who uses it: Contractors preparing floors for tiling, builders constructing new homes, renovators levelling old floors.


### 6.2 Formula

Screed Volume

Volume (m³) = Area (m²) x Thickness (m)

Dry Mix Mass

Dry Mix (kg) = Volume (m³) x 1,800 to 2,000 kg/m³

Cement Quantity

Cement (kg) = Volume (m³) x 350 to 400 kg/m³ Bags of Cement = Ceiling(Cement (kg) / 50)

(50kg is the standard cement bag size in South Africa)

Sand Quantity

Sand (kg) = Volume (m³) x 1,400 to 1,600 kg/m³ Sand (m³ loose) = Sand (kg) / 1,600 kg/m³ (loose bulk density)

Water Quantity

Water (litres) = Volume (m³) x 80 to 100 litres/m³

Drying Time

If thickness <= 40mm: Drying Time (days) = Thickness (mm) x 1 If thickness > 40mm: Drying Time (days) = 40 + (Thickness (mm) - 40) x 2


### 6.3 Lookup Tables

Screed Types and Minimum Thickness (SANS 10400-J)

| Screed Type | Minimum Thickness | Application |
| --- | --- | --- |
| Bonded screed | 15mm | Applied directly to concrete slab with bonding agent |
| Unbonded screed | 35mm | Separated from slab by damp-proof membrane |
| Floating screed | 35mm | Over insulation or underfloor heating |

Material Quantities per m³ of Screed

| Material | Quantity per m³ | Notes |
| --- | --- | --- |
| Cement | 350-400 kg | 7-8 x 50kg bags |
| Sand (dry) | 1,400-1,600 kg | ~0.9-1.0 m³ loose |
| Water | 80-100 litres | Adjust for workability |
| Total dry mix | 1,800-2,000 kg | Per m³ of screed |

Drying Time by Thickness

| Thickness | Drying Time | Ready for Tiling |
| --- | --- | --- |
| 15mm (bonded min) | 15 days | 2 weeks + |
| 20mm | 20 days | 3 weeks |
| 25mm | 25 days | ~4 weeks |
| 30mm | 30 days | ~1 month |
| 35mm | 35 days | 5 weeks |
| 40mm | 40 days | 6 weeks |
| 50mm | 60 days | 2 months |
| 60mm | 80 days | ~3 months |
| 75mm | 110 days | ~4 months |

Typical Mix Ratios by Volume

| Application | Cement : Sand | Strength Class |
| --- | --- | --- |
| Domestic floors | 1 : 3-4 | C20-C25 |
| Commercial floors | 1 : 3 | C25-C30 |
| Heavy duty floors | 1 : 2.5 | C30+ |
| Underfloor heating | 1 : 4 with additives | C20-F4 |


### 6.4 Step-by-Step Method

Measure the area to be screeded in m²

Determine the required screed thickness based on:

Type of screed (bonded/unbonded/floating)

Existing floor level variations

Any services or thresholds to match

Calculate screed volume: Area x Thickness (in metres)

Determine the mix ratio (typically 1:3 to 1:4 cement:sand)

Calculate cement required: Volume x 350-400 kg/m³

Convert cement to 50kg bags (round UP)

Calculate sand required: Volume x 1,400-1,600 kg/m³

Convert sand to cubic metres loose (divide by 1,600)

Calculate water required: Volume x 80-100 litres

Calculate drying time using the thickness-based formula

Advise on tiling start date (add drying time + 7 days safety)


### 6.5 Worked Example

Scenario: A builder in Midrand needs to install a bonded screed over a concrete slab in a new house. The lounge area is 28 m² and requires 25mm of screed to achieve the correct floor levels.

Given: - Area: 28 m² - Thickness: 25mm = 0.025m - Screed type: Bonded - Mix: 1:4 (cement:sand by volume)

Calculation: - Volume = 28 x 0.025 = 0.70 m³ - Cement = 0.70 x 375 = 262.5 kg -> 6 bags of 50kg cement (300 kg) - Sand = 0.70 x 1,500 = 1,050 kg -> ~0.66 m³ loose - Water = 0.70 x 90 = 63 litres - Drying time = 25 x 1 = 25 days - Ready for tiling = 25 + 7 = 32 days

Material Summary: | Material | Quantity | Estimated Cost (2025) | |———-|———-|———————-| | 50kg cement bags | 6 bags | 6 x R95 = R570 | | Building sand | 0.7 m³ | R350 | | Water | 63 L | negligible | | Bonding agent | 2-3 L | R150 | | Total Materials | | ~R1,070 |

Timeline: Screed laid on Day 0, ready for tiling on Day 32.


### 6.6 SANS / Regulatory Reference

SANS 10400-J: Floor screed minimum thickness requirements

SANS 10109: Screed preparation for tiling

SANS 784: Cement specifications

TR34 (Concrete Society): Classification of floor flatness


### 6.7 Chatbot Instruction Notes

When a customer asks about screed requirements: 1. Ask for the area to be screeded 2. Ask what type of screed they need (bonded, unbonded, floating) 3. Ask the required thickness (or help them determine it) 4. Ask if the screed is over a concrete slab, insulation, or underfloor heating 5. Calculate volume, cement bags, sand quantity, and water 6. Emphasise the DRYING TIME - many homeowners underestimate this 7. Explain that tiling on damp screed causes tile failure 8. Recommend a moisture test before tiling (should read < 75% RH) 9. Mention that bonded screeds need a bonding agent (slurry coat) 10. Suggest getting a professional for anything over 50mm thick



<!-- RAG_CHUNK: calculator -->

---

## CALCULATOR 7: SELF-LEVELLING COMPOUND CALCULATOR

**RAG search aliases:** self levelling, levelling compound, primer, uneven floor



### 7.1 Name and Purpose

Name: Self-Levelling Compound Calculator Purpose: Calculates the quantity of self-levelling compound and primer needed to create a flat, level surface for tiling, especially over uneven concrete or existing floors.

Who uses it: Tilers, contractors, and DIY enthusiasts preparing floors for tile installation.


### 7.2 Formula

Self-Levelling Compound (kg)

Compound (kg) = Area (m²) x Thickness (mm) x 1.6

Where 1.6 is the coverage factor in kg/m² per mm of thickness.

For Thicknesses Over 20mm

Compound (kg) = Area x Thickness x 1.6 x 1.3

(30% graded sand 0/4mm is added for bulk)

Primer Required

Primer (L) = Area (m²) x 0.25

(0.2-0.3 L/m²; 0.25 is the midpoint)

Bags Required

Bags = Ceiling(Compound (kg) / 25)

(25kg is the standard bag size in SA)


### 7.3 Lookup Tables

Compound Coverage (25kg bag)

| Thickness | Coverage per 25kg Bag | kg per m² |
| --- | --- | --- |
| 1mm | ~15.6 m² | 1.6 |
| 2mm | ~7.8 m² | 3.2 |
| 3mm | ~5.2 m² | 4.8 |
| 5mm | ~3.1 m² | 8.0 |
| 8mm | ~1.95 m² | 12.8 |
| 10mm | ~1.56 m² | 16.0 |
| 15mm | ~1.04 m² | 24.0 |
| 20mm | ~0.78 m² | 32.0 |

Thickness Guidelines

| Application | Minimum | Maximum Single Pour | Notes |
| --- | --- | --- | --- |
| Over smooth surface | 1mm | 20mm | Self-levelling only |
| Over prepared concrete | 2mm | 20mm | Self-levelling only |
| Over very uneven surface | 5mm | 20mm | May need screed instead |
| Over 20mm | Add 30% sand | Consult manufacturer | Extended pour |

Primer Requirements by Substrate

| Substrate Type | Primer Rate (L/m²) | Notes |
| --- | --- | --- |
| Absorbent concrete | 0.2-0.3 | May need 2 coats |
| Non-absorbent concrete | 0.15-0.2 | Smooth power-floated |
| Ceramic tiles | 0.2-0.3 | Special primer required |
| Existing screed | 0.2-0.25 | Standard preparation |
| Wooden floors | 0.2-0.3 | Flexible primer |

Drying Times

| Product Stage | Drying Time | Conditions |
| --- | --- | --- |
| Primer (tack-free) | 1-2 hours | 20°C, 65% RH |
| Primer (ready for compound) | 2-4 hours | 20°C, 65% RH |
| Self-levelling compound | 2-4 hours walkable | 20°C, 65% RH |
| Ready for tiling | 24 hours minimum | 20°C, 65% RH |
| Full cure | 7 days | 20°C, 65% RH |


### 7.4 Step-by-Step Method

Measure the area to be levelled in m²

Determine the required thickness:

Check floor level variations with a straightedge

Measure the deepest depression that needs filling

Add 1-2mm for tolerance

If thickness <= 20mm:

Calculate compound: Area x Thickness x 1.6

If thickness > 20mm:

Calculate compound: Area x Thickness x 1.6 x 1.3

OR recommend a traditional screed instead

Calculate bags: Compound (kg) / 25 (round UP)

Calculate primer: Area x 0.25 L/m²

Check if 2 coats of primer are needed (porous substrates)

Present material list with drying times


### 7.5 Worked Example

Scenario: A homeowner in Sandton needs to level their concrete floor before installing 600x600mm porcelain tiles. The lounge is 22 m². Floor level variations measured up to 5mm.

Given: - Area: 22 m² - Thickness: 5mm + 1mm tolerance = 6mm - Substrate: Concrete (absorbent)

Calculation: - Compound = 22 x 6 x 1.6 = 211.2 kg - Bags = 211.2 / 25 = 8.45 -> 9 bags - Primer = 22 x 0.25 = 5.5 L - Primer coats: 1 coat (concrete is absorbent but not excessively porous)

Material Summary: | Material | Quantity | Est. Cost (2025) | |———-|———-|—————–| | Self-levelling compound (25kg) | 9 bags | 9 x R180 = R1,620 | | Primer (5L) | 1 x 5L | R280 | | Total | | ~R1,900 |

Timeline: - Day 1: Apply primer, wait 2-4 hours - Day 1 (afternoon): Pour self-levelling compound - Day 2: Compound dry, ready for tiling


### 7.6 SANS / Regulatory Reference

SANS 10109: Floor preparation requirements for tiling

SANS 10400-J: Floor finishes and flatness requirements

Manufacturer specifications: Always follow compound manufacturer’s guidelines


### 7.7 Chatbot Instruction Notes

When a customer asks about self-levelling compound: 1. Ask for the area to be levelled 2. Ask how uneven the floor is (measure with a straightedge) 3. Ask what the substrate is (concrete, old tiles, wood) 4. If thickness > 20mm, suggest a traditional screed instead (it’s cheaper) 5. If thickness <= 20mm, calculate compound and primer 6. Explain that the floor MUST be clean and primed before application 7. Mention that self-levelling compound dries quickly - be ready to work fast 8. Warn that temperatures below 10°C slow curing significantly 9. Recommend a professional for areas over 30 m² 10. Mention that some products can be tiled over in 24 hours



<!-- RAG_CHUNK: calculator -->

---

## CALCULATOR 8: WATERPROOFING CALCULATOR

**RAG search aliases:** bathroom, shower, balcony, membrane, primer, tape



### 8.1 Name and Purpose

Name: Waterproofing Calculator Purpose: Calculates the quantity of waterproofing membrane, primer, and ancillary materials needed for wet areas (bathrooms, showers, balconies, etc.) in compliance with SANS 10400 Part P.

Who uses it: Contractors, tilers, bathroom renovators - anyone working in wet areas.


### 8.2 Formula

Floor Waterproofing

Membrane (L) = Floor Area (m²) x Coats x Coverage per Coat (L/m²)

Wall Waterproofing (Upstands)

Wall Area (m²) = Perimeter Length (m) x Upstand Height (m) Wall Membrane (L) = Wall Area x Coats x Coverage per Coat

Total Waterproofing

Total Membrane (L) = Floor Membrane + Wall Membrane

Primer Required

Primer (L) = (Floor Area + Wall Area) x 0.3

(0.2-0.4 L/m² depending on substrate porosity)

Reinforcement Tape

Tape (linear metres) = Floor Perimeter + Internal Corners + Pipe Penetrations x 2


### 8.3 Lookup Tables

Waterproofing Requirements by Area (SANS 10400 Part P)

| Area | Minimum Requirement |
| --- | --- |
| Shower floor | Full waterproofing, 2.5-3.0 L/m² |
| Shower walls (full height) | Full waterproofing up to 1.8m |
| Shower walls (behind mixer) | 300mm minimum around fixture |
| Bathroom floor | Full waterproofing |
| Bathroom walls | 150mm upstand minimum |
| Balcony / patio | Full waterproofing + drainage falls |
| Kitchen floor | Optional (recommended under sink area) |

Coverage Rates (Liquid Membrane)

| Application | Coverage per Coat | Coats Required | Total Coverage |
| --- | --- | --- | --- |
| Standard floor | 1.0-1.5 L/m² | 2 | 2.0-3.0 L/m² |
| Shower floor (heavy) | 1.25-1.5 L/m² | 2 | 2.5-3.0 L/m² |
| Wall upstands | 1.0 L/m² | 2 | 2.0 L/m² |

Primer Coverage

| Substrate | Coverage (L/m²) |
| --- | --- |
| Concrete | 0.2-0.3 |
| Screed | 0.2-0.3 |
| Plaster | 0.3-0.4 |
| Rendered brick | 0.2-0.3 |

Upstand Requirements

| Area Type | Minimum Upstand Height |
| --- | --- |
| Shower walls | 1,800mm (full shower height) |
| Shower curb/entry | 150mm above finished floor |
| General bathroom walls | 150mm minimum |
| Bath surround | 150mm above bath rim |
| Balcony perimeter | 150mm minimum |
| Doorway threshold | Full width, 150mm upstand |


### 8.4 Step-by-Step Method

Identify the wet area type (shower, bathroom, balcony, etc.)

Measure the floor area in m²

Determine the upstand height required (see table above)

Measure the perimeter length of the floor area

Calculate wall waterproofing area: Perimeter x Upstand Height

Determine coverage rate based on application type

Calculate floor membrane: Floor Area x Total Coverage Rate

Calculate wall membrane: Wall Area x Total Coverage Rate

Sum total membrane required in litres

Calculate primer: (Floor Area + Wall Area) x Primer Rate

Calculate reinforcement tape: Floor Perimeter + additional for details

Add details:

Internal corners: 2 x length per corner

Pipe penetrations: 200mm diameter minimum

Floor waste: seal around penetration

Present complete material list


### 8.5 Worked Example

Scenario: A contractor in Cape Town is renovating a bathroom. The shower area (1.2m x 0.9m) and general bathroom floor (2.5m x 2.0m) need waterproofing. Shower walls need waterproofing to 1.8m height.

Given: - Bathroom floor: 2.5m x 2.0m = 5.0 m² - Shower floor (within bathroom): 1.2m x 0.9m = 1.08 m² - Shower perimeter: 1.2 + 0.9 + 1.2 + 0.9 = 4.2 linear metres - Shower wall height: 1.8m - Liquid membrane coverage: 1.25 L/m² per coat, 2 coats

Calculation:

Floor Waterproofing: - Bathroom floor area: 5.0 m² - Shower floor (included in bathroom floor): already counted - Floor membrane: 5.0 x 1.25 x 2 = 12.5 L

Shower Wall Waterproofing: - Shower wall area: 4.2 x 1.8 = 7.56 m² - Wall membrane: 7.56 x 1.25 x 2 = 18.9 L

Bathroom Wall Upstands: - Bathroom perimeter (excluding shower, which is already done to full height): - Full bathroom perimeter: 2.5 + 2.0 + 2.5 + 2.0 = 9.0m - Less shower entrance (~0.9m): ~8.1m of wall needs 150mm upstand - But more accurately: all walls at 150mm upstand - Wall upstand area: 9.0 x 0.15 = 1.35 m² - Less shower walls already covered: ~0.9 x 0.15 x 2 = 0.27 (approximate) - Actually, let’s simplify: shower is fully waterproofed, remaining walls at 150mm - Remaining wall length: 9.0 - 4.2 = 4.8m (approximately, this varies by layout) - Wall upstand area: 4.8 x 0.15 = 0.72 m² - Plus shower entrance wall at 150mm: 0.9 x 0.15 = 0.135 m² - Total upstand: ~0.86 m² - Upstand membrane: 0.86 x 1.25 x 2 = 2.15 L

Total Membrane: 12.5 + 18.9 + 2.15 = 33.55 L -> 34 L

Primer: - Total area (floor + walls): 5.0 + 7.56 + 0.86 = 13.42 m² - Primer: 13.42 x 0.3 = 4.03 L -> 5 L container

Reinforcement Tape: - Floor perimeter: 9.0 linear metres - Internal corners: 4 corners x 0.3m each = 1.2m - Shower internal corners: 4 x 0.3m = 1.2m - Pipe penetrations (1 shower, 1 basin, 1 toilet): 3 x 0.5m = 1.5m - Total tape: 9.0 + 1.2 + 1.2 + 1.5 = 12.9 linear metres


### 8.6 SANS / Regulatory Reference

SANS 10400 Part P: Drainage and waterproofing of buildings - MANDATORY for wet areas

SANS 10109: Preparation and treatment of wet area substrates

NHBRC requirements: Waterproofing is a warranty item


### 8.7 Chatbot Instruction Notes

When a customer asks about waterproofing: 1. Ask what area needs waterproofing (shower, bathroom, balcony, etc.) 2. Ask for the floor dimensions 3. If it’s a shower, ask the wall dimensions and whether it’s a full shower enclosure or over-bath 4. Explain that SANS 10400 Part P REQUIRES waterproofing in wet areas 5. Emphasise that shower walls need waterproofing to 1.8m height 6. Explain that all bathroom walls need at least 150mm upstand 7. Calculate membrane, primer, and tape quantities 8. Explain the 2-coat minimum requirement 9. Mention that waterproofing MUST be done BEFORE tiling 10. Recommend a flood test: fill the shower floor with water and check for leaks before tiling 11. Warn that waterproofing failure is one of the most common (and expensive) defects



<!-- RAG_CHUNK: calculator -->

---

## CALCULATOR 9: PATTERN LAYOUT WASTAGE CALCULATOR

**RAG search aliases:** herringbone, diagonal, chevron, wastage, layout



### 9.1 Name and Purpose

Name: Pattern Layout Wastage Calculator Purpose: Determines the total tile wastage percentage based on the chosen laying pattern and any room complications, then calculates the final tile quantity including wastage.

Who uses it: Homeowners selecting tile patterns, designers, tilers quoting for patterned installations.


### 9.2 Formula

Base Wastage by Pattern

Base Wastage % = Lookup(Pattern)

Complication Additions

Complication Addition % = Sum of all applicable complication factors

Total Wastage

Total Wastage % = Base Wastage % + Complication Addition %

Tiles with Wastage

Total Tiles Required = Gross Tiles x (1 + Total Wastage % / 100)

Box Calculation

Boxes Required = Ceiling(Total Tiles Required / Tiles per Box)


### 9.3 Lookup Tables

Base Wastage by Pattern

| Pattern | Wastage % | Notes |
| --- | --- | --- |
| Straight / stack bond | 10% | Standard baseline, minimal cuts |
| Brick bond / running bond (50% offset) | 12% | More cuts, some reusable offcuts |
| Diagonal (45 degrees) | 15-18% | Triangular cuts, limited reuse |
| Herringbone | 18-22% | Complex angles, minimal offcut reuse |
| Chevron | 18-22% | Similar to herringbone |
| Basket weave | 12-15% | Multiple tile orientation |
| Versailles / modular (multi-size) | 15% | Multiple sizes in pattern |
| Windmill / pinwheel | 14-16% | Four tiles around a central tile |
| Hexagon | 12-15% | More edge cuts than square |
| Fish scale | 18-22% | Complex curved cuts |
| Subway / brick pattern (on walls) | 10-12% | Similar to brick bond |

Complication Additions

| Complication | Additional Wastage | Cumulative? |
| --- | --- | --- |
| L-shaped room | +3% | Yes |
| Pillars / columns | +2% per obstruction | Yes |
| Pipes / conduits | +2% per cluster | Yes |
| Many doorways | +2% | Yes |
| Feature strips / borders | +2% | Yes |
| Floor waste penetrations | +1% each | Yes |
| Skirting tile cuts | +2% | Yes |
| Step-down / level change | +3% | Yes |

Pattern Suitability by Tile Type

| Tile Type | Best Patterns | Avoid |
| --- | --- | --- |
| Square ceramic | Straight, diagonal, herringbone | Chevron (needs rectangular) |
| Rectangular (subway) | Brick bond, herringbone, straight stack | Diagonal (wasteful) |
| Large format (600mm+) | Straight stack, minimal patterns | Herringbone (very wasteful) |
| Wood-look plank | Straight, staggered, herringbone | Diagonal |
| Mosaic sheets | Sheet layout | Individual pattern layout |
| Natural stone | Any pattern | Herringbone (expensive waste) |


### 9.4 Step-by-Step Method

Select the desired laying pattern

Look up the base wastage percentage for that pattern

Examine the room for complications:

Is it L-shaped?

Are there pillars or columns?

Are there many pipes or conduits?

Are there many doorways?

Are feature strips or borders being used?

Are there floor waste penetrations?

Is skirting being tiled?

Add all applicable complication percentages

Calculate total wastage: Base + Complications

Calculate gross tiles: Area / Tile Area

Calculate total tiles with wastage: Gross x (1 + Total Wastage%)

Round up to whole tiles

Convert to boxes (round up)

Add 1 spare box for future repairs


### 9.5 Worked Example

Scenario: A designer in Johannesburg is specifying a herringbone pattern with 1200x200mm wood-look porcelain planks for an L-shaped lounge that has a central pillar. The net tiling area is 32 m².

Given: - Tile: 1200mm x 200mm planks - Pattern: Herringbone - Room: L-shaped - Complications: 1 central pillar, 2 doorways

Calculation: - Tile area = 1.2 x 0.2 = 0.24 m² - Gross tiles = 32 / 0.24 = 133.3 -> 134 tiles - Base wastage (herringbone): 20% (midpoint of 18-22%) - Complications: - L-shaped room: +3% - Central pillar: +2% - Two doorways: +2% - Total complications: +7% - Total wastage: 20% + 7% = 27% - Tiles with wastage: 134 x 1.27 = 170.2 -> 171 tiles - Tiles per box (1200x200mm): 6 tiles per box - Boxes: 171 / 6 = 28.5 -> 29 boxes - Add 1 spare box = 30 boxes

Comparison with straight bond (same room): - Base wastage (straight): 10% - Complications: 7% - Total wastage: 17% - Tiles with wastage: 134 x 1.17 = 156.8 -> 157 tiles - Boxes: 157 / 6 = 26.2 -> 27 boxes - Add 1 spare = 28 boxes

Difference: 30 - 28 = 2 extra boxes for herringbone pattern Cost difference (at R250/tile): 2 boxes x 6 tiles x R250 = R3,000 extra for pattern


### 9.6 SANS / Regulatory Reference

SANS 10109: Recommended wastage allowances for different patterns

BS 5385: British standard wastage tables (referenced in SA)

Manufacturer recommendations: Some tiles specify minimum wastage for warranty


### 9.7 Chatbot Instruction Notes

When a customer asks about tile patterns and wastage: 1. Ask what pattern they’re considering (show them options if unsure) 2. Ask about the room shape and any obstructions 3. Explain that diagonal, herringbone, and chevron patterns use significantly more tiles 4. Calculate the wastage and show them the cost difference between patterns 5. For budget-conscious customers, recommend straight bond or brick bond 6. For premium projects, confirm they’re happy with the extra cost 7. Mention that complex patterns take longer to lay (higher labour cost too) 8. Remind them that the extra tiles are not wasted - they’re used for cuts and future repairs 9. For large format tiles, discourage herringbone (wasteful with expensive tiles) 10. Show a comparison table of different patterns and their costs



<!-- RAG_CHUNK: calculator -->

---

## CALCULATOR 10: LABOUR COST ESTIMATOR

**RAG search aliases:** installer cost, tiler rate, installation cost



### 10.1 Name and Purpose

Name: Labour Cost Estimator Purpose: Estimates tiling labour costs based on tile type, size, laying pattern, and location (floor vs wall), including day-rate calculations and additional worker requirements.

Who uses it: Homeowners budgeting for labour, contractors preparing labour quotes, project managers estimating project costs.


### 10.2 Formula

Per Square Metre Pricing

Labour Cost = Area (m²) x Base Rate (R/m²) x Pattern Factor x Size Factor

Day Rate Pricing

Labour Cost = Days Required x Day Rate (R/day) Days Required = Area (m²) / Daily Output (m²/day)

Assistant Costs

Assistant Cost = Days Required x Assistant Rate (R/day)

Pattern Surcharge

Pattern Surcharge % = Lookup(Pattern) Adjusted Rate = Base Rate x (1 + Pattern Surcharge % / 100)


### 10.3 Lookup Tables

Base Labour Rates by Application (2025/2026)

| Service | Rate per m² | Notes |
| --- | --- | --- |
| Standard floor tiling (ceramic) | R150-200 | Single tiler |
| Standard floor tiling (porcelain) | R180-250 | Single tiler |
| Wall tiling (ceramic) | R180-250 | Higher precision needed |
| Wall tiling (porcelain) | R200-300 | Higher precision needed |
| Large format floor (>600mm) | R250-400 | Two-person team |
| Large format wall (>600mm) | R280-450 | Two-person team |
| Mosaic installation | R250-400 | Time-consuming |
| Natural stone installation | R300-500 | Specialist work |
| Outdoor tiling | R200-350 | Weather-dependent |
| Commercial tiling | R150-250 | Economy of scale |

Pattern Surcharges

| Pattern | Surcharge on Base Rate |
| --- | --- |
| Straight / stack bond | 0% (base rate) |
| Brick bond / running bond | +10% |
| Diagonal (45 degrees) | +30-40% |
| Herringbone | +40-50% |
| Chevron | +40-50% |
| Versailles / modular | +25-35% |
| Basket weave | +15-25% |
| Feature strip insertion | +10-15% |

Tile Size Factors

| Tile Size | Size Factor | Notes |
| --- | --- | --- |
| Up to 300x300mm | 1.0 | Standard handling |
| 400x400mm to 500x500mm | 1.05-1.10 | Slightly more care |
| 600x600mm | 1.10-1.15 | Two-person recommended |
| 800x800mm to 900x900mm | 1.30-1.50 | Two-person required |
| 1200x600mm or larger | 1.50-2.00 | Team required, specialist |
| Mosaics | 1.50-2.00 | Very time-consuming |

Daily Output Rates (Experienced Tiler)

| Application | Daily Output | Notes |
| --- | --- | --- |
| Standard floor tiles (300-400mm) | 8-12 m²/day | Straight bond |
| Standard wall tiles (300-400mm) | 6-8 m²/day | Straight bond |
| Large format floor (600mm+) | 5-8 m²/day | Two-person team |
| Mosaic installation | 3-5 m²/day | Depends on sheet size |
| Herringbone pattern | 4-6 m²/day | Significantly slower |
| Diagonal pattern | 5-7 m²/day | More cuts |
| Natural stone | 4-6 m²/day | Extra care needed |

Day Rates (2025/2026)

| Role | Day Rate (R/day) | Notes |
| --- | --- | --- |
| Experienced tiler | R1,000-1,500 | Self-employed rate |
| Junior tiler | R600-900 | Working under supervision |
| Tiler’s assistant/labourer | R400-600 | Mixing, carrying, cutting |
| Specialist tile fixer | R1,500-2,500 | Natural stone, mosaics |


### 10.4 Step-by-Step Method

Determine the total tiling area in m²

Identify the tile type and size

Look up the base labour rate for the application (floor/wall, tile type)

Identify the laying pattern and look up the pattern surcharge

Determine the tile size factor

Calculate adjusted rate: Base x (1 + Surcharge%) x Size Factor

Calculate labour cost: Area x Adjusted Rate

Alternative: Calculate by day rate

Look up daily output for the application

Days required = Area / Daily Output

Cost = Days x Day Rate

Determine if assistant is needed:

Tiles > 600mm: assistant required

Large areas (> 20 m²): assistant recommended

Add assistant cost if applicable

Compare per-m² and day-rate methods, use higher figure


### 10.5 Worked Example

Scenario: A homeowner in Durban needs a tiler for their bathroom. 600x600mm porcelain floor tiles in straight bond (8 m²), and matching wall tiles to 2.1m height (18 m²). Two walls have windows/door cuts.

Given: - Floor: 8 m², 600x600mm porcelain, straight bond - Walls: 18 m², 600x600mm porcelain, straight bond - Total area: 26 m² - Tile size: 600x600mm (size factor 1.10)

Calculation - Per m² Method:

Floor tiling: - Base rate: R200/m² (porcelain floor) - Pattern: Straight (0% surcharge) - Size factor: 1.10 - Adjusted rate: 200 x 1.0 x 1.10 = R220/m² - Floor cost: 8 x 220 = R1,760

Wall tiling: - Base rate: R250/m² (porcelain wall) - Pattern: Straight (0% surcharge) - Size factor: 1.10 - Adjusted rate: 250 x 1.0 x 1.10 = R275/m² - Wall cost: 18 x 275 = R4,950

Assistant (600mm tiles): - Days estimate: 26 m² / 7 m²/day = 3.7 days -> 4 days - Assistant: 4 x R500 = R2,000

Total Labour: R1,760 + R4,950 + R2,000 = R8,710

Calculation - Day Rate Method (comparison): - Floor: 8 m² / 10 m²/day = 0.8 days - Walls: 18 m² / 7 m²/day = 2.6 days - Total: 3.4 days -> 4 days - Tiler cost: 4 x R1,200 = R4,800 - Assistant: 4 x R500 = R2,000 - Total: R6,800

Comparison: Per m² method gives R8,710 vs Day rate R6,800. The per m² method is higher because the wall area with cuts is complex. A fair quote would be in the range of R7,500 - R8,500.


### 10.6 SANS / Regulatory Reference

SANS 10109: Workmanship standards that affect labour time

National Building Regulations: Licensed contractor requirements

Department of Labour: Minimum wage compliance (if applicable)


### 10.7 Chatbot Instruction Notes

When a customer asks about labour costs: 1. Ask for the total area to be tiled 2. Ask whether it’s floor, wall, or both 3. Ask what size and type of tiles they’re using 4. Ask what pattern they want (this significantly affects cost) 5. Calculate using both per-m² and day-rate methods 6. Present a range rather than a fixed figure 7. Explain that labour rates vary by region (Gauteng highest, rural areas lower) 8. Mention that experienced tilers charge more but work faster and better 9. Recommend getting 3 written quotes from registered contractors 10. Warn about unusually cheap quotes - they often lead to problems 11. Explain that 600mm+ tiles need two people (affects cost) 12. Mention that wall tiling costs more than floor tiling due to precision



<!-- RAG_CHUNK: calculator -->

---

## CALCULATOR 11: STAIR TILING CALCULATOR

**RAG search aliases:** stairs, risers, treads, stair nosing



### 11.1 Name and Purpose

Name: Stair Tiling Calculator Purpose: Calculates the tile area, quantities, and additional materials needed for tiling staircases, including treads, risers, nosings, and bullnose trim.

Who uses it: Contractors tiling staircases in homes, commercial buildings, and apartment complexes.


### 11.2 Formula

Tread Area (the part you step on)

Tread Area (m²) = Number of Treads x Tread Depth (m) x Stair Width (m)

Riser Area (the vertical face)

Riser Area (m²) = Number of Risers x Riser Height (m) x Stair Width (m)

Nosing Overhang Area

Nosing Area (m²) = Number of Treads x Nosing Overhang (m) x Stair Width (m)

Total Stair Tiling Area

Total Area (m²) = Tread Area + Riser Area + Nosing Area

Bullnose / Trim Length

Bullnose Length (m) = Number of Treads x Stair Width (m) x 1 (one edge per tread)

Stair-Specific Wastage

Stair Wastage Factor = 1.20 to 1.25 (20-25% additional wastage)


### 11.3 Lookup Tables

Standard Stair Dimensions (South Africa)

| Dimension | Standard Range | Notes |
| --- | --- | --- |
| Riser height (going up) | 150-180mm | 170mm typical |
| Tread depth (step depth) | 250-300mm | 280mm typical |
| Nosing overhang | 20-30mm | 25mm typical |
| Stair width (domestic) | 800-1,000mm | 900mm typical |
| Stair width (commercial) | 1,000-1,200mm |  |
| Maximum riser height (SANS) | 200mm | Building regulation limit |
| Minimum tread depth (SANS) | 250mm | Building regulation limit |

Stair Types and Tiling Considerations

| Stair Type | Tiling Approach | Difficulty |
| --- | --- | --- |
| Straight single flight | Standard | Easy |
| Straight double flight | Standard | Easy |
| Quarter-turn (L-shape) | Corner details | Moderate |
| Half-turn (U-shape) | Landing + winders | Complex |
| Spiral | Custom cuts | Very complex |
| External stairs | Slip-resistant tiles | Moderate |

Material Requirements per Standard Stair (15 steps, 900mm wide)

| Item | Quantity | Notes |
| --- | --- | --- |
| Tread tiles | 15 pieces | Cut to tread depth + nosing |
| Riser tiles | 15 pieces | Cut to riser height |
| Nosing trim / bullnose | 15 linear metres | Or tiles with factory bullnose |
| Adhesive | ~25-30 kg | Higher coverage due to edges |
| Grout | ~2-3 kg | Joints on all edges |
| Spacers | 2-3 packs | Small format for precise alignment |

Anti-Slip Requirements (SANS 10107)

| Application | Minimum Slip Rating | Tile Type |
| --- | --- | --- |
| Internal domestic stairs | R10-R11 | Matte/slight texture |
| Internal commercial stairs | R11-R12 | Textured surface |
| External stairs | R11-R12 | Anti-slip tiles |
| Wet area stairs | R12-R13 | Specialised anti-slip |


### 11.4 Step-by-Step Method

Count the number of treads (steps) on the staircase

Count the number of risers (usually one more than treads for a straight flight)

Measure the tread depth in millimetres (front to back, excluding nosing)

Measure the riser height in millimetres (vertical face)

Measure the stair width in millimetres

Measure the nosing overhang (if any) in millimetres

Calculate tread area: Treads x (Tread Depth + Nosing) x Width

Calculate riser area: Risers x Riser Height x Width

Calculate nosing area if separate tiles: Treads x Nosing x Width

Sum total tiling area

Apply stair wastage factor: 20-25%

Calculate bullnose/trim length: Treads x Width

Determine if using bullnose tiles or separate trim

Calculate adhesive (add 20% to standard rate for edges)

Calculate grout (standard rate)


### 11.5 Worked Example

Scenario: A homeowner in Pretoria wants to tile their internal straight staircase with 15 steps. The stairs are 900mm wide with 170mm risers, 280mm treads, and 25mm nosing overhang.

Given: - Number of treads: 15 - Number of risers: 15 (straight flight, top riser to landing) - Tread depth: 280mm = 0.28m - Riser height: 170mm = 0.17m - Stair width: 900mm = 0.90m - Nosing overhang: 25mm = 0.025m - Tile: 300x300mm anti-slip porcelain

Calculation:

Tread area: - Each tread: (0.28 + 0.025) x 0.90 = 0.305 x 0.90 = 0.2745 m² - Total treads: 15 x 0.2745 = 4.12 m²

Riser area: - Each riser: 0.17 x 0.90 = 0.153 m² - Total risers: 15 x 0.153 = 2.30 m²

Total tiling area: - 4.12 + 2.30 = 6.42 m²

With wastage (22%): - 6.42 x 1.22 = 7.83 m²

Bullnose trim: - 15 x 0.90 = 13.5 linear metres

Material Summary: | Material | Quantity | Est. Cost (2025) | |———-|———-|—————–| | Anti-slip tiles (7.83 m² at R350/m²) | | R2,740 | | Bullnose trim (13.5m at R120/m) | | R1,620 | | Adhesive (~50kg at R130/bag) | 3 bags | R390 | | Grout (~4kg at R100/bag) | 1 bag | R100 | | Spacers | 2 packs | R60 | | Total Materials | | ~R4,910 |

Labour Estimate: - Stair tiling: 6.42 m² at R350/m² (premium rate for stairs) = R2,247 - Or day rate: 2 days x R1,500 = R3,000

Total Stair Tiling Cost: ~R7,500 - R8,500


### 11.6 SANS / Regulatory Reference

SANS 10107: Slip resistance requirements for stair treads

SANS 10400-A: General building requirements including stair dimensions

SANS 10109: Tile adhesion requirements for vertical surfaces (risers)


### 11.7 Chatbot Instruction Notes

When a customer asks about tiling stairs: 1. Ask how many steps (treads) they have 2. Ask for the stair width, tread depth, and riser height 3. Ask if there’s a nosing overhang 4. Explain that stairs need ANTI-SLIP tiles (mandatory per SANS 10107) 5. Explain the difference between treads (horizontal) and risers (vertical) 6. Ask if they want bullnose tiles (rounded edge) or separate nosing trim 7. Calculate the total area and material quantities 8. Warn that stair tiling is specialised work - not every tiler does it well 9. Recommend a tiler with stair experience 10. Mention that open-riser stairs (floating stairs) have different requirements 11. External stairs need special consideration for weather exposure 12. Consider recommending porcelain over ceramic for stairs (higher durability)



<!-- RAG_CHUNK: calculator -->

---

## CALCULATOR 12: SKIRTING AND TRIM LENGTH CALCULATOR

**RAG search aliases:** trim, edging, skirting length, linear metres



### 12.1 Name and Purpose

Name: Skirting and Trim Length Calculator Purpose: Calculates the total linear metres of skirting tiles, edge trim, or decorative border required for a tiling project, accounting for door openings, corners, and wastage.

Who uses it: Anyone installing tiled skirtings, feature borders, or edge trims.


### 12.2 Formula

Skirting Linear Metres

Gross Skirting (m) = Room Perimeter (m) - Total Door Widths (m)

Corner Allowances

Internal Corners = Number of Internal Corners x Corner Cut Allowance (mm) External Corners = Number of External Corners x Corner Cut Allowance (mm)

Total Skirting with Wastage

Total Skirting (m) = Gross Skirting + Corner Allowances + Wastage (10%)

Skirting Tile Pieces

Skirting Height (mm) = Selected skirting height (typically 60-100mm) Skirting Piece Length = Standard tile dimension (typically 300, 400, or 600mm) Number of Pieces = Ceiling(Total Skirting / Skirting Piece Length) Number of Pieces per Box = Lookup(Box Size) Boxes Required = Ceiling(Number of Pieces / Pieces per Box)

Edge Trim Linear Metres

Edge Trim (m) = Exposed Edge Length (m) x 1.05 (5% wastage for cuts) Number of Trim Pieces = Ceiling(Edge Trim / Trim Length per piece)


### 12.3 Lookup Tables

Standard Skirting Heights

| Skirting Height | Application | Notes |
| --- | --- | --- |
| 60mm | Residential (modern, minimal) | Contemporary homes |
| 70mm | Residential (standard) | Most common in SA |
| 80mm | Residential (traditional) | Older homes |
| 100mm | Residential (generous) | High ceilings |
| 120mm | Commercial | Heavy-duty areas |
| 150mm | Commercial / wet areas | Maximum protection |

Standard Trim Lengths (South Africa)

| Trim Type | Standard Length | Notes |
| --- | --- | --- |
| Aluminium L-trim | 2.5m | Most common |
| Aluminium T-trim | 2.5m | Transition strips |
| Aluminium round edge | 2.5m | External corners |
| PVC trim (white) | 2.5m | Budget option |
| Stainless steel trim | 2.5m | Premium, commercial |
| Stair nosing | 2.5m | With anti-slip insert |
| Expansion joint trim | 2.5m | Flexible insert |

Skirting Tile Packaging

| Skirting Height | Pieces per Box | Linear Metres per Box |
| --- | --- | --- |
| 60mm (from 600x600 tile, cut 10 per tile) | 50 pieces | 30 linear metres |
| 70mm (from 600x600 tile, cut 8 per tile) | 40 pieces | 24 linear metres |
| 80mm (from 600x600 tile, cut 7 per tile) | 35 pieces | 21 linear metres |
| 100mm (from 600x600 tile, cut 6 per tile) | 30 pieces | 18 linear metres |

Corner Allowances

| Corner Type | Allowance per Corner | Notes |
| --- | --- | --- |
| Internal corner | 0mm (mitre cut) | Tiles meet at angle |
| External corner | 0mm (mitre or trim) | Use trim or mitre |
| Round external corner | Special trim piece | Radius-dependent |

Trim Applications

| Application | Trim Type | Notes |
| --- | --- | --- |
| Tile to carpet transition | T-trim or Z-bar | Height difference trim |
| Tile to vinyl transition | L-trim | Same level |
| Tile to tile transition | T-trim | Different tiles |
| External corner (wall) | Round edge / quarter-round | Protects corner |
| Internal corner | No trim (grout joint) | Grout line |
| Stair nosing | Bullnose / stair nosing | Anti-slip required |
| Expansion joint | Flexible joint trim | Allows movement |
| Perimeter joint | Scotia / quarter-round | Covers expansion gap |


### 12.4 Step-by-Step Method

Measure the perimeter of the room in metres

Measure and total all door opening widths

Calculate gross skirting: Perimeter - Door widths

Count internal and external corners

Add corner allowances (if using trim pieces for external corners)

Apply 10% wastage for cuts

Determine the skirting tile height required

Determine how the skirting tiles will be sourced:

Purchased as dedicated skirting tiles (check piece length)

Cut from field tiles (check tile dimension)

Calculate number of pieces: Total linear metres / Piece length

Round up to whole pieces

If using field tiles, calculate how many tiles need to be cut

Calculate edge trim requirements for exposed edges

Sum all trim lengths and convert to number of trim pieces


### 12.5 Worked Example

Scenario: A homeowner in Cape Town wants 80mm tiled skirting in their rectangular lounge (4.5m x 5.2m) with two door openings. They have 600x600mm floor tiles and will cut the skirting from matching tiles.

Given: - Room: 4.5m x 5.2m - Perimeter: 2 x (4.5 + 5.2) = 19.4m - Door openings: 2 doors x 0.82m each = 1.64m - Skirting height: 80mm - Cut from 600x600mm tiles (7 pieces of 80mm skirting per tile)

Calculation:

Gross skirting: - 19.4 - 1.64 = 17.76 linear metres

Corner allowances: - 4 internal corners: 0 additional (mitre cuts) - 0 external corners - Additional: 0m

With wastage (10%): - 17.76 x 1.10 = 19.54 linear metres

Pieces required: - Piece length: 600mm (cut from 600x600 tile) - Number of pieces: 19.54 / 0.6 = 32.6 -> 33 pieces

Tiles needed for skirting (cut from 600x600): - 7 pieces per tile - Tiles needed: 33 / 7 = 4.7 -> 5 tiles

Edge trim for doorway transitions: - 2 doorways x 0.90m width = 1.8 linear metres - 2.5m trim pieces needed: 1 piece

Material Summary: | Material | Quantity | Est. Cost (2025) | |———-|———-|—————–| | Tiles for skirting (cut from field tiles) | 5 tiles | Included in floor tiles | | Doorway L-trim | 1 x 2.5m | R55 | | Grout for skirting joints | Small amount | Included in floor grout | | Silicone at door frames | 1 tube | Included in ancillaries |


### 12.6 SANS / Regulatory Reference

SANS 10109: Skirting installation requirements

SANS 10400: Building regulations for skirting in different building types

SANS 10107: Skirting slip resistance in commercial applications


### 12.7 Chatbot Instruction Notes

When a customer asks about skirting or trim: 1. Ask if they want tiled skirting or edge trim (or both) 2. Ask for the room dimensions 3. Ask how many doors/openings there are 4. Ask what height skirting they want (recommend 70-80mm for standard homes) 5. Ask if they’re using matching tile cut to size or dedicated skirting tiles 6. Calculate the linear metres needed 7. Explain the difference between internal and external corners 8. For external corners, recommend a trim piece or mitre cut 9. Explain that door frames need silicone sealant, not grout 10. Mention that skirting protects the wall and hides the floor expansion gap 11. Suggest using the same tile as the floor for a seamless look 12. Mention that PVC or aluminium trims are alternatives to tiled skirting



<!-- RAG_CHUNK: calculator -->

---

## CALCULATOR 13: UNDERFLOOR HEATING AREA CALCULATOR

**RAG search aliases:** heating, electric heating, heated area, watts



### 13.1 Name and Purpose

Name: Underfloor Heating Area Calculator Purpose: Calculates the effective heated area for underfloor heating installation, accounting for perimeter exclusion zones and fixed furniture areas, then determines the heating system wattage requirements.

Who uses it: Homeowners installing underfloor heating, heating contractors, electricians, tilers working with heated floors.


### 13.2 Formula

Heated Area Calculation

Heated Area (m²) = Total Floor Area (m²) - Exclusions (m²)

Exclusions

Perimeter Zone (m²) = Floor Perimeter (m) x 0.1 (100mm exclusion) Fixed Furniture Area (m²) = Sum of all fixed furniture areas Total Exclusions = Perimeter Zone + Fixed Furniture Area

Wattage Calculation

Total Wattage (W) = Heated Area (m²) x Wattage per m² (W/m²)

Heated Area Percentage

Heated Area % = (Heated Area / Total Floor Area) x 100

Cable Length (for electric systems)

Cable Length (m) = Total Wattage (W) / Cable Wattage per metre (W/m)


### 13.3 Lookup Tables

Wattage Requirements by Application

| Application | Wattage (W/m²) | Notes |
| --- | --- | --- |
| Primary heating (well-insulated) | 100-120 | Main heat source, good insulation |
| Primary heating (poor insulation) | 130-150 | Main heat source, older building |
| Comfort/secondary heating | 60-80 | Takes chill off floor |
| Bathroom (primary) | 120-150 | Higher for warmth |
| Bathroom (comfort) | 80-100 | Warm floor feel |
| Conservatory | 150-200 | High heat loss area |
| Commercial (primary) | 120-150 | Higher occupancy |

Typical Heated Area Percentages

| Room Type | Typical Heated Area % | Notes |
| --- | --- | --- |
| Bathroom | 60-70% | Around fixtures |
| Kitchen | 50-65% | Around cabinets/island |
| Lounge | 65-85% | Around furniture layout |
| Bedroom | 60-80% | Around bed placement |
| Hallway | 80-90% | Minimal fixed furniture |
| Conservatory | 70-85% | Around perimeter |

Fixed Furniture Exclusions (Typical Sizes)

| Item | Typical Dimensions | Area |
| --- | --- | --- |
| Kitchen cupboards (floor-to-wall) | 0.6m x various | Exclude all |
| Kitchen island | 1.2m x 0.9m | Exclude |
| Bath | 1.7m x 0.7m | Exclude |
| Shower enclosure | 1.2m x 0.9m | Exclude |
| Toilet (WC) | 0.7m x 0.5m | Exclude |
| Vanity | 0.9m x 0.5m | Exclude |
| Built-in wardrobes | Various | Exclude |
| Double bed | 1.9m x 1.5m | Exclude |
| King bed | 2.0m x 1.8m | Exclude |
| Sofa | 2.0m x 0.9m | Exclude |
| Dining table | 1.8m x 1.0m | Exclude (optional) |

Electric Cable Specifications

| Cable Type | Output per Metre | Notes |
| --- | --- | --- |
| Standard heating cable | 10-20 W/m | Most common |
| High-output cable | 20-30 W/m | Faster response |
| Mesh/mat system | Fixed spacing | Pre-spaced on mesh |

System Components

| Component | Coverage | Notes |
| --- | --- | --- |
| Heating cable/mat | Per m² calculated | Main heating element |
| Thermostat | 1 per zone | Programmable recommended |
| Floor sensor | 1 per zone | Temperature feedback |
| Insulation board | Per m² | Under cable, reduces heat loss |
| Flexible adhesive | Per m² | Mandatory for heated floors |


### 13.4 Step-by-Step Method

Measure the total floor area in m²

Measure the floor perimeter in metres

Calculate the perimeter exclusion zone: Perimeter x 0.1m

Identify all fixed furniture and fixtures

Measure the area of each fixed item

Sum all exclusion areas

Calculate heated area: Total Area - Exclusions

Determine the heating purpose (primary or comfort)

Look up the appropriate wattage per m²

Calculate total wattage: Heated Area x W/m²

Select cable type and determine cable length

Calculate number of thermostats (one per zone, max 15-20 m² per zone)

List ancillary components (insulation, adhesive, thermostat)


### 13.5 Worked Example

Scenario: A homeowner in Johannesburg wants to install electric underfloor heating in their bathroom as the primary heat source. The bathroom is 2.5m x 3.0m with a bath, shower, toilet, and vanity.

Given: - Bathroom: 2.5m x 3.0m = 7.5 m² total - Perimeter: 2 x (2.5 + 3.0) = 11.0m - Heating purpose: Primary

Exclusions: - Bath: 1.7m x 0.7m = 1.19 m² - Shower: 1.2m x 0.9m = 1.08 m² - Toilet: 0.7m x 0.5m = 0.35 m² - Vanity: 0.9m x 0.5m = 0.45 m² - Perimeter zone: 11.0 x 0.1 = 1.10 m² - Total exclusions: 1.19 + 1.08 + 0.35 + 0.45 + 1.10 = 4.17 m²

Calculation: - Heated area: 7.5 - 4.17 = 3.33 m² - Heated area %: 3.33 / 7.5 = 44.4%

This is quite low - let’s reconsider the perimeter zone and shower:

Alternative (shower floor can be heated if desired): - Exclude bath, toilet, vanity only: 1.19 + 0.35 + 0.45 = 1.99 m² - Perimeter zone: 1.10 m² - Total exclusions: 3.09 m² - Heated area: 7.5 - 3.09 = 4.41 m² - Heated area %: 58.8% (better)

Wattage (primary heating, bathroom): - 130 W/m² (midpoint of 120-150) - Total wattage: 4.41 x 130 = 573 W

Cable length (18 W/m cable): - 573 / 18 = 31.8m -> 32m cable

Material Summary: | Component | Quantity | Est. Cost (2025) | |———–|———-|—————–| | Heating cable (32m) | 1 system | R2,500 | | Thermostat (programmable) | 1 | R1,200 | | Floor sensor | 1 | R350 | | Insulation board (4.5 m²) | 5 boards | R800 | | Flexible adhesive | ~25kg | R350 | | Total System Cost | | ~R5,200 |


### 13.6 SANS / Regulatory Reference

SANS 10109: Flexible adhesive mandatory for underfloor heating

SANS 10400-A: Energy efficiency requirements for heating systems

SANS 10142-1: Electrical installation code for heating cables

IEC 60800: Standard for heating cables


### 13.7 Chatbot Instruction Notes

When a customer asks about underfloor heating: 1. Ask what room they want to heat 2. Ask the room dimensions 3. Ask what fixtures/furniture are fixed (bath, shower, cupboards, etc.) 4. Ask if it’s for primary heating or just comfort (warm floor) 5. Calculate the heated area with exclusions 6. Calculate the wattage needed 7. Explain that heating cables CANNOT go under fixed furniture 8. Explain that a 100mm perimeter exclusion is required 9. Emphasise that flexible adhesive MUST be used with heated floors 10. Recommend insulation boards underneath to improve efficiency 11. Mention that a programmable thermostat saves on electricity costs 12. Explain that underfloor heating adds 10-20mm to floor height 13. Recommend a qualified electrician for all electrical connections 14. Warn that the heating system must be tested before tiling over it



<!-- RAG_CHUNK: calculator -->

---

## CALCULATOR 14: MOVEMENT JOINT SPACING CALCULATOR

**RAG search aliases:** expansion joints, movement joints, spacing, perimeter joint



### 14.1 Name and Purpose

Name: Movement Joint Spacing Calculator Purpose: Calculates the required spacing, width, and number of movement joints for a tiled installation based on substrate type, environment, and tile dimensions, in accordance with SANS 10109 and BS 5385.

Who uses it: Contractors, architects, quantity surveyors, tilers planning large installations.


### 14.2 Formula

Maximum Joint Spacing

Max Spacing (m) = Lookup(Substrate Type, Environment)

Number of Joints Required

Number of Joints in Direction = Ceiling(Room Dimension (m) / Max Spacing (m)) - 1

Joint Width Calculation

Joint Width (mm) = (Coefficient of Expansion x Temperature Range x Distance (mm)) + Safety Factor

Simplified Joint Width

For joints up to 3m: Minimum 6mm For each additional metre beyond 3m: +2mm

Total Joint Length

Total Joint Length (m) = Sum of all joint lengths in both directions

Joint Filler Required

Joint Filler (m) = Total Joint Length (m) Backing Rod (m) = Total Joint Length (m) Sealant (L) = Total Joint Length (m) x Joint Width (mm) x Joint Depth (mm) / 1,000,000


### 14.3 Lookup Tables

Maximum Joint Spacing (SANS 10109 / BS 5385)

| Location | Substrate Type | Max Spacing (m) | Notes |
| --- | --- | --- | --- |
| Interior floors | Concrete slab (ground bearing) | 8m x 8m | Standard commercial |
| Interior floors | Suspended concrete floor | 4.5m x 4.5m | More movement |
| Interior floors | Timber floor (overboarded) | 3m x 3m | High movement |
| Interior floors | Screed on insulation | 4m x 4m | Floating construction |
| Exterior floors / balconies | Concrete | 3m x 3m | Weather exposure |
| Exterior floors / terraces | Screed | 2.5m x 2.5m | Maximum exposure |
| Facades / cladding | Various backing | 3m x 3m | Vertical, wind loading |
| Wet areas | Concrete/screed | 3m x 3m | Moisture movement |
| Heated floors | Concrete/screed | 3m x 3m | Thermal cycling |

Joint Width Requirements

| Distance Between Joints | Minimum Joint Width | Sealant Depth |
| --- | --- | --- |
| Up to 3m | 6mm | 6-10mm |
| 3-4m | 8mm | 8-10mm |
| 4-6m | 10mm | 10-12mm |
| 6-8m | 12mm | 12-15mm |
| 8-10m | 14mm | 14-16mm |

Coefficient of Thermal Expansion

| Tile Material | Coefficient (x 10^-6 / °C) | Notes |
| --- | --- | --- |
| Ceramic (porcelain) | 4-6 | Most common |
| Ceramic (earthenware) | 5-7 | Higher absorption |
| Natural stone (granite) | 7-9 | Varies by type |
| Natural stone (marble) | 10-14 | High expansion |
| Natural stone (travertine) | 8-12 | Varies by type |
| Glass mosaic | 9-10 | Different from ceramic |
| Terrazzo tiles | 10-12 | Cement-based |

Typical Temperature Ranges (South Africa)

| Location | Temperature Range (°C) | Notes |
| --- | --- | --- |
| Interior (heated/cooled) | 10-15 | Stable environment |
| Interior (unheated) | 15-25 | Moderate variation |
| Exterior (coastal) | 20-30 | Mild climate |
| Exterior (Highveld) | 30-40 | Large variation |
| Exterior (Karoo) | 35-45 | Extreme variation |
| Facade (sunny side) | 40-60 | Solar gain |

Joint Types and Applications

| Joint Type | Application | Notes |
| --- | --- | --- |
| Structural (building) | Across structural joints | Must align |
| Construction | Changes in substrate | Different materials |
| Perimeter | Around room edges | Mandatory |
| Intermediate | Large area division | Regular spacing |
| Isolation | Around columns/pipes | Isolates movement |
| Control | In screed only | Below tile joints |

Joint Filler Materials

| Filler Type | Application | Movement Accommodation |
| --- | --- | --- |
| Polyurethane sealant | General purpose | +/- 25% |
| Silicone sealant | Wet areas | +/- 50% |
| Polysulphide sealant | Heavy duty | +/- 25% |
| Epoxy (rigid) | No movement | 0% |
| Preformed compressible | Large joints | High accommodation |


### 14.4 Step-by-Step Method

Determine the total tiled area dimensions (length and width)

Identify the substrate type (concrete, suspended, timber, etc.)

Determine the location (interior, exterior, wet area, heated)

Look up the maximum joint spacing from the table

Calculate number of joints in length direction

Calculate number of joints in width direction

Determine the tile material and look up thermal expansion coefficient

Determine the expected temperature range for the location

Calculate joint width using the formula or simplified method

Calculate total joint length (sum of all joints in both directions)

Select appropriate joint filler material

Calculate sealant quantity needed

Calculate backing rod quantity

Draw a sketch showing joint locations


### 14.5 Worked Example

Scenario: A shopping centre in Centurion is tiling a 24m x 18m ground floor area with 600x600mm porcelain tiles on a concrete slab. Interior, air-conditioned environment.

Given: - Area: 24m x 18m - Substrate: Concrete slab (ground bearing) - Location: Interior, air-conditioned - Tile: Porcelain (coefficient: 5 x 10^-6 / °C) - Temperature range: 12°C (10-15°C variation, air-conditioned)

Calculation:

Maximum spacing: - Interior, concrete slab: 8m x 8m

Number of joints in 24m direction: - 24 / 8 = 3 bays - Number of intermediate joints: 3 - 1 = 2 joints - Plus perimeter joints at 0m and 24m (already at walls)

Number of joints in 18m direction: - 18 / 8 = 2.25 -> need joints - Use 6m spacing: 18 / 6 = 3 bays - Number of intermediate joints: 3 - 1 = 2 joints

Joint width: - Using simplified method for 8m spacing: - Base 6mm for up to 3m - Additional: (8 - 3) x 2mm = 10mm - Total: 6 + 10 = 16mm - Wait, that seems too wide. Let’s recalculate using the proper method:

Joint Width = (Coefficient x Temperature Range x Distance) + Safety Factor - Coefficient: 5 x 10^-6 / °C - Temperature range: 12°C - Distance: 8,000mm (8m in mm) - Safety factor: 2mm

Joint Width = (5 x 10^-6 x 12 x 8000) + 2 = (0.000005 x 12 x 8000) + 2 = 0.48 + 2 = 2.48mm

This is below the minimum, so we use the practical minimum of 6mm.

Total joint length: - Joints in 24m direction: 2 joints x 18m wide = 36m - Joints in 18m direction: 2 joints x 24m long = 48m - Perimeter joint: (24 + 18) x 2 = 84m - Total: 36 + 48 + 84 = 168 linear metres

Sealant required (6mm wide x 10mm deep): - Volume per metre: 6 x 10 = 60 mm² per mm of length - Wait: 6mm x 10mm = 60 mm² cross-section - Per metre: 60 x 1000 = 60,000 mm³ = 0.06 L/m - Total: 168 x 0.06 = 10.08 L

Backing rod: - 168 linear metres

Material Summary: | Material | Quantity | Est. Cost (2025) | |———-|———-|—————–| | Polyurethane sealant (cartridges) | 11 L | R1,650 | | Backing rod (6mm) | 168m | R340 | | Movement joint profiles (if used) | As needed | Variable | | Total | | ~R2,000 |


### 14.6 SANS / Regulatory Reference

SANS 10109: Code of Practice for Tiling - movement joint requirements

BS 5385: British Standard (referenced in SANS for movement joint tables)

SANS 10400-J: Structural movement considerations

SANS 10142: Building expansion joint coordination


### 14.7 Chatbot Instruction Notes

When a customer asks about movement joints: 1. Ask about the size of the area being tiled 2. Ask what the floor is made of (concrete slab, suspended floor, etc.) 3. Ask if it’s inside or outside 4. Ask if the area has underfloor heating 5. Calculate the maximum spacing and number of joints needed 6. Explain that movement joints PREVENT tiles from cracking 7. Emphasise that perimeter joints are MANDATORY in every installation 8. Explain that large areas MUST have intermediate joints 9. Mention that joints must go through the tile AND the adhesive bed 10. Recommend polyurethane sealant for most applications 11. Explain that movement joints are often the most neglected part of tiling 12. Show the customer where joints should be placed 13. For areas over 8m in any direction, stress that intermediate joints are essential



<!-- RAG_CHUNK: calculator -->

---

## CALCULATOR 15: STRUCTURAL LOAD CALCULATOR

**RAG search aliases:** tile weight, floor load, slab load, kg per m2



### 15.1 Name and Purpose

Name: Structural Load Calculator Purpose: Calculates the total dead load imposed by a tiled floor system on the building structure, including tiles, adhesive, screed, and underfloor heating, to ensure the floor can support the weight.

Who uses it: Architects, structural engineers, builders, and homeowners installing heavy tiling systems (especially on upper floors or suspended slabs).


### 15.2 Formula

Total Dead Load

Total Load (kg/m²) = Tile Weight + Adhesive Weight + Screed Weight + Underlayment Weight + Additional Layers

Component Weights

Tile Weight (kg/m²) = Tile Thickness (mm) x Tile Density (kg/m² per mm) Adhesive Weight (kg/m²) = Adhesive Thickness (mm) x 1.8 (kg/m² per mm) Screed Weight (kg/m²) = Screed Thickness (mm) x 2.0 (kg/m² per mm)

Load Comparison

Safety Factor = Allowable Floor Load (kg/m²) / Total Load (kg/m²) If Safety Factor >= 1.5: Safe If Safety Factor < 1.5: Engineering review required

Total Floor Load

Total Floor Load (kg) = Total Load (kg/m²) x Area (m²) Total Floor Load (kN) = Total Floor Load (kg) x 9.81 / 1000


### 15.3 Lookup Tables

Tile Weights by Type

| Tile Type | Thickness | Weight per m² | Density Factor |
| --- | --- | --- | --- |
| Ceramic wall tile | 6-8mm | 12-16 kg/m² | ~2.0 kg/m² per mm |
| Ceramic floor tile | 9-10mm | 18-22 kg/m² | ~2.1 kg/m² per mm |
| Porcelain tile (standard) | 9-11mm | 20-25 kg/m² | ~2.3 kg/m² per mm |
| Porcelain tile (heavy duty) | 11-14mm | 25-35 kg/m² | ~2.5 kg/m² per mm |
| Large format porcelain | 12-15mm | 28-38 kg/m² | ~2.5 kg/m² per mm |
| Extra-large / porcelain slab | 12-20mm | 30-50 kg/m² | ~2.5 kg/m² per mm |
| Natural stone (granite) | 20-30mm | 55-80 kg/m² | ~2.7 kg/m² per mm |
| Natural stone (marble) | 20mm | 54 kg/m² | ~2.7 kg/m² per mm |
| Natural stone (travertine) | 12-20mm | 28-48 kg/m² | ~2.4 kg/m² per mm |
| Mosaic (with mesh) | 4-6mm | 8-12 kg/m² | ~2.0 kg/m² per mm |
| Terrazzo tile | 15-25mm | 35-60 kg/m² | ~2.4 kg/m² per mm |

Adhesive Weights

| Application | Thickness | Weight per m² |
| --- | --- | --- |
| Standard wall tile | 3-4mm | 5-7 kg/m² |
| Standard floor tile | 5-8mm | 9-14 kg/m² |
| Large format floor | 8-12mm | 14-22 kg/m² |
| With back-buttering | 10-15mm total | 18-27 kg/m² |
| Full adhesive bed | 10mm | 18 kg/m² |

Screed Weights

| Screed Type | Thickness | Weight per m² |
| --- | --- | --- |
| Bonded screed (min) | 15mm | 30 kg/m² |
| Standard bonded screed | 25mm | 50 kg/m² |
| Standard bonded screed | 40mm | 80 kg/m² |
| Unbonded screed (min) | 35mm | 70 kg/m² |
| Floating screed (min) | 35mm | 70 kg/m² |
| Heavy screed | 50mm | 100 kg/m² |
| Thick screed | 75mm | 150 kg/m² |

Additional Layer Weights

| Layer | Typical Weight | Notes |
| --- | --- | --- |
| Self-levelling compound (3mm) | 5 kg/m² | Per 3mm |
| Waterproofing membrane | 1-2 kg/m² | Two coats |
| Underfloor heating (electric) | 2-4 kg/m² | Cable + insulation |
| Underfloor heating (hydronic) | 10-15 kg/m² | Pipes + water |
| Insulation board | 2-5 kg/m² | Underfloor heating |
| Damp-proof membrane | 0.5 kg/m² | Sheet membrane |
| Tile grout | 0.5-1 kg/m² | In joints only |

Floor Load Capacity (SANS 10400)

| Floor Type | Allowable Load | Notes |
| --- | --- | --- |
| Residential ground floor (concrete slab) | 300-500 kg/m² | Ground bearing |
| Residential suspended floor (concrete) | 200-300 kg/m² | Depends on design |
| Residential timber floor | 150-200 kg/m² | May need reinforcement |
| Commercial concrete floor | 300-500 kg/m² | Designed for higher loads |
| Roof terrace / balcony | 200-300 kg/m² | Check structural design |
| Mezzanine floor | Check engineer | Always verify |


### 15.4 Step-by-Step Method

Identify the tile type and thickness

Look up tile weight per m² (or calculate: thickness x density factor)

Identify the adhesive application and thickness

Look up or calculate adhesive weight per m²

Determine if a screed is required

Look up screed weight per m² based on thickness

Identify any additional layers (waterproofing, heating, insulation)

Sum all component weights for total load per m²

Identify the floor type and allowable load capacity

Calculate safety factor: Allowable / Total

Assess if the installation is structurally safe

If safety factor < 1.5, recommend engineering consultation


### 15.5 Worked Example

Scenario: An architect is specifying large format porcelain tiles for a bathroom on the second floor of a house (suspended concrete slab). The specification includes a waterproofing membrane, 25mm screed, and 12mm thick porcelain tiles with 10mm adhesive bed.

Given: - Floor type: Residential suspended concrete slab - Tile: 12mm thick large format porcelain - Adhesive: 10mm bed - Screed: 25mm bonded - Waterproofing: Liquid membrane (2 coats) - Area: 12 m²

Calculation:

Component weights: - Tile weight: 12mm x 2.5 kg/m²/mm = 30 kg/m² - Adhesive weight: 10mm x 1.8 kg/m²/mm = 18 kg/m² - Screed weight: 25mm x 2.0 kg/m²/mm = 50 kg/m² - Waterproofing: 2 kg/m² (from table) - Grout: 1 kg/m² (allowance)

Total load per m²: - 30 + 18 + 50 + 2 + 1 = 101 kg/m²

Safety check: - Allowable load (suspended residential): 200-300 kg/m², use 250 kg/m² - Safety factor: 250 / 101 = 2.47 - 2.47 >= 1.5: SAFE

Total floor load: - 101 kg/m² x 12 m² = 1,212 kg - In kN: 1,212 x 9.81 / 1000 = 11.9 kN

Load Breakdown: | Component | Weight (kg/m²) | % of Total | |———–|—————|————| | Tile | 30 | 29.7% | | Adhesive | 18 | 17.8% | | Screed | 50 | 49.5% | | Waterproofing | 2 | 2.0% | | Grout | 1 | 1.0% | | Total | 101 | 100% |


### 15.6 SANS / Regulatory Reference

SANS 10400-B: Structural design - floor load capacity

SANS 10400-J: Floor finishes and imposed loads

SANS 10109: Tile adhesion and substrate requirements

SANS 10160: Basis of structural design and actions for building


### 15.7 Chatbot Instruction Notes

When a customer asks about structural loads: 1. Ask what floor they’re tiling (ground floor, upper floor, timber, concrete) 2. Ask what type of tiles they’re using and the thickness 3. Ask if they’re having a screed installed (this is usually the heaviest component) 4. Ask about any additional layers (waterproofing, underfloor heating) 5. Calculate the total load per m² 6. Compare to the allowable load for their floor type 7. Explain that the SCREED is usually the heaviest component 8. If the safety factor is below 1.5, recommend they consult a structural engineer 9. For timber floors, be extra cautious - they have lower load capacity 10. For upper floors in older buildings, recommend checking the slab capacity 11. Mention that natural stone tiles are significantly heavier than ceramic/porcelain 12. Explain that removing an existing screed and replacing with self-levelling compound can reduce load



<!-- RAG_CHUNK: calculator -->

---

## CALCULATOR 16: FLOOR REMOVAL AND DISPOSAL COST CALCULATOR

**RAG search aliases:** old tile removal, disposal, skip, rubble



### 16.1 Name and Purpose

Name: Floor Removal and Disposal Cost Calculator Purpose: Estimates the cost of removing existing flooring, preparing the substrate, and disposing of rubble, including labour, equipment, and skip/bin hire.

Who uses it: Homeowners planning renovations, contractors preparing removal quotes, project managers budgeting for strip-out work.


### 16.2 Formula

Removal Cost

Removal Cost (R) = Area (m²) x Removal Rate (R/m²)

Thinset/Adhesive Grinding

Grinding Cost (R) = Area (m²) x Grinding Rate (R/m²)

Disposal Cost

Disposal Cost (R) = Number of Loads x Cost per Load (R) Number of Loads = Ceiling(Total Debris Volume (m³) / Vehicle Capacity (m³))

Total Removal and Preparation Cost

Total Cost (R) = Removal Cost + Grinding Cost + Disposal Cost + Access Cost + Protection Cost


### 16.3 Lookup Tables

Removal Rates by Floor Type (2025/2026)

| Floor Type | Removal Rate (R/m²) | Notes |
| --- | --- | --- |
| Ceramic floor tiles | R50-100 | Standard removal |
| Porcelain floor tiles | R60-120 | Harder material |
| Natural stone | R80-150 | Heavy, labour-intensive |
| Vinyl sheeting (loose) | R15-30 | Easy removal |
| Vinyl tiles | R25-40 | Adhesive residue |
| Laminate flooring | R20-40 | Floating floor, easy |
| Carpet (with underlay) | R15-30 | Quick removal |
| Cork flooring | R30-50 | Adhesive residue |
| Terrazzo | R100-200 | Very difficult |
| Epoxy coating | R80-150 | Chemical removal |
| Existing screed | R60-120 | Dusty work |

Wall Tile Removal Rates (2025/2026)

| Wall Type | Removal Rate (R/m²) | Notes |
| --- | --- | --- |
| Ceramic wall tiles | R60-120 | Vertical work |
| Porcelain wall tiles | R70-150 | Harder material |
| Mosaic tiles | R80-160 | Many small pieces |
| Natural stone wall tiles | R100-200 | Heavy |
| Subway tiles | R50-100 | Standard removal |

Thinset/Adhesive Grinding Rates

| Substrate Condition | Grinding Rate (R/m²) | Notes |
| --- | --- | --- |
| Light adhesive residue | R20-40 | Quick pass |
| Moderate adhesive residue | R40-70 | Standard preparation |
| Heavy adhesive residue | R60-100 | Multiple passes |
| Screed removal + grind | R80-150 | To concrete slab |
| Concrete scarification | R50-80 | Mechanical preparation |

Disposal Options and Costs

| Disposal Method | Capacity | Cost (2025) | Notes |
| --- | --- | --- | --- |
| Small skip (2m³) | 2 cubic metres | R1,500-2,000 | Small bathrooms |
| Medium skip (4m³) | 4 cubic metres | R2,500-3,500 | Standard rooms |
| Large skip (6m³) | 6 cubic metres | R3,500-4,500 | Multiple rooms |
| Large skip (9m³) | 9 cubic metres | R4,500-6,000 | Full house |
| Tip truck load | 4-6m³ | R2,000-3,000 | Per load |
| Builder’s rubble bag (1m³) | 1 cubic metre | R400-600 | Small jobs |
| Self-disposal (private tip) | Variable | R200-400/tonne | Own transport |

Debris Volume by Floor Type

| Floor Type | Debris per m² | Notes |
| --- | --- | --- |
| Ceramic tiles + adhesive | 0.03-0.05 m³/m² | ~50-80 kg/m² |
| Porcelain tiles + adhesive | 0.04-0.06 m³/m² | ~60-100 kg/m² |
| Natural stone | 0.05-0.08 m³/m² | ~80-120 kg/m² |
| Screed (25mm) | 0.03-0.04 m³/m² | ~50-70 kg/m² |
| Screed (50mm) | 0.05-0.07 m³/m² | ~100-140 kg/m² |
| Vinyl/carpet | 0.01-0.02 m³/m² | ~10-20 kg/m² |

Access Cost Adjustments

| Access Condition | Cost Adjustment | Notes |
| --- | --- | --- |
| Ground floor, direct access | No adjustment | Standard |
| Upper floor, stair access | +20-30% | Labour for carrying |
| Upper floor, lift access | +10-15% | Lift availability |
| Upper floor, crane required | +50-100% | Specialist equipment |
| Limited working hours | +15-25% | After-hours/ weekends |
| Remote location | +20-40% | Travel time |


### 16.4 Step-by-Step Method

Identify the existing floor type to be removed

Measure the area to be removed in m²

Look up the removal rate for that floor type

Calculate removal cost: Area x Rate

Assess the condition of the substrate after removal

Determine if grinding/scarification is needed

Look up grinding rate if applicable

Calculate grinding cost: Area x Grinding Rate

Calculate total debris volume using debris table

Select appropriate disposal method (skip size)

Calculate disposal cost

Assess access conditions and apply adjustments

Sum all costs for total removal cost


### 16.5 Worked Example

Scenario: A homeowner in Durban is renovating their kitchen and needs to remove existing ceramic floor tiles. The kitchen is 3.5m x 4.0m (14 m²) on the ground floor with direct access. Moderate adhesive residue is expected.

Given: - Area: 14 m² - Existing floor: Ceramic tiles - Floor level: Ground floor - Access: Direct (sliding door to garden) - Adhesive residue: Moderate (expected)

Calculation:

Removal cost: - 14 m² x R75/m² (midpoint of R50-100) = R1,050

Grinding cost: - 14 m² x R55/m² (midpoint of R40-70) = R770

Debris volume: - Ceramic tiles + adhesive: 0.04 m³/m² (midpoint) - Total debris: 14 x 0.04 = 0.56 m³

Disposal: - 0.56 m³: Use builder’s rubble bags or small skip - 1 x builder’s rubble bag (1m³): R500 - Or share a small skip: R1,500 (if other work ongoing) - Select: 1 x rubble bag = R500

Access adjustment: - Ground floor, direct access: No adjustment

Total Removal Cost: | Item | Cost | |——|——| | Tile removal (14 m² x R75) | R1,050 | | Adhesive grinding (14 m² x R55) | R770 | | Rubble disposal (1 bag) | R500 | | Total (excl. VAT) | R2,320 | | VAT (15%) | R348 | | Total (incl. VAT) | R2,668 |


### 16.6 SANS / Regulatory Reference

SANS 10109: Substrate preparation requirements after removal

SANS 10400-J: Floor preparation standards

Occupational Health and Safety Act: Dust control during removal

Municipal bylaws: Rubble disposal regulations


### 16.7 Chatbot Instruction Notes

When a customer asks about floor removal: 1. Ask what type of floor they currently have 2. Ask the area to be removed 3. Ask what floor level (ground, upstairs) and access conditions 4. Ask if they’re doing the removal themselves or hiring someone 5. Calculate removal cost based on floor type 6. ALWAYS recommend including grinding/cleaning of the substrate 7. Explain that tiling over old adhesive residue causes failure 8. Mention that removal creates a LOT of dust - recommend sealing off the area 9. Advise on skip/bin sizes - most people underestimate debris volume 10. Mention that some tilers include removal in their quote, others don’t 11. Recommend dust extraction if available (reduces mess significantly) 12. Warn about asbestos in older vinyl flooring (pre-1990s) - needs specialist removal



<!-- RAG_CHUNK: calculator -->

---

## CALCULATOR 17: PRIMER AND PREPARATION CALCULATOR

**RAG search aliases:** primer, preparation, substrate prep



### 17.1 Name and Purpose

Name: Primer and Preparation Calculator Purpose: Calculates the quantities of primers, sealers, and preparation chemicals needed for different substrate types before tiling, including coverage rates and drying times between coats.

Who uses it: Tilers, contractors, and DIY enthusiasts preparing substrates for tiling.


### 17.2 Formula

Primer Quantity

Primer (L) = Area (m²) x Primer Coverage (L/m²) x Number of Coats

Sealer Quantity

Sealer (L) = Area (m²) x Sealer Coverage (L/m²) x Number of Coats

Total Preparation Time

Total Time = Sum of all coat drying times + 24 hours safety buffer

Dilution Calculation

Working Solution (L) = Concentrate (L) x Dilution Ratio


### 17.3 Lookup Tables

Primer Coverage by Substrate Type

| Substrate Type | Primer Type | Coverage (L/m²) | Coats | Notes |
| --- | --- | --- | --- | --- |
| Absorbent concrete | Acrylic primer | 0.2-0.3 | 1 | May need 2 if very porous |
| Non-absorbent concrete | Epoxy primer | 0.15-0.2 | 1 | Power-floored surface |
| Screed (cement) | Acrylic primer | 0.2-0.3 | 1 | Ensure fully cured |
| Old ceramic tiles | Special primer | 0.2-0.3 | 1 | Bonding bridge |
| Painted surfaces | Special primer | 0.2-0.3 | 1 | After scarification |
| Wooden floors | Flexible primer | 0.2-0.3 | 1 | Over tile backer board |
| Gypsum plaster | Special primer | 0.3-0.4 | 1 | Low suction primer |
| Anhydrite screed | Special primer | 0.2-0.3 | 1 | Must be laitance-free |
| Bitumen | Special primer | 0.15-0.2 | 1 | Check compatibility |
| Metal | Metal primer | 0.15-0.2 | 1 | Very rare in tiling |

Sealer Coverage by Type

| Sealer Type | Coverage (L/m²) | Coats | Notes |
| --- | --- | --- | --- |
| Penetrating sealer (natural stone) | 0.1-0.2 | 2 | Before and after grouting |
| Surface sealer (ceramic) | 0.05-0.1 | 1-2 | Optional protection |
| Colour-enhancing sealer | 0.1-0.2 | 2 | For natural stone |
| Anti-stain sealer | 0.1-0.15 | 2 | Kitchens/bathrooms |
| Efflorescence blocker | 0.1-0.15 | 1 | Over concrete/screed |

Drying Times by Product Type

| Product Type | Tack-Free | Ready for Next Coat | Ready for Tiling | Full Cure |
| --- | --- | --- | --- | --- |
| Acrylic primer | 30-60 min | 2-4 hours | 4-6 hours | 24 hours |
| Epoxy primer | 4-6 hours | 12-24 hours | 24 hours | 7 days |
| Polyurethane primer | 1-2 hours | 4-6 hours | 6-8 hours | 48 hours |
| Latex primer | 30-60 min | 2-3 hours | 4-6 hours | 24 hours |
| Penetrating sealer | 30 min | 1-2 hours | N/A | 24 hours |
| Surface sealer | 1-2 hours | 4-6 hours | N/A | 48 hours |

Preparation Product Costs (2025)

| Product | Container Size | Price Range | Coverage |
| --- | --- | --- | --- |
| Standard acrylic primer | 5 L | R200-350 | 20-25 m² |
| High-bond primer | 5 L | R350-500 | 20-25 m² |
| Epoxy primer | 5 L | R500-800 | 25-35 m² |
| Flexible primer | 5 L | R400-600 | 20-25 m² |
| Penetrating sealer | 5 L | R350-600 | 25-50 m² |
| Surface sealer | 5 L | R250-400 | 50-100 m² |
| Efflorescence blocker | 5 L | R300-450 | 35-50 m² |
| Bonding agent (slurry) | 5 L | R250-400 | 10-15 m² |
| Tile cleaner | 1 L | R80-150 | 20-30 m² |
| Grout remover | 1 L | R100-180 | 10-15 m² |


### 17.4 Step-by-Step Method

Identify the substrate type (concrete, screed, old tiles, wood, etc.)

Identify the substrate condition (new, old, dusty, painted, etc.)

Look up the appropriate primer type and coverage rate

Determine the number of coats needed

Calculate primer quantity: Area x Coverage x Coats

Determine if sealing is needed (natural stone, porous tiles)

Look up sealer type and coverage

Calculate sealer quantity: Area x Coverage x Coats

Determine total preparation time from drying times table

Add 24-hour safety buffer before tiling

Present material list with estimated costs


### 17.5 Worked Example

Scenario: A contractor in Port Elizabeth is preparing a newly screeded floor (15 m²) for porcelain tile installation. The screed is 3 weeks old and fully cured.

Given: - Area: 15 m² - Substrate: Cement screed (3 weeks old) - Condition: Clean, dust-free, fully cured - Tile: Porcelain (non-porous, no sealing needed)

Calculation:

Primer: - Type: Acrylic primer for screed - Coverage: 0.25 L/m² (midpoint of 0.2-0.3) - Coats: 1 - Quantity: 15 x 0.25 x 1 = 3.75 L - Container: 5 L (standard size) - Cost: R280 (midpoint)

Sealer: - Porcelain tiles: Not required (non-porous) - Quantity: 0 L - Cost: R0

Timing: - Primer application: 30 minutes - Tack-free: 1 hour - Ready for tiling: 5 hours (midpoint of 4-6) - Safety buffer: 24 hours - Total: Apply primer, wait 5 hours minimum, then tile next day

Material Summary: | Product | Quantity | Cost | |———|———-|——| | Acrylic primer (5 L) | 1 container | R280 | | Sealer | Not required | R0 | | Total | | R280 |

Timeline: - Day 1 (morning): Apply primer - Day 1 (afternoon): Primer dry, ready for tiling - Day 2: Commence tiling


### 17.6 SANS / Regulatory Reference

SANS 10109: Substrate preparation and priming requirements

SANS 10400-J: Floor preparation standards

Manufacturer specifications: Always follow manufacturer’s guidelines


### 17.7 Chatbot Instruction Notes

When a customer asks about primers and preparation: 1. Ask what their floor/substrate is made of (concrete, screed, old tiles, etc.) 2. Ask if it’s new or existing, and what condition it’s in 3. Look up the appropriate primer type for their substrate 4. Calculate the quantity needed 5. Explain WHY priming is important (prevents loose tiles) 6. Explain that different substrates need different primers 7. Give them the drying time so they can plan their schedule 8. Mention that priming is often skipped by cheap tilers - and that’s when tiles come loose 9. For natural stone tiles, explain they also need sealing (before AND after grouting) 10. Mention that some primers need diluting - always read the manufacturer’s instructions 11. Recommend applying primer just before tiling (not days before) 12. Explain that dusty or chalky surfaces MUST be primed



<!-- RAG_CHUNK: calculator -->

---

## CALCULATOR 18: LVT AND LAMINATE PLANK QUANTITY CALCULATOR

**RAG search aliases:** vinyl, laminate, planks, glue down lvt



### 18.1 Name and Purpose

Name: LVT and Laminate Plank Quantity Calculator Purpose: Calculates the quantity of Luxury Vinyl Tile (LVT), laminate flooring planks, and associated materials (underlay, spacers, trim) needed for an installation, including pattern-specific wastage calculations.

Who uses it: Homeowners choosing LVT or laminate flooring, flooring contractors, retailers.


### 18.2 Formula

Plank/Tile Area

Plank Area (m²) = (Plank Length (mm) / 1000) x (Plank Width (mm) / 1000)

Number of Planks Required

Gross Planks = Ceiling(Area (m²) / Plank Area (m²)) Planks with Wastage = Ceiling(Gross Planks x (1 + Wastage % / 100)) Packs Required = Ceiling(Planks with Wastage / Planks per Pack)

Underlay Quantity

Underlay (m²) = Floor Area (m²) x 1.05 (5% overlap wastage) Underlay Rolls = Ceiling(Underlay (m²) / Coverage per Roll (m²))

Expansion Gap

Expansion Gap (mm) = (Room Perimeter (m) x 1000) x 8-10mm per 10m run Standard gap: 8-10mm from all walls


### 18.3 Lookup Tables

LVT Plank Sizes (Common in SA)

| Size (mm) | Planks per Pack | Coverage per Pack | Common Use |
| --- | --- | --- | --- |
| 1210 x 190 x 5mm | 8-10 | 1.84-2.30 m² | Standard residential |
| 1210 x 170 x 4mm | 10-12 | 2.06-2.47 m² | Budget residential |
| 1220 x 180 x 4.2mm | 10 | 2.20 m² | Common import size |
| 1510 x 220 x 6mm | 6-8 | 1.99-2.66 m² | Premium wide plank |
| 610 x 305 x 5mm (tile format) | 8-10 | 1.49-1.86 m² | Stone/tile look |
| 914 x 457 x 5mm (tile format) | 6-8 | 2.51-3.34 m² | Large tile look |

Laminate Plank Sizes (Common in SA)

| Size (mm) | Planks per Pack | Coverage per Pack | Common Use |
| --- | --- | --- | --- |
| 1285 x 192 x 8mm | 8-9 | 1.97-2.22 m² | Standard 8mm |
| 1285 x 192 x 12mm | 6-8 | 1.48-1.97 m² | Heavy-duty 12mm |
| 1380 x 193 x 8mm | 8 | 2.13 m² | Premium import |
| 1210 x 195 x 8mm | 8 | 1.89 m² | Common domestic |
| 852 x 156 x 7mm | 9-10 | 1.20-1.33 m² | Compact/utility |

Wastage by Pattern

| Pattern | Wastage % | Notes |
| --- | --- | --- |
| Straight lay | 5-8% | Standard, planks aligned |
| Random stagger | 7-10% | Varied end joints |
| Brick bond / 1/3 offset | 8-12% | Regular offset pattern |
| Herringbone | 15-20% | Complex angular cuts |
| Diagonal | 15-18% | 45-degree angle |
| Chevron | 18-22% | Special chevron planks |

Underlay Types and Coverage

| Underlay Type | Thickness | Coverage per Roll | Price per Roll | Use |
| --- | --- | --- | --- | --- |
| Foam underlay | 2-3mm | 15 m² | R80-150 | Budget laminate |
| Combined underlay + DPM | 3mm | 15 m² | R150-250 | LVT/concrete |
| Rubber underlay | 3-5mm | 10 m² | R200-350 | Premium sound |
| Fibreboard underlay | 5-7mm | 7 m² | R250-400 | Heavy-duty laminate |
| Acoustic underlay | 3-5mm | 10 m² | R300-500 | Apartments/flats |
| Self-levelling underlay | 1-3mm | 15 m² | R200-350 | Minor levelling |

Trim Requirements

| Trim Type | Application | Standard Length | Notes |
| --- | --- | --- | --- |
| Scotia/beading | Perimeter expansion gap cover | 2.4m | Matches floor colour |
| T-bar transition | Doorway, same level | 0.9m or 2.7m | Metal or wood effect |
| Reducer ramp | Doorway, height difference | 0.9m or 2.7m | Gradual transition |
| Stair nosing | Stair tread edge | 0.9m or 2.7m | With anti-slip |
| End cap | Edge termination | 0.9m or 2.7m | Against threshold |


### 18.4 Step-by-Step Method

Measure the floor area in m² (use Calculator 1)

Select LVT or laminate product and note plank dimensions

Calculate plank area in m²

Calculate gross planks: Area / Plank Area (round up)

Select laying pattern and look up wastage percentage

Check for complications (L-shape, pillars) and add 2-3%

Calculate planks with wastage: Gross x (1 + Wastage%)

Round up to whole planks

Convert to packs: Total Planks / Planks per Pack (round up)

Calculate underlay: Floor Area x 1.05 (5% overlap)

Select underlay type based on application

Calculate underlay rolls: Underlay Area / Coverage per Roll (round up)

Measure perimeter for expansion gap and scotia/beading

Count doorways for transition trims

List all accessories (spacers, adhesive for trims, etc.)


### 18.5 Worked Example

Scenario: A homeowner in Johannesburg wants to install 1210x190x5mm LVT planks in their bedroom (3.5m x 4.0m = 14 m²) in a straight lay pattern. The floor is concrete and needs a combined underlay + DPM.

Given: - Area: 14 m² - Plank: 1210mm x 190mm x 5mm - Planks per pack: 10 - Pattern: Straight lay - Substrate: Concrete

Calculation:

Plank area: - 1.21 x 0.19 = 0.2299 m² per plank

Gross planks: - 14 / 0.2299 = 60.9 -> 61 planks

Wastage (straight lay): 7% (midpoint of 5-8%) - 61 x 1.07 = 65.3 -> 66 planks

Packs required: - 66 / 10 = 6.6 -> 7 packs

Underlay: - 14 x 1.05 = 14.7 m² - Combined underlay + DPM (15 m² per roll): 1 roll

Perimeter (for scotia/beading): - 2 x (3.5 + 4.0) = 15.0 linear metres - Scotia: 15.0 / 2.4m = 6.25 -> 7 lengths

Doorways: - 1 doorway: 1 x T-bar transition

Material Summary: | Material | Quantity | Est. Cost (2025) | |———-|———-|—————–| | LVT planks (7 packs) | 7 packs | 7 x R450 = R3,150 | | Combined underlay + DPM | 1 roll | R200 | | Scotia beading (7 lengths) | 7 x 2.4m | 7 x R45 = R315 | | T-bar transition | 1 x 0.9m | R85 | | Expansion spacers | 1 pack | R35 | | Total Materials | | ~R3,785 |

Labour Estimate: - LVT installation: 14 m² x R120/m² = R1,680

Total Project: ~R5,465


### 18.6 SANS / Regulatory Reference

SANS 10109: Flooring installation requirements

SANS 10400-J: Floor finishes and tolerances

SANS 10107: Slip resistance requirements

Manufacturer specifications: Acclimatisation and expansion requirements


### 18.7 Chatbot Instruction Notes

When a customer asks about LVT or laminate flooring: 1. Ask for the room dimensions 2. Ask if they want LVT (vinyl) or laminate (wood fibre) 3. Explain the difference: LVT is waterproof, laminate is not 4. Ask what pattern they want (straight, herringbone, etc.) 5. Ask about the substrate (concrete, wood, existing floor) 6. Calculate planks/packs, underlay, and trim requirements 7. Explain that LVT/Laminate needs an EXPANSION GAP around the perimeter 8. Mention that scotia/beading covers the expansion gap 9. For concrete floors, recommend underlay with built-in DPM (damp-proof membrane) 10. Explain that laminate should NOT go in bathrooms (moisture damage) 11. LVT CAN go in bathrooms if it’s the click-lock waterproof type 12. Mention acclimatisation: planks should sit in the room for 48 hours before installation



<!-- RAG_CHUNK: calculator -->

---

## CALCULATOR 19: DECORATIVE FEATURE AND MOSAIC CALCULATOR

**RAG search aliases:** feature wall, mosaic, decorative strip



### 19.1 Name and Purpose

Name: Decorative Feature and Mosaic Calculator Purpose: Calculates the quantities of materials needed for decorative tiling elements including feature strips, mosaic panels, decorative borders, and medallions.

Who uses it: Interior designers, homeowners adding decorative elements, specialist tilers.


### 19.2 Formula

Feature Strip / Panel Area

Feature Area (m²) = Strip Length (m) x Strip Height (m)

Mosaic Sheet Count

Mosaic Area (m²) = Panel Width (m) x Panel Height (m) Sheets Required = Ceiling(Mosaic Area (m²) / Area per Sheet (m²)) Sheets with Wastage = Ceiling(Sheets Required x 1.15)

Decorative Border Linear Metres

Border Length (m) = Wall Perimeter (m) - Door/Window Openings (m) Border Pieces = Ceiling(Border Length (m) / Border Piece Length (m))

Medallion Calculation

Medallion Area (m²) = pi x Radius² (m²) [for circular] Medallion Area (m²) = Side x Side (m²) [for square]

Cut-in Feature Tiles

Feature Tiles = (Feature Area (m²) / Individual Feature Tile Area (m²)) x 1.20


### 19.3 Lookup Tables

Mosaic Sheet Sizes and Coverage

| Mosaic Type | Sheet Size | Tiles per Sheet | Area per Sheet |
| --- | --- | --- | --- |
| 20x20mm on mesh | 327x327mm | 225 tiles | 0.107 m² |
| 25x25mm on mesh | 306x306mm | 144 tiles | 0.094 m² |
| 48x48mm on mesh | 306x306mm | 36 tiles | 0.094 m² |
| 25x50mm on mesh | 306x327mm | 72 tiles | 0.100 m² |
| Penny round on mesh | 306x327mm | ~140 tiles | 0.100 m² |
| Hexagon on mesh | 260x300mm | ~90 tiles | 0.078 m² |
| Subway pattern on mesh | 306x327mm | varies | 0.100 m² |
| Glass mosaic on mesh | 327x327mm | varies | 0.107 m² |
| Mixed stone mosaic | 305x305mm | varies | 0.093 m² |

Feature Strip/Border Sizes

| Border Type | Typical Size | Coverage per Piece | Notes |
| --- | --- | --- | --- |
| Listello (decorative strip) | 50-100mm x 300-600mm | 0.015-0.06 m² | Decorative accent strip |
| Pencil liner | 15-20mm x 300mm | 0.0045-0.006 m² | Thin accent border |
| Chair rail | 75-100mm x 300mm | 0.0225-0.03 m² | Mid-wall border |
| Decorative border tile | 50-150mm x 200-400mm | 0.01-0.06 m² | Ornate pattern |
| Glass strip | 20-50mm x 300mm | 0.006-0.015 m² | Metallic/glass accent |

Medallion Sizes

| Medallion Size | Diameter/Width | Area | Notes |
| --- | --- | --- | --- |
| Small inset | 300-400mm | 0.07-0.13 m² | Feature in field |
| Medium feature | 500-800mm | 0.20-0.50 m² | Entry foyer |
| Large statement | 900-1200mm | 0.64-1.13 m² | Grand entrance |
| Custom | Any size | Calculated | Bespoke design |

Mosaic Wastage

| Application | Wastage % | Notes |
| --- | --- | --- |
| Standard flat wall | 15% | Standard cuts |
| Feature panel | 15-20% | Precise alignment needed |
| Shower niche | 20-25% | Multiple small cuts |
| Curved surface | 25-30% | Complex cutting |
| Medallion installation | 20-25% | Radial cuts |

Adhesive and Grout for Mosaics

| Application | Adhesive Coverage | Grout Coverage | Notes |
| --- | --- | --- | --- |
| Glass mosaic | 2-3 kg/m² | 0.8-1.2 kg/m² | White adhesive required |
| Stone mosaic | 3-4 kg/m² | 0.6-1.0 kg/m² | Penetrating sealer needed |
| Ceramic mosaic | 2-3 kg/m² | 0.5-0.8 kg/m² | Standard adhesive |
| Metal mosaic | 2-3 kg/m² | 0.5-0.8 kg/m² | Use white adhesive |
| Mixed material | 3-4 kg/m² | 0.8-1.2 kg/m² | Check compatibility |


### 19.4 Step-by-Step Method

For a Feature Strip:

Determine the wall(s) where the feature strip will go

Measure the total length of the strip in metres

Determine the height of the strip in metres

Calculate the feature area: Length x Height

Select the feature tile/border type

Look up the coverage per piece

Calculate pieces needed: Feature Area / Piece Area (round up)

Add 15% wastage for cuts and alignment

Calculate adhesive: Feature Area x Mosaic Adhesive Rate

Calculate grout: Feature Area x Mosaic Grout Rate

For a Mosaic Panel:

Measure the panel dimensions (width x height)

Calculate panel area

Select mosaic type and sheet size

Calculate sheets needed: Panel Area / Sheet Area (round up)

Add 15-20% wastage

Calculate adhesive: Panel Area x Mosaic Adhesive Rate

Calculate grout: Panel Area x Mosaic Grout Rate

Order penetrating sealer if stone mosaic

For a Decorative Border:

Measure the wall perimeter where border will go

Subtract door and window openings

Calculate border length

Select border piece size

Calculate pieces needed: Border Length / Piece Length (round up)

Add 10% wastage


### 19.5 Worked Example

Scenario: An interior designer in Cape Town is specifying a feature wall in a luxury bathroom. The design includes: - A glass mosaic feature panel behind the vanity: 1.8m wide x 0.9m high - A decorative listello strip at 1.2m height around the shower: 3.0m perimeter - A pencil liner border around the feature panel

Given: - Mosaic panel: 1.8m x 0.9m = 1.62 m² - Listello strip: 3.0m x 0.08m height = 0.24 m² - Pencil liner around mosaic panel: 2 x (1.8 + 0.9) = 5.4 linear metres

Calculation:

Mosaic panel: - Glass mosaic sheets: 327x327mm, 0.107 m² per sheet - Sheets needed: 1.62 / 0.107 = 15.1 -> 16 sheets - With 20% wastage: 16 x 1.20 = 19.2 -> 20 sheets - Adhesive: 1.62 x 2.5 = 4.05 kg - Grout: 1.62 x 1.0 = 1.62 kg - Penetrating sealer: 1.62 x 0.15 = 0.24 L

Listello strip: - Listello size: 80mm x 300mm = 0.024 m² each - Pieces needed: 0.24 / 0.024 = 10 pieces - With 15% wastage: 10 x 1.15 = 11.5 -> 12 pieces

Pencil liner: - Pencil liner: 20mm x 300mm, 0.3m long each - Pieces needed: 5.4 / 0.3 = 18 pieces - With 15% wastage: 18 x 1.15 = 20.7 -> 21 pieces

Material Summary: | Material | Quantity | Est. Cost (2025) | |———-|———-|—————–| | Glass mosaic sheets | 20 sheets | 20 x R85 = R1,700 | | Listello tiles | 12 pieces | 12 x R45 = R540 | | Pencil liner | 21 pieces | 21 x R25 = R525 | | White adhesive (5kg) | 1 bag | R150 | | Grout (2kg) | 1 small bag | R80 | | Glass mosaic sealer | 500ml | R180 | | Total Materials | | ~R3,175 |


### 19.6 SANS / Regulatory Reference

SANS 10109: Decorative tile installation requirements

SANS 10107: Slip resistance for decorative floor features

SANS 10400 Part P: Waterproofing behind mosaic features in wet areas


### 19.7 Chatbot Instruction Notes

When a customer asks about decorative tiling features: 1. Ask what type of feature they want (strip, panel, border, medallion) 2. Ask for the dimensions of the feature area 3. Ask what material they prefer (glass, stone, ceramic, metal mosaic) 4. For glass mosaics, explain that WHITE adhesive is essential 5. For stone mosaics, explain that sealing is required before AND after grouting 6. Calculate the quantities based on their specific design 7. Show them the cost breakdown 8. Mention that mosaic installation is labour-intensive (higher labour cost) 9. Explain that feature strips break up large wall areas and add visual interest 10. Suggest complementary grout colours (matching or contrasting) 11. Recommend using a tiler experienced with mosaic work 12. For shower features, remind about waterproofing requirements behind the mosaic



<!-- RAG_CHUNK: calculator -->

---

## CALCULATOR 20: COMPLETE PROJECT BUDGET CALCULATOR

**RAG search aliases:** full project budget, complete estimate, all-in cost



### 20.1 Name and Purpose

Name: Complete Project Budget Calculator Purpose: A master calculator that combines all elements from the previous 19 calculators into a comprehensive, room-by-room project budget with contingency planning and total all-in cost estimation.

Who uses it: Homeowners planning complete home renovations, project managers, quantity surveyors, contractors preparing comprehensive quotes.


### 20.2 Formula

Master Budget Formula

Total Project Cost = Sum of all room costs + Contingency + VAT Where each room cost = Materials (tiles + adhesive + grout + trims + features) + Preparation (screed + levelling + waterproofing + primer) + Removal (old floor + disposal + grinding) + Labour (installation + patterns + complications) + Finishing (sealers + silicon + cleaning) + Special systems (underfloor heating + movement joints)

Contingency

Contingency = (Sum of all room costs) x Contingency Rate Contingency Rate = 10% for new work, 15% for renovations, 20% for complex/unknown


## Vat

VAT = (Sum of all room costs + Contingency) x 0.15

Cost per Square Metre

Cost per m² = Total Project Cost / Total Area (m²)


### 20.3 Lookup Tables

Budget Template Structure

| Category | Items to Include | Typical % of Budget |
| --- | --- | --- |
| Tiles | Floor tiles, wall tiles, mosaic, features | 25-35% |
| Adhesive & Grout | All adhesives, grouts, spacers | 5-8% |
| Preparation | Screed, levelling, waterproofing, primer | 10-20% |
| Removal | Old floor removal, disposal, grinding | 5-15% |
| Labour | All installation labour | 25-35% |
| Trims & Accessories | Edge trims, skirting, transitions | 3-5% |
| Finishing | Sealers, silicon, cleaners | 2-3% |
| Special systems | Underfloor heating, movement joints | 5-15% |
| Contingency | Unknown/unexpected costs | 10-15% |

Room-by-Room Budget Template

| Room | Area (m²) | Tiles | Adhesive | Grout | Prep | Removal | Labour | Trims | Finishing | Subtotal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bathroom 1 |  |  |  |  |  |  |  |  |  |  |
| Bathroom 2 |  |  |  |  |  |  |  |  |  |  |
| Kitchen |  |  |  |  |  |  |  |  |  |  |
| Lounge |  |  |  |  |  |  |  |  |  |  |
| Dining room |  |  |  |  |  |  |  |  |  |  |
| Bedrooms |  |  |  |  |  |  |  |  |  |  |
| Hallway |  |  |  |  |  |  |  |  |  |  |
| Entrance |  |  |  |  |  |  |  |  |  |  |
| Patio / Balcony |  |  |  |  |  |  |  |  |  |  |
| TOTAL |  |  |  |  |  |  |  |  |  |  |

Budget Benchmarks (South Africa 2025)

| Project Type | Cost per m² | Notes |
| --- | --- | --- |
| Budget renovation (ceramic) | R400-600 | Entry-level materials |
| Mid-range renovation (porcelain) | R600-1,000 | Good quality |
| Premium renovation | R1,000-1,500 | Designer tiles |
| Luxury renovation | R1,500-3,000 | Imported/premium |
| Commercial (standard) | R500-800 | Economy of scale |
| Commercial (premium) | R800-1,500 | High-end commercial |


### 20.4 Step-by-Step Method

List ALL rooms/areas to be tiled

For each room, measure and record the area in m²

For each room, determine the tile type and calculate tile cost

Calculate adhesive and grout for each room

Calculate preparation requirements for each room

Calculate removal costs if applicable

Calculate labour for each room

Calculate trims and accessories for each room

Calculate finishing items for each room

Add any special systems (heating, waterproofing, etc.)

Sum all room subtotals

Apply contingency percentage

Add VAT at 15%

Calculate cost per m² for benchmarking

Present the complete budget breakdown


### 20.5 Worked Example

Scenario: A homeowner in Sandton is renovating their entire ground floor. The project includes:

| Room | Area | Tile Type | Pattern | Notes |
| --- | --- | --- | --- | --- |
| Kitchen | 15 m² | 600x600 porcelain | Straight | Old tiles to remove |
| Guest toilet | 2 m² | 300x300 ceramic | Straight | Old tiles to remove |
| Lounge | 30 m² | 800x800 porcelain | Straight | Old tiles to remove |
| Patio | 20 m² | 600x600 anti-slip porcelain | Straight | New concrete slab |

Comprehensive Budget Calculation:

KITCHEN (15 m²)

| Item | Calculation | Cost |
| --- | --- | --- |
| Porcelain tiles (R280/m²) | 15 x 280 | R4,200 |
| Adhesive (5 kg/m², 3 bags) | 3 x R130 | R390 |
| Grout (5kg bag) | 1 x R100 | R100 |
| Spacers | 1 pack | R35 |
| Edge trim | 2 lengths | R110 |
| Tile removal | 15 x R80 | R1,200 |
| Disposal (share of skip) | 1/4 of R2,500 | R625 |
| Floor primer | 15 x R25 | R375 |
| Self-levelling (2mm) | 15 x 2 x 1.6 = 48kg, 2 bags | R360 |
| Labour - floor tiling | 15 x R220 | R3,300 |
| Silicon sealant | 1 tube | R85 |
| Kitchen Subtotal |  | R10,780 |

GUEST TOILET (2 m²)

| Item | Calculation | Cost |
| --- | --- | --- |
| Ceramic tiles (R120/m²) | 2 x 120 | R240 |
| Adhesive (4 kg/m², 1 bag) | 1 x R130 | R130 |
| Grout (small amount, share) | portion | R50 |
| Tile removal | 2 x R80 | R160 |
| Waterproofing (SANS 10400-P) | 2 x R200 | R400 |
| Primer | 2 x R25 | R50 |
| Labour - floor + wall tiling | 2 x R280 | R560 |
| Silicon | 1 tube | R85 |
| Guest Toilet Subtotal |  | R1,675 |

LOUNGE (30 m²)

| Item | Calculation | Cost |
| --- | --- | --- |
| 800x800 porcelain (R350/m²) | 30 x 350 | R10,500 |
| Adhesive (7 kg/m² with back-butter, 11 bags) | 11 x R130 | R1,430 |
| Grout (2 x 5kg bags) | 2 x R100 | R200 |
| Spacers | 2 packs | R70 |
| Edge trim (doorways) | 3 lengths | R165 |
| Tile removal | 30 x R80 | R2,400 |
| Disposal (share of skip) | 1/2 of R2,500 | R1,250 |
| Floor primer | 30 x R25 | R750 |
| Self-levelling (3mm) | 30 x 3 x 1.6 = 144kg, 6 bags | R1,080 |
| Labour - large format floor | 30 x R300 | R9,000 |
| Movement joints | 15 linear metres | R200 |
| Silicon | 2 tubes | R170 |
| Lounge Subtotal |  | R27,215 |

PATIO (20 m²)

| Item | Calculation | Cost |
| --- | --- | --- |
| Anti-slip porcelain (R250/m²) | 20 x 250 | R5,000 |
| Adhesive (5 kg/m², 5 bags) | 5 x R140 | R700 |
| Grout (1 x 5kg bag) | 1 x R100 | R100 |
| Spacers | 1 pack | R35 |
| Primer (new concrete) | 20 x R20 | R400 |
| Labour - outdoor tiling | 20 x R250 | R5,000 |
| Movement joints (exterior) | 20 linear metres | R350 |
| Silicon (outdoor grade) | 2 tubes | R200 |
| Patio Subtotal |  | R11,785 |


## Project Total

| Item | Cost |
| --- | --- |
| Kitchen | R10,780 |
| Guest Toilet | R1,675 |
| Lounge | R27,215 |
| Patio | R11,785 |
| Subtotal (before contingency) | R51,455 |
| Contingency (12%) | R6,175 |
| Subtotal with Contingency | R57,630 |
| VAT (15%) | R8,645 |
| TOTAL PROJECT COST | R66,275 |

Summary Statistics

Total area: 67 m²

Cost per m² (excl. VAT): R769

Cost per m² (incl. VAT): R885

Budget category: Mid-range renovation


### 20.6 SANS / Regulatory Reference

SANS 10109: Complete tiling project standards

SANS 10400: Building Regulations compliance

SANS 10107: Slip resistance requirements (especially patio)

Consumer Protection Act: Itemised quote requirements


### 20.7 Chatbot Instruction Notes

When a customer asks for a complete project budget: 1. Ask them to list ALL rooms/areas they want to tile 2. For each room, ask for dimensions and current floor type 3. Ask what type of tiles they want for each area 4. Ask about any special requirements (heating, waterproofing, patterns) 5. Work through each room systematically using the budget template 6. Build up the budget room by room so they can see where costs are 7. Show them the total and the cost per m² 8. Compare their cost per m² to the benchmarks so they understand their budget level 9. Suggest where savings could be made if needed 10. Remind them to get 3 quotes from registered contractors 11. Explain that VAT should be included in final comparisons 12. Recommend not cutting corners on preparation and waterproofing 13. Suggest phasing the project if budget is tight (do priority rooms first)


## Appendix A: Quick Reference Summary

Complete Formula Reference

| Calculator | Key Formula | Unit |
| --- | --- | --- |
| 1. Floor Area | Length x Width | m² |
| 2. Tile Quantity | Ceiling((Area / Tile Area) x (1 + Wastage%)) | tiles |
| 3. Total Cost | Sum of all components x 1.15 (VAT) | R |
| 4. Adhesive | Area x Coverage x Condition Factor | kg |
| 5. Grout | [(L+W)/(LxW)] x JW x JD x SG x 0.001 x Area | kg |
| 6. Screed | Area x Thickness = Volume; Vol x 1,900 kg/m³ | kg |
| 7. Self-levelling | Area x Thickness x 1.6 | kg |
| 8. Waterproofing | Area x Coats x Coverage per Coat | L |
| 9. Pattern Wastage | Base% + Complication% = Total Wastage | % |
| 10. Labour | Area x Rate x Pattern Factor x Size Factor | R |
| 11. Stairs | Tread Area + Riser Area + Nosing Area | m² |
| 12. Skirting | Perimeter - Door Widths + Wastage | linear m |
| 13. UF Heating | Area - (Perimeter x 0.1 + Fixed Furniture) | m² |
| 14. Movement Joints | Ceiling(Dimension / Max Spacing) - 1 | joints |
| 15. Structural Load | Sum of all component weights | kg/m² |
| 16. Removal | Area x Removal Rate + Disposal | R |
| 17. Primer | Area x Coverage x Coats | L |
| 18. LVT/Laminate | Ceiling((Area / Plank Area) x (1 + Wastage%)) | packs |
| 19. Decorative | Feature Area / Piece Area x 1.15 | pieces |
| 20. Complete Budget | Sum of all rooms + Contingency + VAT | R |

Standard Coverage Rates Summary

| Material | Coverage | Unit |
| --- | --- | --- |
| Tile adhesive (standard) | 4-5 kg/m² | per m² |
| Tile adhesive (large format) | 7-10 kg/m² | per m² |
| Tile grout (cement) | 0.2-0.8 kg/m² | per m² |
| Self-levelling compound | 1.6 kg/m²/mm | per mm thickness |
| Waterproofing membrane | 2.0-3.0 L/m² | total (2 coats) |
| Waterproofing primer | 0.2-0.4 L/m² | per m² |
| Floor primer (general) | 0.2-0.3 L/m² | per m² |
| Screed (1:4 mix) | 1,900 kg/m³ | per m³ |

VAT and Pricing Notes

All prices in this document are exclusive of VAT unless stated otherwise

VAT rate: 15% (South Africa)

Labour rates are indicative and vary by region

Material prices vary by supplier and brand

Always obtain current prices from suppliers

Prices are for 2025/2026 and subject to inflation

Regional Price Variations

| Region | Price Factor | Notes |
| --- | --- | --- |
| Gauteng (Johannesburg/Pretoria) | 1.0 (baseline) | Highest labour costs |
| Western Cape (Cape Town) | 0.95-1.0 | High material costs |
| KwaZulu-Natal (Durban) | 0.90-0.95 | Moderate costs |
| Eastern Cape | 0.85-0.90 | Lower costs |
| Free State | 0.80-0.85 | Lower costs |
| Mpumalanga / Limpopo | 0.80-0.90 | Lower costs |
| North West / Northern Cape | 0.75-0.85 | Lowest costs |
| Rural areas | 0.70-0.85 | Significantly lower |


## Appendix B: Chatbot Conversation Flow Templates

Template 1: Initial Customer Enquiry

When a customer first asks about tiling, follow this flow:

Greeting and scope identification

“Great! I’d love to help you with your tiling project.”

“Which room(s) are you looking to tile?”

“Is this a new installation or a renovation?”

Room details

“What are the dimensions of the room?” (length x width)

“What shape is the room?” (rectangle, L-shape, irregular)

“Are there any fixed items like island baths or built-in cupboards?”

Tile selection

“What type of tiles are you considering?” (ceramic, porcelain, natural stone, LVT)

“What size tiles do you prefer?” (300x300, 600x600, etc.)

“What pattern are you thinking of?” (straight, diagonal, herringbone)

Current floor condition

“What’s currently on the floor?” (concrete, old tiles, carpet, etc.)

“Is the floor level or uneven?”

“Is there any damp issues?”

Budget discussion

“Do you have a budget in mind?”

“Are you looking for budget, mid-range, or premium tiles?”

Calculation and presentation

Calculate area (Calculator 1)

Calculate tile quantity with wastage (Calculator 2)

Estimate costs (Calculator 3 or 20)

Present results clearly with explanations

Template 2: Material Quantity Enquiry

When a customer wants to know how much material to buy:

Confirm area

“What’s the total area to be tiled?” (use Calculator 1 if needed)

Material-specific questions

For adhesive: “What size tiles are you using?” (Calculator 4)

For grout: “What size tiles and what joint width?” (Calculator 5)

For waterproofing: “Is this a shower, bathroom, or balcony?” (Calculator 8)

For screed: “How thick does the screed need to be?” (Calculator 6)

Calculation

Use the appropriate calculator

Show the working

Round up appropriately

Buying advice

“You need X bags - I recommend buying X+1 for safety”

“Keep your receipt - you can usually return unopened bags”

“Different brands have slightly different coverage rates”

Template 3: Cost Comparison Enquiry

When a customer wants to compare options:

Identify options

“What are your two options?” (e.g., ceramic vs porcelain, straight vs herringbone)

Calculate Option A

Use Calculator 3 for each option

Show itemised breakdown

Calculate Option B

Use Calculator 3 for each option

Show itemised breakdown

Comparison table | Item | Option A | Option B | Difference | |——|———-|———-|————| | Tiles | R X | R Y | R Z | | Labour | R X | R Y | R Z | | Total | R X | R Y | R Z |

Recommendation

Highlight the pros and cons of each option

Make a recommendation based on their budget and needs

Template 4: Problem-Solving Enquiry

When a customer has a specific problem:

Identify the problem

“What’s the issue you’re trying to solve?”

Common problems: cracking tiles, loose tiles, uneven floor, damp, budget constraints

Gather context

“How old is the current installation?”

“What type of substrate is it?”

“Has anything changed recently?” (new roof, plumbing work, etc.)

Use appropriate calculator(s)

Cracking: Check movement joints (Calculator 14) and structural load (Calculator 15)

Loose tiles: Check adhesive and preparation (Calculators 4, 17)

Uneven floor: Use self-levelling calculator (Calculator 7)

Damp: Check waterproofing (Calculator 8)

Provide solution

Explain the likely cause

Recommend the appropriate remedy

Estimate the cost using relevant calculators


## Appendix C: Common Mistakes To Avoid

Measurement Mistakes

| Mistake | Consequence | Prevention |
| --- | --- | --- |
| Measuring in feet/inches | Wrong quantities | Always use metres |
| Not deducting fixed items | Over-ordering | Use Calculator 1 |
| Forgetting door recesses | Under-ordering | Include all floor space |
| Not accounting for walls | Wrong skirting length | Measure perimeter carefully |
| Rounding down | Not enough materials | Always round UP |

Material Mistakes

| Mistake | Consequence | Prevention |
| --- | --- | --- |
| Not buying enough tiles | Colour mismatch later | Add proper wastage |
| Wrong adhesive for tile size | Tile failure | Match adhesive to tile size |
| Skipping primer | Loose tiles | Always prime prepared surfaces |
| Wrong grout type | Staining, cracking | Match grout to application |
| No movement joints | Cracked tiles | Use Calculator 14 |

Cost Mistakes

| Mistake | Consequence | Prevention |
| --- | --- | --- |
| Not including VAT | Budget shortfall | Add 15% VAT |
| No contingency | Budget overrun | Add 10-15% contingency |
| Forgetting preparation costs | Under-budgeting | Include all preparation |
| Not getting multiple quotes | Over-paying | Get 3 quotes minimum |
| Choosing cheapest quote | Poor workmanship | Check references |

Technical Mistakes

| Mistake | Consequence | Prevention |
| --- | --- | --- |
| Tiling on damp screed | Tile failure, efflorescence | Moisture test first |
| No waterproofing in wet areas | Leaks, damage | SANS 10400-P mandatory |
| Wrong tile for application | Cracking, slipping | Check tile classification |
| No expansion gaps | Tile buckling | Follow SANS 10109 |
| Tiling over old adhesive | Poor adhesion | Remove and grind old adhesive |


## Appendix D: Glossary Of Terms

| Term | Definition |
| --- | --- |
| Adhesive | Material used to bond tiles to the substrate (also called thinset or tile cement) |
| Back-buttering | Applying adhesive to the back of the tile as well as the substrate |
| Bonded screed | Screed applied directly to the concrete slab with a bonding agent |
| Bullnose | Tile with a rounded edge, used for finishing exposed edges |
| Contingency | Extra budget allowance for unexpected costs |
| Efflorescence | White salt deposits that appear on tile or grout surfaces |
| Expansion gap | Gap left around the perimeter to allow for thermal movement |
| Floating screed | Screed separated from the slab by insulation |
| Grout | Material used to fill the joints between tiles |
| Herringbone | Tile pattern where tiles are laid at 45-degree angles in a zigzag |
| Joint width | The gap between adjacent tiles |
| Laitance | Weak, powdery layer on the surface of new concrete |
| Large format | Tiles larger than 600x600mm |
| Levelling compound | Self-levelling material used to create a flat surface |
| Listello | Decorative border strip tile |
| Movement joint | Joint designed to accommodate thermal and structural movement |
| Mosaic | Small tiles (typically 20-50mm) mounted on mesh sheets |
| Notched trowel | Trowel with notches that create ridges in the adhesive |
| Porcelain | High-density, low-porosity ceramic tile |
| Primer | Liquid applied to the substrate before tiling to improve adhesion |
| SANS | South African National Standards |
| Screed | Layer of sand and cement used to level or prepare floors |
| Self-levelling | Compound that flows to create a level surface |
| Specific gravity | Density of a material relative to water |
| Substrate | The surface to which tiles are adhered |
| Thinset | See adhesive |
| Trowel notch | The size of the notches on a notched trowel |
| Upstand | Waterproofing extended up a wall from the floor |
| Wastage | Extra tiles ordered to allow for cuts and breakages |
| Waterproofing | System to prevent water penetration |


## Appendix E: Conversion Tables

Length Conversions

| From | To | Multiply By |
| --- | --- | --- |
| Millimetres (mm) | Metres (m) | 0.001 |
| Centimetres (cm) | Metres (m) | 0.01 |
| Metres (m) | Millimetres (mm) | 1,000 |
| Inches | Millimetres (mm) | 25.4 |
| Feet | Metres (m) | 0.3048 |

Area Conversions

| From | To | Multiply By |
| --- | --- | --- |
| Square centimetres (cm²) | Square metres (m²) | 0.0001 |
| Square millimetres (mm²) | Square metres (m²) | 0.000001 |
| Square feet | Square metres (m²) | 0.0929 |

Volume Conversions

| From | To | Multiply By |
| --- | --- | --- |
| Litres (L) | Cubic metres (m³) | 0.001 |
| Cubic centimetres (cm³) | Litres (L) | 0.001 |
| Cubic feet | Cubic metres (m³) | 0.0283 |

Weight Conversions

| From | To | Multiply By |
| --- | --- | --- |
| Kilograms (kg) | Tonnes (t) | 0.001 |
| Grams (g) | Kilograms (kg) | 0.001 |
| Pounds (lb) | Kilograms (kg) | 0.4536 |


## Appendix F: South African Standards Reference

Primary Standards for Tiling

| Standard | Title | Relevance |
| --- | --- | --- |
| SANS 10109 | Code of Practice for Tiling | Primary tiling standard |
| SANS 10400 | National Building Regulations | Building compliance |
| SANS 10400-B | Structural Design | Floor loading |
| SANS 10400-J | Floors | Floor construction and finishes |
| SANS 10400-P | Drainage | Waterproofing requirements |
| SANS 10107 | Slip Resistance | Safety requirements |
| SANS 1449 | Ceramic Tiles - Classification | Tile quality grades |
| SANS 784 | Cement | Cement specifications |
| SANS 1085 | Aggregates | Sand and stone for screeds |
| SANS 10142-1 | Electrical Installation | Underfloor heating wiring |
| SANS 10160 | Basis of Structural Design | Load calculations |

International Standards Referenced in SA

| Standard | Title | Relevance |
| --- | --- | --- |
| BS 5385 | Wall and Floor Tiling | Wastage and movement joints |
| BS 8204 | Screeds, Bases and In-situ Floorings | Screed specifications |
| BS EN 14411 | Ceramic Tiles | European tile standard |
| ISO 13006 | Ceramic Tiles | International tile standard |
| ISO 10545 | Ceramic Tiles - Test Methods | Quality testing |


## Appendix G: Emergency Contacts And Resources

Professional Bodies

| Organisation | Contact | Purpose |
| --- | --- | --- |
| Tile Council of South Africa (TCSA) | www.tcsa.org.za | Industry standards and training |
| Master Builders South Africa | www.mbsa.org.za | Contractor registration |
| National Home Builders Registration Council (NHBRC) | www.nhbrc.org.za | Home warranty and standards |
| South African Bureau of Standards (SABS) | www.sabs.co.za | Standards and certification |
| Institute of Tile Layering South Africa (ITLSA) | Various | Tiler training and certification |

Consumer Protection

| Resource | Contact | Purpose |
| --- | --- | --- |
| National Consumer Commission | www.thencc.gov.za | Consumer rights and complaints |
| Consumer Protection Act No. 68 of 2008 | Legislation | Legal protection for consumers |
| Small Claims Court | Local magistrate’s office | Dispute resolution under R20,000 |


## Document End

Disclaimer: This document is intended as a guide for estimation purposes. All calculations should be verified by a qualified professional before purchasing materials or commencing work. Prices are indicative for South Africa in 2025/2026 and will vary by supplier, region, and market conditions. Always follow manufacturer’s specifications for all products and comply with applicable SANS standards and local building regulations.

Copyright: This calculator suite is provided for professional and personal use. All formulas and data are compiled from industry-standard sources including SANS standards, manufacturer specifications, and industry practice.

Document Version: 1.0 Last Updated: June 2025 Total Calculators: 20 Target Market: South Africa


## Supplementary Calculation Examples

Detailed Multi-Scenario Worked Examples for Common SA Home Types

Scenario A: Small Apartment Renovation (Parkhurst, Johannesburg)

Property: 2-bedroom apartment, 85 m² Scope: Replace all flooring, update bathroom Budget: Mid-range

| Room | Area | Current Floor | New Floor | Pattern |
| --- | --- | --- | --- | --- |
| Main bedroom | 12 m² | Carpet | 600x600 porcelain | Straight |
| Second bedroom | 10 m² | Carpet | 600x600 porcelain | Straight |
| Bathroom | 5 m² | Old ceramic | 300x300 ceramic | Straight |
| Kitchen | 8 m² | Vinyl | 600x600 porcelain | Straight |
| Lounge | 18 m² | Carpet | 800x800 porcelain | Straight |
| Passage | 6 m² | Vinyl | 600x600 porcelain | Straight |

Complete Material Calculation:

Porcelain tiles (600x600): Bedrooms + Kitchen + Passage = 12 + 10 + 8 + 6 = 36 m² - At R280/m²: 36 x 280 = R10,080 - Wastage 10%: R1,008 - Tile subtotal: R11,088

Porcelain tiles (800x800): Lounge = 18 m² - At R350/m²: 18 x 350 = R6,300 - Wastage 10%: R630 - Tile subtotal: R6,930

Ceramic tiles (300x300): Bathroom = 5 m² - At R120/m²: 5 x 120 = R600 - Wastage 10%: R60 - Tile subtotal: R660

Adhesive: - 600x600 areas: 36 m² x 5 kg/m² = 180 kg = 9 bags - 800x800 areas: 18 m² x 7 kg/m² = 126 kg = 7 bags - 300x300 bathroom: 5 m² x 4 kg/m² = 20 kg = 1 bag - Total adhesive: 17 x R130 = R2,210

Grout: - Total area: 59 m² - Average grout: 0.4 kg/m² = 23.6 kg - 5 x 5kg bags: 5 x R100 = R500

Preparation: - Carpet removal (22 m²): 22 x R25 = R550 - Vinyl removal (14 m²): 14 x R30 = R420 - Ceramic removal (5 m²): 5 x R80 = R400 - Disposal (2 x 4m³ skip): 2 x R3,000 = R6,000 - Primer (59 m²): 59 x R25 = R1,475 - Bathroom waterproofing: 5 x R200 = R1,000 - Subtotal preparation: R9,845

Labour: - 600x600 areas: 36 m² x R200 = R7,200 - 800x800 areas: 18 m² x R300 = R5,400 - 300x300 bathroom: 5 m² x R250 = R1,250 - Bathroom waterproofing labour: 5 x R200 = R1,000 - Subtotal labour: R14,850

Finishing: - Sealers, silicon, cleaners: R800 - Edge trims: R500

Subtotal: R11,088 + R6,930 + R660 + R2,210 + R500 + R9,845 + R14,850 + R800 + R500 = R47,383 Contingency (12%): R5,686 Total (excl. VAT): R53,069 VAT (15%): R7,960 TOTAL PROJECT: R61,029

Scenario B: New Build House (Midstream Estate, Centurion)

Property: 4-bedroom new build, 320 m² Scope: Floor and wall tiling throughout Budget: Premium

| Area | Floor Area | Wall Area | Tile Specification |
| --- | --- | --- | --- |
| 4 x En-suite bathrooms | 18 m² | 72 m² | 600x600 floor, 300x600 wall |
| Guest bathroom | 5 m² | 20 m² | 600x600 floor, 300x600 wall |
| Main bathroom | 10 m² | 40 m² | 600x600 floor, feature wall mosaic |
| Kitchen | 20 m² | 8 m² (splashback) | 600x600 floor, 100x300 subway wall |
| Scullery | 8 m² | 4 m² (splashback) | 600x600 floor, 100x300 subway wall |
| Entrance hall | 12 m² | - | 800x800 porcelain |
| Passages | 24 m² | - | 600x600 porcelain |
| Lounge | 35 m² | - | 800x800 porcelain |
| Dining room | 18 m² | - | 800x800 porcelain |
| Patio | 25 m² | - | 600x600 anti-slip |
| Double garage | 36 m² | - | 300x300 industrial |

Total Floor Area: 211 m² Total Wall Area: 144 m²

This scenario demonstrates the scale of new-build projects where multiple calculators must be applied across different areas with varying specifications.

Scenario C: Small Commercial Office (Umhlanga, Durban)

Property: Office suite, 150 m² Scope: Replace carpet with porcelain tiles Budget: Commercial mid-range

Key Considerations for Commercial Projects: - Higher traffic requires heavier-duty tiles (PEI 4-5) - Movement joints at 4.5m spacing (suspended floor) - Anti-slip requirements (R10 minimum) - After-hours installation may be required - Warranty requirements typically 10 years

Floor specification: 600x600mm PEI 4 porcelain, straight bond Area: 150 m² Budget estimate: R75,000 - R95,000 (materials + labour + preparation)

Scenario D: Heritage Home Renovation (Observatory, Cape Town)

Property: Victorian-era home, 180 m² Scope: Restore original floor tiles, install new in extensions Budget: Premium (heritage considerations)

Key Considerations: - Heritage overlay requirements for visible areas - Uneven original floors requiring extensive levelling - Potential asbestos in old vinyl (pre-1990s) - Timber floor reinforcement needed in some areas - Specialist tiler required for restoration work

Budget estimate: R150,000 - R250,000 (heritage work is specialist and expensive)**


## Expanded Calculation Workbooks

Calculator 1: Floor Area - Complex Room Examples

Example 1: U-Shaped Kitchen with Island

Room Shape: U-shaped kitchen with central island Method: Divide into 3 rectangles + subtract island

Measurements: - Rectangle A (main area): 4.0m x 3.0m = 12.0 m² - Rectangle B (return 1): 1.5m x 2.5m = 3.75 m² - Rectangle C (return 2): 1.5m x 2.5m = 3.75 m² - Island: 1.2m x 0.9m = 1.08 m²

Total Area: 12.0 + 3.75 + 3.75 - 1.08 = 18.42 m²

Example 2: Bathroom with Multiple Recesses

Room Shape: Rectangular with shower recess and vanity nook Method: Main rectangle + additions

Measurements: - Main area: 2.5m x 2.0m = 5.0 m² - Shower recess: 1.2m x 0.3m = 0.36 m² - Vanity nook: 0.9m x 0.3m = 0.27 m²

Total Area: 5.0 + 0.36 + 0.27 = 5.63 m²

Example 3: Circular Entrance Foyer

Room Shape: Circular Method: Circle area formula

Measurements: - Diameter: 3.5m - Radius: 1.75m

Total Area: pi x (1.75)² = 9.62 m²

Calculator 2: Tile Quantity - Pattern Comparison Table

Same Room, Different Patterns (20 m² with 600x600 tiles)

| Pattern | Wastage % | Tiles Needed | Boxes (4 per box) | Cost @ R120/tile | Cost vs Straight |
| --- | --- | --- | --- | --- | --- |
| Straight bond | 10% | 67 | 17 | R8,040 | Baseline |
| Brick bond | 12% | 69 | 18 | R8,280 | +3% |
| Diagonal | 16% | 72 | 18 | R8,640 | +7.5% |
| Herringbone | 20% | 75 | 19 | R9,000 | +12% |
| Versailles | 15% | 71 | 18 | R8,520 | +6% |

Note: This table shows that pattern choice can add 3-12% to tile costs alone. Labour costs also increase proportionally.

Calculator 4: Adhesive - Comprehensive Scenario Matrix

Adhesive Required for 20 m² by Tile Size and Condition

| Tile Size | Trowel | Smooth Floor | Uneven Floor | Uneven + Back-butter |
| --- | --- | --- | --- | --- |
| 100x100 mosaic | 6mm | 60 kg (3 bags) | 75 kg (4 bags) | N/A |
| 300x300 ceramic | 8mm | 90 kg (5 bags) | 110 kg (6 bags) | N/A |
| 600x600 porcelain | 10mm | 120 kg (6 bags) | 150 kg (8 bags) | 210 kg (11 bags) |
| 800x800 porcelain | 12mm | 160 kg (8 bags) | 200 kg (10 bags) | 300 kg (15 bags) |
| 1200x600 porcelain | 12mm | 180 kg (9 bags) | 225 kg (12 bags) | 350 kg (18 bags) |

Calculator 5: Grout - Comprehensive Colour and Type Selection Guide

Grout Consumption by Tile Size and Joint Width

| Tile Size | 2mm Joint | 3mm Joint | 4mm Joint | 5mm Joint | Epoxy Multiplier |
| --- | --- | --- | --- | --- | --- |
| 100x100mm | 0.60 | 0.90 | 1.20 | 1.50 | x 1.07 |
| 200x200mm | 0.30 | 0.45 | 0.60 | 0.75 | x 1.07 |
| 300x300mm | 0.20 | 0.30 | 0.40 | 0.50 | x 1.07 |
| 400x400mm | 0.15 | 0.23 | 0.30 | 0.38 | x 1.07 |
| 600x600mm | 0.10 | 0.15 | 0.20 | 0.25 | x 1.07 |
| 800x800mm | 0.08 | 0.11 | 0.15 | 0.19 | x 1.07 |
| 1200x600mm | 0.08 | 0.11 | 0.15 | 0.19 | x 1.07 |

Values in kg/m² for cement grout (SG=1.5). Multiply by area for total kg.

Grout Colour Selection Guide

| Tile Colour | Recommended Grout | Effect |
| --- | --- | --- |
| White tiles | White or light grey | Seamless, clean |
| White tiles | Dark grey or black | Bold contrast, graphic |
| Grey tiles | Matching grey tone | Subtle, cohesive |
| Grey tiles | White | Defined edges |
| Beige/cream tiles | Similar tone | Warm, blended |
| Beige/cream tiles | White | Fresh, defined |
| Black tiles | Dark grey | Sophisticated |
| Black tiles | White | High contrast, dramatic |
| Wood-look tiles | Brown/tan | Mimics wood joints |
| Natural stone | Similar tone | Natural look |
| Patterned/mosaic tiles | Neutral tone | Doesn’t compete |

Calculator 6: Screed - Drying Time Planning Chart

Project Timeline Planning with Screed Drying

| Screed Thickness | Drying Time | Earliest Tiling | Recommended Tiling |
| --- | --- | --- | --- |
| 15mm (bonded) | 15 days | Day 16 | Day 22 |
| 20mm (bonded) | 20 days | Day 21 | Day 28 |
| 25mm (bonded) | 25 days | Day 26 | Day 35 |
| 30mm (bonded) | 30 days | Day 31 | Day 42 |
| 35mm (unbonded) | 35 days | Day 36 | Day 49 |
| 40mm (unbonded) | 40 days | Day 41 | Day 56 |
| 50mm | 60 days | Day 61 | Day 75 |
| 60mm | 80 days | Day 81 | Day 98 |
| 75mm | 110 days | Day 111 | Day 133 |

Note: These timelines assume 20°C and good ventilation. Drying takes longer in cold, damp conditions.

Calculator 8: Waterproofing - Wet Area Coverage Calculator

Waterproofing Material Calculator by Room Type

| Room Type | Floor Area | Wall Upstand | Wall Full Height | Membrane (L) | Primer (L) | Tape (m) |
| --- | --- | --- | --- | --- | --- | --- |
| Small shower (0.9x0.9m) | 0.81 m² | 0.54 m² | 2.43 m² | 4.5 L | 1.2 L | 5 m |
| Standard shower (1.2x0.9m) | 1.08 m² | 0.63 m² | 3.24 m² | 5.5 L | 1.5 L | 6 m |
| Large shower (1.5x1.0m) | 1.50 m² | 0.75 m² | 4.50 m² | 7.5 L | 2.0 L | 7 m |
| Small bathroom (2.0x2.0m) | 4.0 m² | 2.0 m² | - | 7.5 L | 1.8 L | 10 m |
| Medium bathroom (2.5x3.0m) | 7.5 m² | 3.75 m² | - | 12.5 L | 3.4 L | 16 m |
| Large bathroom (3.0x4.0m) | 12.0 m² | 6.0 m² | - | 18.0 L | 5.4 L | 22 m |
| Small balcony (2.0x3.0m) | 6.0 m² | 3.0 m² | - | 10.0 L | 2.7 L | 12 m |
| Medium balcony (3.0x4.0m) | 12.0 m² | 6.0 m² | - | 18.0 L | 5.4 L | 22 m |

Assumes 2.5 L/m² total membrane coverage for floors, 2.0 L/m² for walls, 0.3 L/m² primer.

Calculator 10: Labour - Rate Card by Province

Regional Labour Rate Variations (2025/2026)

| Province | Standard Floor | Wall Tiling | Large Format | Mosaic | Day Rate |
| --- | --- | --- | --- | --- | --- |
| Gauteng | R180-260 | R220-320 | R300-450 | R300-450 | R1,000-1,600 |
| Western Cape | R170-250 | R200-300 | R280-420 | R280-420 | R950-1,500 |
| KwaZulu-Natal | R160-240 | R190-280 | R260-400 | R260-400 | R900-1,400 |
| Eastern Cape | R140-220 | R170-260 | R240-360 | R240-360 | R800-1,200 |
| Free State | R140-220 | R170-260 | R240-360 | R240-360 | R800-1,200 |
| Mpumalanga | R150-230 | R180-270 | R250-380 | R250-380 | R850-1,300 |
| Limpopo | R140-220 | R170-260 | R240-360 | R240-360 | R800-1,200 |
| North West | R130-210 | R160-250 | R230-350 | R230-350 | R750-1,100 |
| Northern Cape | R130-210 | R160-250 | R230-350 | R230-350 | R750-1,100 |

Calculator 11: Stairs - Material and Cost by Stair Count

Cost per Stair (Standard 900mm width, 170mm riser, 280mm tread)

| Material | Per Tread Cost | Per Riser Cost | Adhesive | Total per Step | 15 Steps Total |
| --- | --- | --- | --- | --- | --- |
| Ceramic (300x300) | R120 | R80 | R40 | R240 | R3,600 |
| Porcelain (300x600) | R180 | R100 | R50 | R330 | R4,950 |
| Porcelain (custom cut) | R250 | R150 | R60 | R460 | R6,900 |
| Natural stone | R400 | R250 | R80 | R730 | R10,950 |
| Anti-slip porcelain | R200 | R120 | R55 | R375 | R5,625 |

Includes tile, adhesive, grout, and bullnose trim estimate. Labour additional.

Calculator 14: Movement Joints - Layout Planning Guide

Joint Placement by Room Size (Interior Concrete Floor)

| Room Size | Joints in Length | Joints in Width | Joint Spacing | Joint Width |
| --- | --- | --- | --- | --- |
| 4m x 3m | 0 | 0 | Perimeter only | 6mm |
| 6m x 4m | 0 | 0 | Perimeter only | 6mm |
| 8m x 5m | 0 | 0 | Perimeter only | 6mm |
| 10m x 6m | 1 (at 5m) | 0 | 5m in length | 8mm |
| 12m x 8m | 1 (at 6m) | 0 | 6m in length | 8mm |
| 15m x 10m | 1 (at 7.5m) | 1 (at 5m) | 7.5m x 5m | 10mm |
| 20m x 12m | 1 (at 10m) | 1 (at 6m) | 10m x 6m | 10mm |
| 24m x 16m | 2 (at 8m, 16m) | 1 (at 8m) | 8m x 8m | 10mm |
| 30m x 20m | 2 (at 10m, 20m) | 2 (at 6.7m, 13.3m) | 10m x 6.7m | 10mm |

Calculator 15: Structural Load - Typical SA Floor Types

Load Capacity by Building Type

| Building Type | Floor Type | Safe Load | Max Tiling System |
| --- | --- | --- | --- |
| New house (ground) | Ground-bearing slab | 500+ kg/m² | Any system |
| New house (upper) | Suspended concrete | 250-300 kg/m² | Up to 50mm screed |
| Old house (pre-1980) | Suspended concrete | 200-250 kg/m² | Up to 40mm screed |
| Old house | Timber joist + boards | 150 kg/m² | No screed, direct fix |
| Apartment (new) | Suspended slab | 300-350 kg/m² | Up to 50mm screed |
| Apartment (old) | Suspended slab | 200-250 kg/m² | Up to 40mm screed |
| Office building | Suspended slab | 350-500 kg/m² | Any system |
| Shopping centre | Post-tensioned slab | 500+ kg/m² | Any system |

Tile System Weights (Complete System per m²)

| System Components | Thickness | Weight | Safety Assessment |
| --- | --- | --- | --- |
| Tiles only (porcelain) | 10mm | 25 kg/m² | Always safe |
| Tiles + adhesive | 10+5mm | 35 kg/m² | Always safe |
| Tiles + adhesive + 15mm screed | 10+5+15mm | 65 kg/m² | Always safe |
| Tiles + adhesive + 25mm screed | 10+5+25mm | 85 kg/m² | Usually safe |
| Tiles + adhesive + 40mm screed | 10+5+40mm | 115 kg/m² | Check floor |
| Tiles + adhesive + 50mm screed | 10+5+50mm | 135 kg/m² | Check floor |
| Stone + adhesive + 50mm screed | 20+5+50mm | 165 kg/m² | Check floor |
| Stone + adhesive + 75mm screed | 20+5+75mm | 215 kg/m² | Engineer review |

Calculator 16: Removal - Cost Breakdown by Floor Type for 20 m²

Removal and Disposal Cost Comparison

| Floor Type | Removal (R) | Grinding (R) | Disposal (R) | Total (R) | Time (days) |
| --- | --- | --- | --- | --- | --- |
| Ceramic tiles | R1,400 | R1,000 | R800 | R3,200 | 1-2 |
| Porcelain tiles | R1,800 | R1,200 | R1,000 | R4,000 | 1-2 |
| Natural stone | R2,400 | R1,400 | R1,200 | R5,000 | 2-3 |
| Vinyl sheeting | R500 | R600 | R400 | R1,500 | 0.5 |
| Vinyl tiles | R700 | R800 | R500 | R2,000 | 0.5-1 |
| Laminate | R600 | R400 | R400 | R1,400 | 0.5 |
| Carpet + underlay | R500 | R0 | R400 | R900 | 0.5 |
| Existing screed | R1,800 | R0 | R1,000 | R2,800 | 1-2 |
| Terrazzo | R3,000 | R1,800 | R1,500 | R6,300 | 2-3 |

Costs for 20 m² on ground floor with direct access. Upper floors add 20-30%.

Calculator 17: Primer - Application Decision Tree

Primer Selection Flowchart (Text Version)

START: What is your substrate? | |---> NEW CONCRETE SLAB | |---> Smooth (power-floated) ---> Epoxy primer (0.15 L/m²) | |---> Rough/tamped ---> Acrylic primer (0.25 L/m², may need 2 coats) | |---> NEW SCREED (cement) | |---> Fully cured (>28 days) ---> Acrylic primer (0.25 L/m²) | |---> Not fully cured ---> WAIT. Do not tile. | |---> OLD CERAMIC TILES | |---> Well-adhered, clean ---> Special bonding primer (0.25 L/m²) | |---> Loose/damaged ---> Remove first | |---> OLD VINYL | |---> Well-adhered, clean ---> Remove recommended, or special primer | |---> Contains asbestos (pre-1990) ---> SPECIALIST REMOVAL REQUIRED | |---> TIMBER FLOOR | |---> Overboarded with tile backer ---> Flexible primer (0.25 L/m²) | |---> Direct to timber ---> Overboard first, then prime | |---> GYPSUM/PLASTER | |---> Low-suction primer required (0.35 L/m²) | |---> ANHYDRITE SCREED | |---> Special anhydrite primer required (0.25 L/m²) | |---> Must be laitance-free

Calculator 18: LVT and Laminate - Acclimatisation Guide

Product Conditioning Requirements

| Product Type | Acclimatisation Time | Temperature | Humidity | Notes |
| --- | --- | --- | --- | --- |
| Standard laminate | 48 hours | 18-24°C | 35-65% RH | Keep boxes sealed |
| Waterproof laminate | 48 hours | 18-24°C | 35-65% RH | Keep boxes sealed |
| Standard LVT (glue-down) | 24 hours | 18-24°C | 35-65% RH | Less sensitive |
| Click LVT | 48 hours | 18-24°C | 35-65% RH | Keep boxes sealed |
| Rigid core SPC | 24 hours | 18-24°C | 35-65% RH | Stable product |
| Engineered wood | 72 hours | 18-24°C | 35-65% RH | Most sensitive |

Installation Environment

| Condition | Minimum | Ideal | Maximum |
| --- | --- | --- | --- |
| Air temperature | 15°C | 20°C | 30°C |
| Floor temperature | 15°C | 18°C | 25°C |
| Relative humidity | 35% | 50% | 65% |
| Concrete moisture content | - | < 2% CM | 2% CM |
| Concrete RH | - | < 75% | 75% |


## Final Checklist: Before You Start Tiling

Pre-Installation Checklist

Use this checklist before commencing any tiling project:

Planning Phase

☐ Room dimensions measured accurately

☐ Tile type and size selected

☐ Pattern chosen and wastage calculated

☐ All materials ordered (including 10% spare tiles)

☐ Floor/substrate inspected and assessed

☐ Moisture test completed (for concrete/screed)

☐ Structural load check completed (upper floors)

☐ Waterproofing specified (wet areas)

☐ Movement joints planned

☐ Budget finalised with contingency

Material Verification

☐ Tiles delivered and checked for damage

☐ Tiles from same batch/production run

☐ Adhesive quantity confirmed

☐ Grout quantity and colour confirmed

☐ Primer quantity confirmed

☐ Spacers on hand

☐ Edge trims on hand

☐ Sealers on hand (natural stone)

☐ Waterproofing materials on hand (wet areas)

☐ Silicon sealant on hand

☐ Cleaning products on hand

Substrate Preparation

☐ Old flooring removed (if applicable)

☐ Substrate cleaned and ground (if applicable)

☐ Screed installed and cured (if applicable)

☐ Self-levelling applied and cured (if applicable)

☐ Substrate primed and dry

☐ Waterproofing applied and tested (wet areas)

☐ Movement joint profiles in place

Installation

☐ Tiler confirmed and available

☐ Start point determined (centre of room or focal point)

☐ Tile layout dry-fitted before fixing

☐ Expansion gap allowed around perimeter

☐ Movement joints installed at correct intervals

☐ Adhesive mixed to correct consistency

☐ Trowel size matched to tile size

☐ Back-buttering used for large format

☐ Spacers used consistently

☐ Level checked regularly

☐ Grout applied after full adhesive cure

☐ Sealers applied after full grout cure

Post-Installation

☐ Floor protected during construction

☐ Expansion joints filled with flexible sealant

☐ Perimeter joints sealed with silicone

☐ Final cleaning completed

☐ Spare tiles stored for future repairs

☐ Warranty documentation filed

☐ Final inspection completed

Acknowledgment of Standards

This document references the following South African National Standards:

SANS 10109 - Code of Practice for Tiling

SANS 10400 - The application of the National Building Regulations

SANS 10107 - The classification of pedestrian surface materials according to slip resistance properties

SANS 1449 - Ceramic tiles - Classification and marking

SANS 784 - Portland cement (ordinary, rapid-hardening and sulfate-resisting)

SANS 1085 - Aggregates from natural sources - Aggregates for concrete

SANS 10142-1 - The wiring of premises

SANS 10160 - Basis of structural design and actions for building and industrial structures

All calculations should be verified by qualified professionals. This document is a guide only and does not replace professional advice.


## End Of Document

Total Calculators: 20 Target Length: 5,000-8,000 lines Document Version: 1.0 Market: South Africa Currency: ZAR (South African Rand) Units: Metric (metres, kilograms, litres, square metres) Standards: SANS, BS (referenced)


## Additional Comprehensive Reference Data

Extended Material Price Guide (South Africa 2025/2026)

Ceramic Tiles (per m²)

| Brand/Grade | Wall Tiles | Floor Tiles | Notes |
| --- | --- | --- | --- |
| Entry level (local) | R60-100 | R80-120 | Basic white/colours |
| Mid-range (local) | R100-180 | R120-220 | Good quality, variety |
| Premium (local) | R180-300 | R220-350 | High quality, designer |
| Import (Italian/Spanish) | R300-600 | R350-700 | Premium imported |
| Luxury (designer) | R600-1,200 | R700-1,500 | Exclusive ranges |

Porcelain Tiles (per m²)

| Brand/Grade | Standard | Large Format | Extra-Large |
| --- | --- | --- | --- |
| Entry level (local) | R120-180 | R180-250 | R250-350 |
| Mid-range (local) | R180-350 | R250-450 | R350-550 |
| Premium (local/import) | R350-600 | R450-800 | R550-900 |
| Luxury (Italian/Spanish) | R600-1,000 | R800-1,500 | R900-2,000 |
| Ultra-premium | R1,000-2,000 | R1,500-3,000 | R2,000-4,000 |

Natural Stone (per m²)

| Stone Type | Tile Size | Price Range | Origin |
| --- | --- | --- | --- |
| Granite | 600x600x20mm | R400-800 | Local/imported |
| Marble (Carrara) | 600x600x20mm | R500-1,000 | Italian |
| Marble (Calacatta) | 600x600x20mm | R800-1,500 | Italian |
| Travertine | 600x600x12mm | R350-700 | Turkish/Italian |
| Slate | 600x300x10mm | R300-600 | Local/Indian |
| Sandstone | 600x400x20mm | R250-500 | Local |
| Onyx | 600x600x20mm | R1,000-2,500 | Imported |
| Terrazzo | 600x600x15mm | R400-800 | Local |
| Composite quartz | Various | R800-1,500 | Various |

Adhesive Price Guide (2025)

| Type | Brand Examples | Bag Size | Price Range | Coverage |
| --- | --- | --- | --- | --- |
| Standard cement adhesive | Mapei, Tal, Davco | 20kg | R80-130 | 4-6 m² |
| Flexible adhesive | Mapei, Tal, Davco | 20kg | R120-180 | 4-6 m² |
| Large format adhesive | Mapei, Tal, Davco | 20kg | R150-220 | 3-5 m² |
| Rapid-set adhesive | Mapei, Tal, Davco | 20kg | R140-200 | 4-6 m² |
| White adhesive (mosaics) | Mapei, Tal, Davco | 20kg | R130-190 | 4-6 m² |
| Epoxy adhesive | Mapei, LATICRETE | 10kg kit | R400-700 | 3-4 m² |

Grout Price Guide (2025)

| Type | Brand Examples | Size | Price Range | Coverage |
| --- | --- | --- | --- | --- |
| Standard cement grout | Mapei, Tal, Davco | 5kg | R60-100 | 10-20 m² |
| Flexible grout | Mapei, Tal, Davco | 5kg | R80-130 | 10-20 m² |
| Waterproof grout | Mapei, Tal, Davco | 5kg | R100-150 | 10-20 m² |
| Epoxy grout | Mapei, LATICRETE | 5kg kit | R350-600 | 8-15 m² |
| Furan grout | LATICRETE | 5kg | R500-800 | 8-15 m² |
| Pre-mixed grout | Various | 1kg tube | R80-150 | 2-4 m² |

Tile Classification Guide (SANS 1449 / ISO 13006)

PEI Rating (Porcelain Enamel Institute Wear Rating)

| PEI Class | Application | Typical Locations |
| --- | --- | --- |
| PEI 0 | Walls only | Bathroom walls, feature walls |
| PEI 1 | Very light traffic | Guest bathrooms, powder rooms |
| PEI 2 | Light traffic | Bedrooms, residential bathrooms |
| PEI 3 | Light to moderate traffic | Residential living areas, kitchens |
| PEI 4 | Moderate to heavy traffic | All residential, light commercial |
| PEI 5 | Heavy traffic | Commercial, public spaces |

Tile Group Classification (ISO 13006)

| Group | Water Absorption | Typical Tiles | Application |
| --- | --- | --- | --- |
| Group I (AIa) | <= 0.5% | Porcelain, glass | Any application |
| Group II (AIb) | 0.5-3% | Vitrified tiles | Floors and walls |
| Group III (AIIa) | 3-6% | Semi-vitrified | Walls, light floors |
| Group IV (AIIb) | 6-10% | Earthenware | Walls only |
| Group V (B) | > 10% | Terracotta | Walls, outdoor |

Slip Resistance Ratings (SANS 10107 / DIN 51130)

| Rating | Slip Angle | Application | Locations |
| --- | --- | --- | --- |
| R9 | 6-10° | Normal walking | Dry interior areas |
| R10 | 10-19° | Some slip risk | General commercial |
| R11 | 19-27° | Increased slip risk | Wet areas, commercial kitchens |
| R12 | 27-35° | High slip risk | Industrial, commercial wet |
| R13 | > 35° | Very high slip risk | Swimming pools, ramps |

| Rating (Pendulum) | Value | Application |
| --- | --- | --- |
| P0 | < 20 | Very slippery |
| P1 | 20-34 | Low slip resistance |
| P2 | 35-39 | Moderate slip resistance |
| P3 | 40-44 | Good slip resistance |
| P4 | 45-54 | Very good slip resistance |
| P5 | >= 55 | Excellent slip resistance |

Comprehensive Decision Tree: Which Calculator to Use

New Installation (New Build or Extension)

START: New Installation | |---> Is the concrete slab ready? | |---> NO ---> Wait for concrete to cure (28 days minimum) | |---> YES ---> Is the slab level? | |---> YES (within 3mm over 2m) ---> Use Calculator 17 (Primer) | |---> NO ---> Use Calculator 7 (Self-levelling) or Calculator 6 (Screed) | |---> Thickness <= 20mm ---> Calculator 7 | |---> Thickness > 20mm ---> Calculator 6 | |---> Are there wet areas (bathrooms, balconies)? | |---> YES ---> Use Calculator 8 (Waterproofing) BEFORE tiling | |---> NO ---> Continue | |---> Calculate materials | |---> Area ---> Calculator 1 | |---> Tile quantity ---> Calculator 2 | |---> Adhesive ---> Calculator 4 | |---> Grout ---> Calculator 5 | |---> Any patterns? ---> Calculator 9 | |---> Large area? ---> Calculator 14 (Movement joints) | |---> Upper floor? ---> Calculator 15 (Structural load) | |---> Underfloor heating? ---> Calculator 13 | |---> Calculate costs | |---> Labour ---> Calculator 10 | |---> Total project ---> Calculator 3 or 20

Renovation (Replacing Existing Floor)

START: Renovation | |---> What's the current floor? | |---> Ceramic/porcelain tiles ---> Calculator 16 (Removal) | |---> Natural stone ---> Calculator 16 (Removal) | |---> Vinyl (pre-1990) ---> ASBESTOS TEST REQUIRED | |---> Vinyl (post-1990) ---> Calculator 16 (Removal) | |---> Carpet ---> Calculator 16 (Removal) | |---> Laminate ---> Calculator 16 (Removal) | |---> Existing screed ---> Calculator 16 (Removal) | |---> Is the substrate ready after removal? | |---> Needs grinding ---> Calculator 16 includes grinding | |---> Needs levelling ---> Calculator 7 (Self-levelling) | |---> Needs new screed ---> Calculator 6 (Screed) | |---> Ready for primer ---> Calculator 17 (Primer) | |---> Continue as per New Installation flow

Special Applications

START: Special Application | |---> Staircase? ---> Calculator 11 |---> Skirting/trim? ---> Calculator 12 |---> Decorative feature? ---> Calculator 19 |---> LVT/Laminate? ---> Calculator 18 |---> Complete house budget? ---> Calculator 20

Seasonal Considerations for Tiling in South Africa

Summer (December - February)

| Factor | Impact | Recommendation |
| --- | --- | --- |
| High temperatures | Adhesive dries faster | Work in smaller sections |
| High humidity (coastal) | Extended drying times | Allow extra curing time |
| Afternoon thunderstorms | External work affected | Plan indoor work |
| Peak holiday season | Tiler availability limited | Book well in advance |

Autumn (March - May)

| Factor | Impact | Recommendation |
| --- | --- | --- |
| Moderate temperatures | Ideal tiling conditions | Best season for tiling |
| Lower humidity | Optimal curing | Standard procedures |
| Good availability | Tilers readily available | Good time to schedule |

Winter (June - August)

| Factor | Impact | Recommendation |
| --- | --- | --- |
| Low temperatures (Highveld) | Slower adhesive curing | Use rapid-set adhesives |
| Frost (inland areas) | External tiling difficult | Avoid outdoor work |
| Shorter days | Less working time | Plan accordingly |
| Wet weather (Western Cape) | Damp conditions | Ensure enclosed workspace |

Spring (September - November)

| Factor | Impact | Recommendation |
| --- | --- | --- |
| Moderate temperatures | Good tiling conditions | Second-best season |
| Increasing humidity | Monitor curing times | Standard procedures |
| Dust storms (Free State) | Substrate contamination | Clean before priming |

Temperature Guidelines for Tiling Products

| Product | Minimum Temp | Maximum Temp | Ideal Temp |
| --- | --- | --- | --- |
| Cement adhesive | 5°C | 35°C | 15-25°C |
| Epoxy adhesive | 10°C | 30°C | 15-25°C |
| Cement grout | 5°C | 35°C | 15-25°C |
| Epoxy grout | 10°C | 30°C | 15-25°C |
| Self-levelling compound | 5°C | 30°C | 15-25°C |
| Waterproofing membrane | 5°C | 35°C | 15-25°C |
| Primer (acrylic) | 5°C | 35°C | 15-25°C |
| Sealers | 10°C | 30°C | 15-25°C |

Common SA Subfloor Types and Preparation Requirements

Concrete Slab (Ground-Bearing)

| Condition | Preparation | Products |
| --- | --- | --- |
| New, smooth | Clean, prime | Acrylic primer |
| New, rough | Grind, clean, prime | Acrylic primer |
| Old, good condition | Clean, grind, prime | Bonding primer |
| Old, damaged | Repair, self-level | Levelling compound |
| Damp (>75% RH) | Damp-proof membrane | Epoxy DPM |
| Very damp (>95% RH) | Professional assessment | Specialist system |

Suspended Concrete Slab

| Condition | Preparation | Products |
| --- | --- | --- |
| New | Clean, prime | Acrylic primer |
| Old, good | Clean, grind, prime | Bonding primer |
| With movement joints | Align tile joints | Flexible adhesive |
| Lightweight concrete | Check load capacity | Lightweight screed |

Timber Floor

| Condition | Preparation | Products |
| --- | --- | --- |
| Solid timber | Overboard with tile backer | Flexible adhesive |
| Floorboards | Overboard with tile backer | Flexible adhesive |
| Plywood | Check thickness (min 18mm), prime | Flexible adhesive |
| Chipboard | Not recommended without overboarding | Flexible system |
| Existing timber | Check for rot, overboard | Flexible system |

Existing Tile Floor

| Condition | Preparation | Products |
| --- | --- | --- |
| Well-adhered ceramic | Clean, prime with special primer | Bonding primer |
| Well-adhered porcelain | Clean, prime with special primer | Bonding primer |
| Loose/damaged tiles | Remove all tiles | Full preparation |
| Glazed tiles | Scarify surface first | Bonding primer |

Screed

| Type | Preparation | Curing Time | Products |
| --- | --- | --- | --- |
| Cement screed (traditional) | Clean, laitance removal | 1 day/mm | Acrylic primer |
| Cement screed (rapid) | Clean, laitance removal | 7 days minimum | Acrylic primer |
| Anhydrite screed | Sand, special primer | Per manufacturer | Anhydrite primer |
| Calcium sulphate | Sand, special primer | Per manufacturer | Specialist primer |

Warranty and Guarantee Information

Typical Tiler Warranties (South Africa)

| Warranty Type | Duration | Covers | Doesn’t Cover |
| --- | --- | --- | --- |
| Workmanship | 1-2 years | Installation defects | Substrate movement, impact |
| Waterproofing | 5-10 years | Leaks from waterproofing | Structural cracks |
| Manufacturer (adhesive) | 10 years | Product defects | Improper application |
| Manufacturer (tiles) | 10+ years | Manufacturing defects | Installation errors |

NHBRC Warranty (New Homes)

The National Home Builders Registration Council provides a warranty for new homes: - Major structural defects: 5 years - Roofing defects: 1 year - Non-compliance with NHBRC standards: Enrolled homes only

Note: Tiling defects may be covered if they result from non-compliance with NHBRC Technical Requirements. Always check if your builder is NHBRC registered.

What Voids a Warranty

| Action | Consequence |
| --- | --- |
| Tiling over damp substrate | Voids all warranties |
| No priming | Voids adhesive warranty |
| Wrong adhesive for tile size | Voids all warranties |
| No movement joints | Voids tile and adhesive warranty |
| No waterproofing in wet areas | Voids all warranties |
| DIY installation (some products) | May void manufacturer warranty |
| Using unregistered contractor | May affect NHBRC warranty |

Troubleshooting Guide: Common Tiling Problems

Problem: Tiles Coming Loose

| Possible Cause | Solution | Prevention |
| --- | --- | --- |
| No primer used | Remove and re-tile with primer | Always prime |
| Substrate contaminated | Clean thoroughly | Clean before priming |
| Wrong adhesive | Use correct adhesive for tile size | Match adhesive to tile |
| Damp substrate | Allow to dry, moisture test | Test moisture before tiling |
| Old adhesive left on floor | Grind off completely | Full surface preparation |
| Tiles walked on too early | Remove and re-tile | Follow curing times |

Problem: Cracked Tiles

| Possible Cause | Solution | Prevention |
| --- | --- | --- |
| No movement joints | Install movement joints | Plan joints before tiling |
| Structural movement | Professional assessment | Check substrate |
| Tiles too thin for application | Replace with thicker tiles | Check tile specification |
| Impact damage | Replace damaged tiles | Use appropriate tile |
| Substrate cracking | Repair substrate first | Address substrate issues |
| Thermal shock | Use appropriate tiles | Check thermal shock rating |

Problem: Grout Cracking or Falling Out

| Possible Cause | Solution | Prevention |
| --- | --- | --- |
| Grout too dry when mixed | Remove and re-grout | Follow mixing ratios |
| Movement in substrate | Install movement joints | Plan for movement |
| Joints too narrow | Widen joints minimum 3mm | Follow minimum widths |
| Wrong grout type | Use flexible grout | Match grout to application |
| Grouted too early | Wait for adhesive to cure | Follow curing times |

Problem: Efflorescence (White Powder on Tiles)

| Possible Cause | Solution | Prevention |
| --- | --- | --- |
| Damp substrate | Allow to dry thoroughly | Moisture test before tiling |
| No damp-proof membrane | Install DPM | Use DPM where required |
| Water infiltration | Fix water source | Proper waterproofing |
| Cement-rich adhesive/grout | Use low-alkali products | Follow specifications |

Problem: Discoloured Grout

| Possible Cause | Solution | Prevention |
| --- | --- | --- |
| Wrong grout colour chosen | Re-grout or stain | Sample test first |
| Staining from spills | Clean with appropriate cleaner | Use stain-resistant grout |
| Mould/mildew | Clean with anti-mould product | Use anti-mould grout in wet areas |
| Inconsistent mixing | Remove and re-grout | Mix batches consistently |

Problem: Uneven Tiles (Lippage)

| Possible Cause | Solution | Prevention |
| --- | --- | --- |
| Uneven substrate | Level substrate first | Proper preparation |
| Wrong trowel size | Use correct notched trowel | Match trowel to tile size |
| No tile levelling system | Use levelling clips | Use system for large format |
| Poor workmanship | Remove and re-tile | Hire experienced tiler |
| Tile warpage | Check tile quality | Check tiles before fixing |

Contractor Selection Checklist

Before Hiring a Tiler

| Check | Why It Matters | How to Verify |
| --- | --- | --- |
| References | Quality of work | Ask for 3 recent references |
| Photos of previous work | Skill level | Request portfolio |
| Years of experience | Reliability | Ask directly |
| Specialisation relevant | Correct expertise | Ask about similar projects |
| Written quote | Budget protection | Insist on itemised quote |
| Insurance | Protection against damage | Request proof |
| Warranty offered | After-service support | Get in writing |
| Registered with body | Professional standards | Check TCSA/MBSA membership |
| Availability | Project timeline | Confirm start and end dates |
| Communication | Project management | Assess responsiveness |

Questions to Ask Your Tiler

“How many years have you been tiling?”

“Can I see examples of your recent work?”

“Do you have references I can contact?”

“Are you familiar with SANS 10109?”

“What preparation will you do before tiling?”

“Will you prime the substrate?”

“How will you handle movement joints?”

“What waterproofing system do you use in wet areas?”

“What adhesive and grout do you recommend for these tiles?”

“Do you offer a warranty on your work?”

“When can you start and how long will it take?”

“Will you protect the tiles after installation?”

Red Flags to Watch For

| Red Flag | Why It’s a Problem |
| --- | --- |
| No written quote | No protection if things go wrong |
| Significantly cheaper than others | Likely cutting corners |
| No references | No track record |
| Doesn’t mention preparation | Will likely skip essential steps |
| Says priming isn’t necessary | Will likely have adhesion failures |
| No mention of movement joints | Tiles will crack |
| Asks for full payment upfront | High risk of non-completion |
| No business card or contact details | Hard to hold accountable |
| Unwilling to put warranty in writing | No after-service protection |
| Can’t explain adhesive choice | May not know what they’re doing |

Environmental Considerations

Sustainable Tiling Practices

| Practice | Benefit |
| --- | --- |
| Use local tiles | Reduced transport emissions |
| Recycled content tiles | Reduced virgin material use |
| Low-VOC adhesives | Better indoor air quality |
| Water-based sealers | Lower environmental impact |
| Proper waste segregation | Recycling opportunities |
| Accurate ordering | Reduced waste to landfill |
| Reusable off-cuts | Less waste, possible DIY projects |
| Energy-efficient underfloor heating | Lower running costs |

Green Building Council South Africa (GBCSA)

The GBCSA Green Star rating system includes credits for: - Indoor air quality (low-VOC products) - Material sourcing (local, recycled content) - Waste management (construction waste diversion) - Energy efficiency (underfloor heating with renewables)

Disposal and Recycling

| Material | Disposal Method | Recycling Option |
| --- | --- | --- |
| Ceramic tiles | Builder’s rubble | Crushed for aggregate |
| Porcelain tiles | Builder’s rubble | Crushed for aggregate |
| Adhesive bags | General waste | Check local recycling |
| Grout bags | General waste | Check local recycling |
| Empty containers | General waste | Rinse and recycle |
| Metal trims | Scrap metal | Metal recycling |
| Timber offcuts | Builder’s rubble | Wood recycling |
| Cardboard packaging | Recycling | Paper recycling |

Final Document Summary

This comprehensive document contains 20 South African tiling and flooring calculators, each with:

Name and Purpose - Clear explanation of what the calculator does

Formula - Mathematically correct, dimensionally consistent equations

Lookup Tables - Quick-reference data for common scenarios

Step-by-Step Method - Numbered instructions anyone can follow

Worked Example - Realistic South African scenarios with actual numbers

SANS / Regulatory Reference - Applicable South African standards

Chatbot Instruction Notes - How an AI should guide customers through calculations

Calculator Summary Table

| # | Calculator | Key Input | Key Output |
| --- | --- | --- | --- |
| 1 | Floor Area Calculator | Room dimensions | Area in m² |
| 2 | Tile Quantity Calculator | Area, tile size, pattern | Tiles and boxes |
| 3 | Total Project Cost Estimator | All project details | Itemised budget |
| 4 | Tile Adhesive Calculator | Area, tile size, substrate | kg and bags |
| 5 | Grout Quantity Calculator | Tile size, joint width, area | kg and bags |
| 6 | Screed Volume Calculator | Area, thickness | m³, cement, sand, drying time |
| 7 | Self-Levelling Calculator | Area, thickness | kg, bags, primer |
| 8 | Waterproofing Calculator | Area, type, upstands | Litres, primer, tape |
| 9 | Pattern Wastage Calculator | Pattern, complications | Wastage %, tile quantity |
| 10 | Labour Cost Estimator | Area, tile type, pattern | Labour cost estimate |
| 11 | Stair Tiling Calculator | Step dimensions, count | Area, materials, cost |
| 12 | Skirting and Trim Calculator | Perimeter, doors, height | Linear metres, pieces |
| 13 | Underfloor Heating Calculator | Area, exclusions, type | Heated area, wattage |
| 14 | Movement Joint Calculator | Dimensions, substrate | Joint spacing, width, quantity |
| 15 | Structural Load Calculator | All layer weights | kg/m², safety factor |
| 16 | Floor Removal Calculator | Floor type, area | Removal, grinding, disposal cost |
| 17 | Primer and Preparation Calculator | Substrate type, area | Litres, coats, drying time |
| 18 | LVT and Laminate Calculator | Area, plank size, pattern | Packs, underlay, trim |
| 19 | Decorative Feature Calculator | Feature dimensions | Pieces, sheets, cost |
| 20 | Complete Project Budget Calculator | All rooms, all elements | Total project cost with VAT |


## Document End - Final Version

Document Statistics: - Total Calculators: 20 - Master Reference Tables: 11 - Appendices: 7 (A through G) - Supplementary Scenarios: 4 - Expanded Lookup Tables: 15+ - Glossary Terms: 30+ - Standards Referenced: 15+ - Regional Price Adjustments: 9 provinces - Currency: ZAR (South African Rand) - Units: Metric only - Standards: SANS, BS, ISO - Target Audience: Homeowners, contractors, tilers, AI chatbots

Document Version: 1.0 FINAL Last Updated: June 2025 Total File Size: ~170KB Intended Use: AI chatbot training data and customer service reference


---

# Final Guardrails for Tori

- Calculations are estimates for planning and quoting support, not final stock confirmation.
- Always round up practical buying quantities.
- Always check the exact product packaging, box coverage, adhesive coverage, grout coverage and manufacturer specifications.
- Exact Tiletoria prices, stock levels, batch availability and branch availability must be confirmed by a consultant.
- Risky technical areas such as showers, balconies, ramps, exterior floors, heavy loads, suspended floors and commercial spaces should be escalated.
- For LVT, remember that Tiletoria sells glue-down LVT only unless future RAG content explicitly says otherwise.
- For any user-provided measurements, repeat the inputs back before giving the final result.
- When in doubt, say: “I don’t want to guess on this one — let’s get a Tiletoria consultant to confirm before you spend money.”
