import scrapper
from scrapper_mongo_manager import ScrapperMongoManager
from config_manager import ConfigManager

pages_details = scrapper.scrap()
succeeded = True
try:
    db_manager = ScrapperMongoManager(ConfigManager())
    db_manager.open_connection()
    db_manager.insert_pages_details(pages_details)
    db_manager.close_connection()
except Exception:
    succeeded = False
scrapper.print_result(succeeded)
