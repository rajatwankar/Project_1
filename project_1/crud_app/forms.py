from django import forms
from .models import Laptop


class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'

        labels = {
            'l_id': 'LAPTOP_ID',
            'brand': 'BRAND',
            'model': 'MODEL',
            'ram': 'RAM',
            'memory': 'STORAGE',
            'price': 'PRICE'
        }

        widgets = {
            'l_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'ram': forms.NumberInput(attrs={'class': 'form-control'}),
            'memory': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'})
        }
