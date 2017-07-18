from django.forms import ModelForm
from django import forms
from .models import Product,Category

# CATEGORY_CHOICES = Category.objects.all()

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
        'name': forms.TextInput(attrs={'placeholder': 'Name', 'class':'form-control focusedInput'}),
        'tags': forms.Textarea(attrs={'id': 'tags', 'class':'form-control focusedInput', 'rows':'3'}),
        # 'categories': forms.Select(choices=CATEGORY_CHOICES, attrs={'class':'form-control focusedInput'}),
        'description': forms.Textarea(attrs={'class':'form-control focusedInput', 'rows':'3'}),
        'image': forms.FileInput(attrs={'class':'form-control focusedInput image'}),

        }
