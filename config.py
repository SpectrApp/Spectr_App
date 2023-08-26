import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DADATA_API_KEY = os.environ.get('DADATA_API_KEY') or 'key'
    DADATA_SECRET_KEY = os.environ.get('DADATA_SECRET_KEY') or 'secret'