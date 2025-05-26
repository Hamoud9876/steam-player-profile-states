from src.steam_personal_states import *
from unittest.mock import patch
import pytest
import aiohttp
import asyncio


class TestSteamAPI:
    @pytest.mark.skip
    def test_getting_data(self):
        api_response = pull_steam_data()
        for row in api_response["steam_data"]["response"]["games"]:
            assert isinstance(row["appid"], int)
            assert isinstance(row["name"], str)
            assert isinstance(row["playtime_forever"], int)


@pytest.mark.asyncio
class TestAPIsAscynroFunctions:
    @pytest.mark.skip
    async def test_fetching_data_makes_successful_api_call(self):
        appids = [10, 20, 30, 40]
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_game_data(session, appid) for appid in appids]
            result = await asyncio.gather(*tasks)

        assert isinstance(result, list)
        assert isinstance(result[0], tuple)
        for appid, desc in result:
            assert desc.get(str(appid), {}).get("success")

    @pytest.mark.skip
    async def test_process_all_data_categories(self):
        appids = [10, 20, 30, 40]
        await process_http_requests(appids)

        conn = connection()
        query = """SELECT * FROM categories;"""
        db_respone = conn.run(query)
        for row in db_respone:
            assert isinstance(row[0], int)
            assert isinstance(row[1], int)
            assert isinstance(row[2], str)

    @pytest.mark.skip
    async def test_process_all_data_genres(self):
        appids = [10, 20, 30, 40]
        await process_http_requests(appids)

        conn = connection()
        query = """SELECT * FROM genres;"""
        db_respone = conn.run(query)
        for row in db_respone:
            assert isinstance(row[0], int)
            assert isinstance(row[1], int)
            assert isinstance(row[2], str)

    @pytest.mark.skip
    async def test_process_all_data_price(self):
        appids = [10, 20, 30, 40]
        await process_http_requests(appids)

        conn = connection()
        query = """SELECT * FROM prices;"""
        db_respone = conn.run(query)
        for row in db_respone:
            assert isinstance(row[0], int)
            assert isinstance(row[1], int)
            assert isinstance(row[2], str)
