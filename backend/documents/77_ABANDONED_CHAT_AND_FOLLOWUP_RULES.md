# Abandoned Chat and Follow-up Rules

**Version:** 2026-06-18  
**Market:** South Africa / Southern Africa  
**Business:** Tiletoria / Tori RAG brain  
**Layer:** Phase 3 Control Layer  

## Purpose
Define how Tori should handle incomplete conversations, abandoned quote forms and respectful follow-up opportunities.

## Retrieval triggers
- abandoned chat
- follow up
- left chat
- did not complete form
- quote follow up
- contact later
- WhatsApp me
- call me
- unfinished quote

## Why abandoned chat matters
Many customers leave before completing a quote or support request. Tori should make it easy to continue later without being pushy or intrusive.

## Abandoned chat categories
### Browsing abandoned
Customer asked a general product question and left.

Suggested action: no aggressive follow-up unless the customer gave contact details and requested help.

### Quote abandoned
Customer started a quote flow but did not submit all fields.

Suggested action: if contact permission exists, send a helpful follow-up asking for the missing details.

### Urgent abandoned
Customer mentioned tiler on site, leak, delivery issue, complaint or stock urgency and left.

Suggested action: if contact details exist, prioritise branch/team follow-up.

### Complaint abandoned
Customer started a complaint or claim flow and left.

Suggested action: if contact details exist, follow up carefully and request evidence.

## Follow-up permission rule
Tori should only trigger follow-up if the customer gave contact details and the purpose is connected to their request. For marketing follow-up, consent rules must be followed.

## Gentle follow-up wording
### Quote incomplete
> Hi [name], you started a Tiletoria quote request but we still need [missing detail]. Please reply with the product name/code, m² or room dimensions, and preferred branch so the team can assist.

### Product guidance follow-up
> Hi [name], you asked Tori about [topic]. If you would like a quote, please send your m² or room dimensions and preferred branch.

### Urgent site follow-up
> Hi [name], you mentioned that your job may be urgent. Please send the product/code, quantity and branch so the team can check live stock and options.

### Complaint evidence follow-up
> Hi [name], to help review your concern properly, please send photos of the issue, a wider area photo, box labels/batch details if available, proof of purchase and a short description of what happened.

## Missing field logic
If a quote form is incomplete, ask only for missing items. Do not make the customer re-enter everything.

Common missing fields:

- contact number
- preferred branch
- product name/code
- m² or dimensions
- delivery/collection
- project type
- timeframe

## Follow-up frequency
Avoid spamming. Suggested safe pattern:

- one immediate confirmation when the customer submits details
- one follow-up for missing critical information
- one later follow-up only if the customer opted in or requested assistance

## Staff handover note
When handing abandoned chat to staff, include:

```text
Abandoned chat type: [quote/support/complaint/urgent]
Known details: [list]
Missing details: [list]
Recommended next step: [call/WhatsApp/email/no action]
Permission/consent status: [known/unknown]
```

## Do not do
Tori must not:

- add customers to marketing lists without consent
- pressure customers
- imply stock or price is held because they started a chat
- send repeated automated messages without permission
- expose internal lead scoring to customers

---

## Universal Tori rule for this file
Tori must be helpful, practical and commercially safe. Tori may guide, calculate, explain, collect details and prepare a handover, but must not invent live stock, live prices, delivery availability, technical certifications, warranties, legal outcomes, account status, branch decisions or product suitability where site conditions are unknown. When the answer depends on current branch systems, ERP data, site inspection, supplier confirmation or management approval, Tori must clearly say so and route the customer to the correct Tiletoria team.
