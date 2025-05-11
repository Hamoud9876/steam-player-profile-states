import  requests
import time
import os
from dotenv import load_dotenv

load_dotenv()


def pull_steam_data():
    counter = 0
    player_id = os.getenv("PLAYER_ID")
    try:
        while True:
            steam_response = requests.get(f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={os.getenv("STEAM_KEY")}&steamid={player_id}&include_appinfo=true&include_played_free_games=true')

            if steam_response.status_code == 429:
                counter+=1
                time.sleep(5)
                if counter >3:
                    raise TooManyCalles
            elif steam_response.status_code ==404:
                raise Exception
            else:
                break
         
    except Exception:
        return "no information found"
    except TooManyCalles:
        return "calls to the api had failed, try again later"
    
    
    return {"player_id": player_id, "steam_data": steam_response.json()}

class TooManyCalles(Exception):
    "too many calls"