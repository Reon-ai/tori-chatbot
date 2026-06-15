# Tori UX 00: Retrieval Manifest and File Map

This file helps Tori retrieve the correct UX flow file and knowledge file from short, practical South African customer messages.

Purpose: Use this as the index file for Tori’s RAG system.

Important rule: UX files guide the conversation sequence. Product knowledge files provide technical answers.

## Retrieval Priority

Summary: If the customer’s message is short, unclear or broad, retrieve UX files before technical files.

Priority 1: Master prompt inside chatbot.
Use: Always active.
Purpose: Controls tone, behaviour, safety, one-question rule and escalation.

Priority 2: UX orchestration files.
Use: Short queries, unclear intent, customer journey, user-type routing, handover, next-best-step logic.

Priority 3: Product and technical RAG files.
Use: Tiles, glue-down LVT, sanitaryware, tapware, adhesives, grout, spacers, cleaning, suitability, calculations and complaints.

Priority 4: Store and commercial routing files.
Use: Stock, price, quote, branch, collection, delivery, returns, samples and complaints.

## UX File Map

Summary: These files teach Tori how to behave.

File: tiletoria_tori_ux_01_master_flow_controller.md
Use when: Any conversation starts, query is vague, or Tori must decide what to ask next.

File: tiletoria_tori_ux_02_south_african_short_query_interpreter.md
Use when: Customer uses short phrases like “outside tile”, “got stock”, “bathroom floor”, “need glue”, “can this go shower”, “how many boxes”.

File: tiletoria_tori_ux_03_user_type_routing_playbooks.md
Use when: Customer seems to be DIY, homeowner, renovator, contractor, developer, designer, architect or quantity surveyor.

File: tiletoria_tori_ux_04_intent_router_next_best_step_map.md
Use when: Tori must decide which knowledge file to retrieve next.

File: tiletoria_tori_ux_05_minimum_question_sets_by_scenario.md
Use when: Tori needs missing information and must ask only one useful question.

File: tiletoria_tori_ux_06_project_journey_playbooks.md
Use when: Customer is planning a project, not asking a single product question.

File: tiletoria_tori_ux_07_response_templates_and_style.md
Use when: Tori needs a concise, South African, customer-friendly response pattern.

File: tiletoria_tori_ux_08_lead_capture_and_handover.md
Use when: Human follow-up, quote, stock, complaint, trade project or branch handover is required.

File: tiletoria_tori_ux_09_do_not_hallucinate_rules.md
Use when: Stock, price, delivery, returns, claims, safety, compliance or high-risk suitability appear.

File: tiletoria_tori_ux_10_test_prompt_evaluation_set.md
Use when: Testing chatbot performance.

## Existing Knowledge File Map

Summary: Retrieve these after the UX file identifies intent.

File: tiletoria_rag_measurement_quantity_calculation_reference_guide.md
Use for: how many boxes, adhesive, grout, spacers, clips, wedges, trims, self-leveller, waterproofing, glue-down LVT adhesive, quantities.

File: tiletoria_rag_utility_01_what_else_do_i_need_addon_shopping_lists.md
Use for: what else do I need, add-ons, accessories, shopping list.

File: tiletoria_rag_utility_02_before_you_install_inspection_stop_work_checklist.md
Use for: before installing, inspect boxes, wrong batch, wrong adhesive, no waterproofing, stop work.

File: tiletoria_rag_utility_03_south_african_consumer_project_planning_guides.md
Use for: bathroom renovation, kitchen, patio, braai room, rental, body corporate, old house, new build, coastal, Gauteng, KZN, Western Cape.

File: tiletoria_rag_utility_04_complaint_triage_and_escalation_guide.md
Use for: complaints, warranty, cracked, leaking, broken, slippery, loose, chipped, bubbling, peeling.

File: tiletoria_rag_utility_05_product_suitability_decision_guide.md
Use for: can I use this here, outside, bathroom, shower, balcony, pool, ramp, LVT bathroom, wall tile on floor.

File: tiletoria_rag_utility_06_installer_questions_trade_handover_guide.md
Use for: questions for tiler, plumber, installer, handover, final payment, snag list.

File: tiletoria_rag_utility_07_cleaning_and_maintenance_schedules.md
Use for: cleaning, maintenance, grout haze, limescale, black tap care, glue-down LVT cleaning, patio algae.

File: tiletoria_rag_utility_08_budget_drivers_project_cost_explainers.md
Use for: budget, cost drivers, why expensive, quote comparison, hidden costs.

File: tiletoria_store_details_for_tori_chatbot.md
Use for: branch, address, phone, Cape Town, Johannesburg, Durban, Paarl, stock, price, quote, collection, delivery.

## Universal Retrieval Keywords

Summary: These short words should trigger the correct routing.

“outside”, “patio”, “braai room”, “pool”, “balcony”:
Retrieve: Short Query Interpreter, Product Suitability, Project Planning, Add-On Shopping Lists.

“bathroom”, “shower”, “toilet”, “basin”, “bath”:
Retrieve: Minimum Question Sets, Project Journey Playbooks, Product Suitability, Add-On Shopping Lists.

“stock”, “price”, “quote”, “collect”, “delivery”:
Retrieve: Store Details, Intent Router, Lead Capture Handover, Do-Not-Hallucinate Rules.

“how many”, “m2”, “boxes”, “bags”, “clips”:
Retrieve: Measurement Guide, Minimum Question Sets, Intent Router.

“installer”, “tiler”, “plumber”, “snag”:
Retrieve: Installer Questions, Before Install, Lead Capture Handover.

“complaint”, “faulty”, “leaking”, “broken”, “slippery”:
Retrieve: Complaint Triage, Do-Not-Hallucinate Rules, Store Details.

## Global Safe Phrase

Summary: Use this when final details require branch, installer or plumber confirmation.

Safe phrase:
“I can guide you, but final stock, pricing, suitability or installation details must be confirmed by the relevant Tiletoria branch, installer or plumber.”
