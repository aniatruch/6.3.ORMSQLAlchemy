import pandas as pd
from sqlalchemy import create_engine

stations_df = pd.read_csv("clean_stations.csv")
measure_df = pd.read_csv("clean_measure.csv")

engine = create_engine("sqlite:///climate.db")

with engine.connect() as conn:
    dbapi_conn = conn.connection

    stations_df.to_sql("stations", con=dbapi_conn, if_exists="replace", index=False)
    measure_df.to_sql("measure", con=dbapi_conn, if_exists="replace", index=False)

print("Baza danych została utworzona.")







