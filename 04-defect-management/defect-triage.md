# Defect Triage and Root Cause Analysis

## Defect Record

**Title:** API returns success when required business field is missing  
**Severity:** High  
**Priority:** P1  
**Area:** API / business validation  
**Environment:** Test  

### Reproduction
1. Send request without the required field.
2. Verify HTTP response and payload.
3. Compare actual behavior with acceptance criteria.

### Expected
Validation error with a clear client-safe message.

### Actual
Request is accepted and downstream processing begins.

### Risk
Invalid business data can enter downstream processing and create reconciliation or customer-impacting defects.

## RCA Framework

- **Trigger:** Missing validation rule.
- **Escape point:** API integration test coverage did not include the negative scenario.
- **Systemic cause:** Requirements were not mapped to negative test conditions.
- **Corrective action:** Add API contract/negative tests and requirement traceability.
- **Preventive action:** Review negative scenarios during test-case review and add them to regression automation.
