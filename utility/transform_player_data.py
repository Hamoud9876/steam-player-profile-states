import pandas as pd
import json




def transform_player_data(player_data: dict):
    if type(player_data["player_id"]) != int or not player_data["steam_data"] or type(player_data["steam_data"]) != str :
        return -1
    pd.set_option("display.max_columns", None)
    steam_data = json.loads(player_data["steam_data"])
    games = steam_data["response"]["games"]
    game_data_df = pd.DataFrame(games)

    game_data_df = game_data_df.drop(columns=["playtime_disconnected", "rtime_last_played", "playtime_deck_forever", "playtime_linux_forever", "playtime_mac_forever", "playtime_windows_forever", "img_icon_url", "has_community_visible_stats"], errors="ignore")


    return game_data_df
    
    
