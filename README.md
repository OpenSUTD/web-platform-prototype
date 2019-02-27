# web-platform-prototype
Prototype for the Eventual OpenSUTD Web Platform

## Database setup

Database will not be pushed to github (will be local on your computer). Run migration to create the DB according to the models specified in the code.

```
python3 manage.py makemigrations
python3 manage.py migrate
```

## Running the test server

```
python3 manage.py runserver
```