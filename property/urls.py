from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<property_id>[0-9]+)/$', views.property),
]
