import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
country_list = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

for i in country_list:
    if i.text == "India":
        i.click()
        break
print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"
time.sleep(2)
