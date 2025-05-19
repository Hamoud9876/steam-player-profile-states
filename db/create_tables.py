from db.db_connection import connection






def create_games_table():
    conn = connection()
    conn.run("DROP TABLE IF EXISTS games")
    query_games_table = """CREATE TABLE games(
    appid int PRIMARY KEY,
    player_id int8,
    game_name varchar,
    play_time int
    )
    """

    conn.run(query_games_table)

    conn.close()


def create_genre():
    conn = connection()
    conn.run("DROP TABLE IF EXISTS genres")
    query = """CREATE TABLE genres(
    genre_id SERIAL PRIMARY KEY,
    appid int REFERENCES games(appid),
    genre_text varchar(150)
    )"""

    conn.run(query)
    conn.close()


def create_category_table():
    conn = connection()
    conn.run("DROP TABLE IF EXISTS categories")
    query = """CREATE TABLE categories(
    category_id SERIAL PRIMARY KEY,
    appid int REFERENCES games(appid),
    category_description varchar(200)
    )"""

    conn.run(query)
    conn.close()

def create_prices_table():
    conn = connection()
    conn.run("DROP TABLE IF EXISTS prices")
    query = """CREATE TABLE prices(
    price_id SERIAL PRIMARY KEY,
    appid int REFERENCES games(appid),
    currency varchar(50),
    initial_price int,
    final_price int,
    discount_percent int
    )"""

    conn.run(query)
    conn.close()

def create_table_failed_keys():
    conn = connection()
    conn.run("DROP TABLE IF EXISTS failed_keys")
    query = """CREATE TABLE failed_keys (
    failed_key_id SERIAL PRIMARY KEY,
    appid int REFERENCES games(appid),
    retried int
    )"""

    conn.run(query)
    conn.close()