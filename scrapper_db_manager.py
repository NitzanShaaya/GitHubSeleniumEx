from dbmanager import DbManager


insert_sql = "INSERT INTO search_results(uuid,is_error,title,description,tags,last_update_time,language,stars) " \
             "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"


class ScrapperDbManager(DbManager):
    def __init__(self):
        self.host = "localhost"
        self.port = 5400
        self.user = "scrapper"
        self.passwd = "scrapper"
        self.database = "scrapper_output"

    def insert_search_results(self, search_results):
        values = []
        for search_result in search_results:
            error_num = 0
            if search_result.is_error:
                error_num = 1
            values.append((search_result.uuid,
                           error_num,
                           search_result.title,
                           search_result.description,
                           ",".join(search_result.tags),
                           search_result.last_update_time,
                           search_result.language,
                           search_result.stars))

        self.insert(insert_sql, values)
