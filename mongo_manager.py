import pymongo


class MongoManager:
    def __init__(self, url, database, col, user, password):
        self.url = url
        self.database = database
        self.col = col
        self.user = user
        self.password = password
        self.client = None
        self.mongo_db = None
        self.col = None

    def open_connection(self):
        self.client = pymongo.MongoClient(self.url)
        result = self.client.scrapper_output.authenticate(self.user, self.password)
        print result
        self.mongo_db = self.client[self.database]
        self.col = self.mongo_db[self.col]

    def close_connection(self):
        self.client.close()

    def insert(self, values):
        self.col.insert_many(values)
