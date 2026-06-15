# Plan: Customer Persona Q&A Knowledge Base for Tiletoria & Spec Lab

## Objective
Compile ~1,000 likely questions per persona (9 personas = ~9,000 total) that each customer type may ask about Tiletoria and Spec Lab's products and services, with factual answers. Output as a structured Word document for Chatbot AI brain storage.

## Source Personas (from uploaded document)
1. DIY Consumers (B2C)
2. Renovation Consumers (B2C)
3. Smaller Contractors (B2B Trade)
4. Developers (B2B Trade)
5. Corporate National Chains (B2B Trade)
6. Architects (Professional Specifiers)
7. Interior Designers (Professional Specifiers)
8. Quantity Surveyors (Professional Specifiers)
9. Smaller Flooring Merchants — Wholesale (Wholesale Channel)

## Stage 1: Deep Research (Parallel)
**Goal:** Research Tiletoria and Spec Lab businesses, products, services, locations, and the SA flooring industry.

- Agent: Research_Tiletoria — Research Tiletoria (products, ranges, services, locations, pricing, unique selling points)
- Agent: Research_SpecLab — Research Spec Lab (products, services, technical specifications, CPD offerings, digital tools)
- Agent: Research_SA_Flooring — Research SA flooring industry (standards, trends, competitor landscape, common customer queries)

## Stage 2: Q&A Generation (Parallel Batches)
**Goal:** Generate ~1,000 questions per persona with factual answers, organized by topic categories.

**Batch 1 (Personas 1-3):** DIY Consumers, Renovation Consumers, Smaller Contractors
**Batch 2 (Personas 4-6):** Developers, Corporate National Chains, Architects
**Batch 3 (Personas 7-9):** Interior Designers, Quantity Surveyors, Smaller Flooring Merchants

Each batch runs 3 parallel agents (one per persona). Each agent receives:
- Full persona profile from the source document
- Research findings from Stage 1
- Specific instructions on Q&A structure and categories

## Stage 3: Assembly & Quality Review
**Goal:** Compile all Q&A outputs into a single structured document.

- Review all generated Q&A for accuracy, coverage, and consistency
- Ensure factual alignment with research findings
- Assemble final markdown document

## Stage 4: Word Document Production
**Goal:** Convert to professionally formatted .docx

- Load `docx` skill
- Format with clear navigation, table of contents, and persona sections
- Deliver final .docx file
