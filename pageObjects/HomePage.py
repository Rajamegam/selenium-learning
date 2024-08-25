from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    user_name = (By.NAME, "name")
    user_mail_id = (By.NAME, "email")
    user_password = (By.ID, "exampleInputPassword1")
    user_checkbox = (By.ID, "exampleCheck1")
    user_gender_dropdown = (By.ID, "exampleFormControlSelect1")
    user_radio_button = (By.ID, "inlineRadio1")
    user_dob = (By.NAME, "bday")
    user_submit_button = (By.CSS_SELECTOR, ".btn.btn-success")
    user_success_message = (By.CSS_SELECTOR,".alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout = CheckoutPage(self.driver)
        return checkout

    def name(self):
        return self.driver.find_element(*HomePage.user_name)

    def email(self):
        return self.driver.find_element(*HomePage.user_mail_id)

    def password(self):
        return self.driver.find_element(*HomePage.user_password)

    def checkbox(self):
        return self.driver.find_element(*HomePage.user_checkbox)

    def gender(self):
        return self.driver.find_element(*HomePage.user_gender_dropdown)

    def radio_button(self):
        return self.driver.find_element(*HomePage.user_radio_button)

    def birthday(self):
        return self.driver.find_element(*HomePage.user_dob)

    def submit_button(self):
        return self.driver.find_element(*HomePage.user_submit_button)

    def success_message(self):
        return self.driver.find_element(*HomePage.user_success_message)
