import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
product_name = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for i in product_name:
    product = i.find_element(By.XPATH, "div/h4/a").text
    if product == "Blackberry":
        i.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR,".btn-success").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,".btn.btn-success.btn-lg").click()
success_message=driver.find_element(By.CSS_SELECTOR,".alert.alert-success.alert-dismissible").text

assert "Success! Thank you!" in success_message
time.sleep(2)
