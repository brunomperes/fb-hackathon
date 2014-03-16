# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	(r'^myapp/', include('myproject.myapp.urls')),
	(r'^$', RedirectView.as_view(url='/myapp/list/')), # Just for ease of use.
)
