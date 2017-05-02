# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=225)
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=225)
    description=models.TextField(max_length=225)
    image=models.ImageField(upload_to='images',blank=True)
    categories=models.ManyToManyField(Category, related_name="products_categories", blank=True)
    tags=models.ManyToManyField(Tag, related_name="products_tags", blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    seller=models.ForeignKey(User, related_name="products")
    rental=models.ManyToManyField(User, through="Rental")
    def __str__(self):
        return self.name

class Rental(models.Model):
    renter=models.ForeignKey(User, related_name="user_rental")
    product=models.ForeignKey(Product, related_name="product_rental")
    rented_at_start=models.DateField()
    rented_at_end =models.DateField()
