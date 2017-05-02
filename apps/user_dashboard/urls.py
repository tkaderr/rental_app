from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^edit_profile$', views.edit_profile),
    url(r'^user_dashboard_process$', views.edit_profile_process),
    url(r'^home_page$', views.home_page)
    url(r'^/login/logout$', views.logout),
    url(r'^/new_item$', views.add_product)
]
