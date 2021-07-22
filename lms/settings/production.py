from .base import *

from .base import *

ALLOWED_HOSTS = ['139.59.238.153','api.lanka.institute']

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



AWS_ACCESS_KEY_ID = 'CQCKAKNPLGAAQEPHVTNR'
AWS_SECRET_ACCESS_KEY = 'EQR+a5wXEVgNS2CLT2RorGEdis5zrZp45TJ7+maruYs'
AWS_STORAGE_BUCKET_NAME = 'lankaspace'
AWS_S3_ENDPOINT_URL = 'https://sgp1.digitaloceanspaces.com'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'DATA'

STATIC_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'