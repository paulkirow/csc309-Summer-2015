from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^(?P<userid>[0-9]+)/$', 'userprofile.views.profile', name="profile"),
]
