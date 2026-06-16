from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QuestionRequest(BaseModel):
    role: str

class AnswerRequest(BaseModel):
    question: str
    answer: str

@app.post("/generate-questions")
def generate_questions(data: QuestionRequest):
    return {
        "questions": [
            f"What is {data.role}?",
            f"Explain a project related to {data.role}",
            f"What challenges did you face?"
        ]
    }

@app.post("/evaluate-answer")
def evaluate_answer(data: AnswerRequest):
    return {
        "score": 8,
        "feedback": "Good technical explanation."
    }