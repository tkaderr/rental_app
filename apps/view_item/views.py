# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from add_item.models import Product
from django.shortcuts import render, redirect

# Create your views here.

def item(request, id):
    context = {
    "item" : Product.objects.get(id = id)
    }
    return render(request, "view_item.html", context)
