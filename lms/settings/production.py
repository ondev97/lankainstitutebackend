from .base import *

from .base import *

ALLOWED_HOSTS = ['139.59.238.153']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lanka',
        'USER': 'lanka',
        'PASSWORD': config('db_password'),
        'HOST': 'private-lankainstitutedb-do-user-9562704-0.b.db.ondigitalocean.com',
        'PORT': '25060',
    }
}

INSTALLED_APPS += [
    'storages'
]