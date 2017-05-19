#-*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps import views as sitemaps_views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'angular/', include('djng.urls', 'angular')),

    url(r'^sitemap.xml$', sitemaps_views.index, {'sitemaps': sitemaps, 'sitemap_url_name': 'sitemaps'}),
        url(r'^sitemap-(?P<section>.+)\.xml$',
            sitemaps_views.sitemap,
            {'sitemaps': sitemaps}, name='sitemaps'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL_DEV, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL_DEV, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__', include(debug_toolbar.urls)),
    ]