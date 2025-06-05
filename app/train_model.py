# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load Titanic dataset
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Preprocessing
df = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "Survived"]].dropna()
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

X = df.drop("Survived", axis=1)
y = df["Survived"]

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Save model
joblib.dump(model, "app/model.pkl")
print("Model saved to app/model.pkl")
