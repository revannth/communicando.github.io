#config.py

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.environ['SECRET_KEY']
#SECRET_KEY = "SJonfekvwmpkdsv"
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')


#Mail Details(Will go in as Environment Varialbles)
'''MAIL_SERVER='smtp.googlemail.com'
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME = 'noreplycommunicando@gmail.com'
MAIL_PASSWORD = 'Revanth@1'''
#SQLALCHEMY_MIGRATE_REPO = os.environ['HEROKU_POSTGRESQL_PINK_URL']

SQL_TRACK_MODIFICATIONS = True

'''MAIL_SERVER=os.environ['MAIL_SERVER']
MAIL_PORT=os.environ['MAIL_PORT']
MAIL_USE_TLS=os.environ['MAIL_USE_TSL']
MAIL_USERNAME = os.environ['MAIL_USERNAME']
MAIL_PASSWORD = os.environ['MAIL_PASSWORD']'''