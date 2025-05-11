from src.steam_personal_states import pull_steam_data


class TestCheckingData():
    def test_getting_data(self):
        pull_steam_data()