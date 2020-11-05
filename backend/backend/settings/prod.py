from .base import *

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = ["vps-2ea52359.vps.ovh.net", "localhost", "127.0.0.1"]

# CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://vps-2ea52359.vps.ovh.net',
    'https://vps-2ea52359.vps.ovh.net'
]
