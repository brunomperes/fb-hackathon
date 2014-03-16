# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('myproject.myapp.views',
	url(r'^$', 'index', name='index'),
    url(r'^ready/$', 'ready', name='ready'),
    url(r'^settings/$', 'settings', name='settings'),
    url(r'^game/$', 'game', name='game'),
    url(r'^list/$', 'list', name='list'),
    url(r'^login/$', 'user_login', name='login'),
    url(r'^logout/$', 'user_logout', name='logout'),
    url(r'^death/$', 'death', name='death'),
    url(r'^register/$', 'register', name='register'),
)
