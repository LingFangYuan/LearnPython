import requests


r = requests.get('http://localhost:6800/listprojects.json')
print(r.text)
