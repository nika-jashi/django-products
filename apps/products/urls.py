from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.products.views import (ProductCreateView,
                                 ProductCategoryCreateView,
                                 ProductDetailView,
                                 ProductUpdateView,
                                 ProductDeleteView,
                                 ProductGalleryDelete,
                                 ProductListView,
                                 ProductCategoryListView,
                                 ProductCategoryUpdateView,
                                 CategoryDeleteView)
from django.contrib.auth.decorators import login_required as lr


app_name = "products"
urlpatterns = [
    path('', ProductListView.as_view(), name="list"),
    path('create/', lr(ProductCreateView.as_view()), name="create"),
    path('detail/<slug:slug>/', ProductDetailView.as_view(), name="detail"),
    path('update/<slug:slug>/', lr(ProductUpdateView.as_view()), name="update"),
    path('delete/<slug:slug>/', lr(ProductDeleteView.as_view()), name="delete"),
    path('gallery/delete/<slug:slug>/<int:pk>/', lr(ProductGalleryDelete.as_view()), name='gallery-delete'),

    # categories
    path('categories/', ProductCategoryListView.as_view(), name="category-list"),
    path('categories/create/', ProductCategoryCreateView.as_view(), name="category-create"),
    path('categories/edit/<slug:slug>/', ProductCategoryUpdateView.as_view(), name="product-category-edit"),
    path('categories/delete/<slug:slug>/', CategoryDeleteView.as_view(), name="product-category-delete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
