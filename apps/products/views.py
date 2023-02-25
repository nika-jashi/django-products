from django.shortcuts import render, redirect
from django.views import View

from apps.products.forms import ProductForm, ProductGalleyForm, ProductCategoryForm
from apps.products.models import Product, ProductGallery


class ProductCreateView(View):
    def get(self, request, *args, **kwargs):
        product_form = ProductForm()
        product_gallery_form = ProductGalleyForm()
        context = {
            'product_form': product_form,
            'product_gallery_form': product_gallery_form,
        }
        return render(request, 'products/product_create.html', context)

    def post(self, request, *args, **kwargs):
        product_form = ProductForm(request.POST, request.FILES)
        product_gallery_form = ProductGalleyForm(request.POST, request.FILES)
        images_gallery = request.FILES.getlist('image')
        if product_form.is_valid() and product_gallery_form.is_valid():
            product_instance = Product.objects.create(**product_form.cleaned_data)
            for image in images_gallery:
                ProductGallery.objects.create(product=product_instance, image=image)
            return redirect('products:create')

        context = {
            'product_form': product_form,
            'product_gallery_form': product_gallery_form,
        }
        return render(request, 'products/product_create.html', context)


class ProductCategoryCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ProductCategoryForm()
        context = {
            'form': form,
        }
        return render(request, 'categories/category_create.html', context)

    def post(self, request, *args, **kwargs):
        form = ProductCategoryForm(request.POST, request.FILES)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('products:category-create')
        return render(request, 'categories/category_create.html', context)
