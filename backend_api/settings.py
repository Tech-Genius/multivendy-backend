"""
Django settings for backend_api project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-o-_=8#0i)t&ha&jj1z32v1!d$zi%#1p_91+1y@372vx5+k_32b'
SECRET_KEY = os.getenv("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['multivendy-backend-production.up.railway.app', 'localhost']

CSRF_TRUSTED_ORIGINS = ['https://multivendy-backend-production.up.railway.app']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'rest_framework',
    'corsheaders',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend_api.urls'

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

WSGI_APPLICATION = 'backend_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# Update database configuration from $DATABASE_URL.
# import dj_database_url
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES = ['default'].update(db_from_env)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'multivendor',
        'USER': 'postgres',
        'PASSWORD': 'wale2003',
        'HOST': '127.0.0.1',
        'PORT': '5432'

    }
}

# DATABASE_URL = os.getenv("DATABASE_URL")

# DATABASES = {
#     "default": dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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



REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ],

    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'rest_framework_simplejwt.authentication.JWTAuthentication',
    # ],

    'DEFAULT_PAGINATION_CLASS': 'main.pagination.CustomPagination',
    'PAGE_SIZE': 100,


}

CORS_ORIGIN_ALLOW_ALL = True

# CORS_ALLOWED_ORIGINS = [
#     "https://monumental-froyo-aac200.netlify.app"
    
    
# ]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL="/media/"
# MEDIA_ROOT =os.path.join(BASE_DIR,'media_cdn')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'