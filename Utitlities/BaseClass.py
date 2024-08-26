import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:


    def verify_link_presence(self,text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def select_option_by_text(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def getLogger(self):
        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler('logfile.log')
        error_log_format = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        filehandler.setFormatter(error_log_format)
        logger.addHandler(filehandler)

        logger.setLevel(logging.INFO)
        # logger.debug("This is a debug error")
        # logger.info("THis is a info error")
        # logger.warning("This is a warning error")
        # logger.error("This is a error")
        # logger.critical("This is a critical error")
        return logger
