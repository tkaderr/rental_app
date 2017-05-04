from django.shortcuts import render, redirect
from ..login.models import User, Address
from ..add_item.models import Product, Tag, Rental, Message
import datetime
# from datetime import datetime


def index(request):
    today=datetime.date.today()
    user = User.objects.get(id = request.session["current_user_id"])
    product = Product.objects.filter(seller= user)
    message= Message.objects.filter(to_user=user)
    curr_rental= Rental.objects.filter(product__seller=user, rented_at_end__gte=datetime.date(today.year, today.month, today.day), rented_at_start__lte=datetime.date(today.year, today.month, today.day))
    rental= Rental.objects.filter(renter=user, rented_at_end__gte=datetime.date(today.year, today.month, today.day), rented_at_start__lte=datetime.date(today.year, today.month, today.day))
    not_rental = Product.objects.filter(seller=user).exclude(product_rental__rented_at_end__gt=datetime.date(today.year, today.month, today.day), product_rental__rented_at_start__lt=datetime.date(today.year, today.month, today.day))
    context={
        "users": user,
        "rentals": rental,
        "products": product,
        "curr_rentals":curr_rental,
        "not_rentals":not_rental,
        "messages":message,
        "today":today
    }
    return render(request, 'user_dashboard/dashboard.html', context)

def edit_profile(request):
    user=User.objects.get(id = request.session["current_user_id"])
    context={
        "users": user
    }
    return render(request, 'user_dashboard/user_profile.html', context)

def add_product(request):
    return redirect('/new_item')

def home_page(request):
    return redirect('/home/home_page')

def edit_profile_process(request):
    user=User.objects.get(id = request.session["current_user_id"])
    check=User.objects.validate(request.POST)
    if check:
        for x in range(0, len(check)):
            messages.add_message(request, messages.INFO, check[x])
        return redirect ('/edit_profile')
    User.objects.filter(id=user.id).update(username=request.POST["username"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
    return redirect('/user')

def delete_item(request, id):
    prod=Product.objects.get(id=id)
    prod.delete()
    return redirect('/user')


def logout(request):
    request.session.clear()
    return redirect('/login/logout')
