from sqlalchemy import Column, Integer, Float, String
from app.database import Base

class PredictionLog(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    GHGEmissionsIntensity = Column(Float)
    YearBuilt = Column(Integer)
    BuildingAge = Column(Integer)
    NumberofFloors = Column(Integer)
    Log_Surface = Column(Float)
    PropertyGFATotal = Column(Float)
    LargestPropertyUseTypeGFA = Column(Float)
    PropertyGFABuilding_s = Column(Float)
    BuildingType = Column(String)
    PrimaryPropertyType = Column(String)
    City = Column(String)
    State = Column(String)
    prediction = Column(Float)