from fastapi import FastAPI
from app.schemas import BuildingInput
from app.ml_model import predict_energy

app = FastAPI(
    title="Seattle Energy Prediction API",
    description="Prédiction de la consommation énergétique des bâtiments",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Seattle Energy Prediction API"
    }

@app.post("/predict")
def predict(building: BuildingInput):

    features = {
        "GHGEmissionsIntensity": building.GHGEmissionsIntensity,
        "YearBuilt": building.YearBuilt,
        "BuildingAge": building.BuildingAge,
        "NumberofFloors": building.NumberofFloors,
        "Log_Surface": building.Log_Surface,
        "PropertyGFATotal": building.PropertyGFATotal,
        "LargestPropertyUseTypeGFA": building.LargestPropertyUseTypeGFA,
        "PropertyGFABuilding_s": building.PropertyGFABuilding_s,
        "BuildingType": building.BuildingType,
        "PrimaryPropertyType": building.PrimaryPropertyType,
        "City": building.City,
        "State": building.State
    }

    prediction = predict_energy(features)

    return {
        "prediction_kbtu": prediction
    }