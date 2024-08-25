import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
product_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actual_list = []
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(results))
assert len(results) > 0

for i in results:
    i.find_element(By.XPATH, "div/button").click()

run_time_list = driver.find_elements(By.CSS_SELECTOR, "div[class='products'] div h4")

for j in run_time_list:
    actual_list.append(j.text)

print(actual_list)
assert product_list == actual_list

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

prices = driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)

total_amount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
print(f"totalamount:", total_amount)
assert sum == total_amount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
promo_info = driver.find_element(By.CLASS_NAME, "promoInfo")
print(promo_info.text)

discount_amount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(discount_amount)
assert total_amount > discount_amount
time.sleep(2)
