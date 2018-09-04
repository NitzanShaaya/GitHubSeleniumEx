from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from github_locators import SearchBoxLocator
import time_common


class Toolbar(object):

    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(self.driver, 100)\
            .until(EC.visibility_of_element_located(SearchBoxLocator.SEARCH_BOX_LOCATOR))
        self.search_box = self.driver.find_element(*SearchBoxLocator.SEARCH_BOX_LOCATOR)

    def search(self, value):
        self.search_box.clear()
        self.search_box.send_keys(value)
        search_time = time_common.measure_time_of_action(self.search_box.submit)
        #  Page loads here for some reason. So i can only measure here
        return "Search took {0} seconds".format(search_time)
