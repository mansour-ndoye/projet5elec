import pandas as pd
import joblib

MODEL_PATH = "data/model.pkl"

model = joblib.load(MODEL_PATH)

def predict_energy(data):

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    return float(prediction[0])