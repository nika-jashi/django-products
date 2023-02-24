# Generated by Django 4.1.7 on 2023-02-24 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_sale',
            new_name='product_sale_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_meta_description',
        ),
        migrations.AddField(
            model_name='product',
            name='product_meta_caption',
            field=models.TextField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_caption',
            field=models.TextField(max_length=128),
        ),
    ]