import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!!330jk3yeea3o3r(m(t-fc7fey#_$yup@%@4hycwjo3es3k*v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',

  # My Apps
  'BackEnd.Apps.Orm.apps.OrmConfig',

  # Apps de terceros
  'django_extensions',
]

SHELL_PLUS = "ipython"  # Si tienes IPython instalado, usa esta opción
SHELL_PLUS_PRINT_SQL = True

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Orm_Django.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates']
    ,
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

WSGI_APPLICATION = 'Orm_Django.wsgi.application'

# >>> BD SQLITE3 <<< =============================================================================
# DATABASES = {
#   'default': {
#     'ENGINE': 'django.db.backends.sqlite3',
#     'NAME': BASE_DIR / 'db.sqlite3',
#   }
# }

# CONECTOR DE LA BD <<< pip install psycopg2-binary >>> POSTGRESQL ====================================
DATABASES = {
  'default': {
    'ENGINE': os.getenv('DB_ENGINE', ''),
    'NAME': os.getenv('DB_NAME_DATABASE', ''),
    'USER': os.getenv('DB_USERNAME_DATABASE', ''),
    'PASSWORD': os.getenv('DB_PASSWORD_DATABASE', ''),
    'HOST': os.getenv('DB_HOST_DATABASE', ''),
    'PORT': os.getenv('DB_PORT_DATABASE', '5432'),
  }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'