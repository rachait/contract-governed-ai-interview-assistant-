# Contract-Governed AI Interview Assistant

## Overview

This project demonstrates how executable API contracts can improve reliability, reduce integration uncertainty, and act as guardrails for AI-assisted software development.

The application is a full-stack AI Interview Assistant built using:

- React (Frontend)
- FastAPI (Backend)
- OpenAPI (API Contract)
- Specmatic (Contract Testing, Resiliency Testing & Service Virtualization)

The OpenAPI contract serves as the single source of truth for frontend development, backend implementation, testing, and integration.

---

# Problem Statement

AI coding assistants can generate working code rapidly, but they can also introduce implementation drift from agreed API contracts.

Examples include:

- Incorrect field names
- Missing required properties
- Unexpected response structures
- Invalid request handling
- Integration failures discovered late in development

Without executable contracts, these issues are often detected only during integration testing or production debugging.

---

# Solution

This project adopts a Contract-First Development approach.

The API is defined using OpenAPI and treated as the source of truth.

Specmatic is used to:

- Generate executable mocks from the contract
- Enable frontend development before backend completion
- Validate backend behavior against the contract
- Execute resiliency tests automatically
- Detect contract violations before integration testing
- Act as guardrails for AI-generated code

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

Instead of treating documentation as an afterthought, the contract drives development, testing, and integration.

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

### Request Example

```json
{
  "role": "Machine Learning Engineer"
}
```

### Response Example

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

### Request Example

```json
{
  "question": "What is supervised learning?",
  "answer": "A machine learning technique..."
}
```

### Response Example

```json
{
  "score": 8,
  "feedback": "Good technical explanation."
}
```

---

# Specmatic Integration

## Contract Testing

The API contract is used to verify that the backend implementation conforms to the agreed specification.

Benefits:

- Detects contract drift
- Validates request/response structure
- Ensures implementation matches API expectations
- Reduces integration failures

---

## Service Virtualization

Specmatic generates a mock service directly from the OpenAPI contract.

This allows frontend development to continue even when the backend implementation is unavailable.

### Without Backend

```text
Frontend
    |
    X
Backend unavailable
```

Development stalls.

### With Specmatic Mock

```text
Frontend
    |
Specmatic Mock
    |
OpenAPI Contract
```

Frontend development continues independently.

---

## AI-Assisted Development Guardrails

To simulate a common AI-generated implementation error, the backend can intentionally return:

```json
{
  "rating": 8
}
```

instead of:

```json
{
  "score": 8
}
```

The contract remains the source of truth.

Specmatic immediately identifies this mismatch, preventing integration surprises and reducing debugging effort.

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

# Running a Specmatic Mock

From the project root:

```bash
docker run --rm -p 8000:8000 -v "${PWD}:/usr/src/app" specmatic/enterprise:latest mock contracts/interview-api.yaml --port 8000
```

Expected output:

```text
Mock server is running...
Contract matched: contracts/interview-api.yaml
```

This starts a contract-generated mock service.

The React frontend can continue functioning even when the FastAPI backend is unavailable.

---

# Running Contract Tests

Start the backend first:

```bash
cd backend
uvicorn main:app --reload
```

Run Specmatic contract tests:

```bash
docker run --rm -v "${PWD}:/usr/src/app" specmatic/enterprise:latest test contracts/interview-api.yaml --host http://host.docker.internal:8000
```

Expected result:

```text
Tests run: X
Successes: X
Failures: 0
```

These tests validate that the FastAPI implementation conforms to the OpenAPI contract.

---

# Running Resiliency Tests

Specmatic can automatically generate edge-case and negative test scenarios.

Run:

```bash
docker run --rm -v "${PWD}:/usr/src/app" specmatic/enterprise:latest test contracts/interview-api.yaml --host http://host.docker.internal:8000 --resiliency-tests
```

Resiliency tests verify how the API behaves when receiving:

- Invalid payloads
- Missing required fields
- Unexpected data types
- Malformed requests

Benefits:

- Improves API robustness
- Reduces production failures
- Provides stronger validation for AI-generated implementations

---

# Continuous Integration

Contract validation is automated using GitHub Actions.

On every push and pull request:

1. Backend starts automatically
2. Specmatic contract tests execute
3. Contract compliance is verified

GitHub Actions workflow:

```text
.github/workflows/specmatic.yml
```

---

# Test Reports

## Contract Test Report

Add screenshot here:

```text
docs/images/contract-test-report.png
```

---

## Resiliency Test Report

Add screenshot here:

```text
docs/images/resiliency-test-report.png
```

---

## GitHub Actions Report

Add screenshot here:

```text
docs/images/github-actions-success.png
```

---

# Demonstration Scenarios

## Scenario 1: Contract-First Development

- Define API contract
- Build frontend and backend independently
- Validate implementation through executable contracts

---

## Scenario 2: Frontend Development Without Backend

- Stop FastAPI
- Start Specmatic Mock
- Verify frontend functionality

---

## Scenario 3: AI-Generated Integration Error

Change:

```json
{
  "score": 8
}
```

to:

```json
{
  "rating": 8
}
```

Observe contract mismatch and re-validate after fixing.

---

# Key Learnings

- Executable contracts reduce integration uncertainty.
- API contracts provide clear boundaries for both humans and AI coding agents.
- Service virtualization enables independent development.
- Contract-first development catches integration issues earlier.
- Resiliency testing improves API robustness.
- Specmatic acts as a practical guardrail for AI-assisted software development.

---

# Future Improvements

- Gemini-powered interview question generation
- AI-based answer evaluation
- Persistent interview history
- User authentication
- Interview performance analytics dashboard

---

# Author

**Rachait Talwar**

Submission for the **Specmatic Full Stack AI Engineering Intern / Trainee Challenge**.
