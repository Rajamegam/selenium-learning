from selenium.webdriver.common.by import By


class ConfirmPage:
    country_key_value = (By.ID, "country")
    link_text = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase_button = (By.CSS_SELECTOR, ".btn.btn-success.btn-lg")
    success_message = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def __init__(self, driver):
        self.driver = driver

    def country_value(self):
        return self.driver.find_element(*ConfirmPage.country_key_value)

    def link_text_value(self):
        return self.driver.find_element(*ConfirmPage.link_text)

    def confirm_checkbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def purchase(self):
        return self.driver.find_element(*ConfirmPage.purchase_button)

    def confirmation_message(self):
        return self.driver.find_element(*ConfirmPage.success_message)
