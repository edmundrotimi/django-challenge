#-*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

#Admin page basic styling
admin.site.site_header = 'Django Chanllenge'
admin.site.site_title = 'Django Chanllenge'
admin.site.index_title = 'Chanllenge Task'
admin.empty_value_display = '*** Empty ***'


admin.autodiscover()

urlpatterns = [
    url(r'^matchflow_78594_kjyemgtyu/', include(admin.site.urls)),
    url(r'^', include("mailer.urls")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
