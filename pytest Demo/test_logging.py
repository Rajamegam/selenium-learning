import logging


def test_logging():
    logger = logging.getLogger(__name__)
    filehandler = logging.FileHandler('logfile.log')
    error_log_format = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
    filehandler.setFormatter(error_log_format)
    logger.addHandler(filehandler)

    logger.setLevel(logging.INFO)
    logger.debug("This is a debug error")
    logger.info("THis is a info error")
    logger.warning("This is a warning error")
    logger.error("This is a error")
    logger.critical("This is a critical error")
