import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestClass:
    @pytest.mark.parametrize('username,pwd', [("Admin", "admin123"),("Admin","admin")])
    def test_login(self, username, pwd):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='username']"))
        ).send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(pwd)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
            self.status = WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH,
                                                                   "//div[@class='oxd-topbar-header-title']/span/h6")))
            # self.status = self.driver.find_element(By.XPATH,
            # "//div[@class='oxd-topbar-header-title']/span/h6")
            assert self.status.is_displayed()
            self.driver.close()
        except NoSuchElementException:
            print("Web element not found")
            assert False
