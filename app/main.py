# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from .predict import predict_from_prompt

app = FastAPI(title="Titanic GenAI Predictor")

class Query(BaseModel):
    prompt: str

@app.post("/predict")
def predict(query: Query):
    result = predict_from_prompt(query.prompt)
    return {
        "input": query.prompt,
        "prediction": "Yes" if result["survived"] else "No",
        "confidence": f"{result['probability']*100:.2f}%"
    }
