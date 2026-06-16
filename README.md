# Contract-Governed AI Interview Assistant

## Overview

This project demonstrates how executable API contracts can improve reliability, reduce integration uncertainty, and act as guardrails for AI-assisted software development.

The application is a full-stack AI Interview Assistant built using:

- React (Frontend)
- FastAPI (Backend)
- OpenAPI (API Contract)
- Specmatic (Contract Testing & Service Virtualization)

The OpenAPI contract serves as the single source of truth for both frontend and backend development.

---

## Problem Statement

AI coding assistants can generate working code rapidly, but they can also introduce implementation drift from agreed API contracts.

Examples include:

- Incorrect field names
- Missing required properties
- Unexpected response structures
- Integration failures discovered late in development

Without executable contracts, these issues are often detected only during integration testing or production debugging.

---

## Solution

This project adopts a contract-first development approach.

The API is defined using OpenAPI and treated as the source of truth.

Specmatic is used to:

- Generate executable mocks from the contract
- Enable frontend development before backend completion
- Validate implementation behavior against the contract
- Detect contract violations before integration testing

---

## Architecture

```text
React Frontend
       |
       v
OpenAPI Contract (Source of Truth)
       |
       +------------------+
       |                  |
       v                  v
Specmatic Mock     Contract Validation
       |                  |
       +------------------+
               |
               v
         FastAPI Backend
```

---

## API Contract

Location:

```text
contracts/interview-api.yaml
```

### Generate Interview Questions

```http
POST /generate-questions
```

Request:

```json
{
  "role": "Machine Learning Engineer"
}
```

Response:

```json
{
  "questions": [
    "What is Machine Learning Engineer?",
    "Explain a project related to Machine Learning Engineer"
  ]
}
```

### Evaluate Answer

```http
POST /evaluate-answer
```

Request:

```json
{
  "question": "Explain supervised learning",
  "answer": "..."
}
```

Response:

```json
{
  "score": 8,
  "feedback": "Good technical explanation."
}
```

---

## Specmatic Integration

### Contract Testing

The API contract is used to verify that the backend implementation conforms to the agreed specification.

This prevents contract drift between frontend and backend teams.

### Service Virtualization

Specmatic generates a mock service directly from the OpenAPI contract.

This allows frontend development to continue even when the backend implementation is unavailable.

### AI-Assisted Development Guardrails

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

## Running the Backend

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

## Running the Frontend

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

## Running a Specmatic Mock

From the project root:

```bash
docker run --rm -p 8000:8000 -v "${PWD}:/usr/src/app" specmatic/enterprise:latest mock contracts/interview-api.yaml --port 8000
```

This starts a contract-generated mock service.

The React frontend can continue functioning even when the FastAPI backend is unavailable.

---

## Demonstration Scenarios

### Scenario 1: Contract-First Development

- Define API contract
- Implement frontend and backend independently
- Validate integration through the contract

### Scenario 2: Frontend Development Without Backend

- Stop FastAPI
- Start Specmatic Mock
- Verify frontend functionality

### Scenario 3: AI-Generated Integration Error

- Modify backend response field:
  - `score` → `rating`
- Compare implementation against contract
- Observe contract mismatch
- Fix implementation
- Re-validate

---

## Key Learnings

- Executable contracts reduce integration uncertainty.
- API contracts provide clear boundaries for both humans and AI coding agents.
- Service virtualization enables independent development.
- Contract-first development catches integration issues earlier.
- Specmatic acts as a practical guardrail for AI-assisted software development.

---

## Future Improvements

- Gemini/OpenAI-powered question generation
- AI-based answer evaluation
- Persistent interview history
- Automated contract validation in CI/CD
- Advanced schema resiliency testing

---

## Author

**Rachait Talwar**

Submission for the **Specmatic Full Stack AI Engineering Intern / Trainee Challenge**.
