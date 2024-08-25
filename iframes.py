from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
iframe_text=driver.find_element(By.CSS_SELECTOR,"body[id='tinymce'] p").text
print(iframe_text)
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)