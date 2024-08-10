import time

from selenium import webdriver

#invoking chrome browser
driver = webdriver.Chrome()

driver.get("https://www.rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)





















time.sleep(2)
