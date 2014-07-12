from settings_global import *

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'NAME': 'bikeshare',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'mateuszklimek',
        'PASSWORD': '',
    }
}