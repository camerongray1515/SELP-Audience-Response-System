from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'tutor.views.welcome'),
    url(r'^select_course/$', 'tutor.views.select_course'),
    url(r'^sessions/$', 'tutor.views.sessions'),
    url(r'^sessions/new/$', 'tutor.views.new_session'),
    url(r'^sessions/edit/(?P<session_id>\d+)/$', 'tutor.views.edit_session'),
)
