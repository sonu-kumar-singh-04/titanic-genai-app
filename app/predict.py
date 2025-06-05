# app/predict.py
import joblib
from .parser import parse_prompt

model = joblib.load("app/model.pkl")

def predict_from_prompt(prompt: str):
    df = parse_prompt(prompt)
    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]
    return {
        "survived": bool(pred),
        "probability": round(prob, 2)
    }
