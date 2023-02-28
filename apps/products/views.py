from django.shortcuts import render, redirect, get_object_or_404
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
            product_form.save()
            product_slug = product_form.cleaned_data['product_slug']
            product = Product.objects.filter(product_slug=product_slug).first()
            for image in images_gallery:
                ProductGallery.objects.create(product=product, image=image)
            return redirect('products:create')

        context = {
            'product_form': product_form,
            'product_gallery_form': product_gallery_form,
        }
        return render(request, 'products/product_create.html', context)


class ProductDetailView(View):
    def get_product_obj(self, slug):
        product_instance = Product.objects.filter(product_slug=slug).first()
        return product_instance

    def get_gallery_obj(self, slug):
        gallery_instance = ProductGallery.objects.filter(product__product_slug=slug).first()
        return gallery_instance

    def get(self, request, *args, **kwargs):
        product_slug = self.kwargs['slug']
        product = self.get_product_obj(slug=product_slug)
        gallery = self.get_gallery_obj(slug=product_slug)
        if product is None:
            return render(request, 'errors/404.html')
        context = {
            'product': product,
            'gallery': gallery,
        }

        return render(request, 'products/product_read.html', context)


class ProductUpdateView(View):
    def get_product_obj(self, slug):
        product_instance = Product.objects.filter(product_slug=slug).first()
        return product_instance

    def get_gallery_obj(self, slug):
        gallery_instance = ProductGallery.objects.filter(product__product_slug=slug).first()
        return gallery_instance

    def get(self, request, *args, **kwargs):
        product_slug = self.kwargs['slug']

        product = self.get_product_obj(slug=product_slug)
        gallery = self.get_gallery_obj(slug=product_slug)
        product_form = ProductForm(instance=product)
        product_gallery_form = ProductGalleyForm(instance=gallery)
        context = {
            'product_form': product_form,
            'product_gallery_form': product_gallery_form,
        }
        return render(request, 'products/product_update.html', context)

    def post(self, request, *args, **kwargs):
        product_slug = self.kwargs['slug']

        product = self.get_product_obj(slug=product_slug)
        gallery = self.get_gallery_obj(slug=product_slug)

        product_form = ProductForm(request.POST, request.FILES, instance=product)
        product_gallery_form = ProductGalleyForm(request.POST, request.FILES, instance=gallery)
        images_gallery = request.FILES.getlist('image')

        if product_form.is_valid() and product_gallery_form.is_valid():
            product_form.save()
            product = Product.objects.filter(product_slug=product_slug).first()

            for image in images_gallery:
                ProductGallery.objects.update(product=product, image=image)

            return redirect('products:read', product_slug)

        context = {
            'product_form': product_form,
            'product_gallery_form': product_gallery_form,
        }

        return render(request, 'products/product_update.html', context)


class ProductDeleteView(View):
    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug)
        product.delete()
        return redirect('products:create')


""" Category """


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
