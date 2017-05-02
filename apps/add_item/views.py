# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from forms import NewItemForm
from models import Product, User

from django.shortcuts import render, redirect

# Create your views here.
def add_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.get(id=request.session['current_user_id'])
            instance = Product(name=data['name'],description=data['description'],image=request.FILES['image'], seller=user)
            instance.save()
            return redirect('/new_item/thanks')
        else:
            print form.errors
            return render(request, 'add_item/form.html', {'form': form})
    else:
        form = NewItemForm()

    return render(request, 'add_item/form.html', {'form': form})

def thanks(request):
    context= {
    'user':request.user,
    'products': Product.objects.all()
    }
    return render(request, 'add_item/thanks.html', context)
