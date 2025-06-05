# app/parser.py
import re
import pandas as pd

def parse_prompt(prompt: str) -> pd.DataFrame:
    info = {
        "Pclass": 3,
        "Sex": 0,
        "Age": 30.0,
        "SibSp": 0,
        "Parch": 0,
        "Fare": 30.0,
        "Embarked": 0
    }

    if "1st" in prompt:
        info["Pclass"] = 1
    elif "2nd" in prompt:
        info["Pclass"] = 2

    if "female" in prompt:
        info["Sex"] = 1

    age_match = re.search(r"(\d+)[ -]?year[- ]?old", prompt)
    if age_match:
        info["Age"] = float(age_match.group(1))

    if "Cherbourg" in prompt:
        info["Embarked"] = 1
    elif "Queenstown" in prompt:
        info["Embarked"] = 2

    return pd.DataFrame([info])
