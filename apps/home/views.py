from django.shortcuts import render
from django.utils import timezone
from ..add_item.models import Product, Tag
from datetime import datetime


# Create your views here.(
def index(request):
    # thirtyday=[]
    # product=Product.objects.all()
    # today = datetime.now()
    # today.replace(tzinfo=timezone.utc)
    # for products in product:
    #     productdt=products.created_at
    #     productdt.replace(tzinfo=timezone.utc)
    #     delta = today-productdt
    #     if delta.days <= 30:
    #         thirtyday.append(products)

    context = {
        "products": Product.objects.all(),
        'tags': Tag.objects.all()
        # "30d_products": thirtyday
    }
    return render(request, 'home/home_page.html', context)
