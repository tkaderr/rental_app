# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import User
from django.contrib import messages
from django.shortcuts import render, redirect, reverse

# Create your views here.

def index(request):
    return render(request, 'login/login.html')

def register(request):
    data = {
    "username": request.POST['username'],
    'first_name': request.POST['first_name'],
    'last_name': request.POST['last_name'],
    'email': request.POST['email'],
    'password': request.POST['password'],
    'confirm_pw': request.POST['confirm_pw']
    }
    warnings=User.objects.validate(data)
    if not warnings:
        request.session['current_user_id'] = User.objects.create(username=data['username'],first_name=data['first_name'],last_name=data['last_name'], email=data['email'],password=User.objects.hashPW(data)).id
        return redirect(('/'))
    else:
        for i in warnings:
            messages.error(request, i)
        return redirect('/login')
    pass

def login(request):
    data = {
    'username': request.POST['username'],
    'password': request.POST['password']
    }
    warnings=User.objects.login(data)
    if not warnings:
        request.session['current_user_id'] = User.objects.get(username=data['username']).id
        return redirect('/')
    else:
        for i in warnings:
            messages.error(request,i)
        return redirect('/login')

def logout(request):
    request.session.flush()
    return redirect('/login')
