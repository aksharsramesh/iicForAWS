from django.conf.urls import url, include
from django.contrib import admin
from .import views


app_name='iichome'

urlpatterns=[
    url(r'^$', views.iichome, name='home'),
]
