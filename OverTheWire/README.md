#Natas

Natas enseña los fundamentos de la seguridad web en servidores.

Cada nivel de natas consiste en su propio sitio web ubicado en http://natasX.natas.labs.overthewire.org, donde X es el número de nivel. No hay inicio de sesión SSH. Para acceder a un nivel, introduzca el nombre de usuario de ese nivel (por ejemplo, natas0 para el nivel 0) y su contraseña.

Cada nivel tiene acceso a la contraseña del siguiente nivel. Tu trabajo es obtener de alguna manera esa contraseña siguiente y subir de nivel. Todas las contraseñas se almacenan también en /etc/natas_webpass/. Por ejemplo, la contraseña para natas5 se almacena en el archivo /etc/natas_webpass/natas5 y sólo puede ser leída por natas4 y natas5.

Traducción realizada con la versión gratuita del traductor DeepL.com
