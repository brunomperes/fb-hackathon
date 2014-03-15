# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('myproject.myapp.views',
	url(r'^$', 'index', name='index'),
    url(r'^ready/$', 'ready', name='ready'),
    url(r'^game/$', 'game', name='game'),
    url(r'^list/$', 'list', name='list'),
    url(r'^login/$', 'login', name='login'),
    url(r'^death/$', 'death', name='death'),
)
