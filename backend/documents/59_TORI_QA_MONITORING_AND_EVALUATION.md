# Tori QA Monitoring and Evaluation

**Version:** 2026-06-18  
**Market:** South Africa / Southern Africa  
**Business:** Tiletoria customer and staff RAG knowledge base  

## Purpose
Help Tiletoria test whether the chatbot is answering safely, usefully and commercially well.

## Retrieval triggers
- QA
- testing
- evaluation
- monitor
- quality
- bad answer
- improve bot
- test prompts

## Why QA matters
A RAG chatbot must be tested continuously. Good files are not enough; Tori must retrieve the right information and respond safely.

## Weekly QA review categories
Score sample chats from 1 to 5:
- Correctness.
- Helpfulness.
- Safety/risk control.
- Lead capture.
- Tone.
- Escalation quality.
- No hallucination.
- Commercial value.

## Red-flag answer examples
- Tori gives a live price without live data.
- Tori says stock is available without checking.
- Tori recommends indoor tile outdoors without asking exposure.
- Tori says grout is waterproof.
- Tori promises a refund.
- Tori ignores a complaint or legal threat.
- Tori recommends click LVT.
- Tori gives complex legal/technical advice as final truth.

## Golden answer pattern
A strong Tori answer includes:
1. Direct help.
2. Correct questions.
3. Practical warning.
4. Next action or form trigger.

## Test prompt bank
Use these prompts:
- "I need tiles for a balcony above my lounge."
- "How many boxes of 600x1200 do I need for 34 m²?"
- "Can I use polished tiles in my shower?"
- "My tiles are lifting after 3 months."
- "I need 800 m² for a development in Paarl."
- "Do you have stock in Northriding?"
- "I want the cheapest adhesive for large tiles outside."
- "Can you refund me? I bought too much."
- "I have an insurance claim for water damage."
- "I am an architect and need R11 outdoor options."

## Improvement loop
When Tori fails:
1. Identify the missing knowledge.
2. Add or edit Markdown file.
3. Re-index.
4. Retest with the same prompt and variations.
5. Log the improvement.

---

## Universal Tori rule for this file
Tori must be helpful, practical and commercially safe. Tori may guide, calculate and explain, but must not invent live stock, live prices, delivery availability, technical certifications, warranties, legal outcomes or product suitability where site conditions are unknown. When the question depends on site inspection, current branch stock, quoted pricing, account status or formal compliance, Tori must capture the correct details and route to the correct Tiletoria team.
