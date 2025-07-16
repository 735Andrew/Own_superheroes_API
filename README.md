<h2>Own_superheroes_API</h2>
<br>
<div>
<b>This project provides an API service that allows users to:</b>
<ul>
<li>Collect and manage your favourite superheroes.</li>
<li>Classify and compare them by their abilities.</li>
<li>Access to superheroes from different lores.</li>
</ul>
</div>
<br>
:eight_spoked_asterisk:<b>Tech Stack</b>:eight_spoked_asterisk:<br>
Flask, Flask-SQLAlchemy, PostgreSQL, Docker, Docker-Compose, Pytest
<br><br>
:eight_pointed_black_star:<b>Essential dependencies</b>:eight_pointed_black_star:<br>
Python 3.10+, Docker 28+ 
<hr> 
<div>
<h3>Docker Deploy</h3>
Open a terminal and run the following command:

```commandline
git clone https://github.com/735Andrew/Own_superheroes_API
```
<br>
Create a <b>.env</b> file in the root directory with the following variables: <br>
<b>/Own_superheroes_API/.env</b>

```commandline 
API_TOKEN = <API_VARIABLE>      # Obtain it from https://superheroapi.com/
POSTGRES_USER = <USER_VARIABLE>
POSTGRES_PASSWORD = <PASSWORD_VARIABLE>
POSTGRES_DB = <DB_VARIABLE>
POSTGRESQL_DATABASE_URL = postgresql+psycopg2://<USER_VARIABLE>:<PASSWORD_VARIABLE>@db:5432/<DB_VARIABLE>
```
<br>
Open a terminal in the root directory and execute this command to build the Docker container:

```commandline
docker-compose up -d 
```
</div>
<hr>
<h3>API Functionality</h3>

- Add a new superhero `POST http://localhost:5000/hero`

Request example:
```json
{
  "name": "thor"
}
```

Response example:
```json
{
    "id": 1,
    "intelligence": 100,
    "name": "thor",
    "power": 68,
    "speed": 25,
    "strength": 53
}
```
<br>

- Query a superhero by name `GET http://127.0.0.1:5000/hero?name=thor`


Response example:
```json
{
    "id": 1,
    "intelligence": 100,
    "name": "thor",
    "power": 68,
    "speed": 25,
    "strength": 53
}
```
<br>

- Classify your superheroes by abilities `GET http://127.0.0.1:5000/hero?power=50`


Response example:
```json
{
    "power": {
        "Heroes with an ability level 50": [],
        "Heroes with an ability level higher than 50": [
            {
                "id": 1,
                "intelligence": 100,
                "name": "thor",
                "power": 68,
                "speed": 25,
                "strength": 53
            }
        ],
        "Heroes with an ability level lower than 50": []
    }
}
```
<br>