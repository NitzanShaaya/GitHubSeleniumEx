from selenium import webdriver
from github_mainpage import GitHubMainPage
from github_search_results_page import SearchResultsPage


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
    # (which can cause bug if a result is pushed down in order). Without it elements would be stale.
    search_result = search_results_page.get_search_result(index)
    time_in_seconds_for_load = search_results_page.click_on_search_result_and_measure(index)
    measurements.append("Page with id:{0},name:{1} took {2} seconds to load"
                        .format(search_result.uuid, search_result.title, time_in_seconds_for_load))
    search_result.is_error = driver.page_source.__contains__('404')
    search_results.append(search_result)
    driver.back()
driver.quit()
with open("performance_results.txt", "w") as text_file:
    text_file.write('\n'.join(measurements) + '\n')
