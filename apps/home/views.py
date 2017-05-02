from django.shortcuts import render
from ..add_item.models import Product, Tag

# Create your views here.(
def index(request):
    context = {
        "products": Product.objects.all(),
        'tags': Tag.objects.all()
    }
    return render(request, 'home/home_page.html', context)
