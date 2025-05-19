# from db.seed import seed
from db.db_connection import connection
from db.insert_into_tables import *
from src.steam_personal_states import fetch_game_data
import pytest
import asyncio
import aiohttp




@pytest.mark.skip
class TestGamesTable:
    def test_selecting_from_games_table():
        conn = connection()
        response =conn.run("SELECT * FROM GAMES")
        for game in response:
            assert isinstance(game[0], int)
            assert isinstance(game[1], int)
            assert isinstance(game[2], str)
            assert isinstance(game[3], int)

class TestCategoriesTable:
    @pytest.mark.asyncio
    async def test_insert_bulk_checks_if_request_was_seccussful(self):
        appids = [10,20,30,40]
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_game_data(session, appid) for appid in appids]
            result = await asyncio.gather(*tasks)

            insert_into_category_table_bulk(result)
        
        conn = connection()
        query = """SELECT * FROM categories;"""
        db_respone = conn.run(query)
        for row in db_respone:
            assert isinstance(row[0], int)
            assert isinstance(row[1], int)
            assert isinstance(row[2], str)
        