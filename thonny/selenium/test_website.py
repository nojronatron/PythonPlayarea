from selenium.webdriver import Firefox

# quit and close all webdriver handles' windows and tabs
# def tearDown(self):
#     self.driver.quit()
    
with Firefox() as driver:
    driver = Firefox()
    # navigate to website
    driver.get("https://en.wikipedia.org")
    # get current url
    driver.current_url
    # refresh page
    driver.refresh()
    # get curent page title
    PageTitle = driver.title
    # webdriver can manage any page or tab it opens so long as it has a handle to it
    OriginalWindow = driver.current_window_handle
    # find the search textbox enter a query and press Enter key
    driver.find_element(By.NAME, "search"),send_keys("boeing" + Keys.ENTER)
    # search_button = driver.find_element(By.NAME, "go")
    # search_button.
    actual_result = driver.current_url
    # tearDown()
    print("Expected URL: https://en.wikipedia.org/wiki/Boeing")
    print("Actual URL: ", actual_result)
