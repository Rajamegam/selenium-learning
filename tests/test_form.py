from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utitlities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestFormSubmission(BaseClass):
    def test_form_submission(self):
        homepage = HomePage(self.driver)
        homepage.name().send_keys("Rajamegam")
        homepage.email().send_keys("rajamegam7@gmail.com")
        homepage.password().send_keys("Test@123")
        homepage.checkbox().click()
        gender_dropdown = Select(homepage.gender())
        gender_dropdown.select_by_index(1)
        homepage.radio_button().click()
        homepage.birthday().send_keys("11/16/1995")
        homepage.submit_button().click()
        success_message = homepage.success_message().text
        assert "Success!" in success_message
