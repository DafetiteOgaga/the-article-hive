"""
Django settings for article_hive_project project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os, sys
# Your GitHub personal access token
sys.path.append(os.path.expanduser("~"))
from my_credentials import credentials
# print(f'credentials: {credentials}')

CACHE_TTL = 60 * 60 * 24 # a day

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ks%dws4&%hgxe21a(9g+8dmp)9l(tq7k&w&s4cuz2=dy4joql^'

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = [
    # 'dafetite.pythonanywhere.com',
    'dafe.pythonanywhere.com',
    'localhost',
    '127.0.0.1',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'article_hive_app',		# <- added article_hive_app here
    # 'django_extensions',		# <- added django_extensions here
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'article_hive_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'article_hive_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# print('MY_LOCAL_MACHINE:', os.environ.get('MY_LOCAL_MACHINE'))
if os.environ.get('MY_LOCAL_MACHINE'):
    # print(f"development mode: {os.environ.get('MY_LOCAL_MACHINE')}")
    # print(f"MY_LOCAL_REDIS_LOCATION (from env): {os.environ.get('MY_LOCAL_REDIS_LOCATION')}")
    # print(f"MY_LOCAL_REDIS_LOCATION (from file): {credentials['MY_LOCAL_REDIS_LOCATION']}"),
    # print(f"MY_REDIS_LOCATION (from file): {credentials['MY_REDIS_LOCATION']}"),
    DEBUG = True # for development
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    # CACHES = {
    #     "default": {
    #         "BACKEND": "django_redis.cache.RedisCache",
    #         "LOCATION": credentials['MY_LOCAL_REDIS_LOCATION'],
    #         "OPTIONS": {
    #             "CLIENT_CLASS": "django_redis.client.DefaultClient",
    #         }
    #     }
    # }
    # CACHES = {
    #     "default": {
    #         "BACKEND": "django_redis.cache.RedisCache",
    #         "LOCATION": credentials['MY_REDIS_LOCATION'],
    #         "OPTIONS": {
    #             "CLIENT_CLASS": credentials['CLIENT_CLASS'],
    #             "PASSWORD": credentials['PASSWORD'],
    #         }
    #     }
    # }

else:
    DEBUG = False # production
    try:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'dafetite$article-hive_db',
                'USER': credentials['MY_DB_USERNAME'],
                'PASSWORD': credentials['MY_DB_PASSWORD'],
                'HOST': 'dafetite.mysql.pythonanywhere-services.com',
            }
        }
    except:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'dafe$article-hive_db',
                'USER': credentials['MY_DB_USERNAME'],
                'PASSWORD': credentials['MY_DB_PASSWORD'],
                'HOST': 'dafetite.mysql.pythonanywhere-services.com',
            }
        }
    # CACHES = {
    #     "default": {
    #         "BACKEND": "django_redis.cache.RedisCache",
    #         "LOCATION": credentials['MY_LOCAL_REDIS_LOCATION'],
    #         "OPTIONS": {
    #             "CLIENT_CLASS": "django_redis.client.DefaultClient",
    #         }
    #     }
    # }
    # CACHES = {
    #     "default": {
    #         "BACKEND": "django_redis.cache.RedisCache",
    #         "LOCATION": credentials['MY_REDIS_LOCATION'],
    #         "OPTIONS": {
    #             "CLIENT_CLASS": credentials['CLIENT_CLASS'],
    #             "PASSWORD": credentials['PASSWORD'],
    #         }
    #     }
    # }

# ############### for tests ##############
# DEBUG = True # for test
# SERVE_STATIC_FILES = True  # for test
# ALLOWED_HOSTS = ['*'] # for test
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'OPTIONS': {
#             'read_default_file': '../MySQL_credentials.cnf',
#         },
#     }
# }
# ########################################


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Added static variable here
STATICFILES_DIRS = [
    BASE_DIR / 'static',		# <- added static to BASE_DIR
    BASE_DIR / 'static/article_hive_project',		# <- added static to project dir.
]

# custom user model
AUTH_USER_MODEL = 'article_hive_app.User'

# login redirect for anonymous users
LOGIN_URL = '/login/'

# Media files custom added
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# for production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATICFILES_FINDERS = [
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# ]
