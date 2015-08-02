from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<userid>[0-9]+)/$', views.profile),
]
