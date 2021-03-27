import os
from .base import BASE_DIR

SECRET_KEY = 'secret122312'
DEBUG = True
ALLOWED_HOSTS = []
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'music',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5434',
    }
}
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'static')
]
