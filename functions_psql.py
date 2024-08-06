import psycopg2

class PSQL:

    def __init__(self, user: str, password: str, port: int, database: str):
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.connection = None

    def close_connection(self):
        if self.connection:
            try:
                self.connection.close()
            except Exception as error:
                msg = ("ERROR: Ошибка закрытия соединения - ", repr(error))
                print(msg)

    def set_query(self, query: str, params: tuple = None):
        try:
            self.connection = psycopg2.connect(user=self.user, password=self.password,
                                               port=self.port, database=self.database)
            with self.connection.cursor() as cursor:
                if params is not None:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)

                self.connection.commit()

        except (Exception, psycopg2.Error) as error:
            self.connection.rollback()
            msg = ("ERROR: Не удалось выполнить запрос - ", error)
            print(msg)
            raise Exception(msg)

    def get_query(self, query: str, params: tuple = None) -> list:
        result = []
        try:
            self.connection = psycopg2.connect(user=self.user, password=self.password,
                                               port=self.port, database=self.database)
            with self.connection.cursor() as cursor:
                if params is not None:
                    cursor.execute(query, params)
                    self.connection.commit()
                else:
                    cursor.execute(query)
                    self.connection.commit()
                for row in cursor.fetchall():
                    result.append(row)

        except (Exception, psycopg2.Error) as error:
            self.connection.rollback()
            msg = ("ERROR: Не удалось получить данные - ", error)
            print(msg)
            raise Exception(msg)

        return result

    def commit(self) -> None:
        if self.connection:
            try:
                self.connection.commit()
            except Exception as error:
                self.connection.rollback()
                msg = ("ERROR: psql> Ошибка commit соединения - ", repr(error))
                print(msg)

