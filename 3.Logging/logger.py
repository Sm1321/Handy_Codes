import logging

# configuring logging
logging.basicConfig(
    filename = 'app.log',
    filemode = 'w',
    level = logging.DEBUG,
    format = '%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
)

# log messages with different severity levels
logging.debug("This is a Debug Message")
logging.info("This is an info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is a critical Message")