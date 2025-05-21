import requests
import time
import os
from db.db_connection import connection
from dotenv import load_dotenv
from db.insert_into_tables import *
from db.db_connection import connection
import asyncio
import aiohttp

load_dotenv()


def pull_steam_data():
    counter = 0
    player_id = os.getenv("PLAYER_ID")
    try:
        while True:
            steam_response = requests.get(
                f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={os.getenv("STEAM_KEY")}&steamid={player_id}&include_appinfo=true&include_played_free_games=true'
            )

            if steam_response.status_code == 429:
                counter += 1
                time.sleep(5)
                if counter > 3:
                    raise TooManyCalles
            elif steam_response.status_code == 404:
                raise Exception
            else:
                break

    except Exception:
        return "no information found"
    except TooManyCalles:
        return "calls to the api had failed, try again later"

    return {"player_id": player_id, "steam_data": steam_response.json()}


async def get_game_genres_categories_price():

    conn = connection()
    query = """SELECT appid FROM games where appid != 0 ORDER BY appid"""
    db_response = conn.run(query)
    appids = [row[0] for row in db_response]
    await process_http_requests(appids)
    conn.close()


async def process_http_requests(appids):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_game_data(session, appid) for appid in appids]
        result = await asyncio.gather(*tasks)
        insert_into_category_table_bulk(result)
        insert_into_genres_table_bulk(result)
        insert_into_prices_table_bulk(result)


semaphore = asyncio.Semaphore(1)


async def fetch_game_data(session, appid):
    async with semaphore:
        await asyncio.sleep(1)
        url = f"https://store.steampowered.com/api/appdetails?appids={appid}"
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return appid, await response.json()
    except Exception as e:
        print(appid, e)
        conn = connection()
        query = "INSERT INTO failed_keys(appid) VALUES (:appid)"
        conn.run(query, appid=appid)


class TooManyCalles(Exception):
    "too many calls"


class NoInformationFound(Exception):
    def __init__(self, appid, message="the ID return no information"):
        self.appid = appid
        self.message = f"{message}: (appid: {appid})"
        super().__init__(self.message)
