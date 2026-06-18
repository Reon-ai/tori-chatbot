# Afrikaans and Local Terms Mapping

**Version:** 2026-06-18  
**Market:** South Africa / Southern Africa  
**Business:** Tiletoria / Tori RAG brain  
**Layer:** Phase 3 Control Layer  

## Purpose
Map common Afrikaans, South African English and local hybrid terms to the correct Tori intent while keeping Tori's answer in English unless instructed otherwise.

## Retrieval triggers
- Afrikaans
- local terms
- teëls
- teels
- gom
- sement
- vloer
- muur
- badkamer
- kombuis
- stoep
- braaikamer
- plakker
- kwotasie

## Language rule
Tori should answer in English by default unless the customer clearly asks for Afrikaans or another language. However, Tori must understand local terms.

## Afrikaans/local term mapping
- teëls / teels = tiles
- vloerteëls = floor tiles
- muurteëls = wall tiles
- badkamer = bathroom
- kombuis = kitchen
- stoep = patio/veranda/outdoor covered area
- braaikamer / braai room = braai/entertainment room
- gom = glue/adhesive
- teëlgom = tile adhesive
- sement = cement; may mean adhesive in customer language
- voegbry / grout = grout
- waterdigting = waterproofing
- stort = shower
- bad = bath
- kraan = tap
- menger = mixer
- toilet = toilet
- wasbak = basin/sink
- vloer = floor
- muur = wall
- plakker / teëlplakker = tiler
- bouer = builder
- loodgieter = plumber
- kwotasie = quote
- aflewering = delivery
- optel / afhaal = collection
- voorraad = stock
- prys = price
- boks / bokse = box/boxes

## Common mixed-language customer examples
### "Het julle voorraad van hierdie teel?"
Intent: stock check.

Response should ask for product/code, branch and quantity.

### "Ek soek gom vir 600x1200 teels"
Intent: adhesive guidance for large-format tiles.

Response should explain adhesive depends on tile, substrate and site conditions; route for product recommendation.

### "Kan ek dit op my stoep gebruik?"
Intent: outdoor/patio suitability.

Ask about rain exposure, slope, wet conditions and product rating.

### "Wat kos dit per m2?"
Intent: price per m².

Requires live branch price confirmation.

### "Stuur kwotasie"
Intent: quote request.

Trigger quote form.

## Customer-friendly bridge wording
If the customer uses Afrikaans terms but Tori replies in English:

> Yes, I can help with that. For the stoep/patio area, I need to know whether it gets wet and whether the surface has a slope.

## Do not over-translate brand/product names
Keep product names, codes and branch names exactly as entered where possible.

## Staff note
If Tiletoria later wants bilingual support, create separate approved Afrikaans response templates. Until then, Tori should understand Afrikaans/local terms but answer clearly in English.

---

## Universal Tori rule for this file
Tori must be helpful, practical and commercially safe. Tori may guide, calculate, explain, collect details and prepare a handover, but must not invent live stock, live prices, delivery availability, technical certifications, warranties, legal outcomes, account status, branch decisions or product suitability where site conditions are unknown. When the answer depends on current branch systems, ERP data, site inspection, supplier confirmation or management approval, Tori must clearly say so and route the customer to the correct Tiletoria team.
