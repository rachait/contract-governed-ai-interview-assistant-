from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Create FastAPI app
app = FastAPI(
    title="AI Interview Assistant API",
    version="1.0.0",
    description="Contract-Governed AI Interview Assistant API"
)

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request Models
class QuestionRequest(BaseModel):
    role: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

class AnswerRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=5
    )

    answer: str = Field(
        ...,
        min_length=10
    )

# Response Models
class QuestionResponse(BaseModel):
    questions: list[str]

class EvaluationResponse(BaseModel):
    score: int = Field(
        ...,
        ge=0,
        le=10
    )
    feedback: str = Field(
        ...,
        min_length=5
    )

# Error Response Model
class ErrorResponse(BaseModel):
    error: str

# Generate Interview Questions
@app.post(
    "/generate-questions",
    response_model=QuestionResponse,
    responses={
        400: {
            "model": ErrorResponse,
            "description": "Invalid request"
        }
    }
)
def generate_questions(data: QuestionRequest):
    if not data.role.strip():
        raise HTTPException(
            status_code=400,
            detail="role cannot be empty"
        )

    return {
        "questions": [
            f"What is {data.role}?",
            f"Explain a project related to {data.role}",
            f"What challenges did you face while working as a {data.role}?"
        ]
    }

# Evaluate Candidate Answer
@app.post(
    "/evaluate-answer",
    response_model=EvaluationResponse,
    responses={
        400: {
            "model": ErrorResponse,
            "description": "Invalid request"
        }
    }
)
def evaluate_answer(data: AnswerRequest):
    if not data.answer.strip():
        raise HTTPException(
            status_code=400,
            detail="answer cannot be empty"
        )

    return {
        "score": 8,
        "feedback": "Good technical explanation with relevant examples."
    }

# Health Check Endpoint
@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "AI Interview Assistant API"
    }