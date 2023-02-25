from django.urls import path
from apps.products.views import ProductCreateView,ProductCategoryCreateView

app_name = "products"

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name="create"),
    path('category/create/', ProductCategoryCreateView.as_view(), name="category-create"),
]
