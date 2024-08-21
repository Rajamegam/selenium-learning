import pytest
from selenium import webdriver

""" Sending browser values in the command line terminal
    Below is the syntax to send browser name in the command 
    'browser_name' --> is a key where we need to pass the value to it(either it is a chrome or firefox
"""


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


"""  command to run the browser in the command line options --> "py.test --browser_name chrome"
    '--browser_name' is a key and we need to pass the browser name as a value
    if we dont specify browser name in command line, it will default run on "chrome" browser 
"""


@pytest.fixture(scope="class")
def setup(request):  # invoking the browser
    """retreiving the value of browser name passed in the command line and store it in a variable
     """
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        driver = webdriver.Ie()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    """here the cls.driver--> represents the driver in the class file of the test file. here we are assigning the
        local driver to the driver in the class level
    """
    yield
    driver.close()
