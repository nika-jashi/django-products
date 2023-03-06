from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.cart.views import CartAddView

app_name = "cart"
urlpatterns = [
    path('add/<slug:slug>/', CartAddView.as_view(), name="cart-add"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
