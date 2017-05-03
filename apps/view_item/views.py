# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..add_item.models import Product, Rental
from django.shortcuts import render, redirect

# Create your views here.

def item(request, id):
    context = {
    "item" : Product.objects.get(id = id),
    'rentals': Rental.objects.filter(product__id=id)
    }
    return render(request, "view_item.html", context)
