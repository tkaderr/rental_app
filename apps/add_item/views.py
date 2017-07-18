# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import NewItemForm
from .models import Product, User, Tag, Category

from django.shortcuts import render, redirect

# Create your views here.
def add_item(request):
    if request.method == 'POST':
        # print "post"
        copied_post = request.POST.copy()
        tags= request.POST['tags'].split(',')
        obj_list=[]    #list of tag objects
        new_tags=[]    #list of tags that don't exist yet
        for i in tags:
            if i and Tag.objects.filter(name=i.strip()):
                obj_list.append(Tag.objects.get(name=i.strip()))
            elif i:
                new_tags.append(i.strip())
        copied_post['tags']=obj_list
        copied_post['categories']=[Category.objects.get(id=request.POST['categories'])]
        # print copied_post['categories']
        form = NewItemForm(copied_post, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.get(id=request.session['current_user_id'])
            instance = Product(name=data['name'],description=data['description'],image=request.FILES['image'], seller=user)
            # print tags
            instance.save()
            for i in new_tags:
                if not Tag.objects.filter(name=i):
                    new_tag=Tag.objects.create(name=i)
                    obj_list.append(new_tag)
            for i in obj_list:
                instance.tags.add(i)
            instance.categories.add(data['categories'][0])
            instance.save()
            return redirect('/user')
        else:
            # print form.errors
            return render(request, 'add_item/form.html', {'form': form, 'products': Product.objects.all(), 'tags': Tag.objects.all(), 'user' : User.objects.get(id=request.session['current_user_id'])})
    else:
        form = NewItemForm()

    return render(request, 'add_item/form.html', {'form': form, 'products': Product.objects.all(), 'tags': Tag.objects.all(), 'user' : User.objects.get(id=request.session['current_user_id'])})

# def thanks(request):
#     context= {
#     'user':request.user,
#     'products': Product.objects.all()
#     }
#     return render(request, 'add_item/thanks.html', context)
