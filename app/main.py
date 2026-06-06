
from fastapi import FastAPI
from app.schemas import EnergyInput
from app.ml_model import predict_energy

app = FastAPI(title="Seattle Energy API")

@app.get("/")
def home():
    return {"message": "API Energy Prediction"}

@app.post("/predict")
def predict(data: EnergyInput):

    prediction = predict_energy(data)

    return {
        "prediction_kbtu": prediction
    }