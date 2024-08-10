import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkbox_list = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for i in checkbox_list:
    if i.get_attribute("value") == "option2":
        i.click()
        assert i.is_selected()
        break

radiobutton_list = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
for j in radiobutton_list:
    if j.get_attribute("value") == "radio1":
        j.click()
        assert j.is_selected()
        break

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()

time.sleep(2)
