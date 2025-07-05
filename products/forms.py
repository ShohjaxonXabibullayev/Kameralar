from django import forms
from .models import Cameralar

class ProductForm(forms.ModelForm):
    class Meta:
        model = Cameralar
        fields = ['make', 'resolution', 'zoom', 'price', 'image']


