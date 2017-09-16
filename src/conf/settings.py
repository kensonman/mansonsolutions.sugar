"""
Django settings for conf project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(&(&mcuz4ks_7+)eluza_n3%)_8r$o@vol+e5$o@f3cnyk*qfs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'sugar.mansonsolutions.hk',]
SECURE_SSL_REDIRECT=True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS += ['webframe', 'method_override', 'sugar', 'django_tables2']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#file: settings.py
MIDDLEWARE += [
   'webframe.methodoverridemiddleware.MethodOverrideMiddleware', #django 1.10 or aboves
   'webframe.LangMiddleware.LangMiddleware',
   'webframe.CurrentUserMiddleware.CurrentUserMiddleware',
   'django.middleware.locale.LocaleMiddleware',
]

#URL
ROOT_URLCONF = 'conf.urls'
LOGIN_URL    = 'webframe/login'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'webframe.providers.absolute_path', 'webframe.providers.fmt_injection', 'webframe.providers.template_injection',
            ],
        },
    },
]

WSGI_APPLICATION = 'conf.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'dbhost',
        'NAME': 'sugar',
        'USER': 'sugar',
        'PASSWORD': '4cRPECJ8wb5swfxBAHGZEFHe',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh_hant'

TIME_ZONE = 'Asia/Hong_Kong'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/sugar/'
STATIC_ROOT= 'static/sugar'

#LOGGING
if not os.path.isdir('logs'):os.mkdir('logs')
LOGGING={
   'version': 1,
   'disable_existing_loggers': False,
   'formatters': {
      'verbose': { 'format':'[%(asctime)s] %(levelname)s [%(name)s:%(filename)s:%(lineno)s] %(message)s', 'datefmt':'%d/%b/%Y %H:%M:%S' },
      'simple':  { 'format':'%(levelname)s <%(filename)s:%(lineno)d> %(message)s' },
   },
   'handlers': {
        'console': { 'level': 'DEBUG', 'class': 'logging.StreamHandler', 'formatter': 'simple' },
        'file': {'level': 'INFO', 'class': 'logging.handlers.TimedRotatingFileHandler', 'formatter': 'verbose', 'filename': './logs/runtime.log', 'when':'midnight'},
   },
   'loggers':{
      'django': {'handlers':['console', 'file'], 'propagate': True, 'level': 'WARNING'},
      'webframe': { 'handlers': ['console', ], 'level': 'INFO'},
      'sugar': {'handlers': ['console', ], 'level':'DEBUG'},
   },
}

#Template
TMPL_HEADER='sugar/header.html'

#Version
VERSION='v0.1.0'
