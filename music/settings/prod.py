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
    os.path.join(BASE_DIR, 'assets')
]
STATIC_ROOT = os.path.join(BASE_DIR, "static")