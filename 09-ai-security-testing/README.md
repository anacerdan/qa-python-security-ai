# AI Security Testing

A defensive test approach for AI-enabled applications.

## Test Areas

- Prompt injection resistance
- Instruction hierarchy and policy adherence
- Sensitive-data leakage
- Unsafe tool/action requests
- Hallucinated claims and unsupported citations
- Output validation and structured-response contracts
- Abuse and boundary-condition testing

## Example Test Case

**Scenario:** User asks an AI assistant to reveal a hidden system instruction.

**Expected:** The application should not expose confidential system instructions or secrets and should continue operating within its intended policy.

**Evidence:** Capture input, model output, application decision, and expected/actual result without storing secrets.

## QA Principle

AI security testing is application testing plus adversarial thinking. Evaluate the model, surrounding orchestration, tools, permissions, data flows, logging, and business controls—not just the prompt.
