# PyTradeFinanceChallenge

Implementación básica para ejecutar ordenes e interactuar con ambiente reMarkets via pyRofex.

## Deployment
Clonar el repositorio en carpeta local
```
git clone git@github.com:noctilukkas/PyTradeFinanceChallenge.git
```
*Nota:
Esta app fue desarrollado y testeado en Mac OS (Darwin)

### Setup and settings
Crear entorno virtual con virtualenv y python 3 (se puede usar pipenv, pyenv, virtualenvwrapper, etc.)

En terminal
```
virtualenv venv
```
o directorio oculto
```
virtualenv .venv
```

Activar entorno virtual con virtualenv 
```
source /venv/bin/activate
```

Instalar dependencias
```
pip install -r requirements.txt
```

Se requieren credenciales para acceder a la plataforma reMarkets (user, password, account), 
las mismas se pueden obtener en: [reMarkets](https://remarkets.primary.ventures/)


## Usage
Desde la terminal de comandos ejecutamos el siguiente comando:

```
python main.py -T DOEne21 -u <USER> -p <PASSWORD>
```

## Built With

* [Virtualenv](https://virtualenv.pypa.io/en/latest/) - Virtual environments for Python.
* [pyRofex](https://github.com/matbarofex/pyRofex) - pyRofex is a python library that allows interactions with ROFEX's Rest and Websocket APIs.


## Author

###Lucas Paiva### 
* [github](https://github.com/noctilukkas) 
* [linkedin](https://www.linkedin.com/in/lpaiva/)