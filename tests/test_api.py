from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():

    response = client.get("/")

    assert response.status_code == 200


def test_predict():

    payload = {
        "GHGEmissionsIntensity": 4.0,
        "YearBuilt": 2005,
        "BuildingAge": 21,
        "NumberofFloors": 5,
        "Log_Surface": 11,
        "PropertyGFATotal": 100000.0,
        "LargestPropertyUseTypeGFA": 80000.0,
        "PropertyGFABuilding_s": 95000.0,
        "BuildingType": "NonResidential",
        "PrimaryPropertyType": "Office",
        "City": "Seattle",
        "State": "WA"
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200

    assert "prediction_kbtu" in response.json()