from src.steam_personal_states import pull_steam_data
from db.insert_into_tables import insert_into_games_table
from db.create_tables import create_games_table


def seed():
    create_games_table()
    populate_games_table()
    

def populate_games_table():
    steam_data = pull_steam_data()
    insert_into_games_table(steam_data["steam_data"]["response"]["games"], steam_data["player_id"])

