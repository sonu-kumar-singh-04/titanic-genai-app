# Titanic GenAI Predictor 🚢

A FastAPI app that takes natural language queries and predicts Titanic survival using a Logistic Regression model.

### 🧠 Example

```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"prompt": "Will a 25-year-old female in 2nd class who embarked from Cherbourg survive?"}'
```
### ✅ Features:
 - Natural language input

 - ML prediction using Logistic Regression

 - Easy to extend with LangChain or LLMs later

### 🚀 Run Locally
```
pip install -r requirements.txt
python train_model.py
uvicorn app.main:app --reload
```
## 🧪 Example Request & Response
### Request
```json
POST /predict
{
  "prompt": "Will a 22-year-old male in 3rd class who embarked from Southampton survive?"
}
```

### Response
```json
{
  "input": "Will a 22-year-old male in 3rd class who embarked from Southampton survive?",
  "prediction": "No",
  "confidence": "23.45%"
}
```
