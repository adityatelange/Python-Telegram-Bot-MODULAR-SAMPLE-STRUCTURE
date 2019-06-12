"""
    An Advanced Logger for Logging all input as well as output
"""

import logging
import os.path


# Set up logger.
def initialize_logger(output_dir):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    form = '%(asctime)s %(filename)s:%(lineno)s [%(levelname)s] %(message)s'

    # create console handler and set level to info
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(form)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # create error file handler and set level to error
    handler = logging.FileHandler(os.path.join(output_dir, "error.log"), "w", encoding=None, delay="true")
    handler.setLevel(logging.ERROR)
    formatter = logging.Formatter(form)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # create debug file handler and set level to debug
    handler = logging.FileHandler(os.path.join(output_dir, "info.log"))
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(form)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
