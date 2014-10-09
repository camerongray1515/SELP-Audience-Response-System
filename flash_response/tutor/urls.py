from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'tutor.views.welcome'),
    url(r'^select_course/$', 'tutor.views.select_course'),
)
