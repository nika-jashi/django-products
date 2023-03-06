from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('apps.products.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('cart/', include('apps.cart.urls')),
]
