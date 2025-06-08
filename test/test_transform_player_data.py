from utility.transform_player_data import transform_player_data
from utility.transform_games_details import transform_games_details
from data.data import game_details
import json
import pandas as pd




class TestTransformPlayerData:
    def test_handles_empty_dict(self):
        response = transform_player_data({"player_id": 12, "steam_data":{}})
        assert response == -1
        response = transform_player_data({"player_id": None, "steam_data":{}})
        assert response == -1
        response = transform_player_data({"player_id": 11, "steam_data":123})
        assert response == -1


    def test_returns_dataframe(self):
        response = transform_player_data({"player_id": 12, "steam_data": json.dumps({
                "response":{
                    "games": [
                                {
                        "appid": 386360,
                        "name": "SMITE",
                        "playtime_forever": 0,
                        "img_icon_url": "7ed9de7bbfab9accb81e47b84943e7478baf2f3a",
                        "has_community_visible_stats": True,
                        "playtime_windows_forever": 0,
                        "playtime_mac_forever": 0,
                        "playtime_linux_forever": 0,
                        "playtime_deck_forever": 0,
                        "rtime_last_played": 0,
                        "playtime_disconnected": 0
                    },
                    {
                        "appid": 858460,
                        "name": "SMITE - Public Test",
                        "playtime_forever": 0,
                        "img_icon_url": "20e160ebdeddbb45f1066f62797cee2dff94da95",
                        "playtime_windows_forever": 0,
                        "playtime_mac_forever": 0,
                        "playtime_linux_forever": 0,
                        "playtime_deck_forever": 0,
                        "rtime_last_played": 0,
                        "playtime_disconnected": 0
                    },
                    {
                        "appid": 961200,
                        "name": "Predecessor",
                        "playtime_forever": 104,
                        "img_icon_url": "df1af75146dcf9bb96b10f29ad4c0ee7416df9ab",
                        "playtime_windows_forever": 104,
                        "playtime_mac_forever": 0,
                        "playtime_linux_forever": 0,
                        "playtime_deck_forever": 0,
                        "rtime_last_played": 1703674343,
                        "playtime_disconnected": 0
                    },
                    {
                        "appid": 1284210,
                        "name": "Haaa i",
                        "playtime_forever": 18,
                        "img_icon_url": "da75f97c0eb3abcd82fcbd0eee8725f0215b42ac",
                        "playtime_windows_forever": 18,
                        "playtime_mac_forever": 0,
                        "playtime_linux_forever": 0,
                        "playtime_deck_forever": 0,
                        "rtime_last_played": 1666983335,
                        "playtime_disconnected": 0
                    }
                    ]
                }
            })
            }
            )
        assert isinstance(response, pd.DataFrame)

    

    def test_transform_data(self):
        response = transform_player_data({"player_id": 12, "steam_data": json.dumps({
                "response":{
                    "games": [
                                {
                        "appid": 386360,
                        "name": "SMITE",
                        "playtime_forever": 0,
                        "img_icon_url": "7ed9de7bbfab9accb81e47b84943e7478baf2f3a",
                        "has_community_visible_stats": True,
                        "playtime_windows_forever": 0,
                        "playtime_mac_forever": 0,
                        "playtime_linux_forever": 0,
                        "playtime_deck_forever": 0,
                        "rtime_last_played": 0,
                        "playtime_disconnected": 0
                    },
                    {
                        "appid": 858460,
                        "name": "SMITE - Public Test",
                        "playtime_forever": 0,
                        "img_icon_url": "20e160ebdeddbb45f1066f62797cee2dff94da95",
                        "playtime_windows_forever": 0,
                        "playtime_mac_forever": 0,
                        "playtime_linux_forever": 0,
                        "playtime_deck_forever": 0,
                        "rtime_last_played": 0,
                        "playtime_disconnected": 0
                    },
                    {
                        "appid": 961200,
                        "name": "Predecessor",
                        "playtime_forever": 104,
                        "img_icon_url": "df1af75146dcf9bb96b10f29ad4c0ee7416df9ab",
                        "playtime_windows_forever": 104,
                        "playtime_mac_forever": 0,
                        "playtime_linux_forever": 0,
                        "playtime_deck_forever": 0,
                        "rtime_last_played": 1703674343,
                        "playtime_disconnected": 0
                    },
                    {
                        "appid": 1284210,
                        "name": "Haaa i",
                        "playtime_forever": 18,
                        "img_icon_url": "da75f97c0eb3abcd82fcbd0eee8725f0215b42ac",
                        "playtime_windows_forever": 18,
                        "playtime_mac_forever": 0,
                        "playtime_linux_forever": 0,
                        "playtime_deck_forever": 0,
                        "rtime_last_played": 1666983335,
                        "playtime_disconnected": 0
                    }
                    ]
                }
            })
            }
            )
        
        for index, row in response.iterrows():
            assert type(row['appid']) == int
            assert type(row["name"]) == str
            assert isinstance(row["playtime_forever"],int)
        

class TestTransformGamesDetails:
    def test_handles_empty_input(self):
        respones = transform_games_details([])

        assert respones == "Not a valid input for games details"


    def test_returns_dict_dataframe(self):
        respones = transform_games_details(game_details)

        assert isinstance(respones["games_genres_df"], pd.DataFrame)
        assert isinstance(respones["games_categories_df"], pd.DataFrame)
        assert isinstance(respones["games_price_info_df"], pd.DataFrame)


    def test_transforms_games_details(self):
        respones = transform_games_details(game_details)

        for index, i in respones["games_genres_df"].iterrows():
            assert isinstance(index, str)
            assert isinstance(i,pd.Series)

        for index, i in respones["games_categories_df"].iterrows():
            assert isinstance(index, str)
            assert isinstance(i,pd.Series)

        for index, i in respones["games_price_info_df"].iterrows():
            assert isinstance(index, str)
            assert isinstance(i,pd.Series)




        



