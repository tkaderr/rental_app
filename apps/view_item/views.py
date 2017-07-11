# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..add_item.models import Product, Rental, Message
from ..login.models import User
from django.shortcuts import render, redirect
from datetime import datetime
from django.urls import reverse


# Create your views here.

def item(request, id):
    context = {
    "item" : Product.objects.get(id = id),
    'rentals': Rental.objects.filter(product__id=id),
    "user" : User.objects.get(id = request.session['current_user_id'])
    }
    if context['item'].seller != context['user']:
        return render(request, "view_item.html", context)
    else:
        return render(request, 'owner_item_view.html', context)

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
    msg = Message.objects.create(content = message, to_user = to_user, from_user = user, rental = rent, is_request_message = True)
    return redirect(reverse('view_item', kwargs={'id': id }))

def accept(request, id):
    message = Message.objects.get(id = id)
    m_user = User.objects.get(id = message.from_user.id)
    content = "Your request for renting " + message.rental.product.name + " has been accepted"
    rental = Rental.objects.get(id = message.rental.id)
    success_msg = Message.objects.create(content = content, from_user = User.objects.get(id = request.session['current_user_id']), to_user = m_user, rental = rental, is_request_message = False)
    rental.isapproved = True
    rental.save()
    message.delete()
    return redirect('/user')

def decline(request, id):
    message = Message.objects.get(id = id)
    m_user = User.objects.get(id = message.from_user.id)
    content = "Your request to rent " + message.rental.product.name +"has been declined. Please try booking for some other day/product"
    rental = Rental.objects.get(id = message.rental.id)
    declined_msg = Message.objects.create(content = content, from_user = User.objects.get(id = request.session['current_user_id']), to_user = m_user, rental = rental, is_request_message = False)
    print(declined_msg)
    message.delete()
    rental.delete()
    return redirect('/user')
