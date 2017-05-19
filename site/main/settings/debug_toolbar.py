class DebugToolbarMixin:
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'JQUERY_URL': None
    }

    INTERNAL_IPS = ()
    