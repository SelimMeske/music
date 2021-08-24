import os
from .base import BASE_DIR
import logging

SECRET_KEY = os.getenv("__SECRET_KEY")

DEBUG = False
ALLOWED_HOSTS = ['meske.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Meske$music',
        'USER': os.getenv('__DB_USER'),
        'PASSWORD': os.getenv('__DB_PW'),
        'HOST': 'Meske.mysql.pythonanywhere-services.com',
        'PORT': '',
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, "static")

logging.error('PROD IS RUNNING!!!')