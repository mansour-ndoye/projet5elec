from app.models import Prediction

def save_prediction(db, data, prediction):

    row = Prediction(
        YearBuilt=data.YearBuilt,
        NumberofFloors=data.NumberofFloors,
        PropertyGFATotal=data.PropertyGFATotal,
        LargestPropertyUseTypeGFA=data.LargestPropertyUseTypeGFA,
        SourceEUI=data.SourceEUI,
        GHGEmissionsIntensity=data.GHGEmissionsIntensity,
        prediction=prediction
    )

    db.add(row)
    db.commit()
    db.refresh(row)

    return row