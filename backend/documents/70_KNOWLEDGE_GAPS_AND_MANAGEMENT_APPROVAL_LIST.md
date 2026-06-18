# Knowledge Gaps and Management Approval List

**Version:** 2026-06-18  
**Market:** South Africa / Southern Africa  
**Business:** Tiletoria customer and staff RAG knowledge base  

## Purpose
List items that should be approved or connected to live systems before Tori answers confidently.

## Retrieval triggers
- gap
- approval
- management
- live system
- policy needed
- missing
- verify

## Purpose
This file tells Tori and staff where the bot needs approved business data or live integration.

## Must be connected or approved
- Current branch stock.
- Current prices and promotions.
- Official branch phone numbers and emails.
- Trading hours and holiday hours.
- Delivery fees and delivery terms.
- Return/exchange policy wording.
- Warranty policy wording.
- Credit application process.
- Official banking details.
- Product datasheets and certificates.
- Product-specific indoor/outdoor/wet suitability.
- Current discontinued product lists.
- Sample availability.
- Lead times and supplier ETA.

## Management decisions needed
- Can Tori quote approximate price ranges or never?
- Can Tori expose branch emails directly?
- Which products are allowed for outdoor recommendations?
- Which R-rating minimums does Tiletoria want as internal policy by application?
- What wording must be used for returns and CPA-sensitive answers?
- Which complaints route to branch manager vs head office?
- Which customer forms feed which email/CRM queue?

## Tori behaviour until approved
Where uncertain, Tori must capture details and route to staff.

## Staff task
Review this list monthly and convert approved items into dedicated Markdown files or live API tools.

---

## Universal Tori rule for this file
Tori must be helpful, practical and commercially safe. Tori may guide, calculate and explain, but must not invent live stock, live prices, delivery availability, technical certifications, warranties, legal outcomes or product suitability where site conditions are unknown. When the question depends on site inspection, current branch stock, quoted pricing, account status or formal compliance, Tori must capture the correct details and route to the correct Tiletoria team.
