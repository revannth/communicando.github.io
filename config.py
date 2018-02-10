#config.py

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#SECRET_KEY = os.environ['SECRET_KEY']
SECRET_KEY = "SJonfekvwmpkdsv"
#SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')

#SQLALCHEMY_MIGRATE_REPO = os.environ['HEROKU_POSTGRESQL_PINK_URL']

SQL_TRACK_MODIFICATIONS = True
