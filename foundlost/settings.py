import os
from pathlib import Path
import dj_database_url
from django.core.exceptions import ImproperlyConfigured

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET KEY
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'insecure-fallback')

# Debug mode
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Allowed Hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.onrender.com']

# Installed apps
INSTALLED_APPS = [
    'service.apps.ServiceConfig',
    'authentication',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Required for static files on Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL and WSGI config
ROOT_URLCONF = 'foundlost.urls'
WSGI_APPLICATION = 'foundlost.wsgi.application'

# Templates
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'templates/authentication/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Authentication
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

# Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Default primary key field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings (from your info.py file)
EMAIL_USE_TLS = True
EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
EMAIL_PORT = 587

# Contact Email (optional)
try:
    CONTACT_EMAIL = 'itit13779@gmail.com'
except ImproperlyConfigured:
    pass
