"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import environ
from datetime import timedelta
import dj_database_url

# Set up the .env file to load gitignored secrets
env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = "RENDER" not in os.environ # Change to Azure one
DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    # Place azure hosting link for backend here
]


# Application definition

SYSTEM_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
]

CUSTOM_APPS = [
    "users.apps.UsersConfig",
    "common.apps.CommonConfig",
    "medias.apps.MediasConfig",
    "classifications.apps.ClassificationsConfig",
    "projects.apps.ProjectsConfig",
]


INSTALLED_APPS = SYSTEM_APPS + THIRD_PARTY_APPS + CUSTOM_APPS

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        # "config.authentication.TrustMeBroAuthentication",
        # "rest_framework.authentication.TokenAuthentication",
        # "config.authentication.JWTAuthentication",
    ]
}

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # "rest_framework_simplejwt.authentication.JWTAuthentication",
        # "config.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        # "rest_framework.authentication.TokenAuthentication",
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=3),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer", "JWT"),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}


AUTH_USER_MODEL = "users.User"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


LANGUAGE_CODE = "en-au"

TIME_ZONE = "Australia/Perth"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

PAGE_SIZE = 10
USER_LIST_PAGE_SIZE = 250
ROOT_URLCONF = "config.urls"

STATIC_URL = "static/"
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_ROOT = "uploads"
MEDIA_URL = "user-uploads/"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if DEBUG:
    DATABASES = {
        "default": dj_database_url.config(
            default=f"postgresql://{env('PGUSER')}:{env('PGPASS')}@{env('HOST')}:{env('PORT')}/{env('DBNAME')}",
            conn_max_age=600,
        ),
    }
else:
    DATABASES = {
        "default": dj_database_url.config(
            default=f"postgresql+psycopg2://postgres:postgres@localhost:5432/spms",
            conn_max_age=600,
        ),
    }


if DEBUG:
    CORS_ALLOWED_ORIGINS = (
        "http://localhost:3000",
        "http://localhost:8000",
    )

    CORS_TRUSTED_ORIGINS = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]
else:
    CORS_ALLOWED_ORIGINS = [
        # azure frontend backing link
        # azure frontend actual link
        # azure backend link
        # azure backend actual link
    ]
    CORS_TRUSTED_ORIGINS = [
        # azure frontend backing link
        # azure frontend actual link
        # azure backend link
        # azure backend actual link
    ]

if not DEBUG:
    SESSION_COOKIE_DOMAIN = ""  # e.g. ".websitename.com"
    CSRF_COOKIE_DOMAIN = ""  # e.g. ".websitename.com"
    # sentry_sdk.init() #if using sentry

# CF_ID = env("CF_ACCOUNT_ID") # if using cloudflare
# CF_TOKEN = env("CF_TOKEN")  # if using cloudflare
