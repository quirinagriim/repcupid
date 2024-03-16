from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.google.com")
search_box = driver.find_element_by_name("q")
search_box.send_keys("Selenium")
search_box.submit()
