import mysql.connector
import search_result

class DbManager:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.passwd = "Password1"
        self.database = "scrapper_output"
        self.db_connection = None

    def create_connection(self):
        self.db_connection = mysql.connector.connect(host=self.host, user=self.user, passwd=self.passwd, database=self.database)

    def close_connection(self):
        self.db_connection.disconnect()

    def insert(self, sql, values):
        self.create_connection()
        cursor = self.db_connection.cursor()
        cursor.executemany(sql, values)
        self.db_connection.commit()
        self.close_connection()
