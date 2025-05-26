from db.db_connection import connection



def insert_data_to_dimentions():
    conn = connection()
    # query = """INSERT INTO dim_player_info(player_id) 
    # SELECT DISTINCT games.player_id 
    # FROM games 
    # ORDER BY games.player_id"""
    # conn.run(query)

    # query = """INSERT INTO dim_categories(category_desc)
    # SELECT DISTINCT category_description
    # from categories"""
    # conn.run(query)

    # query = """INSERT INTO dim_genres(genre_desc) 
    # SELECT DISTINCT genre_text
    # FROM genres"""
    # conn.run(query)

    # query = """INSERT INTO dim_games_info(game_name)
    # SELECT game_name
    # FROM games
    # ORDER BY appid
    # """
    # conn.run(query)

    # query = """INSERT INTO bridge_games_genres(game_id,genre_id)
    # SELECT game_id, genres.genre_id
    # from dim_games_info
    # JOIN games
    # ON games.game_name = dim_games_info.game_name
    # JOIN genres
    # ON genres.appid = games.appid
    # JOIN dim_genres
    # ON dim_genres.genre_desc = genres.genre_text"""

    # conn.run(query)

    # query = """INSERT INTO bridge_game_categories(game_id, game_category_id)
    # SELECT game_id, dim_categories.category_id
    # FROM dim_games_info
    # JOIN games
    # ON games.game_name = dim_games_info.game_name
    # JOIN categories
    # ON categories.appid = games.appid
    # JOIN dim_categories
    # ON dim_categories.category_desc = categories.category_description"""
    # conn.run(query)

    


    conn.close()
    
    
insert_data_to_dimentions()