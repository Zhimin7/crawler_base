import requests


session = requests.Session()
for i in range(60):
    session.get('http://httpbin.org/delay/1')
    print('i:', i)
