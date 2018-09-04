from selenium import webdriver
from github_mainpage import GitHubMainPage
from github_project_page import ProjectPage
from github_search_results_page import SearchResultsPage
from scrapper_db_manager import ScrapperDbManager

# About the consts, i wanted to move them to a configuration(wrote the config section if you are interested
# but i decided against it once seeing the ramifications or one or two values in danger of changing


driver = webdriver.Chrome("chromedriver\\chromedriver.exe")
driver.get("https://github.com/")
main_page = GitHubMainPage(driver)
search_time = main_page.toolbar.search('selenium')

amount_of_results = 5
search_results = []
measurements = [search_time]

for index in range(0, amount_of_results):
    search_results_page = SearchResultsPage(driver)  # Since im requerying every time the results might change
    # (which can cause bug-duplicate if a result is pushed down in order). Without it elements would be stale.
    time_in_seconds_for_load = search_results_page.click_on_search_result_and_measure(index)
    project_details = ProjectPage(driver).get_project_details()
    measurements.append("Page with id:{0},name:{1} took {2} seconds to load"
                        .format(project_details.uuid, project_details.title, time_in_seconds_for_load))
    search_results.append(project_details)
    driver.back()

driver.quit()

db_manager = ScrapperDbManager()
db_manager.create_connection()
db_manager.insert_search_results(search_results)
db_manager.close_connection()

with open("performance_results.txt", "w") as text_file:
    text_file.write('\n'.join(measurements) + '\n')
