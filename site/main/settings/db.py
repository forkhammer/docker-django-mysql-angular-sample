class DatabaseMixin:
    # Database
    # https://docs.djangoproject.com/en/1.11/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': 'mysql',
            'NAME': 'aks',
            'USER': 'root',
            'PASSWORD': '1'
        }
    }