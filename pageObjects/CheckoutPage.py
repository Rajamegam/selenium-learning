from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    product_name = (By.XPATH, "//div[@class='card h-100']")
    add_button = (By.CSS_SELECTOR,".card-footer button")
    checkout_button = (By.CSS_SELECTOR,"a[class*='btn-primary']")
    cart_page = (By.CSS_SELECTOR,".btn-success")
    product_text = (By.XPATH,"//div/h4/a")

    def getProductNames(self):
        return self.driver.find_elements(*CheckoutPage.product_name)

    def cartload(self):
        return self.driver.find_element(*CheckoutPage.add_button)

    def checkOutButton(self):
        return self.driver.find_element(*CheckoutPage.checkout_button)

    def cart(self):
        self.driver.find_element(*CheckoutPage.cart_page).click()
        confirm_page=ConfirmPage(self.driver)
        return confirm_page

    def productText(self):
        return self.driver.find_element(*CheckoutPage.product_text)
