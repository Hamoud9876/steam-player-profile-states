from db.db_connection import connection
import asyncio


def insert_into_games_table(games_list: list, player_id: int = 0):
    print(">>>>> inserting into games table started <<<<<<<")
    conn = connection()
    for game in games_list:
        query = f"""INSERT INTO games (player_id, appid, game_name,play_time )
                 VALUES (:player_id, :appid,:game_name, :game_play_time );"""
        conn.run(
            query,
            player_id=player_id,
            game_name=game["name"],
            game_play_time=game["playtime_forever"],
            appid=game["appid"],
        )
    conn.close()
    print(">>>>> inserting into games table completed <<<<<<<")


def insert_into_genres_table_bulk(genres_data):
    print(">>>>> inserting into genres table started <<<<<<<")
    conn = connection()
    all_inserts = []
    failed_inserts = []

    for idx, item in enumerate(genres_data):
        if not isinstance(item, (list, tuple)) or len(item) != 2:
            print(f"[Warning] this item causing an error item at index {idx}: {item}")
            continue
        appid, data = item
        try:
            if data.get(str(appid), {}).get("success"):
                genres = data[str(appid)]["data"].get("genres", [])
                for g in genres:
                    all_inserts.append((appid, g["description"]))

        except TypeError as e:
            print(f"somwthing went wrong")
        except KeyError as e:
            print(f"the key: {e}, does not exists")
        except Exception as e:
            print(f"Error parsing the genres for {appid} caused: {e} ")
        finally:
            query = (
                """INSERT INTO failed_keys(appid, retried) VALUES(:appid, :retried)"""
            )
            conn.run(query, appid=appid, retried=0)
    if all_inserts:
        query = f"""INSERT INTO genres(appid, genre_text)
                            values (:appid ,:genre_text)"""
        for appid, desc in all_inserts:
            conn.run(query, genre_text=desc, appid=appid)

    query = """INSERT INTO failed_keys (appid, retried) VALUES (:appid, :retried)"""
    for appid in failed_inserts:
        conn.run(query, appid=appid, retried=0)
    print(">>>>> inserting into genres table completed <<<<<<<")


def insert_into_category_table_bulk(categories_data):
    print(">>>>> inserting bulk data into categories table started <<<<<<<")
    conn = connection()
    all_inserts = []
    failed_inserts = []

    for idx, item in enumerate(categories_data):
        if not isinstance(item, (list, tuple)) or len(item) != 2:
            print(f"[Warning] this item causing an error item at index {idx}: {item}")
            continue
        appid, data = item
        try:
            if data.get(str(appid), {}).get("success"):
                categories = data[str(appid)]["data"].get("categories", [])
                for c in categories:
                    all_inserts.append((appid, c["description"]))

        except TypeError as e:
            print(f"something went wrong")
        except KeyError as e:
            print(f"the key: {e}, does not exists")
        except Exception as e:
            print(f"Error parsing the price for {appid} caused: {e} ")
        finally:
            failed_inserts.append(appid)
    try:
        if all_inserts:
            query = f"""INSERT INTO categories(appid, category_description)
                    values (:appid ,:category_description)"""
            for appid, genre in all_inserts:
                conn.run(query, category_description=genre, appid=appid)

        query = """INSERT INTO failed_keys (appid, retried) VALUES (:appid, :retried)"""
        for appid in failed_inserts:
            conn.run(query, appid=appid, retried=0)
    except Exception:
        return "somehting went wrong with inserting to db"
    print(">>>>> inserting buld data into categories table completed <<<<<<<")


def insert_into_prices_table_bulk(prices_data):
    print(">>>>> inserting into prices table started <<<<<<<")
    conn = connection()
    all_inserts = []
    failed_inserts = []

    for idx, item in enumerate(prices_data):
        if not isinstance(item, (list, tuple)) or len(item) != 2:
            print(f"[Warning] this item causing an error item at index {idx}: {item}")
            continue
        appid, data = item

        try:

            if not data.get(str(appid), {}).get("success"):
                raise Exception("API response was not successful")

            if data[str(appid)]["data"]["is_free"]:
                all_inserts.append((appid, 0, 0, 0, 0))
            else:
                price = data[str(appid)]["data"].get("price_overview", [])
                all_inserts.append(
                    (
                        appid,
                        price["currency"],
                        price["initial"],
                        price["final"],
                        price["discount_percent"],
                    )
                )

        except TypeError as e:
            print(f"something went wrong")
        except KeyError as e:
            print(f"the key: {e}, does not exists")
        except Exception as e:
            print(f"Error parsing the price for {appid} caused: {e} ")
        finally:
            failed_inserts.append(appid)

    query = """INSERT INTO prices(appid, currency,initial_price,final_price, discount_percent )
                        values (:appid ,:currency, :initial_price, :final_price, :discount_percent)"""

    for my_appid, currency, initial, final, discount_percent in all_inserts:
        conn.run(
            query,
            currency=currency,
            appid=my_appid,
            initial_price=initial,
            final_price=final,
            discount_percent=discount_percent,
        )

    query = """INSERT INTO failed_keys (appid, retried) VALUES (:appid, :retried)"""
    for appid in failed_inserts:
        conn.run(query, appid=appid, retried=0)
    print(">>>>> inserting into prices table completed <<<<<<<")
