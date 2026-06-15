# Tori UX 02: South African Short Query Interpreter

This file helps Tori interpret short, practical South African customer messages. Many customers will not write full technical questions.

Purpose: Convert short local phrases into the correct guided UX flow.

Important rule: A short query should usually receive a short response and one smart question.

## Outdoor Short Queries

Summary: Use this when customers ask about outside, patio, braai room, balcony, pool or ramp.

Customer phrase: “Need tiles outside.”
Likely intent: Outdoor tile suitability.
First question: “Is the area covered, fully exposed to rain, or around a pool/ramp?”
Retrieve next: Product Suitability Guide, Outdoor Planning, Add-On Shopping Lists.
Do not say: “Any outdoor tile will work.”

Customer phrase: “Tile for patio?”
Likely intent: Patio tile selection.
First question: “Is the patio covered or open to rain?”
Next step: Explain outdoor suitability, drainage, exterior adhesive and grout.

Customer phrase: “Braai room tile?”
Likely intent: Semi-indoor or semi-outdoor tile selection.
First question: “Is the braai room fully enclosed, or can rain/wet feet come in?”
Next step: If exposed, treat as semi-outdoor.

Customer phrase: “Pool tile?”
Likely intent: Pool surround or pool mosaic.
First question: “Is this for inside the pool, the pool edge, or the surrounding floor?”
Escalate if: Wet barefoot, public pool, slip concern.

Customer phrase: “R11 for ramp?”
Likely intent: Ramp slip-resistance or specification.
First question: “Is this a private ramp or public/commercial walkway?”
Escalate: Always. Do not guarantee slip safety.

## Bathroom and Shower Short Queries

Summary: Use this when customers mention bathroom, shower, toilet, basin or bath.

Customer phrase: “Bathroom tiles?”
Likely intent: Bathroom tile selection.
First question: “Is this for the bathroom floor, shower floor, shower walls, or the whole bathroom?”
Retrieve next: Product Suitability, Project Planning, Add-On Shopping Lists.

Customer phrase: “Shower floor?”
Likely intent: Shower floor tile suitability.
First question: “Are you using a standard drain or a long shower channel?”
Escalate: Waterproofing, falls, slip risk.

Customer phrase: “Can this go shower?”
Likely intent: Shower suitability.
First question: “Is it for the shower wall or shower floor?”
Next step: Mention waterproofing, adhesive, grout, silicone.

Customer phrase: “Need toilet.”
Likely intent: Toilet selection or replacement.
First question: “Are you replacing an existing toilet, and does the waste go through the floor or wall?”
Retrieve next: Add-On Shopping Lists, Product Suitability.

Customer phrase: “Need basin.”
Likely intent: Basin selection.
First question: “Is it going on a vanity, on a countertop, or directly onto the wall?”
Next step: Waste, trap, mixer, valves.

## Quantity Short Queries

Summary: Use this when customer asks how much or how many.

Customer phrase: “How many boxes?”
Likely intent: Tile quantity calculation.
First question: “What is the area in square metres and what tile size are you using?”
Retrieve next: Measurement Guide.

Customer phrase: “How much glue?”
Likely intent: Adhesive estimate.
First question: “What area are you tiling and what tile size is it?”
Rule: Coverage depends on product, tile size, trowel and substrate.

Customer phrase: “How many clips?”
Likely intent: Levelling clip estimate.
First question: “What tile size and layout are you using?”
Rule: Clips are consumable; wedges are reusable.

Customer phrase: “How much grout?”
Likely intent: Grout quantity.
First question: “What tile size, area and grout joint width are you using?”
Rule: Estimate only; confirm product coverage.

## Stock, Price and Branch Short Queries

Summary: Use this when customers ask operational questions.

Customer phrase: “Got stock?”
Likely intent: Live stock availability.
First question: “Which branch is closest to you, and what product name or code are you looking for?”
Retrieve next: Store Details, Do-Not-Hallucinate Rules.
Do not say: Stock available.

Customer phrase: “Price?”
Likely intent: Live pricing.
First question: “Which branch is closest to you, and which product are you looking at?”
Do not invent price.

Customer phrase: “Can I collect?”
Likely intent: Collection readiness.
First question: “Which branch is the order from, and has the branch confirmed it is ready?”
Do not promise collection.

Customer phrase: “Deliver Paarl?”
Likely intent: Delivery enquiry.
First question: “Which product and quantity do you need delivered, and from which branch or location?”
Do not promise delivery cost or time.

Customer phrase: “Paarl branch?”
Likely intent: Store routing.
Answer: “Tiletoria has a Spec Lab presence in Paarl. Please confirm services and stock before visiting.”
Retrieve next: Store Details.

## Product Suitability Short Queries

Summary: Use this when customer asks if something can be used somewhere.

Customer phrase: “Can this go outside?”
First question: “Is the area covered, exposed to rain, or around a pool/ramp?”
Retrieve next: Product Suitability.

Customer phrase: “Can vinyl go bathroom?”
First question: “Is this a normal bathroom floor, a toilet area, or inside a shower/wet area?”
Rule: Glue-down LVT depends on product approval, moisture, adhesive and sealing.

Customer phrase: “Wall tile on floor?”
First response: “Usually no, unless the product is specifically rated for floor use. Is this for a dry floor, bathroom, or decorative area?”

Customer phrase: “Floor tile on wall?”
First response: “Often possible if the wall can carry the weight and the correct adhesive is used. Is it a large-format tile or standard size?”

Customer phrase: “Tile over tiles?”
First question: “Are the existing tiles firmly bonded, with no loose or hollow tiles?”
Rule: Always site-dependent.

## Complaint Short Queries

Summary: Use this when customer gives a short issue message.

Customer phrase: “Tile cracked.”
First question: “Was the tile cracked before installation, or did it crack after installation?”
Retrieve next: Complaint Triage.

Customer phrase: “Tile slippery.”
First question: “Where is the tile installed, and is it slippery when wet, dry, or after cleaning?”
Escalate if slip incident.

Customer phrase: “Tap leaking.”
First question: “Is it dripping from the spout, leaking from the body, or leaking from the connection?”
Escalate if active leak.

Customer phrase: “Vinyl lifting.”
First question: “Was the floor checked for moisture and was approved LVT adhesive used?”
Retrieve next: Complaint Triage, LVT sections.

Customer phrase: “Wrong colour.”
First question: “Is the product installed already, or still in the box?”
Retrieve next: Complaint Triage, Before Install.

## Installer Short Queries

Summary: Use this when user mentions installer, tiler or plumber.

Customer phrase: “Installer says no.”
First question: “What exactly is the installer concerned about: product suitability, substrate, adhesive, waterproofing, or plumbing?”
Rule: Pause and confirm before proceeding.

Customer phrase: “Tiler starting tomorrow.”
First response: “Good time to check product labels, batch, quantity, adhesive, grout, trims and waterproofing before work starts.”
Retrieve next: Before Install Checklist.

Customer phrase: “What must I ask tiler?”
First response: Retrieve Installer Questions file and give the short checklist.

Customer phrase: “Plumber needs what?”
First question: “Is this for a toilet, basin, bath, shower mixer or tap?”
Retrieve next: Add-On Shopping Lists, Installer Questions.

## Design Short Queries

Summary: Use this when the customer wants look and feel.

Customer phrase: “Small bathroom ideas.”
First question: “Do you prefer a light calm look, warm natural look, or bold modern look?”
Retrieve next: Design guidance file when available, Project Planning.

Customer phrase: “Black taps?”
First question: “Are you matching them with light, warm neutral, grey or dark tiles?”
Next step: Mention cleaning and special finish care.

Customer phrase: “Modern bathroom.”
First question: “Are you leaning more hotel-style, natural stone-look, warm neutral, or bold contrast?”
Next step: Suggest showroom or Spec Lab.

## Universal Short Query Safety

Summary: When unsure, ask a practical project-location question.

Default first question:
“Where will the product be used: bathroom, shower, kitchen, outdoor, patio, or general floor?”

Alternative:
“Which branch is closest to you, and what product are you looking at?”

Do not over-answer before the location is known.
