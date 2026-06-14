import joblib
import pandas as pd

model = joblib.load("data/model.pkl")

def predict_energy(features):
    df = pd.DataFrame([features])

    df = df.rename(
        columns={
            "PropertyGFABuilding_s": "PropertyGFABuilding(s)"
        }
    )

    prediction = model.predict(df)

    return float(prediction[0])