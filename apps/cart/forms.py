from django import forms
from apps.cart.models import Cart, CartItem


class CartAddForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = []


class CartItemAddForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = []
