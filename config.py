import os

class Config:
    # Secret key for CSRF protection
    SECRET_KEY = '123456789000000000'

    # Database URI
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/garden_buddy_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Debug mode
    DEBUG = True