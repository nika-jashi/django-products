from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from apps.products.forms import ProductForm, ProductGalleyForm, ProductCategoryForm
from apps.products.models import Product, ProductGallery, ProductCategory
from apps.products.utils import get_product_obj, get_gallery_obj


class ProductListView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        context = {
            'products': products,
        }
        return render(request, 'products/product_list.html', context)


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
            return redirect('products:detail', product_slug)

        context = {
            'product_form': product_form,
            'product_gallery_form': product_gallery_form,
        }
        return render(request, 'products/product_create.html', context)


class ProductDetailView(View):

    def get(self, request, *args, **kwargs):
        product_slug = self.kwargs['slug']
        product = get_product_obj(slug=product_slug)
        gallery = get_gallery_obj(slug=product_slug)
        if product is None:
            return render(request, 'errors/404.html')
        context = {
            'product': product,
            'gallery': gallery,
        }

        return render(request, 'products/product_detail.html', context)


class ProductUpdateView(View):

    def get(self, request, *args, **kwargs):
        product_slug = self.kwargs['slug']

        product = get_product_obj(slug=product_slug)
        product_form = ProductForm(instance=product)
        product_gallery_form = ProductGalleyForm()
        product_gallery = ProductGallery.objects.filter(product__product_slug=product_slug)
        product_instance = Product.objects.get(product_slug=product_slug)
        if product is None:
            return render(request, 'errors/404.html')
        context = {
            'product_form': product_form,
            'product_gallery_form': product_gallery_form,
            'product_gallery': product_gallery,
            'product_instance': product_instance,
        }
        return render(request, 'products/product_update.html', context)

    def post(self, request, *args, **kwargs):
        product_slug = self.kwargs['slug']

        product = get_product_obj(slug=product_slug)

        product_form = ProductForm(request.POST, request.FILES, instance=product)
        product_gallery_form = ProductGalleyForm(request.POST, request.FILES)
        images_gallery = request.FILES.getlist('image')
        if product_form.is_valid() and product_gallery_form.is_valid():
            product_form.save()
            product = Product.objects.filter(product_slug=product_slug).first()

            for image in images_gallery:
                ProductGallery.objects.create(product=product, image=image)

            return redirect('products:detail', product_slug)

        context = {
            'product_form': product_form,
            'product_gallery_form': product_gallery_form,
        }

        return render(request, 'products/product_update.html', context)


class ProductGalleryDelete(View):
    def post(self, request, *args, **kwargs):
        gallery_image_pk = kwargs.get('pk')
        product_instance = kwargs.get('slug')
        image = get_object_or_404(ProductGallery, pk=gallery_image_pk)
        image.delete()
        return redirect('products:update', product_instance)


class ProductDeleteView(View):
    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug)
        product.delete()
        return redirect('products:create')


""" Category """


class ProductCategoryListView(View):
    def get(self, request, *args, **kwargs):
        categories = ProductCategory.objects.all()
        context = {
            'categories': categories,
        }
        return render(request, 'categories/category_list.html', context)


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
            return redirect('products:category-list')
        return render(request, 'categories/category_create.html', context)


class ProductCategoryUpdateView(View):
    def get(self, request, *args, **kwargs):
        category_slug = self.kwargs['slug']
        category = ProductCategory.objects.get(slug=category_slug)
        form = ProductCategoryForm(instance=category)

        context = {
            'form': form
        }

        return render(request, 'categories/category_update.html', context)

    def post(self, request, *args, **kwargs):
        category_slug = self.kwargs['slug']
        category = ProductCategory.objects.get(slug=category_slug)
        form = ProductCategoryForm(request.POST, request.FILES, instance=category)

        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('products:category-list')
        return render(request, 'categories/category_update.html', context)
