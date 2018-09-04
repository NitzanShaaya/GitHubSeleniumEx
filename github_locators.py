from selenium.webdriver.common.by import By


class SearchBoxLocator(object):
    SEARCH_BOX_LOCATOR = (By.CLASS_NAME, 'header-search-input')


class SearchResultsLocator(object):
    RESULTS_LOCATOR = (By.CLASS_NAME, 'repo-list-item')
    TITLE_CONTAINER = (By.CLASS_NAME, 'col-md-8')
    TITLE_LOCATOR = (By.CLASS_NAME, 'v-align-middle')
    DESCRIPTION_LOCATOR = (By.CLASS_NAME, 'd-inline-block')
    TAGS_LOCATOR = (By.CLASS_NAME, 'topic-tag')
    LAST_UPDATE_TIME_LOCATOR = (By.TAG_NAME, 'relative-time')
    LANGUAGE_CONTAINER = (By.CLASS_NAME, 'col-6')
    LANGUAGE_LOCATOR = (By.CLASS_NAME, 'text-gray')
    STARS_LOCATOR = (By.CLASS_NAME, 'muted-link')



