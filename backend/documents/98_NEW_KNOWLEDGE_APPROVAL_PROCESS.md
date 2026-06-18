# New Knowledge Approval Process

**Version:** 2026-06-18  
**Market:** South Africa / Southern Africa  
**Business:** Tiletoria / Tori RAG brain  
**Layer:** Phase 3 Control Layer  

## Purpose
Define how new Tori knowledge should be requested, written, approved, versioned and loaded into GitHub without creating contradictory or unsafe content.

## Retrieval triggers
- new knowledge
- approval
- update markdown
- GitHub
- version control
- content governance
- who approves
- knowledge request

## Purpose
Tori's knowledge must be controlled. Random unapproved files can make the bot contradict itself or create business risk.

## Knowledge request sources
New knowledge can come from:

- repeated customer questions
- staff feedback
- new product ranges
- supplier documents
- complaints
- policy changes
- branch process changes
- promotions
- new calculators
- failed answer logs

## Approval levels
### Level A: General guidance
Examples: measuring explanation, design tips, glossary.

Approver: customer service/sales lead.

### Level B: Product/technical guidance
Examples: adhesive, wet areas, large-format, LVT, slip guidance.

Approver: technical/product expert plus manager.

### Level C: Business process
Examples: returns, delivery, collections, account processes.

Approver: relevant department manager.

### Level D: Legal/privacy/warranty/safety
Examples: CPA, POPIA, public liability, formal warranty wording.

Approver: senior management/legal/privacy owner.

### Level E: Live data/API behaviour
Examples: stock, price, ERP, account, delivery system rules.

Approver: systems owner plus business owner.

## New file template
Use:

```markdown
# Topic

**Version:** YYYY-MM-DD
**Owner:** [department/person]
**Approval level:** [A-E]
**Market:** South Africa / Southern Africa

## Purpose
## Retrieval triggers
## Rules
## Questions to ask
## Safe responses
## Escalation
## Source of truth
## Review date
```

## Version control rule
Every file should include:

- version date
- owner/approver if known
- review date for policy-sensitive content
- clear replacement note if it supersedes older content

## Conflict rule
If two files disagree, Tori should follow this priority:

1. live approved system/API
2. official Tiletoria policy/document
3. supplier/manufacturer datasheet
4. approved technical guidance
5. general RAG guidance

## Loading into GitHub
Recommended process:

1. Draft Markdown file.
2. Review for hallucination, stock/price/legal risk.
3. Approver signs off.
4. Commit to GitHub with clear message.
5. Railway/backend re-ingests.
6. Test with expected questions.
7. Log pass/fail.

## Commit message examples
- `Add Tori knowledge: outdoor balcony escalation rules`
- `Update Tori quote workflow for contractor leads`
- `Fix RAG triggers for tile adhesive questions`
- `Deprecate old returns wording`

## Do not add
- unverified prices
- old promotions
- unofficial supplier claims
- personal staff opinions
- legal advice
- contradictory branch-specific rules without approval

---

## Universal Tori rule for this file
Tori must be helpful, practical and commercially safe. Tori may guide, calculate, explain, collect details and prepare a handover, but must not invent live stock, live prices, delivery availability, technical certifications, warranties, legal outcomes, account status, branch decisions or product suitability where site conditions are unknown. When the answer depends on current branch systems, ERP data, site inspection, supplier confirmation or management approval, Tori must clearly say so and route the customer to the correct Tiletoria team.
