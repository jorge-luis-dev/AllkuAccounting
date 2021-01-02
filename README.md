# AllkuAccounting
Ecuador Accounting

## Software
* Python 3
* PostgreSQL 12

### Create virtual environment
Into folder project
$ virtualenv venv
$ source venv/bin/activate

### Install requirements
$ pip install -r requirements.txt
#### Update to SQLAlchemy 1.4 beta
$ pip list
$ pip uninstall SQLAlchemy
$ pip install SQLAlchemy==1.4.0b1
and replace in file in folder migrations/versions/*.py, search error and put "sa.Identity(start=1)"
also comment instruction of others tables not includes in models (migrations/versions/anyfile.py)

### Create database MacOS with Postgres.app
$ createdb allku
$ createuser jorgeluis
$ psql
allku=# grant all privileges on database allku to jorgeluis;
allku=# alter user jorgeluis with encrypted password 'j';

### Migrate to database
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade

### Run
$ python manage.py runserver

### Generate requirements with vertion
$ pip freeze > requirements_with_version.txt

## Util
### Remove cache (directory __pycache__)
$ py3clean .

## Test
Use HTTPie
https://httpie.io/

### GET (All accounts)
```console
http http://127.0.0.1:5000/rest/v1/accounts
```
### GET (One account)
```console
http http://127.0.0.1:5000/rest/v1/accounts/1
```
### GET (One account by code)
```console
http http://127.0.0.1:5000/rest/v1/accounts/code/1
```
### GET (All active )
```console
http http://127.0.0.1:8080/rest/v1/locations/active
```
### POST (Province and City)
```console
http POST http://127.0.0.1:5000/accounts < files/new_account.json
```
### PUT
```console
http PUT http://127.0.0.1:8080/rest/v1/locations/2 < files/update_location.json
```
### DELETE
```console
http DELETE http://127.0.0.1:8080/rest/v1/locations/41
```

