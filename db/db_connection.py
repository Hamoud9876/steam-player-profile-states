from pg8000.native import Connection
from dotenv import load_dotenv
import OS

load_dotenv()


def connection():
    return Connection(
        host= OS["HOST"],
        port= OS["PORT"],
        username= OS["USERNAME"],
        database= OS["DATABASE"],
        password= OS["PASSWORD"]
    )
