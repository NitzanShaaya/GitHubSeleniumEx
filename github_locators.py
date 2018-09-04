from selenium.webdriver.common.by import By


class SearchBoxLocator(object):
    SEARCH_BOX_LOCATOR = (By.CLASS_NAME, 'header-search-input')


class ProjectDetailsLocator(object):
    RESULTS_LOCATOR = (By.CLASS_NAME, 'repo-list-item')
    TITLE_AUTHOR_LOCATOR = (By.CLASS_NAME, 'fn')
    TITLE_NAME_CONTAINER = (By.CLASS_NAME, 'public')
    TITLE_NAME_LOCATOR = (By.TAG_NAME, 'strong')
    DESCRIPTION_LOCATOR = (By.CLASS_NAME, 'text-gray-dark')
    TAGS_LOCATOR = (By.CLASS_NAME, 'topic-tag')
    LAST_UPDATE_TIME_LOCATOR = (By.TAG_NAME, 'relative-time')
    LANGUAGE_BUTTON_LOCATOR = (By.CLASS_NAME, 'js-toggle-lang-stats')
    LANGUAGE_CONTAINER = (By.CLASS_NAME, 'repository-lang-stats-numbers')
    LANGUAGE_LOCATOR = (By.CLASS_NAME, 'lang')
    STARS_LOCATOR = (By.CSS_SELECTOR,
                        '#js-repo-pjax-container > '
                        'div.pagehead.repohead.instapaper_ignore.readability-menu.experiment-repo-nav > '
                        'div > ul > li:nth-child(2) > a.social-count.js-social-count')
    # This Page is written horribly. Surprising that a website around code management would be written so poorly that
    # css selector is the most normal way to locate an element


class SearchResultsLocator(object):
    RESULTS_LOCATOR = (By.CLASS_NAME, 'repo-list-item')
    TITLE_CONTAINER = (By.CLASS_NAME, 'col-md-8')
    TITLE_LOCATOR = (By.CLASS_NAME, 'v-align-middle')



