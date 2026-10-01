from pathlib import Path
import os


# ==========================================================
# CONFIGURACIÓN GENERAL
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================================================
# SEGURIDAD
# ==========================================================

# En desarrollo se utiliza una clave de respaldo.
# En producción se recomienda definir DJANGO_SECRET_KEY
# como variable de entorno.

SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-alke-wallet-development-key'
)

DEBUG = True

ALLOWED_HOSTS = []


# ==========================================================
# APLICACIONES INSTALADAS
# ==========================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Aplicación principal
    'gestion',
]


# ==========================================================
# MIDDLEWARE
# ==========================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ==========================================================
# URLS
# ==========================================================

ROOT_URLCONF = 'alke_wallet.urls'


# ==========================================================
# TEMPLATES
# ==========================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ==========================================================
# WSGI
# ==========================================================

WSGI_APPLICATION = 'alke_wallet.wsgi.application'


# ==========================================================
# BASE DE DATOS
# ==========================================================

# SQLite se utiliza durante el desarrollo.
# PostgreSQL queda preparado para un entorno de producción.

USE_POSTGRES = os.environ.get(
    'USE_POSTGRES',
    'False'
) == 'True'


if USE_POSTGRES:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',

            'NAME': os.environ.get(
                'POSTGRES_DB',
                'alke_wallet'
            ),

            'USER': os.environ.get(
                'POSTGRES_USER',
                'postgres'
            ),

            'PASSWORD': os.environ.get(
                'POSTGRES_PASSWORD',
                ''
            ),

            'HOST': os.environ.get(
                'POSTGRES_HOST',
                'localhost'
            ),

            'PORT': os.environ.get(
                'POSTGRES_PORT',
                '5432'
            ),
        }
    }

else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',

            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# ==========================================================
# VALIDACIÓN DE CONTRASEÑAS
# ==========================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'MinimumLengthValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'CommonPasswordValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'NumericPasswordValidator'
        ),
    },
]


# ==========================================================
# IDIOMA Y ZONA HORARIA
# ==========================================================

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True


# ==========================================================
# ARCHIVOS ESTÁTICOS
# ==========================================================

STATIC_URL = 'static/'


# ==========================================================
# AUTENTICACIÓN
# ==========================================================

LOGIN_URL = '/cuentas/login/'

LOGIN_REDIRECT_URL = '/clientes/'

LOGOUT_REDIRECT_URL = '/cuentas/login/'


# ==========================================================
# CLAVE PRIMARIA POR DEFECTO
# ==========================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'