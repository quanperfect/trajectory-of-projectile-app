import logging

level = logging.DEBUG
fmt = '[%(levelname)s] %(asctime)s - %(message)s'
logging.basicConfig(level=level, format=fmt)
logging.getLogger('matplotlib').propagate = False


def log_message_debug(message):
    logging.debug(message)
