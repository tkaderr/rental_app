# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

# Create your models here.

class UserManager(models.Manager):
    def validate(self, data):
        no_spaces= re.compile(r'^\S+$')
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
        username=data['username']
        first_name= data['first_name']
        last_name= data['last_name']
        email=data['email']
        pw=data['password']
        confirm_pw=data['confirm_pw']
        valid=True
        message=[]
        if len(username)<1 or len(first_name)<1 or len(last_name)<1 or len(email)<1 or len(pw)<1 or len(confirm_pw)<1:
            message.append("All fields are required!")
            valid=False
        if not no_spaces.match(username):
            message.append("No spaces allowed in username!")
            valid=False
        if not no_spaces.match(first_name):
            message.append("No spaces allowed in first name!")
            valid=False
        if not no_spaces.match(last_name):
            message.append("No spaces allowed in last name!")
            valid=False
        if not email_regex.match(email):
            message.append("Must be a valid Email Address!")
            valid=False
        if pw!=confirm_pw:
            message.append("Password Confirmation must match Password!")
            valid=False
        if len(pw)<8:
            message.append("Password must be longer than 8 characters!")
            valid=False
        if User.objects.filter(username=username):
            message=[]
            message.append("Username already exists! Try loggin in!")
        return message

    def hashPW(self, data):
        pw = data['password'].encode()
        hashed = bcrypt.hashpw(pw, bcrypt.gensalt())
        return hashed

    def login(self, data):
        username = data['username']
        input_pw = data['password'].encode()
        user = User.objects.filter(username=username)
        message=[]
        if user:
            db_pw = user[0].password.encode()
            if bcrypt.hashpw(input_pw, db_pw)==db_pw:
                return message
            else:
                message.append('The Username or Password is incorrect')
                return message
        else:
            message.append('Username does not exist')
            return message

class User(models.Model):
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    username=models.CharField(max_length=55)
    password=models.CharField(max_length=225)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    objects=UserManager()

class Address(models.Model):
    address1=models.CharField(max_length=225)
    address2=models.CharField(max_length=225)
    city=models.CharField(max_length=225)
    state=models.CharField(max_length=225)
    zipcode=models.IntegerField()
    user=models.OneToOneField(User, related_name="user_address")
