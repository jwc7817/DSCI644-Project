# DSCI 644: The "Meaning-Typed Programming" (MTP) Challenge

Done as a semester-long project for RIT's DSCI 644 applying software engineering principles to Data Science and AI workflows. Out of three tracks, we chose Option #2, which was the MTP challenge. The main objective of this project is on engineering quality-reproductibility, testing, modularity, and documenation rather than just model accuracy. 

---
### Project Overview
- Focus: Engineering robust AI applications using the byLLM framework.
- Context: Traditional LLM integration relies on fragile string prompting. You will investigate Meaning-Typed Programming, where you use semantic types (native code) to control AI behavior.
- Goal: Build a data-intensive application (e.g., an automated data cleaning pipeline or a complex information extraction tool) using the `by <model>` operator. Evaluate if this method improves code maintainability and reliability compared to standard prompt engineering.
- Resources: byLLM (Jaseci) & MTP: Meaning-Typed Language Abstraction (2025).

### Research Question (RQ)
- Data Quality: For dirty datasets, can the by
operator (via byLLM) detect and repair dirty records (e.g.,
inconsistent date formats, missing labels) with lower misin-
terpretation rate and comparable or better precision/recall
than regex-based scripts and prompt-based LLM calls?

### Phases & Deliverables
***PHASE 1 | 2026-02-06 | COMPLETED***  
Definition & Open Investigation
- Goal: Define problem scope and validate feasibility of approach.
- Activities:
    - Literature/Context Review: Read MTP paper.
    - Problem Definition: Clearly state what we are building or analyzing.
    - Sanity Check: Propose a high-level architecture. (e.g., "We will ingest the AIDev dataset into MongoDB and use PyDriller to extract metrics.")
    - Deliverable: 1-2 page report outlining the problem, dataset strategy, and Research Questions.

***PHASE 2 | 2026-02-27 | IN PROGRESS***  
Initial Solution (The Baseline)
- Goal: Build an end-to-end "Skeleton" pipeline to identify engineering bottlenecks.
- Activities:
    - Data Ingestion: Write scripts to load and clean your initial data.
    - Baseline Implementation: A "Manual Prompting" version of your app to serve as a baseline.
    - Reflection: Identify "Why is this hard?" (e.g., "The data is too large for memory" or "The LLM is inconsistent").
    - Deliverable: 3-5 page report detailing the initial design, preliminary results, and technical challenges.

***PHASE 3 | 2026-03-19 | NOT STARTED***  
Optimized Solution (Refinement)
- Goal: Apply SE patterns to improve performance, reliability, and validity.
- Activities:
    - Optimization: Address Phase 2 limitations.
    - Implement the full byLLM abstraction with refined Type definitions.
    - Validation: Run your solution on the full dataset.
    - Deliverable: 8-10 page report presenting the improved architecture, quantitative results, and a discussion of trade-offs.

***PHASE 4 | 2026-04-24 | NOT STARTED***  
Final Report and Package
- Goal: Documentation, Validation Analysis, and Packaging.
- Activities:
    - Confusion Matrix / Error Analysis: 
        - If building a tool: When does it fail? (False Positives/Negatives).
        If analyzing data: What are the threats to validity?
    - Documentation: README.md, environment setup (requirements.txt / Dockerfile), and inline comments.
    - Packaging: Organize code into a proper structure (e.g., src/, tests/, data/).
    - Deliverables:
        - Presentation: Live demo and defense of your results.
        - Final Report: 10+ page report + GitHub Repository link.

***Grade Distribution Summary***  
(Phase, Focus, Deliverable, Weight)  
i. Problem Definition, 1-2 Page Report, 20%  
ii. Baseline & Initial Prototype, 3-5 Page Report, 20%  
iii. Optimized Solution, 8-10 Page Report, 20%  
pre-iv. Presentation, Live Demo/Presentation, 20%  
iv. Final Package, 10+ Page Report + Code, 20%  
