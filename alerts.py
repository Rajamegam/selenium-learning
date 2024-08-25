import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "name").send_keys("Rajamegam")
driver.find_element(By.ID, "alertbtn").click()

alert = driver.switch_to.alert
print(alert.text)
assert "Rajamegam" in alert.text
alert.accept()

driver.find_element(By.ID, "name").send_keys("G")
driver.find_element(By.ID, "confirmbtn").click()
time.sleep(2)
alert2 = driver.switch_to.alert
print(alert2.text)
#alert2.accept()
alert2.dismiss()
