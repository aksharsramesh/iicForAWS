from django.conf.urls import url, include
from django.contrib import admin
from .import views

app_name = 'events'

urlpatterns=[
    url('^$', views.allevents_view, name='allevents'),
    url('^ipr/$', views.ipr, name='ipr'),
    url('^it19/$', views.it19, name='it19'),
    url('^pd/$', views.pd, name='pd'),
    url('^od/$', views.od, name='od'),
    url('^kyp/$', views.kyp, name='kyp'),
    url('^ltl/$', views.ltl, name='ltl'),
    url('^ht19/$', views.ht19, name='ht19'),
]
