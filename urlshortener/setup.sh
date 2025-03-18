#! /usr/bin/env sh

python manage.py mysqldb init
python manage.py mysqldb migrate
python manage.py mysqldb upgrade
