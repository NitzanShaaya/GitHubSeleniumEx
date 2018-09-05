from mysql_db_manager import MysqlDbManager


insert_sql = "INSERT INTO search_results(uuid,is_error,title,description,tags,last_update_time,language,stars) " \
             "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"


def convert_details_to_sql_db_input(page_details):
    error_num = 0
    if page_details.is_error:
        error_num = 1
    return (page_details.uuid,
            error_num,
            page_details.title,
            page_details.description,
            ",".join(page_details.tags),
            page_details.last_update_time,
            page_details.language,
            page_details.stars)


class ScrapperMysqlDbManager(MysqlDbManager):
    def __init__(self, config_manager):
        super(ScrapperMysqlDbManager, self).__init__(config_manager.get_config_string('MySql', 'Host'),
                                                     config_manager.get_config_string('MySql', 'Port'),
                                                     config_manager.get_config_string('MySql', 'User'),
                                                     config_manager.get_config_string('MySql', 'Password'),
                                                     config_manager.get_config_string('MySql', 'DataBase'))

    def insert_pages_details(self, pages_details):
        values = []
        for page_details in pages_details:
            db_row = convert_details_to_sql_db_input(page_details)
            values.append(db_row)

        self.insert(insert_sql, values)
