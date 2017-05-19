from django.conf.urls import url, include
from django.contrib import admin
from django.views.decorators.cache import cache_page
from django.views.i18n import javascript_catalog
from django_js_reverse.views import urls_js


urlpatterns = [
    url(r'', include('django.contrib.auth.urls')),

    url('', include('main.service_urls')),

    url(r'^api/', include('main.api.urls')),
    url(r'^jsreverse/$', cache_page(3600)(urls_js), name='js_reverse'),
    url(r'^jsi18n/$', javascript_catalog, name='javascript-catalog'),

]

