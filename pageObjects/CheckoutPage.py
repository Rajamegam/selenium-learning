from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    product_name = (By.XPATH, "//div[@class='card h-100']")
    add_button = (By.CSS_SELECTOR,".card-footer button")
    checkout_button = (By.CSS_SELECTOR,"a[class*='btn-primary']")

    def getProductNames(self):
        return self.driver.find_elements(*CheckoutPage.product_name)

    def cartload(self):
        return self.driver.find_element(*CheckoutPage.add_button)

    def checkOutButton(self):
        return self.driver.find_element(*CheckoutPage.checkout_button)
