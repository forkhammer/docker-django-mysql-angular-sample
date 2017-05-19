import os
from configurations import Configuration
from .auth import AuthMixin
from .debug_toolbar import DebugToolbarMixin
from .static_files import StaticFilesMixin
from .cache import CacheMixin
from .thumbnail import ThumbnailMixin
from .rest import RestMixin
from .email import EmailMixin
from .celery import CeleryMixin
from .https import HttpsMixin
from .logging import LoggingMixin
from .js_reverse import JsReverseMixin
from .middleware import MiddlewareMixin
from .templates import TemplatesMixin
from .db import DatabaseMixin
from .breadcrumbs import BreadcrumbsMixin

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Base(DebugToolbarMixin, StaticFilesMixin, CacheMixin, AuthMixin, 
    ThumbnailMixin, RestMixin, EmailMixin, CeleryMixin, HttpsMixin, 
    LoggingMixin, JsReverseMixin, MiddlewareMixin, TemplatesMixin, DatabaseMixin, BreadcrumbsMixin, 
    Configuration):
    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '_kwz#45+l)xg2@xx=6*i%fwt6qu4h9e4ue92k=no84*xg)z4au'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = []

    IS_ADMIN_PANEL = False

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sitemaps',
        'django.contrib.sites',
        'django.contrib.flatpages',

        'debug_toolbar',
        # 'bootstrap_pagination',
        'easy_thumbnails',
        # 'breadcrumbs',
        'djng',
        'rest_framework',
        # 'django_celery_results',
        'djcelery_email',
        # 'django_js_reverse',
        # 'main',
        # 'administration',
    ]

    ROOT_URLCONF = 'main.urls'

    WSGI_APPLICATION = 'main.wsgi.application'

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

    LANGUAGE_CODE = 'ru-RU'

    TIME_ZONE = 'Europe/Moscow'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    SITE_ID = 1