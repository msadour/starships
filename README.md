# Star ships

## What is it?
An service that provide you star ships of star wars.

## Tech/framework

* Framework: ``Django``
* Database: ``sqlite3``

## installation (via virtual environment)

```
$ git clone https://github.com/msadour/starships

$ cd starships

$ virtualenv .venv

$ source .venv/bin/activate

$ python -m pip install -r requirements.txt

$ python manage.py runserver 
```

## Commands

* Launch server : python manage.py runserver
* Launch tests :  python -m pytest
* If you don't see starships, please launch this command : python manage.py init_db (could take few minutes)

## Utilisation

* the home page with list of starships : http://127.0.0.1:8000/
* Display star ships : http://127.0.0.1:8000/api_starships/starship
* Create your account (with POST method) : http://127.0.0.1:8000/api_starships/account/ 
the body request should be like that : 
```{
    "username": "your username",
    "first_name": "your first name",
    "last_name": "your last name",
    "email": "your email",
    "password": "your password"
}
```
* See all user : same url than above (with GET method)
* Authentication : http://127.0.0.1:8000/api_starships/api-token-auth/ 
the body request should be like that : 
```
{
    "username": "your username",
    "password": "your password"
}
```
* Add a star ship in your favorite (with PATCH method) : http://127.0.0.1:8000/api_starships/starship/<id_starship>/add_favorite/
* Add a star ship in your favorite (with PATCH method) : http://127.0.0.1:8000/api_starships/starship/<id_starship>/remove_favorite/
