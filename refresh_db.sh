#!/bin/bash
echo -e "\n[INFO ] Removing old database file db.sqlite3"
rm db.sqlite3

echo -e "\n[INFO ] Reset and make migrations"
rm -R ./projects/migrations/*.py
touch ./projects/migrations/__init__.py
python3 manage.py makemigrations
python3 manage.py migrate

echo -e "\n[INFO ] Populating database with sample data"
python3 populate_db.py

echo -e "\n[INFO ] Completed!"