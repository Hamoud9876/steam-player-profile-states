import csv
from db.db_connection import connection


def all_player_data_sql_to_csv():
    data = get_player_data_from_tables()
    with open("steam_data.csv", "w") as csv_steam_file:
        my_writer = csv.writer(csv_steam_file)
        my_writer.writerow(
            [
                "appid",
                "player_id",
                "game_name",
                "play_time",
                "genres",
                "categories",
                "currency",
                "initial_price",
                "final_price",
                "discount_percent",
            ]
        )
        for row in data:
            my_writer.writerow(
                [
                    row[0],
                    00000000000000000,
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                    row[9],
                ]
            )


def get_player_data_from_tables():
    conn = connection()
    query = """SELECT  games.appid, player_id, game_name,play_time, ARRAY_AGG(DISTINCT genre_text), ARRAY_AGG(DISTINCT category_description), currency, initial_price, final_price, discount_percent FROM games
    JOIN genres
    ON games.appid = genres.appid
    JOIN categories
    ON categories.appid = games.appid
    JOIN prices
    ON prices.appid = games.appid
    GROUP BY games.appid, currency,initial_price, final_price, discount_percent;"""

    result = conn.run(query)

    return result
