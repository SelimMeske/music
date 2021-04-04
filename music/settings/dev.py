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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'static')
]
