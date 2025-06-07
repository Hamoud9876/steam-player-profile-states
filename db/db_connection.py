from pg8000.native import Connection
from dotenv import load_dotenv
import os

load_dotenv()


def connection():
    return Connection(
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        user=os.getenv("USERNAME"),
        database=os.getenv("DATABASE"),
        password=os.getenv("PASSWORD"),
    )


def db_close(db):
    db.close()
