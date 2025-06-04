from sqlalchemy import create_engine

engine = create_engine("sqlite:///climate.db")
conn = engine.connect()

result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()

for row in result:
    print(row)
