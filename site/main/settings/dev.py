from .base import Base

class Dev(Base):
    DEBUG = True

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': 'mysql',
            'NAME': '',
            'USER': 'root',
            'PASSWORD': '1',
        }
    }

    INTERNAL_IPS = ('127.0.0.1', '172.27.0.1')

    BROKER_URL = 'redis://redis:6379/0'
    CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
    BROKER_HOST = "redis"

    HTTP_PREFIX = 'http'