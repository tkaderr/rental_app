from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)$', views.item, name = "view_item"),
    url(r'^blockdate/(?P<id>\d+)$', views.blockdate),
    url(r'^accept/(?P<id>\d+)$', views.accept),
    url(r'^decline/(?P<id>\d+)$', views.decline),
]
