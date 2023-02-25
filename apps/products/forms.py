from django import forms
from django.forms import ClearableFileInput

from apps.products.models import Product, ProductCategory, ProductGallery


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_caption', 'product_tags', 'product_description', 'product_price',
                  'product_slug', 'product_thumbnail', 'product_category', 'product_sale_percentage']

        widgets = {
            'product_thumbnail': ClearableFileInput(attrs={'multiple': False}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_category'].queryset = ProductCategory.objects.all()


class ProductGalleyForm(forms.ModelForm):
    class Meta:
        model = ProductGallery
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={'multiple': True}),
        }


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['category_name', 'category_slug', 'parent', 'category_image']
        widgets = {
            'category_image': ClearableFileInput(attrs={'multiple': False}),
        }
