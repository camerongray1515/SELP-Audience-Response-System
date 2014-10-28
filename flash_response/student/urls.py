from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^check_question_availability/$', 'student.views.check_question_availability'),
)
