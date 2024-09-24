import logging


class BaseClass:
    def getlogger(self):
        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler('logfile.log')
        error_log_format = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        filehandler.setFormatter(error_log_format)
        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)
        return logger
