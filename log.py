import logging

formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logging.basicConfig(level=logging.DEBUG)


def setup_logger(name):
    logger = logging.getLogger(name)
    logging.getLogger().handlers.clear()
    logger.addHandler(handler)
