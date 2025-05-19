from fastapi import FastAPI
from db.db_connection import connection

app = FastAPI()

@app.get("/get_games")
def get_healthcheck():
    conn = connection()
    query = """SELECT * FROM games order by play_time;"""
    db_respones = conn.run(query)
    return {"games":[ {"game_name":game[2],  "play_time":game[3]} for game in db_respones]}