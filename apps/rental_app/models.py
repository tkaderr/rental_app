from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    password=models.CharField(max_length=225)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Address(models.Model):
    address1=models.CharField(max_length=225)
    address2=models.Charfield(max_length=225)
    city=models.CharField(max_length=225)
    state=models.Charfield(max_length=225)
    zipcode=models.IntegerField()
    user=models.OneToOneField(User, related_name="user_address")

class Product(models.Model):
    name=models.CharField(max_length=225)
    description=models.TextField(max_length=225)
    price=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    seller=models.ForeignKey(User, related_name="products")
    rental=models.ManyToManyField(User, through="Rental")

class Tag(models.Model):
    name=models.Charfield(max_length=225)
    product=models.ManyToManyField(Product, related_name="product_tag")

class Rental(models.Model):
    renter=models.ForeignKey(User, related_name="user_rental")
    product=models.ForeignKey(Product, related_name="product_rental")
    rented_at_start=models.DateField()
    rented_at_end =models.DateField()
