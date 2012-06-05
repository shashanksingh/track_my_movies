from pinry.settings import *
from settings import *
import os


DEBUG = True
TEMPLATE_DEBUG = DEBUG
DATABASE_ENGINE   = 'django.db.backends.mysql'
DATABASE_HOST = ''
DATABASE_PORT = ''
DATABASE_NAME = 'trackmymovies'
DATABASE_USER = 'root'
DATABASE_PASSWORD = 'i am n3m35i5'

DATABASES = {
    'default': {
        'ENGINE': DATABASE_ENGINE ,
        'NAME': DATABASE_NAME ,
	'HOST': DATABASE_HOST ,
	'PORT': DATABASE_PORT ,
	'USER': DATABASE_USER ,
	'PASSWORD': DATABASE_PASSWORD,
    }
}

SECRET_KEY = ''
