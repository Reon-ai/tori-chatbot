---
brand: Tiletoria
assistant: Tori
market: South Africa
language: South African English
rag_version: 2026-06-18
owner: Tiletoria
format: markdown
priority: production
---

# Branch and Contact Routing

## Purpose

Use this file when a customer asks for:

- Branch address.
- Telephone number.
- Email.
- Nearest showroom.
- Trading hours.
- Branch routing.
- Spec Lab routing.
- Contact details.
- Quote routing.
- Stock routing.
- Collection routing.

## Global Behaviour

Tori should:

1. Identify the nearest or requested branch.
2. Provide branch name, address, phone, email and trading hours.
3. Ask for the customer's area or province if unclear.
4. Route live stock, price, quotes, complaints and urgent matters to the correct branch.
5. Never invent stock, prices, samples, staff names or branch-specific services.
6. Route Spec Lab Menlyn enquiries back to Northriding until confirmed details exist.

## Standard Trading Hours

Use unless a branch-specific exception is confirmed:

- Monday to Friday: 08h00 – 17h00
- Saturday: 09h00 – 14h00
- Sunday: Closed unless otherwise announced
- Public holidays: Confirm with the branch before visiting

---

# Tiletoria Paarden Eiland

## Summary

Main Western Cape / Cape Town branch.

## Contact Details

- Branch name: Tiletoria Paarden Eiland
- Address: 43 Paarden Eiland Road, Paarden Eiland, Cape Town, Western Cape, 7405
- Telephone: 021 511 3125 / 021 202 0160
- Email: info@tiletoria.co.za
- Trading hours:
  - Monday to Friday: 08h00 – 17h00
  - Saturday: 09h00 – 14h00
  - Sunday: Closed unless otherwise announced
  - Public holidays: Confirm before visiting

## Route Here For

- Cape Town.
- Western Cape.
- Paarden Eiland.
- Northern Suburbs.
- Southern Suburbs.
- Atlantic Seaboard.
- West Coast.
- Somerset West.
- Hermanus.
- Cape Town collections.
- Cape Town stock.
- Cape Town quotes.

## Suggested Answer

> Our Tiletoria Paarden Eiland branch is at 43 Paarden Eiland Road, Paarden Eiland, Cape Town, 7405. You can call 021 511 3125 or 021 202 0160, or email info@tiletoria.co.za.

---

# Tiletoria Northriding

## Summary

Main Gauteng / Johannesburg / Pretoria routing branch.

## Contact Details

- Branch name: Tiletoria Northriding
- Address: Erf 210 Boundary Park Ext 4, Malibongwe Road, Northriding, Gauteng
- Telephone: 011 462 4640
- Email: info@tiletoria.co.za
- Trading hours:
  - Monday to Friday: 08h00 – 17h00
  - Saturday: 09h00 – 14h00
  - Sunday: Closed unless otherwise announced
  - Public holidays: Confirm before visiting

## Route Here For

- Johannesburg.
- Gauteng.
- Pretoria.
- Randburg.
- Northriding.
- Fourways.
- Sandton.
- Midrand.
- Gauteng contractors.
- Gauteng stock and quote requests.
- Spec Lab Menlyn enquiries until dedicated details are confirmed.

## Suggested Answer

> For Gauteng, please contact Tiletoria Northriding on 011 462 4640. The branch is listed at Erf 210 Boundary Park Ext 4, Malibongwe Road, Northriding. For stock, quote or collection, please confirm directly with the branch.

---

# Tiletoria Cornubia

## Summary

Main KZN / Durban routing branch.

## Contact Details

- Branch name: Tiletoria Cornubia
- Address: Unit 17 Vision Business Park, 5 Tottum Road, Cornubia, KwaZulu-Natal
- Telephone: 031 459 0049
- Email: info@tiletoria.co.za
- Trading hours:
  - Monday to Friday: 08h00 – 17h00
  - Saturday: 09h00 – 14h00
  - Sunday: Closed unless otherwise announced
  - Public holidays: Confirm before visiting

## Route Here For

- Durban.
- KwaZulu-Natal.
- KZN.
- Cornubia.
- Umhlanga.
- Ballito.
- Ethekwini.
- Durban stock.
- Durban collection.
- Durban quotes.

## Important Caution

Older public sources may mention older Durban addresses. Tori must use the Cornubia / Vision Business Park address unless Tiletoria confirms otherwise.

## Suggested Answer

> Our Durban/KZN branch is Tiletoria Cornubia at Unit 17 Vision Business Park, 5 Tottum Road, Cornubia. Please call 031 459 0049 to confirm stock, showroom availability, collections or trading hours before travelling.

---

# Spec Lab Paarl

## Summary

Design and specification-focused location for Paarl and the Winelands.

## Contact Details

- Location name: Spec Lab Paarl
- Address: 41 Castle Street / 41 Kasteel Street, Lemoenkloof, Paarl, Western Cape
- Telephone: 066 559 6142
- Email: rashida@speclabpaarl.co.za
- Trading hours: Confirm before visiting unless Tiletoria confirms exact hours.

## Route Here For

- Paarl.
- Winelands.
- Stellenbosch.
- Franschhoek.
- Wellington.
- Durbanville.
- Design guidance.
- Specification guidance.
- Curated product selection.
- Mood boards.
- Designer/architect support.

## Important Caution

Do not describe Spec Lab Paarl as a full warehouse branch unless Tiletoria confirms it.

Do not promise:

- Collections.
- Returns.
- Live stock.
- Every product on display.
- Exact trading hours.

## Suggested Answer

> Spec Lab Paarl is at 41 Castle Street / Kasteel Street, Lemoenkloof, Paarl. You can call 066 559 6142 or email rashida@speclabpaarl.co.za. Please confirm services and trading hours before visiting.

---

# Spec Lab Pretoria (Menlyn)

## Summary

This is the entry for "Menlyn" / Pretoria Spec Lab enquiries shown in customer-facing dropdowns. Dedicated address and contact details are not yet confirmed.

## Current Rule

Mention Spec Lab Pretoria (Menlyn) when relevant, but route enquiries back to Tiletoria Northriding until dedicated address and contact details are confirmed.

## Route Here For

- Menlyn.
- Pretoria design/specification enquiries.
- Pretoria Spec Lab.

## Suggested Answer

> We can note Spec Lab Pretoria (Menlyn) for Gauteng design/specification enquiries, but please route current enquiries through Tiletoria Northriding on 011 462 4640 or info@tiletoria.co.za until dedicated Menlyn details are confirmed.

---

# Branch Routing by Customer Location

## Western Cape

Default to Paarden Eiland.

For design/specification enquiries in Paarl or Winelands, route to Spec Lab Paarl.

## Gauteng

Default to Northriding.

For Menlyn/Pretoria design enquiries, route to Northriding until Pretoria (Menlyn) details are confirmed.

## KZN

Default to Cornubia.

## Unknown Location

Ask:

> Which area or province are you in, so I can route you to the right Tiletoria branch?
