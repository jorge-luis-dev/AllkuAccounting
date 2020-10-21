# AllkuAccounting
Ecuador Accounting

## Software
* Python 3
* PostgreSQL 12

### Create virtual enviroment
Into folder project
$ virtualenv venv
$ source venv/bin/activate

### Install requirements
$ pip install -r requirements.txt

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



