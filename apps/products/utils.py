from apps.products.models import Product, ProductGallery


def get_product_obj(slug):
    product_instance = Product.objects.filter(product_slug=slug).first()
    return product_instance


def get_gallery_obj(slug):
    gallery_instance = ProductGallery.objects.filter(product__product_slug=slug).first()
    return gallery_instance
