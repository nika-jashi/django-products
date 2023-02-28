from django.urls import path
from apps.products.views import (ProductCreateView,
                                 ProductCategoryCreateView,
                                 ProductDetailView,
                                 ProductUpdateView,
                                 ProductDeleteView)

app_name = "products"

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name="create"),
    path('read/<slug:slug>/', ProductDetailView.as_view(), name="read"),
    path('update/<slug:slug>/', ProductUpdateView.as_view(), name="update"),
    path('delete/<slug:slug>/', ProductDeleteView.as_view(), name="product-delete"),
    path('category/create/', ProductCategoryCreateView.as_view(), name="category-create"),
]
