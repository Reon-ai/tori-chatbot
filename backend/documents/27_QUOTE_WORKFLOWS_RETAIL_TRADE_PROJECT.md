# Quote Workflows — Retail, Trade and Project Customers

**Version:** 2026-06-18  
**Market:** South Africa / Southern Africa  
**Business:** Tiletoria customer and staff RAG knowledge base  

## Purpose
Give Tori a structured quoting journey for different customer types and purchase intents.

## Retrieval triggers
- quote
- quotation
- price me
- estimate
- how much
- send me a quote
- bulk price
- project price
- developer price
- trade price

## Quote intent detection
Quote intent is present when the customer says:
- "Can I get a price?"
- "Quote me."
- "How much will it cost?"
- "I need tiles for my bathroom/kitchen/house."
- "Do you deliver to..."
- "I need 80 m²."
- "I am a contractor/developer/designer/architect/QS."

## Universal quote flow
1. Confirm application.
2. Confirm product or style direction.
3. Confirm quantity or help calculate it.
4. Confirm branch or delivery area.
5. Capture customer details.
6. Route to branch or sales team.

## Minimum quote fields
- Name and surname.
- Cell number.
- Email.
- Province / suburb / delivery area.
- Preferred branch: Cape Town, Northriding, Cornubie/KZN or other.
- Product name/code or style description.
- Area in m² or room dimensions.
- Application: floor, wall, bathroom, shower, patio, balcony, commercial, etc.
- DIY or trade/professional.
- Need delivery or collection?
- Urgency/date required.

## Retail homeowner quote
Tori should be friendly and supportive. Help the customer calculate, then capture details.

Suggested response:
"Absolutely — I can help you get this quote ready. Please share the room length and width, or the total m² if you already have it. Also tell me whether this is for a floor, wall, bathroom, shower, patio or another area."

## Tiler or contractor quote
Tori should be quicker and more trade-focused.

Ask:
- Product/code.
- Required m² or boxes.
- Adhesive/grout/trim required?
- Branch/collection/delivery.
- Account customer or COD?
- Site suburb.

## Designer or architect quote
Ask:
- Project name.
- Client name if allowed.
- Specification/product style.
- Area schedule.
- Finish and slip requirement.
- Lead time.
- Need samples?
- Need technical sheet?

## Developer or QS quote
Ask:
- Project name.
- Bill of quantities or schedule.
- Required quantities per product.
- Phase dates.
- Site address.
- Delivery constraints.
- Required documentation.
- Contact person.
- Tender closing date.

## Insurance replacement quote
Ask:
- Claim number if available.
- Insurer/assessor/contractor name if available.
- Damaged area m².
- Existing tile size, colour and photos.
- Urgency.
- Material-only or contractor-managed.

## When to include add-ons
If customer quotes tiles, Tori should remind them about:
- Adhesive.
- Grout.
- Spacers or levelling clips.
- Trims/profiles.
- Waterproofing for wet areas.
- Primer/self-levelling where substrate needs preparation.
- Extra tiles for cuts, waste and future repairs.

## Safe quote handover sentence
"I have the details needed to prepare a proper quote. A Tiletoria team member should confirm the final product, stock, branch price and delivery before the quote is issued."

---

## Universal Tori rule for this file
Tori must be helpful, practical and commercially safe. Tori may guide, calculate and explain, but must not invent live stock, live prices, delivery availability, technical certifications, warranties, legal outcomes or product suitability where site conditions are unknown. When the question depends on site inspection, current branch stock, quoted pricing, account status or formal compliance, Tori must capture the correct details and route to the correct Tiletoria team.
