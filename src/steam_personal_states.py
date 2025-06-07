from db.db_connection import connection
from dotenv import load_dotenv
from utility.transform_player_data import transform_player_data
import requests
import time
import os
import pandas as pd

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
    except TooManyCalles:
        return "calls to the api had failed, try again later"
    except Exception:
        return "no information found"
    
    game_data_df = transform_player_data({"player_id": player_id, "steam_data": steam_response.json()})

    pass


def get_game_details(game_data_df: pd.DataFrame):
    game_details_list = []
    for index, game in game_data_df.iterrows():
        game_details_list.append(requests.get(f"https://store.steampowered.com/api/appdetails?appids={game["appid"]}"))
        
    


class TooManyCalles(Exception):
    "too many calls"


class NoInformationFound(Exception):
    def __init__(self, appid, message="the ID return no information"):
        self.appid = appid
        self.message = f"{message}: (appid: {appid})"
        super().__init__(self.message)
