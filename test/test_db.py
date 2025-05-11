from db.seed import seed
from db.db_connection import connection
import pytest


@pytest.fixture(scope="function")
def seeding():
    return seed()

def test_connecting_to_db_games_table():
    conn = connection()
    response =conn.run("SELECT * FROM GAMES")
    for game in response:
        isinstance(game[0], int)
        isinstance(game[1], int)
        isinstance(game[2], str)
        isinstance(game[3], int)