from pymongo import MongoClient
from os import environ


def get_db_connection() -> None:
    '''
    Creates a fully-configured MongoClient instance.

    Returns:
        The db client object.

    Raises:
        KeyError: Raised if any connection variables are missing from
        the current environment.
    '''

    # Connect to the Db
    try:
        user = environ['DB_USER']
        pswd = environ['DB_PASSWORD']
        uri = environ['DB_URI']

    except KeyError:
        raise Exception("Missing database credentials: DB_USER, DB_PASSWORD and DB_URI must be defined. Aborting.")  # noqa

    client = MongoClient(f"mongodb://{user}:{pswd}@{uri}/")

    return client
