from sqlalchemy import create_engine

engine = create_engine("sqlite:///climate.db")
conn = engine.connect()

tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print("Tabele w bazie danych:", tables)

print("\nJOIN: Pomiary z informacjami o stacji (pierwsze 5):")
join_result = conn.execute("""
    SELECT measure.date, measure.station, measure.precip, measure.tobs,
           stations.name, stations.latitude, stations.longitude
    FROM measure
    JOIN stations ON measure.station = stations.station
    LIMIT 5
""").fetchall()

for row in join_result:
    print(row)
