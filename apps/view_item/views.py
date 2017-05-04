# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..add_item.models import Product, Rental, Message
from ..login.models import User
from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.

def item(request, id):
    context = {
    "item" : Product.objects.get(id = id),
    'rentals': Rental.objects.filter(product__id=id),
    "user" : User.objects.get(id = request.session['current_user_id'])
    }
    return render(request, "view_item.html", context)

def blockdate(request, id):
    user = User.objects.get(id = request.session['current_user_id'])
    product = Product.objects.get(id = id)
    bookdate = request.POST['dateapp'].split(",")
    startdate =  str(bookdate[0])
    start_date = datetime.strptime(startdate, '%Y-%m-%d')
    enddate = str(bookdate[1])
    end_date = datetime.strptime(enddate, '%Y-%m-%d')
    to_user = User.objects.get(id = product.seller.id)
    rent = Rental.objects.create(renter = user, product = product, rented_at_start = start_date, rented_at_end = end_date)
    message = ''
    message += 'Hey '+ product.seller.first_name + "! Are you okay with " + user.first_name + " renting " + product.name + " from " + startdate + " to " + enddate
    msg = Message.objects.create(content = message, to_user = to_user, from_user = user)
    return redirect('/item/success')

def success(request):
    return render(request, "succcess.html")
