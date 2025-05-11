from db.db_connection import connection

def create_games_table():
    conn = connection()
    conn.run("DROP TABLE IF EXISTS games")
    query_games_table = """CREATE TABLE games(
    recored_id SERIAL PRIMARY KEY,
    player_id int8,
    game_name varchar,
    play_time int
    )
    """

    conn.run(query_games_table)

    conn.close()