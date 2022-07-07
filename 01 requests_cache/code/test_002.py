import requests_cache


session = requests_cache.CachedSession('demo_cache')
for i in range(60):
    session.get('http://httpbin.org/delay/1')
    print('i:', i)