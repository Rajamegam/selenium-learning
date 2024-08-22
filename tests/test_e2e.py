import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utitlities.BaseClass import BaseClass
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
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
            product = checkout.productText().text
            # product = i.find_element(By.XPATH, "div/h4/a").text
            if product == "Blackberry":
                checkout.cartload().click()

        # clicking the checkout button
        checkout.checkOutButton().click()

        # clicking the checkout button in the cart page
        checkout.cart().click()

        confirm_page = ConfirmPage(self.driver)

        confirm_page.country_value().send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        confirm_page.link_text_value().click()
        confirm_page.confirm_checkbox().click()
        confirm_page.purchase().click()
        success_message = confirm_page.confirmation_message().text
        assert "Success! Thank you!" in success_message
        time.sleep(2)
