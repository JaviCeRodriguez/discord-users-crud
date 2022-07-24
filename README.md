# Discord Users CRUD

API hecha con FastAPI. CRUD sencillo para administrar usuarios.


## How to run 🏃🏼

- Windows

```sh
git clone https://github.com/JaviCeRodriguez/discord-users-crud.git

cd discord-users-crud

python -m virtualenv venv

venv/Scripts/activate

pip install -r requirements.txt

uvicorn src.main:app --reload
```


- Linux

```sh
git clone https://github.com/JaviCeRodriguez/discord-users-crud.git

cd discord-users-crud

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn src.main:app --reload
```

## Datos 📖

Se utilizan datos falsos para popular la base de datos (SQLite3). Estos datos se cargan cada inicio de la API, si y solo si no hay registros en la tabla `users`.

En caso de no querer popular la base de datos, comentar la línea 26 de `src/main.py`.