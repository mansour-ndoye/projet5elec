from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.schemas import BuildingInput
from app.ml_model import predict_energy
from app.database import get_db
from app.crud import save_prediction
from app.app_gradio import gradio_interface
import gradio as gr


app = FastAPI(title="Seattle Energy API")


@app.get("/")
def home():
    return {"message": "API Energy Prediction"}


@app.post("/predict")
def predict(
    building: BuildingInput,
    db: Session = Depends(get_db)
):

    features = {
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
        "State": building.State,
    }

    prediction = predict_energy(features)
    
    return {
        "prediction_kbtu": prediction
    }
app = gr.mount_gradio_app(
    app,
    gradio_interface,
    path="/gradio"
)