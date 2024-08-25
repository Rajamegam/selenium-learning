import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
window_list=driver.window_handles
driver.switch_to.window(window_list[1])
message = driver.find_element(By.CSS_SELECTOR,".red").text
email=message.split("at")[1].strip().split(" ")[0]
driver.switch_to.window(window_list[0])
driver.find_element(By.ID,"username").send_keys(email)
driver.find_element(By.ID,"password").send_keys("12345")
driver.find_element(By.ID,"signInBtn").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
alert_message = driver.find_element(By.CSS_SELECTOR,".alert-danger").text
print(alert_message)
