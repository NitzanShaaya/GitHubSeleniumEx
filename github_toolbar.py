from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from github_locators import SearchBoxLocator


class Toolbar(object):

    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(self.driver, 100)\
            .until(EC.visibility_of_element_located(SearchBoxLocator.SEARCH_BOX_LOCATOR))
        self.search_box = self.driver.find_element(*SearchBoxLocator.SEARCH_BOX_LOCATOR)

    def search(self, value):
        self.search_box.clear()
        self.search_box.send_keys(value)
        self.search_box.submit()
