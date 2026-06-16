# Contract-Governed AI Interview Assistant

## Overview

This project demonstrates how executable API contracts improve reliability, reduce integration uncertainty, and act as guardrails for AI-assisted software development.

The application is built using:

- React (Frontend)
- FastAPI (Backend)
- OpenAPI (API Contract)
- Specmatic (Contract Testing, Validation, Service Virtualization & Schema Resiliency Testing)

The OpenAPI contract serves as the single source of truth for both frontend and backend development.

---

## Problem Statement

AI coding assistants can generate working code rapidly, but they can also introduce implementation drift from agreed API contracts.

Common issues include:

- Incorrect field names
- Missing required properties
- Unexpected response structures
- Integration failures discovered late in development

Without executable contracts, these issues are often detected only during integration testing.

---

## Solution

This project follows a Contract-First Development approach.

Specmatic is used to:

- Generate executable mocks
- Validate API behavior
- Run contract tests
- Generate coverage reports
- Perform schema resiliency testing
- Act as guardrails for AI-generated code

---

## Architecture

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

---

## Project Structure

![Project Structure](docs/images/project-structure.png)

---

## Backend

Run:

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

### Backend Running

![Backend Running](docs/images/backend-running.png)

---

## Frontend

Run:

```bash
cd frontend
npm install
npm start
```

Application:

```text
http://localhost:3000
```

### React Application

![React Application](docs/images/react-app-working.png)

---

## OpenAPI Contract Validation

```bash
docker run --rm -v "${PWD}:/usr/src/app" specmatic/enterprise:latest validate --spec-file=contracts/interview-api.yaml
```

### Specification Validation

![Specification Validation](docs/images/spec-validation.png)

### Example Validation

![Example Validation](docs/images/spec-validation-examples.png)

---

## Contract Testing

```bash
docker run --rm -v "${PWD}:/usr/src/app" specmatic/enterprise:latest test contracts/interview-api.yaml --testBaseURL=http://host.docker.internal:8000
```

### Contract Test Execution

![Contract Test Execution](docs/images/contract-test-execution.png)

### Contract Test Report

![Contract Test Report](docs/images/contract-test-report.png)

Results:

- Tests Run: 2
- Successes: 2
- Failures: 0
- API Coverage: 100%

## Schema Resiliency Testing

Specmatic was used to perform Schema Resiliency Testing.

### Baseline Testing

```yaml
schemaResiliencyTests: none
```

Results:

- Tests Run: 3
- Successes: 3

![Schema Resiliency Baseline](docs/images/resiliency-baseline.png)

### Positive-Only Testing

```yaml
schemaResiliencyTests: positiveOnly
```

Results:

- Tests Run: 42
- Successes: 42

![Schema Resiliency Positive Only](docs/images/resiliency-positive-only.png)

---

## API Coverage

| Endpoint | Method | Coverage |
|-----------|----------|----------|
| /generate-questions | POST | 100% |
| /evaluate-answer | POST | 100% |

Overall Coverage: **100%**

---

## Service Virtualization

Start Mock Server:

```bash
docker run --rm -p 8000:8000 -v "${PWD}:/usr/src/app" specmatic/enterprise:latest mock contracts/interview-api.yaml --port 8000
```

Benefits:

- Frontend development without backend dependency
- Faster parallel development
- Reduced integration bottlenecks

---

## Continuous Integration

GitHub Actions automatically:

1. Starts FastAPI
2. Validates OpenAPI contract
3. Runs Specmatic tests
4. Verifies contract compliance

### GitHub Actions Workflow

![GitHub Actions Success](docs/images/github-actions-success.png)

---

## Specmatic as AI Guardrails

Example of an AI-generated contract violation:

Incorrect:

```json
{
  "rating": 8
}
```

Expected:

```json
{
  "score": 8
}
```

Specmatic immediately detects this mismatch during contract testing.

---

## Key Learnings

- Executable contracts reduce integration uncertainty.
- Contract-first development catches integration issues earlier.
- Service virtualization enables independent development.
- Schema resiliency testing increases coverage automatically.
- CI automation prevents contract-breaking changes.
- Specmatic acts as a guardrail for AI-assisted development.

---

## Future Improvements

- Gemini/OpenAI-powered interview question generation
- AI-powered answer evaluation
- Persistent interview history
- Authentication and user profiles
- Analytics dashboard

---

## Author

**Rachait Talwar**

Submission for the **Specmatic Full Stack AI Engineering Intern / Trainee Challenge**.

Built to demonstrate contract-first development using OpenAPI, FastAPI, React, and Specmatic.
