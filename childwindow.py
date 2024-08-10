import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("https://the-internet.herokuapp.com/windows")
# driver.find_element(By.LINK_TEXT, "Click Here").click()
# opened_windows = driver.window_handles
# driver.switch_to.window(opened_windows[1])
# print(driver.find_element(By.TAG_NAME, "h3").text)
# driver.switch_to.window(opened_windows[0])
# print(driver.find_element(By.TAG_NAME, "h3").text)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# action=ActionChains(driver)
# action.context_click(driver.find_element(By.CSS_SELECTOR,".blinkingText")).click().perform()
link = driver.find_element(By.CSS_SELECTOR,".blinkingText")
link.send_keys(Keys.CONTROL+Keys.RETURN)
window=driver.window_handles
driver.switch_to.window(window[1])
email_text=driver.find_element(By.CSS_SELECTOR,".red").text
x=email_text.split("at")[1].strip().split(" ")[0]
print(x)
driver.switch_to.window(window[0])
time.sleep(2)
