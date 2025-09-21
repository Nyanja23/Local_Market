from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    accept_terms = forms.BooleanField(label="Accept terms and conditions", required=True)

    class Meta:
        model = Product
        fields = ('name','price','description')
    
