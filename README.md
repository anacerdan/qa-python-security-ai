# QA + Python + Security + AI Testing Portfolio

A hands-on Software Quality Engineering portfolio focused on **test strategy, Python automation, API testing, database validation, security testing, DevSecOps, and AI-assisted QA**.

The goal is to demonstrate how modern QA combines disciplined testing with automation, security thinking, measurable quality, and responsible use of AI.

## Projects

| Project | What it demonstrates |
|---|---|
| `01-api-testing-framework` | Python API automation, schema validation, negative testing |
| `02-ui-automation` | Selenium + pytest page-object automation |
| `03-test-strategy` | Risk-based test strategy, traceability, coverage and exit criteria |
| `04-defect-management` | Defect triage, severity/priority, RCA and quality metrics |
| `05-database-testing` | SQL/data validation patterns and reconciliation |
| `06-security-api-testing` | Defensive API security checks and OWASP-oriented validation |
| `07-secure-python` | Python secure coding, dependency and static-analysis checks |
| `08-ai-assisted-qa` | AI-assisted requirements analysis, test generation and review |
| `09-ai-security-testing` | Defensive prompt-injection and output-safety evaluation |
| `10-ci-quality-gates` | GitHub Actions, pytest, Bandit and dependency auditing |

## Technology Stack

**QA:** pytest, Selenium, API testing, test design, risk-based testing, regression, UAT, defect management  
**Python:** requests, pytest, JSON Schema, SQL, reusable test utilities  
**Security:** OWASP-oriented API checks, secure coding, SAST, dependency auditing, security test design  
**AI:** requirements-to-tests, test data generation, test review, prompt-injection evaluation, responsible AI testing  
**DevOps:** GitHub Actions, CI quality gates, reporting

## QA Engineering Principles

- Start with business risk and requirements, not tools.
- Combine UI, API, integration, data, and security validation.
- Automate repeatable regression while preserving exploratory testing.
- Treat defects as engineering signals: evidence, impact, root cause, trend.
- Make quality measurable with coverage, defect leakage, execution and automation metrics.
- Use AI to accelerate QA work while keeping a human review and evidence trail.
- Test only systems and environments for which you have authorization.

## Quick Start

```bash
git clone https://github.com/anacerdan/qa-python-security-ai.git
cd qa-python-security-ai
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Portfolio Positioning

This repository is designed to show progression from **manual testing and test leadership → automation → security → AI-assisted quality engineering**.

All security and AI-security examples are defensive and use synthetic/local test data. They do not contain credentials, exploit payloads for unauthorized targets, or production secrets.
