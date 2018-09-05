from mongo_manager import MongoManager


def convert_page_details_to_dictionary(page_details):
    return {"uuid": page_details.uuid,
            "is_error": page_details.is_error,
            "title": page_details.title,
            "description": page_details.description,
            "tags": ",".join(page_details.tags),
            "last_update_time": page_details.last_update_time,
            "language": page_details.language,
            "stars": page_details.stars}


class ScrapperMongoManager(MongoManager):
    def __init__(self):
        self.url = "mongodb://localhost:2017"
        self.database = "scrapper_output"
        self.col = "pages_details"
        self.user = "admin"
        self.password = "admin"

    def insert_pages_details(self, pages_details):
        values = []
        for page_details in pages_details:
            values.append(convert_page_details_to_dictionary(page_details))

        self.insert(values)
