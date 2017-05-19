class CeleryMixin:
    CELERY_RESULT_BACKEND = 'django-cache'
    CELERY_BROKER_URL= 'redis://redis:6379/6'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TIME_ZONE = 'Europe/Moscow'
    CELERY_DEFAULT_QUEUE = 'default'