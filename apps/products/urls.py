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
                                 ProductCategoryUpdateView)

app_name = "products"
urlpatterns = [
    path('', ProductListView.as_view(), name="list"),
    path('create/', ProductCreateView.as_view(), name="create"),
    path('detail/<slug:slug>/', ProductDetailView.as_view(), name="detail"),
    path('update/<slug:slug>/', ProductUpdateView.as_view(), name="update"),
    path('delete/<slug:slug>/', ProductDeleteView.as_view(), name="delete"),
    path('gallery/delete/<slug:slug>/<int:pk>/', ProductGalleryDelete.as_view(), name='gallery-delete'),

    # categories
    path('category/', ProductCategoryListView.as_view(), name="category-list"),
    path('category/create/', ProductCategoryCreateView.as_view(), name="category-create"),
    path('category/edit/<slug:slug>/', ProductCategoryUpdateView.as_view(), name="product-category-edit"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
