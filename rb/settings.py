from pathlib import Path
import environ 
import os

env = environ.Env()
environ.Env.read_env()

MONGO_USER=env("MONGO_USER")
MONGO_PASS=env("MONGO_PASS")
MONGO_HOST=env("MONGO_HOST")
MONGO_NAME=env("MONGO_NAME")
MONGO_DATABASE_HOST = \
'mongodb+srv://%s:%s@%s/%s' \
% (MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_NAME)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_qk1s2aq7*4ou^7*@-1m&(w1hl13^--#90-8um(*#hu88hg%eb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'rbcrypto.herokuapp.com','rb-crypto.web.app']

# Application definition

INSTALLED_APPS = [
    'rbcrypto.apps.RbcryptoConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rb.urls'

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

WSGI_APPLICATION = 'rb.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': "djongo",
        'NAME': MONGO_NAME,
        'CLIENT': {
            'host': MONGO_DATABASE_HOST
        }
    }
}


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


#CORS
CORS_ORIGIN_ALLOW_ALL = False
CSRF_COOKIE_SECURE = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
    'http://localhost:3000',
    'http://localhost', 
    'https://rb-crypto.web.app'
)


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
