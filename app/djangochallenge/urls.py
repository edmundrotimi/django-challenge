#-*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

#Admin page basic styling
admin.site.site_header = 'Django Chanllenge'
admin.site.site_title = 'Django Chanllenge'
admin.site.index_title = 'Chanllenge Task'
admin.empty_value_display = '*** Empty ***'


admin.autodiscover()

urlpatterns = [
    url(r'^'+settings.ADMIN_PATH_FINDER+'/', include(admin.site.urls)),
    url(r'^', include("mailer.urls")),
]


#add admin path to urlpatterns
if settings.DJANGO_HOST != 'production':
    import debug_toolbar
    urlpatterns += [
        url('__debug__/', include(debug_toolbar.urls)),
    ]
