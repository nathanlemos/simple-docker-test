from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnection:
    def __init__(self) -> None:
        self.__connection_string = "mysql+pymysql://root:senha@mysqldb/teste"
        self.session = None

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        sessionmaker = sessionmaker()
        self.session = sessionmaker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
