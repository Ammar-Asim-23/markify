from django import forms

from .models import Product, Advertisement

class AddProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('name', 'price', 'description',)

        