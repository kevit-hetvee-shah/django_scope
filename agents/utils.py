import logging

def get_logger(name):
    logger = logging.getLogger(name)
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(name)s - %(message)s', level=logging.INFO)
    return logger