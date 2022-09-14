# Register_coink
 Aplicación web en Python usando django, donde se puedan registrar los usuarios.

 Los usuarios al ingresar pueden ver sus datos.

 Para visualizar todos lo registos, se ingresa con un superuser.

### Instalación 🔧

Para realizar la instalación se deben seguir los siguientes pasos,

_Clonación del repositorio_

```shell
git clone git@github.com:dickson7/register_coink.git
```

_Ingresamos en el directorio del repositorio clonado, y ejecutamos el siguiente comando para habilitar el entorno virtual_

```shell
python3 -m venv env
```

_Activamos el entorno virtual_

```shell
source env/bin/activate
```

_Instalamos las dependencias con pip_

```shell
(env)$ pip3 install -r requirements.txt
```

_Lanzamos migraciones_

```shell
(env)$ python3 manage.py makemigrations
(env)$ python3 manage.py migrate
```

_Como último paso realizamos la ejecución del servidor_

```shell
(env)$ python3 manage.py runserver
```


#
## Tests
_Para ejecutar los tests usamos este comando_
```shell
(env)$ python3 manage.py test 
```
  
### Informe de cobetura
```shell
(env)$ coverage run manage.py test -v 2 && coverage report 
```

```python
Name                                 Stmts   Miss  Cover
--------------------------------------------------------
authentication/admin.py                  1      0   100%
authentication/apps.py                   4      0   100%
authentication/models.py                 6      0   100%
authentication/urls.py                   3      0   100%
authentication/utils/setup_test.py      24      6    75%
authentication/views.py                 65     14    78%
coink/admin.py                           1      0   100%
coink/apps.py                            4      0   100%
coink/models.py                          1      0   100%
coink/tests.py                           1      0   100%
coink/urls.py                            3      0   100%
coink/views.py                          14      6    57%
coinksite/settings.py                   24      0   100%
coinksite/urls.py                        3      0   100%
manage.py                               12      2    83%
--------------------------------------------------------
TOTAL                                  166     28    83%
```