from django.forms import ModelForm, TextInput, NumberInput
from .models import Inventory


class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['increased_inventory', 'decreased_inventory']
        widgets = {
            'increased_inventory': NumberInput(attrs={
                'class': 'form-control',
                'style': 'width: 100px;',
                'placeholder': '입고량'
            }),
            'decreased_inventory': NumberInput(attrs={
                'class': 'form-control',
                'style': 'width: 100px;',
                'placeholder': '출고량'
            })
        }
