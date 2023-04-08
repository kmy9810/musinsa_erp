from django.forms import ModelForm, TextInput, Textarea, Select
from .models import Product
from inventory.models import Inventory


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'code', 'name', 'description', 'price', 'size']
        categorys = (
            ('h', '후드티'),
            ('j', '청바지'),
        )
        sizes = (
            ('S', 'Small'),
            ('M', 'Medium'),
            ('L', 'Large'),
            ('F', 'Free'),
        )
        widgets = {
            'code': TextInput(attrs={
                'class': "form-control",
                'style': 'resize: none; height: 50px;',
                'placeholder': 'Code'
            }),
            'description': Textarea(attrs={
                "class": "form-control",
                'style': 'resize: none; height: 100px;',
                'placeholder': 'Description'
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 80px; margin-bottom: 5px;',
                'placeholder': 'Price'
            }),
            'name': TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 150px; margin-bottom: 5px',
                'placeholder': 'Name'
            }),
            'category': Select(choices=categorys),
            'size': Select(choices=sizes)
        }

