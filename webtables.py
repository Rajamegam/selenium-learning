from selenium import webdriver
from selenium.webdriver.common.by import By

sortedlist = []
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
# driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggie_list = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(1)")

for ele in veggie_list:
    sortedlist.append(ele.text)
# .copy() --> will take the copy of the already created list
browser_list = sortedlist.copy()
browser_list.sort()
assert browser_list == sortedlist
