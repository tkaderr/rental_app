from django.forms import ModelForm
from django import forms
from models import Product

CATEGORY_CHOICES = Product.objects.all()

class NewItemForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','description', 'image','tags','categories']
        labels = {
        'name': "Name of your item",
        'description': "Brief description of your item",
        'image': 'upload your image',
        'categories': 'Please select a category from the dropdown',
        'tags': 'Please list your tags. Comma separated.'
        }
        widgets = {
        'name': forms.TextInput(attrs={'placeholder': 'Name', 'class':'form-control'}),
        'tags': forms.Textarea(attrs={'id': 'tags', 'class':'form-control'}),
        'categories': forms.Select(choices=CATEGORY_CHOICES, attrs={'class':'form-control'}),
        'description': forms.Textarea(attrs={'class':'form-control'}),
        'image': forms.FileInput(attrs={'class':'form-control'}),

        }
