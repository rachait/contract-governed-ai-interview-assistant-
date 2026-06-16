## Contract Validation

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

## Contract Testing

Specmatic executes contract tests directly against the FastAPI implementation.

Start the backend:

```bash
cd backend
uvicorn main:app --reload
```

Run contract tests:

```bash
docker run --rm -v "${PWD}:/usr/src/app" specmatic/enterprise:latest test contracts/interview-api.yaml --testBaseURL=http://host.docker.internal:8000
```

### Contract Test Results

- Tests Run: 2
- Successes: 2
- Failures: 0
- Errors: 0
- API Coverage: 100%

Covered Endpoints:

- POST /generate-questions
- POST /evaluate-answer

The tests are automatically generated from OpenAPI examples and verify that the FastAPI implementation conforms to the API contract.

![Contract Test Report](docs/images/contract-test-report.png)

---

## API Coverage Report

Specmatic automatically calculates API coverage during contract execution.

| Endpoint | Method | Coverage |
|-----------|----------|----------|
| /generate-questions | POST | 100% |
| /evaluate-answer | POST | 100% |

### Overall Coverage

**100% API Coverage**

This confirms that every operation defined in the OpenAPI specification has been exercised through contract testing.

---

## Generated Reports

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

## Continuous Integration

Contract validation is automated using GitHub Actions.

Workflow location:

```text
.github/workflows/specmatic.yml
```

On every push and pull request:

1. FastAPI backend starts automatically
2. OpenAPI contract is validated
3. Specmatic contract tests execute
4. Contract compliance is verified

This prevents breaking API changes from being merged into the main branch.

![GitHub Actions Report](docs/images/github-actions-success.png)

---

## OpenAPI Examples

The project uses OpenAPI examples to improve generated mocks, documentation, and contract tests.

### Example Request

```json
{
  "role": "Machine Learning Engineer"
}
```

### Example Response

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

## Specmatic as AI Guardrails

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

## Evidence of Successful Validation

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

## Future Improvements

- Gemini-powered interview question generation
- AI-powered answer evaluation using LLMs
- Persistent interview history
- User authentication and profiles
- Interview performance analytics dashboard
- Advanced interview scoring and recommendations
