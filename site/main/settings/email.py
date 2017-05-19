class EmailMixin:
    # EMAIL
    EMAIL_ACTIVATION_DAYS = 2  # кол-во дней для хранения кода активации
    # для отправки кода активации
    AUTH_USER_EMAIL_UNIQUE = True
    SERVER_EMAIL = 'noreply@aks.belzan.ru'
    EMAIL_HOST = 'smtp.yandex.ru'
    EMAIL_PORT = 465
    EMAIL_HOST_USER = 'noreply@aks.belzan.ru'
    EMAIL_HOST_PASSWORD = 'dncrpj'
    EMAIL_USE_SSL = True
    DEFAULT_FROM_EMAIL = 'Магазин Кузя <noreply@aks.belzan.ru>'
    EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

    MODERATOR_EMAILS = ['forkhammer@gmail.com']
    NOTICE_FEEDBACK_EMAIL = ['forkhammer@gmail.com']