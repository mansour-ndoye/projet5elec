import pandas as pd

from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:motdepasse@localhost/energie_db"
)

df = pd.read_csv("data/2016_Building_Energy.csv")

df.to_sql(
    "buildings",
    engine,
    if_exists="replace",
    index=False
)

print("Dataset importé")