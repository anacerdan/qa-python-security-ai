# Risk-Based Test Strategy

## Objective
Minimize production defects by prioritizing testing around business impact, integration complexity, security exposure, and change risk.

## Test Levels
1. Unit — developer-owned fast feedback
2. API/service — contract and business-rule validation
3. Integration — upstream/downstream interfaces
4. UI — critical user journeys
5. Regression — risk-based selection
6. Security — authentication, authorization, validation, data exposure

## Risk Matrix

| Risk | Likelihood | Impact | Priority | Response |
|---|---:|---:|---:|---|
| Authentication failure | Medium | High | P1 | API + UI + negative testing |
| Incorrect business rule | Medium | High | P1 | API + data validation |
| UI regression | High | Medium | P2 | Automated smoke/regression |
| Cosmetic issue | High | Low | P3 | Exploratory/manual |

## Entry Criteria
- Requirements baselined
- Test environment available
- Test data available
- Dependencies identified
- Acceptance criteria testable

## Exit Criteria
- Critical/high defects resolved or formally accepted
- Planned high-risk coverage executed
- Regression completed
- Test evidence retained
- Residual risk communicated

## Metrics
- Requirement coverage
- Risk coverage
- Automation coverage
- Pass/fail trend
- Defect discovery and leakage
- Defect aging
- Regression execution time
