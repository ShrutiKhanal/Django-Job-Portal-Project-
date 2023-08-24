from .base import *
from django.contrib.messages import constants as messages

SECRET_KEY = 'django-insecure-#kk%tfn7a%8(x7be&!ow3$v3ae31rfxyii-$)zh-ab+4dhxxw_'


DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nexusdb',
        'USER': 'postgres',
        'PASSWORD': '9841639491',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '24a4bb800174bd'
EMAIL_HOST_PASSWORD = 'fe6ec0e67b41c5'
EMAIL_PORT = '2525'