import logging
logger = logging.getLogger(__name__)
logger.propagate = False # doesn't show in the logging_main when ran
logger.info("hello from helper")