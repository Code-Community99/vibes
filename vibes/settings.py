"""
Django settings for vibes project.

Generated by 'django-admin startproject' using Django 1.11.23.

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
SECRET_KEY = 'z295*(#i2u&zt^xoh#*oxh0wyqrl=6_83^07els&)g#q7%w+b9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'business',
    'discover',
    'groups',
    'login',
    'vmessages',
    'notifications',
    'settings',
    'signup',
    'uprofile',
    'home',
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

ROOT_URLCONF = 'vibes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR , 'business/templates/'),
            os.path.join(BASE_DIR , 'discover/templates/'),
            os.path.join(BASE_DIR , 'groups/templates/'),
            os.path.join(BASE_DIR , 'login/templates/'),
            os.path.join(BASE_DIR , 'vmessages/templates/'),
            os.path.join(BASE_DIR , 'notifications/templates/'),
            os.path.join(BASE_DIR , 'settings/templates/'),
            os.path.join(BASE_DIR , 'signup/templates/'),
            os.path.join(BASE_DIR , 'uprofile/templates/'),
            os.path.join(BASE_DIR , 'home/templates/'),
        ],
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

WSGI_APPLICATION = 'vibes.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'vibes.db',
        # 'HOST':'127.0.0.1',
        # 'PORT':3306,
        # 'USER':'root',
        # 'PASSWORD':'',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'



STATICFILES_DIRS = [
    os.path.join(BASE_DIR , 'business/static/'),
    os.path.join(BASE_DIR , 'discover/static/'),
    os.path.join(BASE_DIR , 'groups/static/'),
    os.path.join(BASE_DIR , 'login/static/'),
    os.path.join(BASE_DIR , 'vmessages/static/'),
    os.path.join(BASE_DIR , 'notifications/static/'),
    os.path.join(BASE_DIR , 'settings/static/'),
    os.path.join(BASE_DIR , 'signup/static/'),
    os.path.join(BASE_DIR , 'uprofile/static/'),
    os.path.join(BASE_DIR , 'home/static/'),

]
STATIC_ROOT = os.path.join(BASE_DIR , 'static_root')

MEDIA_URL = '/media/'


MEDIA_ROOT = os.path.join(BASE_DIR , 'media_root')
