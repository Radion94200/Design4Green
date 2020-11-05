from .base import *

DEBUG = True
SECRET_KEY = '=$^ot$yl64fkh=ls2s+q6a1(w=z(3w+s%+gob=g+ped3uby0y0'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# CORS
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8080',
    'http://127.0.0.1:8080',
]
