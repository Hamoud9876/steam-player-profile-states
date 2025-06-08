import pandas as pd
import json

def transform_games_details(games_details_list):
    if not games_details_list or type(games_details_list) != list:
        return "Not a valid input for games details"

    games_json_to_dict = []
    for game in games_details_list:
        games_json_to_dict.append(json.loads(game))
    
    game_genres = games_json_to_dict[0]["api_response"][games_json_to_dict[0]["game_id"]]["data"]["genres"]

    game_categories = games_json_to_dict[0]["api_response"][games_json_to_dict[0]["game_id"]]["data"]["categories"]
    game_price_info = games_json_to_dict[0]["api_response"][games_json_to_dict[0]["game_id"]]["data"]["price_overview"]
    
    games_genres_df = pd.DataFrame(game_genres, index=[games_json_to_dict[0]["game_id"]] * len(game_genres) )

    games_categories_df = pd.DataFrame(game_categories, index=[games_json_to_dict[0]["game_id"]]* len(game_categories))

    games_price_info_df = pd.DataFrame([game_price_info], index=[games_json_to_dict[0]["game_id"]])
    
    

    

    return {"games_genres_df": games_genres_df, "games_categories_df": games_categories_df,"games_price_info_df": games_price_info_df }