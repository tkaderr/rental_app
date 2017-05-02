from django.forms import ModelForm
from django import forms
from models import Product

class NewItemForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','description', 'image']
        labels = {
        'name': "Name of your item",
        'description': "Brief description of your item",
        'image': 'upload your image'
        }
        widgets = {
        'name': forms.TextInput(attrs={'placeholder': 'Name'}),
        }
