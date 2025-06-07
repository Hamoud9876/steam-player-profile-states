from src.steam_personal_states import *
from utility.transform_player_data import transform_player_data
from unittest.mock import patch,Mock
import pytest
import json


class TestSteamAPIGetGames:
    @pytest.mark.skip
    @patch('requests.get')
    def test_getting_games_data(self, patch_mock):
        mock_response = Mock()
        mock_response.json.return_value = {
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
            }
        
        patch_mock.return_value = mock_response
        
        
        api_response = pull_steam_data()
        for row in api_response["steam_data"]["response"]["games"]:
            assert isinstance(row["appid"], int)
            assert isinstance(row["name"], str)
            assert isinstance(row["playtime_forever"], int)


    @pytest.mark.skip
    @patch('requests.get')
    def test_failes_too_many_calles_status_code_429(self,patch_mock):
        mock_response = Mock()
        mock_response.status_code = 429
        
        patch_mock.return_value = mock_response
        
        
        api_response = pull_steam_data()
        assert api_response == "calls to the api had failed, try again later"

    
    @pytest.mark.skip
    @patch('requests.get')
    def test_failes_status_code_404(self,patch_mock):
        mock_response = Mock()
        mock_response.status_code= 404
        
        patch_mock.return_value = mock_response
        
        
        api_response = pull_steam_data()
        assert api_response == "no information found"



class TestGetGamesDetails:
    def test_returns_game_details(self):
        games_df = transform_player_data({"player_id": 12, "steam_data": json.dumps({
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
                })
        
        response = get_game_details(games_df)

        print(response)
    
