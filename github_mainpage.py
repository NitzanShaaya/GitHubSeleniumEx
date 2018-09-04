from github_toolbar import Toolbar
from base_page import BasePage

# Mapping for the main page of github.
# for this exercise only the toolbar(and specifically the search box)


class GitHubMainPage(BasePage):

    def __init__(self, driver):
        self.toolbar = Toolbar(driver)
