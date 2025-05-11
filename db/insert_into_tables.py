from db.db_connection import connection

def insert_into_games_table(games_list: list, player_id: int =0):
    conn = connection()
    for game in games_list:
        query = f"""INSERT INTO games (player_id, game_name,play_time )
                 VALUES (:player_id ,:game_name, :game_play_time );"""
        conn.run(query,player_id= player_id,game_name=game["name"],game_play_time=game["playtime_forever"])

    conn.close()