import os
from django.contrib.messages import constants as messages


SITE_ROOT = os.path.join(os.path.realpath(os.path.dirname(__file__)), '../../')


TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(SITE_ROOT, 'media/')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(SITE_ROOT, 'static/')
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "pinry.settings.settings_context_processor.branding",
#    "django_facebook.context_processors.facebook", 
)

ROOT_URLCONF = 'pinry.urls'
WSGI_APPLICATION = 'pinry.wsgi.application'
LOGIN_REDIRECT_URL = '/' #was causing problem with other stuff
INTERNAL_IPS = ['127.0.0.1']
MESSAGE_TAGS = {
    messages.WARNING: 'alert',
    messages.ERROR: 'alert alert-error',
    messages.SUCCESS: 'alert alert-success',
    messages.INFO: 'alert alert-info',
}
API_LIMIT_PER_PAGE = 20

#start django-registration
ACCOUNT_ACTIVATION_DAYS = 2
#end

#start userregistration
AUTH_PROFILE_MODULE = 'userprofile.UserProfile'
#end
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'pinry.vendor',
    'pinry.core',
    'pinry.pins',
    'pinry.api',
    'django.contrib.admin',
#    'registration',
#    'pinry.userprofile',
#    'django_facebook',
#    'pinry.ecommerce',
)

#AUTHENTICATION_BACKENDS = (
#    'django_facebook.auth_backends.FacebookBackend',
#)
