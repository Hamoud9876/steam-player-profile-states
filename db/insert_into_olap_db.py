from db.db_connection import connection
from src.convert_currency import convert_currency_to_gbp


def insert_data_to_dimentions():
    print(">>>>>> Inserting into OLAP database started")
    conn = connection()
    query = """INSERT INTO dim_player_info(player_id) 
    SELECT DISTINCT games.player_id 
    FROM games 
    ORDER BY games.player_id"""
    conn.run(query)

    query = """INSERT INTO dim_categories(category_desc)
    SELECT DISTINCT category_description
    from categories"""
    conn.run(query)

    query = """INSERT INTO dim_genres(genre_desc) 
    SELECT DISTINCT genre_text
    FROM genres"""
    conn.run(query)

    query = """INSERT INTO dim_games_info(game_name)
    SELECT game_name
    FROM games
    ORDER BY appid
    """
    conn.run(query)

    query = """INSERT INTO bridge_games_genres(game_id,genre_id)
    SELECT dim_games_info.game_id, dim_genres.genre_id
    from dim_games_info
    JOIN games
    ON games.game_name = dim_games_info.game_name
    JOIN genres
    ON genres.appid = games.appid
    JOIN dim_genres
    ON dim_genres.genre_desc = genres.genre_text"""

    conn.run(query)

    query = """INSERT INTO bridge_games_categories(game_id, game_category_id)
    SELECT game_id, dim_categories.category_id
    FROM dim_games_info
    JOIN games
    ON games.game_name = dim_games_info.game_name
    JOIN categories
    ON categories.appid = games.appid
    JOIN dim_categories
    ON dim_categories.category_desc = categories.category_description"""
    conn.run(query)

    query = """SELECT * FROM prices"""

    db_prices = conn.run(query)

    for row in db_prices:
        query = """INSERT INTO dim_expenditures(
            currency,
            initial_price ,
            final_price ,
            discount_percent ,
            initial_price_gbp ,
            final_price_gbp ,
            exchange_rate_date 
            )
            VALUES(:currency,:initial_price,:final_price,:discount_percent,:initial_price_gbp,:final_price_gbp,:exchange_date)"""
        converted_prices = convert_currency_to_gbp(row[2], row[3], row[4])

        conn.run(
            query,
            currency=row[2],
            initial_price=row[3],
            final_price=row[4],
            discount_percent=row[5],
            initial_price_gbp=converted_prices["converted_initial_amount"],
            final_price_gbp=converted_prices["converted_final_amount"],
            exchange_date=converted_prices["exchange_rate_date"],
        )

    query = """INSERT INTO fact_player_online_behaviour (
            player_info_id,
            expenditure_id,
            game_id,
            play_time
            )
            SELECT
                dim_player_info.player_info_id,
                dim_expenditures.expenditure_id,
                dim_games_info.game_id,
                games.play_time
            FROM games
            JOIN dim_player_info
                ON dim_player_info.player_id = games.player_id
            JOIN dim_games_info
                ON dim_games_info.game_name = games.game_name
            JOIN prices
                ON prices.appid = games.appid
            JOIN dim_expenditures
                ON dim_expenditures.currency = prices.currency
                AND dim_expenditures.initial_price = prices.initial_price
                AND dim_expenditures.final_price = prices.final_price
                AND dim_expenditures.discount_percent = prices.discount_percent
            WHERE games.play_time IS NOT NULL;
            """
    conn.run(query)

    conn.close()
    print(">>>>>> Inserting into OLAP database completed")


# insert_data_to_dimentions()
