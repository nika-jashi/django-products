from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from apps.cart.models import Cart, CartItem
from apps.products.models import Product
from apps.products.utils import get_product_obj
from apps.cart.forms import CartAddForm, CartItemAddForm


class CartAddView(View):
    def post(self, request, *args, **kwargs):
        cart_form = CartAddForm(request.POST)
        cart_item_form = CartItemAddForm(request.POST)
        product_slug = request.kwargs['slug']
        product_instance = get_product_obj(slug=product_slug)
        account_instance = request.user

        if cart_form.is_valid() and cart_item_form.is_valid():
            cart_instance = Cart.objects.create(account=account_instance)
            CartItem.objects.create(cart=cart_instance, products=product_instance)
        return HttpResponse(request, status=201)
