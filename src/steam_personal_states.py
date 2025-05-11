import  requests
import pprint
import time


def pull_steam_data():
    calls_counter = 0
    try:
        while True:
            x = requests.get('https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key=67132DA3BE8BE1B67B519DD458BF38AC&steamid=76561198321094791&include_appinfo=true&include_played_free_games=true')
            pprint.pprint(x.text)
            if x.status_code == 429:
                counter+=1
                time.sleep(5)
            elif x.status_code ==404:
                raise Exception
    except:
        return "calls to the api had failed, try again later"
