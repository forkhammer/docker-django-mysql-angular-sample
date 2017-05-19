import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CacheMixin:
    # CACHE
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': 'memcached:11211',
            'KEY_PREFIX': 'aks:',
            },
        'file': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': os.path.join(BASE_DIR, 'media/aks-cache'),
        },
    }