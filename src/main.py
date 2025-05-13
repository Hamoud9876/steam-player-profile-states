from fastapi import FastAPI
from db.db_connection import connection
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins for testing (you may restrict in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)



@app.get("/get_games")
def get_healthcheck():
    conn = connection()
    query = """SELECT * FROM games order by play_time;"""
    db_respones = conn.run(query)
    return {"games":[ {"game_name":game[2],  "play_time":game[3]} for game in db_respones]}