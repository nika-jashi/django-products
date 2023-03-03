import os

from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from taggit.managers import TaggableManager


def image_save(filename):
    return os.path.basename(filename)


class Product(models.Model):
    product_name = models.CharField(max_length=58)
    product_caption = models.TextField(max_length=128)
    product_thumbnail = models.ImageField(upload_to="products/thumbnails/%Y/%m/")
    product_tags = TaggableManager(related_name='tags')
    product_slug = models.SlugField(unique=True, max_length=58)
    date_created = models.DateTimeField(auto_now_add=True)
    product_views = models.IntegerField(default=0)
    # product_specification
    product_description = models.TextField(max_length=1024)

    product_price = models.DecimalField(max_digits=12, decimal_places=2)
    product_sale_percentage = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    product_sale_price = models.DecimalField(max_digits=12, decimal_places=2, default=0, null=True, blank=True)

    product_meta_name = models.CharField(max_length=58)
    product_meta_caption = models.TextField(max_length=128)

    product_category = TreeForeignKey('ProductCategory', related_name="products", on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        self.product_thumbnail.name = os.path.basename(self.product_thumbnail.name)
        self.product_meta_name = self.product_name
        self.product_meta_caption = self.product_caption
        if self.product_sale_percentage > 0:
            self.product_sale_price = self.product_price - (self.product_price * (self.product_sale_percentage / 100))
        else:
            self.product_sale_price = None
        super(Product, self).save(*args, **kwargs)


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/gallery/images/%Y/%m/")

    def __str__(self):
        return self.image

    def save(self, *args, **kwargs):
        self.image.name = os.path.basename(self.image.name)
        super(ProductGallery, self).save(*args, **kwargs)


class ProductCategory(MPTTModel):
    category_name = models.CharField(max_length=200)  # noqa
    category_slug = models.SlugField(unique=True)
    category_image = models.ImageField(upload_to='category_images/')
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('category_slug', 'parent',)
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name
