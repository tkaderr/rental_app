from django.shortcuts import render
from ..add_item.models import Product

# Create your views here.(
def index(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, 'home/home_page.html', context)
