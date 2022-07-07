import requests
import logging
import time


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt='%a %d %b %Y %H:%M:%S',
                    filename='log.log',
                    filemode='a')

TOTAL_NUMBER = 100
url = 'http://www.httpbin.org/delay/5'

start_time = time.time()
for _ in range(1, TOTAL_NUMBER+1):
    logging.info('scraping %s', url)
    response = requests.get(url)
end_time = time.time()
logging.info('total time %s seconds', end_time - start_time)
