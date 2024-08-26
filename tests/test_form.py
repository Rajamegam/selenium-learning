import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.formpagetestdata import Testdataformpage
from Utitlities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestFormSubmission(BaseClass):
    def test_form_submission(self, getDataByDict):
        homepage = HomePage(self.driver)
        homepage.name().send_keys(getDataByDict["name"])
        homepage.email().send_keys(getDataByDict["email"])
        homepage.password().send_keys(getDataByDict["password"])
        homepage.checkbox().click()
        # gender_dropdown = Select(homepage.gender())
        # gender_dropdown.select_by_visible_text("Male")
        self.select_option_by_text(homepage.gender(), getDataByDict["gender"])
        homepage.radio_button().click()
        homepage.birthday().send_keys(getDataByDict["DOB"])
        homepage.submit_button().click()
        success_message = homepage.success_message().text
        assert "Success!" in success_message
        self.driver.refresh()

    # @pytest.fixture(params=[("Rajamegam", "rajamegam7@gmail.com","Test@123"),
    #                         ("Priya", "Priya@gmail.com", "Test@123")])
    # def getData(self, request):
    #     return request.param

    """ can pass the values inside the tuple if we need to access the values straightaway from the array. else 
        we can use dictionary to access the params by sending the key of the value
        
        so in the getData() method, i have used array for the firstname, email and password 
        and for getDatabydict() method i have used dictonary for gender and DOB
    """

    # @pytest.fixture(params=[
    #     {"name": "Rajamgam", "email": "rajamegam7@gmail.com", "password": "Test@123", "gender": "Male",
    #      "DOB": "11/16/1995"},
    #     {"name": "Priya", "email": "priya@gmail.com", "password": "Test@123", "gender": "Female", "DOB": "02/03/1995"}])
    # def getDataByDict(self, request):
    #     return request.param

    """Here we are having the seperate class file for test data in the TestData package and accessing the
        values from the formpagetestdata file 
    """

    @pytest.fixture(params=Testdataformpage.test_form_data)
    def getDataByDict(self, request):
        return request.param
