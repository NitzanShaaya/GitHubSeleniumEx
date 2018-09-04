from github_locators import ProjectDetailsLocator
from base_page import BasePage
from project_details import ProjectDetails


class ProjectPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.is_error = driver.page_source.__contains__('404')

    def get_title(self):
        title_author = self.driver.find_element(*ProjectDetailsLocator.TITLE_AUTHOR_LOCATOR).text
        title_name = self.driver.find_element(*ProjectDetailsLocator.TITLE_NAME_CONTAINER)\
            .find_element(*ProjectDetailsLocator.TITLE_NAME_LOCATOR).text
        return title_author + ' / ' + title_name

    def get_description(self):
        description_element = self.driver \
            .find_element(*ProjectDetailsLocator.DESCRIPTION_LOCATOR)
        return description_element.text

    def get_tags(self):
        tags_elements = self.driver.find_elements(*ProjectDetailsLocator.TAGS_LOCATOR)
        return [element.text for element in tags_elements]

    def get_last_update_time(self):
        last_update_time_element = self.driver.find_element(*ProjectDetailsLocator.LAST_UPDATE_TIME_LOCATOR)
        return last_update_time_element.get_attribute('datetime')

    def get_language(self):
        self.driver.find_element(*ProjectDetailsLocator.LANGUAGE_BUTTON_LOCATOR).click()
        language_element = self.driver.find_element(*ProjectDetailsLocator.LANGUAGE_CONTAINER) \
            .find_element(*ProjectDetailsLocator.LANGUAGE_LOCATOR)
        return language_element.text

    def get_stars(self):
        stars_element = self.driver.find_element(*ProjectDetailsLocator.STARS_LOCATOR)
        return stars_element.text

    def get_project_details(self):
        return ProjectDetails(self.is_error,
                              self.get_title(),
                              self.get_description(),
                              self.get_tags(),
                              self.get_last_update_time(),
                              self.get_language(),
                              self.get_stars())
