import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s', 
                    datefmt='%a %d %b %Y %H:%M:%S',
                    filename='my.log',
                    filemode='w')
logging.info('this is a log info.')
logging.debug('this is a debug message')
logging.warning('this is a waring')
