from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^edit_profile$', views.edit_profile),
    url(r'^user_dashboard_process$', views.edit_profile_process)
]
