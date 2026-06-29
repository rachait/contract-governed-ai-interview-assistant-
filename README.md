# 🚀 Contract-Governed AI Interview Assistant

> A Contract-First Full-Stack AI Application demonstrating executable API contracts, external examples, service virtualization, automated contract testing, and CI/CD using **Specmatic**, **OpenAPI**, **FastAPI**, and **React**.

![Specmatic](https://img.shields.io/badge/Specmatic-Enterprise-blue)
![OpenAPI](https://img.shields.io/badge/OpenAPI-3.0-success)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI-blue)
![Coverage](https://img.shields.io/badge/API_Coverage-100%25-brightgreen)
![Contract Testing](https://img.shields.io/badge/Contract_Testing-Passed-success)

---

# 📌 Overview

Modern AI coding assistants can generate code rapidly, but speed often introduces integration risks. APIs may compile successfully, pass unit tests, and still violate the expectations of consumers because implementation and documentation drift apart.

This project demonstrates how **Contract-First Development** with **Specmatic** eliminates those risks by making the **OpenAPI contract the single source of truth**.

The project implements an **AI Interview Assistant** where users can:

- Generate interview questions for any job role
- Submit answers
- Receive AI-based evaluation and feedback

Every interaction is validated against an executable OpenAPI contract, ensuring that the implementation always conforms to the agreed API specification.

---

# 🎯 Objectives

This project was built to demonstrate how executable contracts improve software quality by:

- Eliminating API integration uncertainty
- Detecting contract mismatches early
- Supporting parallel frontend and backend development
- Generating executable mocks automatically
- Validating external examples
- Measuring API coverage
- Automating contract testing through CI/CD

---

# ✨ Key Features

## ✅ Contract-First Development

- OpenAPI 3.0 Contract
- API as the Single Source of Truth
- Request & Response Schema Validation

---

## ✅ Specmatic Features

- OpenAPI Validation
- Contract Testing
- External Examples
- Example Validation
- Dictionary Generation
- Service Virtualization
- HTML Reports
- CTRF Reports
- API Coverage Reports

---

## ✅ Backend

- FastAPI
- Pydantic Validation
- Automatic HTTP 422 Validation Responses

---

## ✅ Frontend

- React
- AI Interview Interface
- REST API Integration

---

## ✅ DevOps

- GitHub Actions CI
- Automated Contract Testing
- Automated API Validation
- Report Uploads

---

# 🛠 Tech Stack

| Layer | Technology |
|---------|------------|
| Frontend | React |
| Backend | FastAPI |
| API Contract | OpenAPI 3.0 |
| Contract Testing | Specmatic Enterprise |
| API Documentation | Swagger UI |
| Validation | Pydantic |
| CI/CD | GitHub Actions |
| Reports | HTML + CTRF |
| Language | Python, JavaScript |

---

# 🏗 Architecture

The OpenAPI contract sits at the center of the application architecture.

Instead of treating documentation as an afterthought, the contract drives implementation, validation, testing, and integration.

![Architecture](docs/images/architecture.png)

```text
                React Frontend
                      │
                      ▼
        OpenAPI Contract (Source of Truth)
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
 Specmatic Mock              Contract Validation
        │                           │
        └─────────────┬─────────────┘
                      ▼
               FastAPI Backend
```

The architecture enables:

- Independent frontend development
- Independent backend development
- Consistent API behaviour
- Reliable integrations
- Early detection of contract violations

---

# 📂 Project Structure

```text
contract-governed-ai-interview-assistant
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── contracts/
│   ├── interview-api.yaml
│   ├── interview-api_dictionary.yaml
│   └── interview-api_examples/
│       ├── interview_flow.json
│       ├── answer_review.json
│       ├── invalid_role.json
│       └── invalid_answer.json
│
├── docs/
│   └── images/
│
├── build/
│   └── reports/
│
├── .github/
│   └── workflows/
│       └── specmatic.yml
│
├── specmatic.yaml
│
└── README.md
```

---

# 📄 Specmatic Configuration

The project includes a dedicated Specmatic configuration file.

```text
specmatic.yaml
```

The configuration defines:

- System Under Test
- OpenAPI Contract Source
- Test Configuration
- HTML Reports
- CTRF Reports
- API Governance

The primary API contract is located at:

```text
contracts/interview-api.yaml
```

External examples are maintained separately:

```text
contracts/interview-api_examples/
```

Dictionary file:

```text
contracts/interview-api_dictionary.yaml
```

---

# 🚀 Running the Project

## Clone Repository

```bash
git clone https://github.com/rachait/contract-governed-ai-interview-assistant.git

cd contract-governed-ai-interview-assistant
```

# ⚙️ Running the Backend

Install the required dependencies:

```bash
cd backend
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Backend URL

```text
http://localhost:8000
```

Swagger Documentation

```text
http://localhost:8000/docs
```

Redoc Documentation

```text
http://localhost:8000/redoc
```

![Backend Running](docs/images/backend-running.png)

---

# 💻 Running the Frontend

Install dependencies:

```bash
cd frontend
npm install
```

Start the React application:

```bash
npm start
```

Application URL

```text
http://localhost:3000
```

The React frontend communicates with the FastAPI backend using REST APIs defined by the OpenAPI contract.

![React Application](docs/images/react-app-working.png)

---

# 📜 OpenAPI Contract

The entire application is governed by an executable OpenAPI contract.

Location:

```text
contracts/interview-api.yaml
```

The contract defines:

- Request Schemas
- Response Schemas
- Validation Rules
- Response Status Codes
- Required Properties
- API Constraints

Rather than serving only as documentation, the contract becomes an executable specification that is continuously validated throughout development.

---

# 📌 Available APIs

## Generate Interview Questions

**POST**

```text
/generate-questions
```

Request

```json
{
  "role": "Machine Learning Engineer"
}
```

Success Response

```json
{
  "questions": [
    "What is supervised learning?",
    "Explain overfitting.",
    "What is feature engineering?"
  ]
}
```

Validation Response (422)

```json
{
  "detail": [
    {
      "type": "string_too_short",
      "msg": "String should have at least 2 characters"
    }
  ]
}
```

---

## Evaluate Interview Answer

**POST**

```text
/evaluate-answer
```

Request

```json
{
  "question": "What is supervised learning?",
  "answer": "A machine learning technique where models learn from labeled data."
}
```

Success Response

```json
{
  "score": 8,
  "feedback": "Good technical explanation with relevant examples."
}
```

Validation Response (422)

```json
{
  "detail": [
    {
      "type": "string_too_short",
      "msg": "String should have at least 10 characters"
    }
  ]
}
```

---

# 📁 External Examples

One of the enhancements made during this project was migrating from inline examples to **External Examples**, following Specmatic best practices.

Project structure:

```text
contracts/
│
├── interview-api.yaml
│
├── interview-api_dictionary.yaml
│
└── interview-api_examples/
    ├── interview_flow.json
    ├── answer_review.json
    ├── invalid_role.json
    └── invalid_answer.json
```

Benefits of External Examples:

- Cleaner OpenAPI specifications
- Easier maintenance
- Reusable API examples
- Independent validation
- Better scalability
- Improved collaboration between teams

---

# 📖 Dictionary Generation

Specmatic automatically generates a reusable dictionary file from external examples.

Generate Dictionary

```bash
docker run --rm \
-v "${PWD}:/usr/src/app" \
specmatic/enterprise:latest \
examples dictionary \
--spec-file contracts/interview-api.yaml
```

Generated dictionary:

```text
contracts/interview-api_dictionary.yaml
```

The dictionary improves consistency across generated examples and future contract tests.

---

# ✅ OpenAPI Validation

Validate the OpenAPI specification

```bash
docker run --rm \
-v "${PWD}:/usr/src/app" \
specmatic/enterprise:latest \
validate \
--spec-file contracts/interview-api.yaml
```

Validation includes:

- OpenAPI syntax validation
- Request schema validation
- Response schema validation
- External example validation
- Global example validation
- Contract consistency checks

Successful validation confirms that both the API contract and all external examples are compliant.

![Specification Validation](docs/images/spec-validation.png)

![Example Validation](docs/images/spec-validation-examples.png)

---

# 🔄 Service Virtualization

Specmatic can automatically generate executable mock services directly from the OpenAPI contract.

Start Mock Server

```bash
docker run --rm \
-p 8000:8000 \
-v "${PWD}:/usr/src/app" \
specmatic/enterprise:latest \
mock contracts/interview-api.yaml \
--port 8000
```

Advantages:

- Frontend development before backend completion
- Parallel development
- Faster delivery
- Stable API behaviour
- Reduced integration dependencies
- Early UI development
- Improved developer productivity

The React frontend was successfully developed and tested using Specmatic-generated mock APIs before the FastAPI implementation was finalized.

![Mock Server](docs/images/specmatic-mock.png)

---
