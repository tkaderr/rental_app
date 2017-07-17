"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.add_item.models import Product, Tag, Rental, Category, Message
from apps.login.models import User, Address

# class UserAdmin(admin.ModelAdmin):
#   pass
# admin.site.register(User, UserAdmin)
# class ProductAdmin(admin.ModelAdmin):
#   pass
# admin.site.register(Product, ProductAdmin)
# class TagAdmin(admin.ModelAdmin):
#   pass
# admin.site.register(Tag, TagAdmin)
# class CategoryAdmin(admin.ModelAdmin):
#   pass
# admin.site.register(Category, CategoryAdmin)
# class RentalAdmin(admin.ModelAdmin):
#   pass
# admin.site.register(Rental, RentalAdmin)
# class AddressAdmin(admin.ModelAdmin):
#    pass
# admin.site.register(Address, AddressAdmin)
# class MessageAdmin(admin.ModelAdmin):
#    pass
# admin.site.register(Message, MessageAdmin)

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.home.urls')),
    url(r'^user/', include('apps.user_dashboard.urls')),
    url(r'^login/', include('apps.login.urls')),
    url(r'^item/', include('apps.view_item.urls')),
    url(r'^new_item/', include('apps.add_item.urls')),
    url(r'^search/', include('apps.search.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
