# from db.seed import seed
from db.db_connection import connection
from db.insert_into_tables import *
from src.steam_personal_states import fetch_game_data
from utility.to_csv import get_player_data_from_tables, all_player_data_sql_to_csv
import pytest
import asyncio
import aiohttp
import csv


@pytest.mark.skip
class TestGamesTable:
    def test_selecting_from_games_table():
        conn = connection()
        response = conn.run("SELECT * FROM GAMES")
        for game in response:
            assert isinstance(game[0], int)
            assert isinstance(game[1], int)
            assert isinstance(game[2], str)
            assert isinstance(game[3], int)


@pytest.mark.skip
class TestCategoriesTable:
    @pytest.mark.asyncio
    async def test_insert_bulk_checks_if_request_was_seccussful(self):
        appids = [10, 20, 30, 40]
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


@pytest.mark.skip
class TestGenresTable:
    @pytest.mark.asyncio
    async def test_insert_genres_request_was_seccussful(self):
        appids = [10, 20, 30, 40]
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_game_data(session, appid) for appid in appids]
            result = await asyncio.gather(*tasks)

            insert_into_prices_table_bulk(result)

        conn = connection()

        query = """SELECT * FROM categories;"""
        db_respone = conn.run(query)
        for row in db_respone:
            assert isinstance(row[0], int)
            assert isinstance(row[1], int)
            assert isinstance(row[2], str)


class TestConvertingSqlToFile:
    def test_select_to_be_converted_is_correct(self):
        result = get_player_data_from_tables()

        for row in result:
            assert isinstance(row[0], int)
            assert isinstance(row[1], int)
            assert isinstance(row[2], str)
            assert isinstance(row[3], int)
            assert isinstance(row[4], list)
            assert isinstance(row[5], list)
            assert isinstance(row[6], str)
            assert isinstance(row[7], int)
            assert isinstance(row[8], int)
            assert isinstance(row[9], int)

    def test_create_csv_file(self):
        all_player_data_sql_to_csv()

        with open("steam_data.csv") as f:
            myreader = csv.reader(f)
            print(myreader)
