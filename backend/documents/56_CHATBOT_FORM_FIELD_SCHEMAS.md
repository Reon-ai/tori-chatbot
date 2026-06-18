# Chatbot Form Field Schemas

**Version:** 2026-06-18  
**Market:** South Africa / Southern Africa  
**Business:** Tiletoria customer and staff RAG knowledge base  

## Purpose
Provide exact form structures the frontend/backend can trigger when Tori detects quote, contact, complaint, account, sample, delivery or technical intent.

## Retrieval triggers
- form
- lead form
- quote form
- contact me
- trigger
- schema
- fields
- frontend
- backend

## Form principle
When intent is clear, Tori should not make the customer type the same information repeatedly. Trigger the correct structured form.

## Universal fields
Use these on most forms:
- full_name
- cell_number
- email
- province
- suburb
- preferred_branch
- customer_type
- message
- consent_to_contact

## Quote form
Trigger when customer asks for price, quote, availability or project estimate.

Fields:
- product_name_or_code
- product_category
- application_area
- indoor_outdoor_wet
- dimensions_or_m2
- quantity_required
- delivery_or_collection
- delivery_suburb
- preferred_branch
- urgency_date
- upload_photos_optional

## Technical help form
Trigger for installation, suitability, wet area, outdoor, failure or product compatibility.

Fields:
- issue_type
- product_name_or_code
- tile_size_or_product_size
- installation_area
- substrate_type
- indoor_outdoor_wet
- installed_or_not_installed
- adhesive_grout_used
- photos_required
- invoice_or_order_if_available

## Complaint/return form
Fields:
- invoice_or_order_number
- branch_purchased_from
- purchase_or_delivery_date
- product_name_or_code
- quantity_affected
- installed_or_not_installed
- issue_description
- photos_required
- preferred_resolution

## Sample request form
Fields:
- project_name
- customer_type
- product_style_or_code
- application_area
- quantity_estimate
- branch_or_delivery_area
- deadline

## Account application enquiry form
Fields:
- company_name
- trading_name
- registration_number_optional
- vat_number_optional
- contact_person
- email
- cell_number
- province
- customer_category
- expected_monthly_spend

## Delivery enquiry form
Fields:
- order_or_quote_number_optional
- product_and_quantity
- delivery_address_or_suburb
- site_type
- access_restrictions
- offload_requirements
- required_date

## Backend handoff rule
Each form submission should create a clean summary for staff. Do not send raw chat history only.

## Tori microcopy before form
"I can get the right team to help. Please complete these few details so they can respond accurately."

---

## Universal Tori rule for this file
Tori must be helpful, practical and commercially safe. Tori may guide, calculate and explain, but must not invent live stock, live prices, delivery availability, technical certifications, warranties, legal outcomes or product suitability where site conditions are unknown. When the question depends on site inspection, current branch stock, quoted pricing, account status or formal compliance, Tori must capture the correct details and route to the correct Tiletoria team.
