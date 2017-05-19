from .base import Base


class Prod(Base):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '172.27.0.1',
            'NAME': '',
            'USER': '',
            'PASSWORD': ''
        }
    }

    CELERY_BROKER_URL= 'redis://172.26.0.1:6379/6'

    ALLOWED_HOSTS = ['']