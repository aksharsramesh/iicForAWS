from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^it21/', include('it20.urls')),
    url(r'^', include('iic.urls')),
    url(r'^events/', include('events.urls')),
    #url(r'^media/', views.error_view),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
