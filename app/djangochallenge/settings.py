#-*- coding: utf-8 -*-

import os
import socket

#import configparser to read config file
from django.utils.six.moves import configparser

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#Project path (i.e djangochallenge)
PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))

#root url path
ROOT_URLCONF = 'djangochallenge.urls'

#wsgi path
WSGI_APPLICATION = 'djangochallenge.wsgi.application'

# allow reading of empty configuration parameter
config = configparser.SafeConfigParser(allow_no_value=True, interpolation=None)


#get django host name
if not socket.gethostname().startswith('DESKTOP-TM7GRJA'):
    DJANGO_HOST = 'production'
    config.read(f'{PROJECT_DIR}/production.cfg')
else:
    DJANGO_HOST = 'development'
    config.read(f'{PROJECT_DIR}/local.cfg')


SECRET_KEY = config.get('security', 'SECRET_KEY')
DEBUG = config.get('security', 'DEBUG')
TEMPLATE_DEBUG = config.get('security', 'TEMPLATE_DEBUG')

#check allowed host and convert to list
CHECK_HOST = config.get('security', 'ALLOWED_HOSTS').replace("'", "")
ALLOWED_HOSTS = list(CHECK_HOST.split(" "))

ADMIN_PATH_FINDER = config.get('admin', 'ADMIN_PATH_FINDER').replace("'", "")


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    #project app
    'mailer',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

if DJANGO_HOST == 'production':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': config.get('database', 'NAME'),
            'HOST': config.get('database', 'HOST'),
            'PORT': config.get('database', 'PORT'),
            'USER': config.get('database', 'USER'),
            'PASSWORD': config.get('database', 'PASSWORD'),
        }
    }

    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'djangochallenge.sqlite3')
        }
    }


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#static settings
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIR =[
    os.path.join(BASE_DIR, 'mailer/static')
]


#additions settings based on production/development mode
if DJANGO_HOST == 'production':
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True 
    CSRF_COOKIE_SECURE = True 
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
else:
    #django debug tool bar settings
    INSTALLED_APPS += (
        #third part app
        'debug_toolbar',
    )

    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    INTERNAL_IPS = ['127.0.0.1', '0.0.0.0']

