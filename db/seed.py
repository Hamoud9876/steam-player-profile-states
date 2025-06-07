from src.steam_personal_states import *
from db.create_tables_olap import create_olap_db
from db.insert_into_olap_db import insert_data_to_dimentions



async def seed():
    populate_games_table()
    await populate_genres_catigories_price()
    create_olap_db()
    populate_olap_db()


def populate_games_table():
    steam_data = pull_steam_data()


async def populate_genres_catigories_price():
    await get_game_genres_categories_price()


def populate_olap_db():
    insert_data_to_dimentions()
