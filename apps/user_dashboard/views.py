from django.shortcuts import render, redirect
from ..login.models import User, Address
from ..add_item.models import Product, Tag, Rental, Message
import datetime
# from datetime import datetime


def index(request):
    # today=datetime.today()
    # print today.year
    user = User.objects.get(id = request.session["current_user_id"])
    rental = Rental.objects.filter(renter = user)
    product = Product.objects.filter(seller= user)
    curr_rental = Product.objects.filter(seller=user, product_rental__rented_at_end__gte=datetime.date(2017, 5, 3), product_rental__rented_at_start__lte=datetime.date(2017, 5, 3))
    not_rental = Product.objects.filter(seller= user, rental = None) | Product.objects.filter(seller=user, product_rental__rented_at_end__lt = datetime.date(2017, 5, 3), product_rental__rented_at_start__gt =datetime.date(2017, 5, 3))
    message= Message.objects.filter(to_user=user)
    context={
        "users": user,
        "rentals": rental,
        "products": product,
        "curr_rentals":curr_rental,
        "not_rentals":not_rental,
        "messages":message
        # "today":today
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
