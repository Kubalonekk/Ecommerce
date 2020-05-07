"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
# eebebebe
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p7%tfn8d&svddibibc%oa_ghfb)=grw5#njh+&l76cfhrr3rk5'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['ex-shop.herokuapp.com','127.0.0.1']
                

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'storages',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'Ecommerce base',
#         'USER':'postgres',
#         'PASSWORD':'###',
#         'HOST':'localhost',
#         'PORT':'5432'
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/






STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )


STATIC_URL = '/static/'
MEDIA_URL = '/images/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_URL = '/login_alert/'

# STATICFILES_DIRS = [
#          os.path.join(BASE_DIR, 'static')
#  ]

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
STATIC_ROOT = "/Users/kuba1/OneDrive/Pulpit/portfolio/static/"






AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',

)

SITE_ID = 1

LOGIN_REDIRECT_URL = '/' # po zalogowaniu przekeirwuje na glowna strone

CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_URL = '/item_list/'

#aws3 bucket

# AWS_ACCESS_KEY_ID = 'AKIA6QI74FRZLG7CV5GL'
# AWS_SECRET_ACCESS_KEY = '#'
# AWS_STORAGE_BUCKET_NAME = 'jakub-smorag-bucket'

# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = None
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_S3_HOST = 's3.us-west-2c.amazonaws.com'
# AWS_S3_REGION_NAME = 'us-west-2c'


# REST API SETTINGS

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework.authentication.TokenAuthentication'
    ]
}


def FILTERS_VERBOSE_LOOKUPS():
    from django_filters.conf import DEFAULTS

    verbose_lookups = DEFAULTS['VERBOSE_LOOKUPS'].copy()
    verbose_lookups.update({
        'exact': (''),
        'iexact': (''),
        'contains': (''),
        'icontains': (''),
    })
    return verbose_lookups


# ...
# <?xml version="1.0" encoding="UTF-8"?>
# <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
# <CORSRule>
#     <AllowedOrigin>*</AllowedOrigin>
#     <AllowedMethod>GET</AllowedMethod>
#     <AllowedMethod>POST</AllowedMethod>
#     <AllowedMethod>PUT</AllowedMethod>
#     <AllowedHeader>*</AllowedHeader>
# </CORSRule>
# </CORSConfiguration>
...