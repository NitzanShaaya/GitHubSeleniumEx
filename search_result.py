import uuid
from github_locators import SearchResultsLocator


def get_title(element):
    title_element = element \
        .find_element(*SearchResultsLocator.TITLE_CONTAINER) \
        .find_element(*SearchResultsLocator.TITLE_LOCATOR)
    return title_element.text


def get_description(element):
    description_element = element \
        .find_element(*SearchResultsLocator.DESCRIPTION_LOCATOR)
    return description_element.text


def get_tags(element):
    tags_elements = element.find_elements(*SearchResultsLocator.TAGS_LOCATOR)
    return [element.text for element in tags_elements]


def get_last_update_time(element):
    last_update_time_element = element.find_element(*SearchResultsLocator.LAST_UPDATE_TIME_LOCATOR)
    return last_update_time_element.get_attribute('datetime')


def get_language(element):
    language_element = element.find_element(*SearchResultsLocator.LANGUAGE_CONTAINER) \
        .find_element(*SearchResultsLocator.LANGUAGE_LOCATOR)
    return language_element.text


def get_stars(element):
    stars_element = element.find_element(*SearchResultsLocator.STARS_LOCATOR)
    return stars_element.text


class SearchResult(object):

    def __init__(self, element):
        self.uuid = uuid.uuid4()  # generating a unique id so no identical lines could be generated later on in the db
        self.is_error = False  # Preferred changing from the outside rather
        #  then risking matching this result to another page
        self.title = get_title(element)
        self.description = get_description(element)
        self.tags = get_tags(element)
        self.last_update_time = get_last_update_time(element)
        self.language = get_language(element)
        self.stars = get_stars(element)

# I have looked for an orm that supports mysql. Found none, how can you say no one likes microsoft
