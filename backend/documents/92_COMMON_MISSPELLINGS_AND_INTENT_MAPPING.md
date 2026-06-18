# Common Misspellings and Intent Mapping

**Version:** 2026-06-18  
**Market:** South Africa / Southern Africa  
**Business:** Tiletoria / Tori RAG brain  
**Layer:** Phase 3 Control Layer  

## Purpose
Help Tori recognise common spelling mistakes, shorthand and typo patterns in tile, LVT, sanitaryware and branch enquiries.

## Retrieval triggers
- misspellings
- typos
- teels
- tils
- porcelin
- ceremic
- grouting
- adhesif
- northriding
- cornubie
- paarden eiland
- speclab

## Purpose
Customers type quickly on mobile. Tori should infer likely intent without embarrassing the customer.

## Product spelling patterns
- teels / tils / tails = tiles
- porcelin / porceline / porcalain = porcelain
- ceremic / seramic = ceramic
- rectifide / rectified tile = rectified
- polished / polish tile = polished finish
- matt / matte = matt finish
- grouting / growt / grout = grout
- tile glue / tile cement / adhesif = adhesive
- levling clips / leveling clips = levelling clips
- spacer / spacers / tile spacer = spacers
- trims / trimms / edging = trims/profiles
- vinal / vinyl / LVT = glue-down LVT in Tiletoria context
- sanitary / sanitory / sanware = sanitaryware
- mixer / mixa = mixer tap
- basin / sink = basin/sink depending context

## Branch/location spelling patterns
- Paarden Eiland / Paarden Island / Paardeneiland = Cape Town branch area
- Northriding / North Riding / Nortriding = Northriding/Gauteng
- Cornubie / Cornubia = KZN/Durban region branch context
- Paarl / Parl = Spec Lab Paarl context where relevant
- Menlyn = Spec Lab Menlyn reference; route according to approved branch routing file

## Intent phrases and likely routing
### "price per meter"
Likely means price per m². Ask product/branch and clarify m².

### "how much for a room"
Intent: measure/quote. Ask dimensions and product.

### "need 20 squares"
May mean 20 m². Confirm.

### "can I fetch"
Intent: collection. Needs branch, stock confirmation, order/payment status.

### "deliver to site"
Intent: delivery quote/logistics. Needs address/suburb, quantity, branch.

### "tiles lifting"
Intent: failure/complaint/technical. Trigger evidence and escalation.

### "floor making hollow sound"
Intent: hollow tile diagnostic. Ask for video/photos and installation details.

### "black marks on tile"
Intent: cleaning/maintenance or defect. Ask when appeared and cleaning products used.

## Clarification rule
If the typo could map to more than one intent, Tori should clarify politely.

Example:

> When you say "cement", do you mean tile adhesive for installing tiles, or grout for filling the joints after installation?

## Do not say
Do not say:

- "I think you spelled that wrong."
- "That word is incorrect."

Preferred:

> Just to make sure I guide you correctly, do you mean [option A] or [option B]?

## RAG keyword expansion
When creating future files, include both professional and customer language:

- adhesive and tile glue
- grout and voeg
- m² and squares
- collection and fetch
- quote and quotation/kwotasie
- branch and store

---

## Universal Tori rule for this file
Tori must be helpful, practical and commercially safe. Tori may guide, calculate, explain, collect details and prepare a handover, but must not invent live stock, live prices, delivery availability, technical certifications, warranties, legal outcomes, account status, branch decisions or product suitability where site conditions are unknown. When the answer depends on current branch systems, ERP data, site inspection, supplier confirmation or management approval, Tori must clearly say so and route the customer to the correct Tiletoria team.
