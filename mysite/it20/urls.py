from django.conf.urls import url, include
from django.contrib import admin
from .import views

app_name = 'it20'

urlpatterns=[
    url('^$', views.it20about, name='it20about'),
    url(r'^signup/$', views.closed, name='signup'),
    url('^submit/', views.closed, name='submit'),
    url('^download/199314/27an19ak$', views.downloadALL_view, name='downloadALL'),
    url('^login/', views.closed, name='login'),
    url('^contact/', views.contact_view, name='contact'),
    url('^logout/', views.closed, name='logout'),
    url('^media/ideaFormat/Ideathon_2.0.docx', views.download_view, name='download'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
]
