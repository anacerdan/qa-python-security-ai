# AI-Assisted QA

This project demonstrates practical, reviewable use of AI in the STLC.

## Use Cases

### 1. Requirements analysis
Convert requirements into:
- functional scenarios
- negative scenarios
- boundary conditions
- integration risks
- questions and ambiguities

### 2. Test case generation
Generate a first draft of test cases from acceptance criteria, then review for:
- missing risk coverage
- duplicate scenarios
- invalid assumptions
- testability

### 3. Regression selection
Use change scope, dependency information, defect history and risk to recommend a regression subset.

### 4. Defect triage
Summarize evidence, cluster similar defects and suggest likely component ownership. A human remains responsible for severity, priority and root-cause decisions.

### 5. Test data
Generate synthetic test data while avoiding production PII and secrets.

## Human-in-the-loop rule

AI-generated tests are **drafts, not evidence**. The QA engineer validates requirements, expected results, data, security implications and execution evidence before approval.
