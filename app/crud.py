from app.models import PredictionLog

def save_prediction(db, data, prediction):

    row = PredictionLog(
        YearBuilt=data.YearBuilt,
        BuildingAge=data.BuildingAge,
        NumberofFloors=data.NumberofFloors,
        Log_Surface=data.Log_Surface,
        PropertyGFATotal=data.PropertyGFATotal,
        LargestPropertyUseTypeGFA=data.LargestPropertyUseTypeGFA,
        PropertyGFABuilding_s=data.PropertyGFABuilding_s,
        BuildingType=data.BuildingType,
        PrimaryPropertyType=data.PrimaryPropertyType,
        City=data.City,
        State=data.State,
        prediction=prediction
    )

    db.add(row)
    db.commit()
    db.refresh(row)

    return row