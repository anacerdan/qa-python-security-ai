# API Security Testing Checklist

For systems you own or are explicitly authorized to test.

## Authentication
- Missing credentials rejected
- Expired/invalid credentials rejected
- Authentication errors do not disclose sensitive details

## Authorization
- Users cannot access resources outside their permitted scope
- Role changes take effect correctly
- Object-level authorization is validated

## Input Validation
- Required fields enforced
- Data types and length constraints enforced
- Unexpected input is rejected safely
- Error responses avoid stack traces and secrets

## Data Exposure
- Sensitive fields are excluded when not required
- Tokens and credentials are never returned in logs or responses
- Security headers are reviewed where applicable

## Abuse Resistance
- Rate limiting behavior is verified where required
- Oversized requests are handled safely
- Repeated failures are observable

## OWASP Alignment
Map each test to the applicable OWASP API Security Top 10 category and retain evidence.
