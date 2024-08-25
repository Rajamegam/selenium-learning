import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input[class='form-control ng-untouched ng-pristine ng-invalid']").send_keys(
    "Rajamegam")
driver.find_element(By.NAME, "email").send_keys("rajamegam1611@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("test")
# handling static dropdown
# select is a class and we need to create a object to access the methods of the class
gender_dropdown=Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
gender_dropdown.select_by_index(1)
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Rajamegam")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
alert_message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(alert_message)
assert "Success" in alert_message

time.sleep(2)
