from db.db_connection import connection



def create_olap_db():
    conn = connection()

    query_dim_player_info = """CREATE TABLE dim_player_info(
        player_info_id SERIAL PRIMARY KEY,
        player_id int8
        )
        """
    conn.run(query_dim_player_info)

    query_dim_expenditures = """CREATE TABLE dim_expenditures(
        expenditure_id SERIAL PRIMARY KEY,
        curreny varchar(10),
        initial_price int,
        final_price int,
        discount_percent int
        )"""
    conn.run(query_dim_expenditures)

    query_dim_games_info = """CREATE TABLE dim_games_info (
        game_id SERIAL PRIMARY KEY,
        game_name varchar
        )
        """
    conn.run(query_dim_games_info)

    query_dim_categories = """CREATE TABLE dim_categories(
        category_id SERIAL PRIMARY KEY,
        category_desc varchar
        )"""
    conn.run(query_dim_categories)

    query_bridge_games_categories = """CREATE TABLE bridge_games_categories(
        game_id int references dim_games_info(game_id),
        game_category_id int references dim_categories(category_id))
        """
    conn.run(query_bridge_games_categories)

    query_dim_game_genre = """CREATE TABLE dim_genres(
        genre_id SERIAL PRIMARY KEY,
        genre_desc varchar
        )"""
    conn.run(query_dim_game_genre)

    query_bridge_games_genres = """CREATE TABLE bridge_games_genres(
        game_id int references dim_games_info(game_id),
        genre_id int references dim_genres(genre_id))
        """
    conn.run(query_bridge_games_genres)


    query_fact = """CREATE TABLE fact_player_online_behaviour (
        profile_id SERIAL PRIMARY KEY,
        player_info_id int references dim_player_info(player_info_id),
        expenditure_id int references dim_expenditures(expenditure_id),
        game_id int references dim_games_info(game_id),
        play_time int
        )"""
    conn.run(query_fact)

    conn.close()

