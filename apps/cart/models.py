from django.db import models
from apps.products.models import Product
from apps.accounts.models import CustomAccount


class Cart(models.Model):
    account = models.ForeignKey(to=CustomAccount, on_delete=models.CASCADE)


class CartItem(models.Model):
    products = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
