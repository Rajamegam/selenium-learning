import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utitlities.BaseClass import BaseClass
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        # Clicking the shop button in the home page
        homepage = HomePage(self.driver)
        homepage.shopItems().click()

        self.driver.implicitly_wait(4)

        # get the product names in the product list page
        checkout = CheckoutPage(self.driver)
        product_name = checkout.getProductNames()

        # adding the product to the cart if the product name is "Blackberry"
        for i in product_name:
            product= checkout.productText().text
            #product = i.find_element(By.XPATH, "div/h4/a").text
            if product == "Blackberry":
                checkout.cartload().click()

        # clicking the checkout button
        checkout.checkOutButton().click()

        #clicking the checkout button in the cart page
        checkout.cart().click()

        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.btn-lg").click()
        success_message = self.driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text

        assert "Success! Thank you!" in success_message
        time.sleep(2)
