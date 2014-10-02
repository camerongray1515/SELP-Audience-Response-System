from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'user_authentication.views.login_main'),
    url(r'^student/', 'user_authentication.views.login_form', {'realm': 'student'}),
    url(r'^tutor/', 'user_authentication.views.login_form', {'realm': 'tutor'}),
    url(r'^logout/', 'user_authentication.views.do_logout'),
)
