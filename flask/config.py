#encoding: utf-8
import os

HOSTNAME = 'dsflask'
PORT     = '3306'
DATABASE = 'datasets'
USERNAME = 'rkwork'
PASSWORD = 'rkwork'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True



SECRET_KEY = "rkworkasdasdasd"
JWT_SECRET_KEY = 'rkwork'

SESSION_COOKIE_SECURE=True,
SESSION_COOKIE_HTTPONLY=True,
SESSION_COOKIE_SAMESITE='None'


