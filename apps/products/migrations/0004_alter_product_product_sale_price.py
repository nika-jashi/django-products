# Generated by Django 4.1.7 on 2023-02-28 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_product_sale_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
    ]
