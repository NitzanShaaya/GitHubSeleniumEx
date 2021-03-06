import scrapper
from scrapper_mysql_db_manager import ScrapperMysqlDbManager
from config_manager import ConfigManager


pages_details = scrapper.scrap()
succeeded = True
try:
    db_manager = ScrapperMysqlDbManager(ConfigManager())
    db_manager.open_connection()
    db_manager.insert_pages_details(pages_details)
    db_manager.close_connection()
except Exception:
    succeeded = False
scrapper.print_result(succeeded)
