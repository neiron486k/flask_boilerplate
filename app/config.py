import os

# Env
ENV = os.getenv('ENV') or 'development'
DEBUG = 'True' == (os.getenv('DEBUG') or 'False')

# Sqlalchemy
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or 'mysql://username:password@server/db'
SQLALCHEMY_TRACK_MODIFICATIONS = 'True' == (os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') or 'False')
