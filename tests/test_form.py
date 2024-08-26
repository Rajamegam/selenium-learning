import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utitlities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestFormSubmission(BaseClass):
    def test_form_submission(self, getData):
        homepage = HomePage(self.driver)
        homepage.name().send_keys(getData[0])
        homepage.email().send_keys(getData[1])
        homepage.password().send_keys(getData[2])
        homepage.checkbox().click()
        # gender_dropdown = Select(homepage.gender())
        # gender_dropdown.select_by_visible_text("Male")
        self.select_option_by_text(homepage.gender(), getData[3])
        homepage.radio_button().click()
        homepage.birthday().send_keys(getData[4])
        homepage.submit_button().click()
        success_message = homepage.success_message().text
        assert "Success!" in success_message
        self.driver.refresh()

    @pytest.fixture(params=[("Rajamegam", "rajamegam7@gmail.com", "Test@123", "Male", "11/16/1995"),
                            ("Priya", "Priya@gmail.com", "Test@123", "Female", "02/23/1995")])
    def getData(self, request):
        return request.param
