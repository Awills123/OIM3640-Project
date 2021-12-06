from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.contrib import admin

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from NewsUpdates import views



urlpatterns = [
    url(r'^$', views.index, name='index') ]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
