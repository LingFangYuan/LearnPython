import http.client as client
import urllib.parse as parse

conn = None
try:
    params = parse.urlencode({'name': 'qiye', 'age': 22})
    headers = {'Content-type': 'application/x-www-form-urlencode',
               'Accept': 'text/plain'}
    conn = client.HTTPConnection('www.zhihu.com', 80, timeout=3)
    conn.request('POST', '/login', params, headers)
    response = conn.getresponse()
    print(response.getheaders())
    print(response.status)
    print(response.read())
except Exception as e:
    print('Error :', e)
finally:
    if conn:
        conn.close()

