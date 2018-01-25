from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$',
                           'motorcu.views.home',
                           name='home'),

                       url(r'^fuel',
                           'fuel.views.fuel',
                           name='fuel'),

                       url(r'^oil-care',
                           'oilcare.views.oilcare',
                           name='oilcare'),

                       url(r'^tire-pressure',
                           'tirepressure.views.tire',
                           name='tire'),

                       url(r'^login',
                           'authentico.views.motorcu_login',
                           name='motorcu_login'),

                       url(r'^register',
                           'authentico.views.motorcu_register',
                           name='motorcu_register'),

                       url(r'^logout$',
                           'authentico.views.motorcu_logout',
                           name='motorcu_logout'),

                       # url(r'^test',
                       #     'motorcu.views.test_new_dashboard',
                       #     name='test_dashboard')

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