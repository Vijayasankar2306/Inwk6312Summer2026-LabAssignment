import logging

logging.basicConfig(
    level=logging.WARNING,
    format='%(levelname)s:%(name)s:%(message)s'
)

logger = logging.getLogger('example_logger')
logger.warning('This is a warning')
