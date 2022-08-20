from utils import get_db_connection
from pymongo import MongoClient


def test_get_db_connection():

    conn = get_db_connection()

    assert conn
    assert isinstance(conn, MongoClient)
