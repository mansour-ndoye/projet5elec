from app.database import engine, Base
from app.models import PredictionLog

Base.metadata.create_all(bind=engine)

print("Base créée")