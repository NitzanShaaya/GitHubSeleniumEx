import mysql.connector


class MysqlDbManager(object):
    def __init__(self, host, port, user, passwd, database):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database
        self.db_connection = None

    def create_connection(self):
        self.db_connection = mysql.connector.connect(host=self.host,
                                                     port=self.port,
                                                     user=self.user,
                                                     passwd=self.passwd,
                                                     database=self.database)

    def close_connection(self):
        self.db_connection.disconnect()

    def insert(self, sql, values):
        self.create_connection()
        cursor = self.db_connection.cursor()
        cursor.executemany(sql, values)
        self.db_connection.commit()
        self.close_connection()
