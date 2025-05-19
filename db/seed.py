from src.steam_personal_states import *
from db.insert_into_tables import *
from db.create_tables import *
import asyncio



async def seed():
    
    create_genre()
    create_prices_table()
    create_category_table()
    create_table_failed_keys()
    await populate_genres_catigories_price()

    #stop creating tables
    if False:
        create_games_table()
        populate_games_table()
        
    

def populate_games_table():
    steam_data = pull_steam_data()
    insert_into_games_table(steam_data["steam_data"]["response"]["games"], steam_data["player_id"])


async def populate_genres_catigories_price():
    await get_game_genres_categories_price()



    

asyncio.run(seed())