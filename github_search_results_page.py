from github_locators import SearchResultsLocator
from base_page import BasePage
import time_common


class SearchResultsPage(BasePage):

    def __init__(self, driver):
        self.results_elements = driver.find_elements(*SearchResultsLocator.RESULTS_LOCATOR)

    def get_search_result_link(self, index):
        return self.results_elements[index] \
                           .find_element(*SearchResultsLocator.TITLE_CONTAINER) \
                           .find_element(*SearchResultsLocator.TITLE_LOCATOR)

    def click_on_search_result_and_measure(self, index):
        return time_common.measure_time_of_action(self.get_search_result_link(index).click)
