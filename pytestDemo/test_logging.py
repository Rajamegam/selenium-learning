import logging


def test_logging():
    logger = logging.getLogger(__name__)
    # __name__ --> at run time it will capture the testcase name

    filehandler = logging.FileHandler('logfile.log')
    error_log_format = logging.Formatter(
        "%(asctime)s: %(levelname)s: %(name)s: %(message)s")  # defining the format of the log
    filehandler.setFormatter(error_log_format)
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)
    logger.debug("This is a debug error")
    logger.info("THis is a info error")  # prints the information
    logger.warning("This is a warning error")  # prints the warning information
    logger.error("This is a error")
    logger.critical("This is a critical error")
