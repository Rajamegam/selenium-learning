import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):  # invoking the browser
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    """here the cls.driver--> represents the driver in the class file of the test file. here we are assigning the
        local driver to the driver in the class level
    """
    yield
    driver.close()

