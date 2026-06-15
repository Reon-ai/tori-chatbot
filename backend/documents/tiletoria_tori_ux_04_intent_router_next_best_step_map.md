# Tori UX 04: Intent Router and Next-Best-Step Map

This file maps customer intent to the correct first question, answer style, RAG files and escalation path.

Purpose: Help Tori decide what to do next.

## Intent: Product Suitability

Summary: Use when customer asks whether something can be used in a specific area.

Customer phrases:
“Can this go outside?”
“Can I use this in shower?”
“Can vinyl go bathroom?”
“Can wall tile go floor?”
“Can this work on balcony?”

First question:
“Where exactly will it be used?”

If location is known:
Answer with “may be suitable if…” language.

Retrieve:
Product Suitability Decision Guide.
South African Project Planning Guides.
Add-On Shopping Lists.

Escalate:
Shower floors, balconies, ramps, pool surrounds, public walkways, commercial areas, glue-down LVT in wet areas.

## Intent: Quantity Calculation

Summary: Use when customer asks how many or how much.

Customer phrases:
“How many boxes?”
“How much glue?”
“How much grout?”
“How many clips?”
“How many trims?”
“How much self-leveller?”

First question:
“What is the area in square metres and what product size are you using?”

Retrieve:
Measurement and Quantity Calculation Reference Guide.

Rules:
Estimate only.
Add waste.
Round up.
Confirm with installer and branch.
Do not invent product-specific coverage.

## Intent: Add-On Shopping List

Summary: Use when customer asks what else is needed.

Customer phrases:
“What else do I need?”
“What must I buy with tiles?”
“What do I need with toilet?”
“Need accessories.”
“What must plumber bring?”

First question:
“What are you installing: tiles, glue-down LVT, toilet, basin, bath, tapware or shower?”

Retrieve:
Add-On Shopping Lists.
Installer Questions.
Before Install Checklist.

Next step:
Give practical checklist.
Avoid pressure selling.

## Intent: Installation Preparation

Summary: Use before work starts.

Customer phrases:
“Tiler starting tomorrow.”
“Before install.”
“Check tiles.”
“Wrong batch?”
“Installer says no.”
“What must I check?”

First question:
“Is the product already installed, or is installation still about to start?”

Retrieve:
Before You Install Checklist.
Installer Questions and Handover Guide.

Escalate:
Wrong product, wrong batch, wrong adhesive, missing waterproofing, installer disagreement.

## Intent: Stock or Price

Summary: Use when customer wants live commercial info.

Customer phrases:
“Got stock?”
“Price?”
“How much?”
“Can I collect?”
“Need quote.”
“Discount?”
“Available?”

First question:
“Which branch is closest to you, and what product name or code are you looking for?”

Retrieve:
Store Details.
Lead Capture and Handover.
Do-Not-Hallucinate Rules.

Rules:
Do not invent stock.
Do not invent price.
Do not promise collection.
Route to branch.

## Intent: Complaint or Warranty

Summary: Use when customer reports a problem.

Customer phrases:
“Cracked.”
“Leaking.”
“Broken.”
“Faulty.”
“Slippery.”
“Wrong colour.”
“Warranty.”
“Refund.”
“Complaint.”

First question:
“Is the product already installed, or is it still in the box?”

Retrieve:
Complaint Triage and Escalation Guide.
Store Details.
Do-Not-Hallucinate Rules.

Rules:
Do not decide fault.
Do not promise refund or replacement.
Collect evidence.
Escalate.

## Intent: Cleaning and Maintenance

Summary: Use when customer asks about cleaning, stains or aftercare.

Customer phrases:
“How to clean?”
“Grout haze.”
“Limescale.”
“Black taps.”
“Vinyl cleaner.”
“Patio algae.”
“Shower mould.”

First question:
“What surface are you cleaning: tile, grout, LVT, tapware, bath, basin or shower glass?”

Retrieve:
Cleaning and Maintenance Schedules.

Rules:
Use mild, compatible cleaner first.
Avoid harsh chemicals unless manufacturer-approved.
Escalate chemical damage.

## Intent: Budget Guidance

Summary: Use when customer asks why project costs more.

Customer phrases:
“Why so expensive?”
“What must I budget?”
“Hidden costs?”
“Quote comparison.”
“Large format cost.”
“Bathroom budget.”

First question:
“What project are you budgeting for: floor tiles, bathroom, shower, patio, LVT, or sanitaryware?”

Retrieve:
Budget Drivers and Project Cost Explainers.

Rules:
Explain cost drivers.
Do not invent prices.
Do not invent labour rates.

## Intent: Design Guidance

Summary: Use when customer asks for look, feel or selection help.

Customer phrases:
“Modern bathroom.”
“Small bathroom ideas.”
“Warm neutral.”
“Black taps?”
“Coastal look.”
“Tile colour?”

First question:
“Do you prefer a light calm look, warm natural look, or bold modern look?”

Retrieve:
Project Planning Guides.
Design files when available.
Store Details for showroom routing.

Rules:
Give design advice but check technical suitability.

## Intent: Professional Specification

Summary: Use for architect, developer, contractor or QS requirements.

Customer phrases:
“Spec.”
“BOQ.”
“R11.”
“Commercial.”
“Developer.”
“Project.”
“Architect.”
“Quantity.”

First question:
“What is the application: internal floor, bathroom, shower, patio, balcony, ramp, public walkway or commercial area?”

Retrieve:
User Type Routing.
Product Suitability.
Measurement Guide.
Budget Guide.
Store Details.

Escalate:
Ramps, public areas, balconies, slip, waterproofing, compliance.
