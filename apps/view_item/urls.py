from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)$', views.item),
    url(r'^blockdate/(?P<id>\d+)$', views.blockdate),
    url(r'^success$', views.success)
]
