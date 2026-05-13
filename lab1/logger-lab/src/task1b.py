import logging

logging.basicConfig(
    filename='app1.log',
    filemode='w',
    level=logging.ERROR,
    format='%(levelname)s:%(name)s:%(message)s'
)

logging.error("This is an error message")
