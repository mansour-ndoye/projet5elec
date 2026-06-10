import joblib
import pandas as pd

model = joblib.load("data/model.pkl")

def predict_energy(data):
    df = pd.DataFrame([data])

    df = df.rename(
        columns={
            "PropertyGFABuilding_s": "PropertyGFABuilding(s)"
        }
    )

    prediction = model.predict(df)

    return float(prediction[0])