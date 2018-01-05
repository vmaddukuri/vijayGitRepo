import logging

fmt_str = "%(asctime)s:%(levelname)s:%(name)s:%(process)s:%(message)s"
logging.basicConfig(level=logging.DEBUG, format=fmt_str, filename='access.log')

logging.debug('a debug message')
logging.info('an confirmation')
logging.warning('warnings information')
logging.error('an error note')
logging.critical('panic error')

