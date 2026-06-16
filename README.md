# Contract-Governed AI Interview Assistant

## Overview

This project demonstrates how executable API contracts can improve reliability, reduce integration uncertainty, and act as guardrails for AI-assisted software development.

The application is a full-stack AI Interview Assistant built using:

- React (Frontend)
- FastAPI (Backend)
- OpenAPI (API Contract)
- Specmatic (Contract Testing, Validation & Service Virtualization)

The OpenAPI contract serves as the single source of truth for both frontend and backend development.

---

## Problem Statement

AI coding assistants can generate working code rapidly, but they can also introduce implementation drift from agreed API contracts.

Common issues include:

- Incorrect field names
- Missing required properties
- Unexpected response structures
- Integration failures discovered late in development
- Increased debugging effort

Without executable contracts, these issues are often detected only during integration testing or production.

---

## Solution

This project adopts a **Contract-First Development** approach.

The API is defined using OpenAPI and treated as the source of truth.

Specmatic is used to:

- Generate executable mocks from the contract
- Enable frontend development before backend completion
- Validate implementation behavior against the contract
- Detect contract violations before integration testing
- Generate API coverage reports
- Act as guardrails for AI-assisted development

---

# Architecture

```text
React Frontend
       |
       v
OpenAPI Contract (Source of Truth)
       |
       +-------------------+
       |                   |
       v                   v
Specmatic Mock      Contract Validation
       |                   |
       +-------------------+
               |
               v
          FastAPI Backend
```

The OpenAPI specification acts as the single source of truth.

Instead of treating documentation as an afterthought, the contract drives development, testing, validation, and integration.

---

## Project Structure

![Project Structure](docs/images/project-structure.png)

---

# API Contract

Location:

```text
contracts/interview-api.yaml
```

## Generate Interview Questions

### Endpoint

```http
POST /generate-questions
```

### Request

```json
{
  "role": "Machine Learning Engineer"
}
```

### Response

```json
{
  "questions": [
    "What is supervised learning?",
    "Explain overfitting.",
    "What is feature engineering?"
  ]
}
```

---

## Evaluate Answer

### Endpoint

```http
POST /evaluate-answer
```

### Request

```json
{
  "question": "What is supervised learning?",
  "answer": "A machine learning technique where models learn from labeled data."
}
```

### Response

```json
{
  "score": 8,
  "feedback": "Good technical explanation."
}
```

---

# Running the Backend

Navigate to:

```bash
cd backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI:

```bash
uvicorn main:app --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Backend Running

![Backend Running](docs/images/backend-running.png)

---

# Running the Frontend

Navigate to:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start React:

```bash
npm start
```

Application:

```text
http://localhost:3000
```

---

## React Application

![React App](docs/images/react-app-working.png)

---

# Contract Validation

Before running contract tests, the OpenAPI specification can be validated using Specmatic.

```bash
docker run --rm -v "${PWD}:/usr/src/app" specmatic/enterprise:latest validate --spec-file=contracts/interview-api.yaml
```

### Validation Result

- OpenAPI Specification: Valid
- API Paths: 2
- API Operations: 2
- Example Validation: Passed

This ensures the API contract is syntactically correct and ready for testing, mocking, and integration.

---

## Contract Validation Report

![Spec Validation](docs/images/spec-validation.png)

---

# Running Contract Tests

Start the FastAPI backend:

```bash
cd backend
uvicorn main:app --reload
```

Run Specmatic contract tests:

```bash
docker run --rm -v "${PWD}:/usr/src/app" specmatic/enterprise:latest test contracts/interview-api.yaml --testBaseURL=http://host.docker.internal:8000
```

---

# Contract Test Results

### Results

- Tests Run: 2
- Successes: 2
- Failures: 0
- Errors: 0
- API Coverage: 100%

Covered Endpoints:

- POST /generate-questions
- POST /evaluate-answer

The tests are automatically generated from OpenAPI examples and verify that the FastAPI implementation conforms to the contract.

---

## Contract Test Report

![Contract Test Report](docs/images/contract-test-report.png)

---

# API Coverage

Specmatic automatically calculates API coverage during contract execution.

| Endpoint | Method | Coverage |
|-----------|----------|----------|
| /generate-questions | POST | 100% |
| /evaluate-answer | POST | 100% |

### Overall Coverage

**100% API Coverage**

This confirms that every operation defined in the OpenAPI specification has been exercised through contract testing.

---

# Generated Reports

Specmatic automatically generates machine-readable and human-readable reports.

Generated artifacts:

```text
build/reports/specmatic/test/ctrf/ctrf-report.json
build/reports/specmatic/test/html/index.html
```

Generated report types:

- CTRF Report (Continuous Test Reporting Format)
- HTML Test Report

These reports can be integrated into CI/CD pipelines and quality dashboards.

---

# Service Virtualization with Specmatic

One of the most valuable features of Specmatic is the ability to generate executable mocks directly from an OpenAPI contract.

Start the mock server:

```bash
docker run --rm -p 8000:8000 -v "${PWD}:/usr/src/app" specmatic/enterprise:latest mock contracts/interview-api.yaml --port 8000
```

Benefits:

- Frontend development without backend dependency
- Faster parallel development
- Reduced integration bottlenecks
- Consistent API behavior across teams

---

## Specmatic Mock Running

![Specmatic Mock](docs/images/specmatic-mock.png)

---

# Continuous Integration

Contract validation has been automated using GitHub Actions.

Workflow Location:

```text
.github/workflows/specmatic.yml
```

On every push and pull request:

1. FastAPI backend starts automatically
2. OpenAPI contract is validated
3. Specmatic contract tests execute
4. Contract compliance is verified

This prevents breaking API changes from being merged into the main branch.

---

## GitHub Actions Workflow

![GitHub Actions](docs/images/github-actions-success.png)

---

# OpenAPI Examples

The project uses OpenAPI examples to improve generated mocks, documentation, and contract tests.

Example Request:

```json
{
  "role": "Machine Learning Engineer"
}
```

Example Response:

```json
{
  "questions": [
    "What is supervised learning?",
    "Explain overfitting.",
    "What is feature engineering?"
  ]
}
```

Benefits:

- Better API documentation
- Higher-quality generated tests
- More realistic service virtualization
- Improved AI-assisted development workflows

---

# Specmatic as AI Guardrails

A key objective of this project was to evaluate how executable contracts can improve AI-assisted software development.

To demonstrate this, the backend can intentionally introduce a contract violation.

### Incorrect AI-Generated Implementation

```json
{
  "rating": 8
}
```

### Expected Contract Response

```json
{
  "score": 8
}
```

Specmatic immediately detects the mismatch during contract testing.

This prevents integration surprises and ensures that AI-generated code remains aligned with the agreed API contract.

---

# Demonstration Scenarios

## Scenario 1: Contract-First Development

- Define API contract
- Implement frontend and backend independently
- Validate integration through the contract

## Scenario 2: Frontend Development Without Backend

- Stop FastAPI
- Start Specmatic Mock
- Verify frontend functionality

## Scenario 3: AI-Generated Integration Error

- Modify backend response field:
  
```text
score → rating
```

- Run contract tests
- Observe contract mismatch
- Fix implementation
- Re-run validation

---

# Evidence of Successful Validation

### Contract Validation

- Specification Status: PASSED
- Example Validation: PASSED

### Contract Testing

- Tests Run: 2
- Successes: 2
- Failures: 0

### Coverage

- API Coverage: 100%

### Reports Generated

- CTRF Report
- HTML Report

### CI Integration

- GitHub Actions Workflow Configured
- Contract Validation Automated

---

# Key Learnings

- Executable contracts reduce integration uncertainty.
- API contracts provide clear boundaries for both humans and AI coding agents.
- Service virtualization enables independent development.
- Contract-first development catches integration issues earlier.
- Specmatic acts as a practical guardrail for AI-assisted software development.
- OpenAPI examples improve test quality and documentation.

---

# Future Improvements

- Gemini-powered interview question generation
- AI-powered answer evaluation using LLMs
- Persistent interview history
- User authentication and profiles
- Interview performance analytics dashboard
- Advanced interview scoring and recommendations

---

# Author

**Rachait Talwar**

Submission for the **Specmatic Full Stack AI Engineering Intern / Trainee Challenge**.

Built to demonstrate how **Spec-Driven Development and executable contracts can improve AI-assisted software development through contract testing, service virtualization, API validation, coverage reporting, and CI automation.**
