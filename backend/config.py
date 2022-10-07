import os, random, string


class Config(object):
    CSRF_ENABLE = True
    SECRET= '1259f126a1ed7542ca3d4dcc1c106cce07901a89'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = (os.path.dirname(os.path.abspath(__file__)))
    APP = None

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s/%s' % (IP_HOST, PORT_HOST)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///estudantes.sqlite3'

app_config = {
    'development' : DevelopmentConfig(),
    'testing': None,
    'production': None
}

app_active = os.getenv('FLASK_ENV')

if app_active is None:
    app_active = 'development'

    