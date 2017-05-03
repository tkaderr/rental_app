from django.shortcuts import render

from ..add_item.models import Product, Tag
import datetime


# Create your views here.(
def index(request):
    # thirtyday=[]
    # date_format = "%m/%d/%Y"
    # product=Product.objects.all()
    # for products in product:
    #     delta = (date_format.strptime(products.created_at, date_format)) - (date_format.strptime(datetime.datetime.now(), date_format))
    #     if delta.days <= 30:
    #         thirtyday.append(products)

    context = {
        "products": Product.objects.all(),
        'tags': Tag.objects.all()
        # "30d_products": thirtyday

    }
    return render(request, 'home/home_page.html', context)
