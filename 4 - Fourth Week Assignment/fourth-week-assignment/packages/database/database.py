import sqlalchemy
from decouple import config


class Database:
    """
    Permit make query to the database

    Attributes:
        db (Database): Database engine
    """

    @classmethod
    def setup_database(cls, url: str):
        cls.db = sqlalchemy.create_engine(config(url))

    @classmethod
    def make_query(cls, query: str):
        """
        Permit make a query to the database without a response

        Args:
            query (str): query to make to the database
        """
        with cls.db.connect() as connection:
            connection.execute(query)

    @classmethod
    def make_query_with_return(cls, query: str) -> list[dict]:
        """
        Permit make a query to the database and wait for a response

        Args:
            query (str): query to make to the database
        Returns:
            response (list[dict]):
        """
        with cls.db.connect() as connection:
            res = connection.execute(query)
            return [{column: value for column, value in res_row.items()}
                    for res_row in res]
