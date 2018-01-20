from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$',
                           'motorcu.views.fuel',
                           name='homefuel'),

                       url(r'^fuel',
                           'motorcu.views.fuel',
                           name='fuel'),

                       url(r'^oil-care',
                           'motorcu.views.oilcare',
                           name='oilcare'),

                       url(r'^tire-pressure',
                           'motorcu.views.tire',
                           name='tire'),

                       )

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$',
                             'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

if settings.DEBUG:   # if DEBUG is True it will be served automatically
    urlpatterns += patterns('',
                            url(r'^static/(?P<path>.*)$',
                                'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                            )