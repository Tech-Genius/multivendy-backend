# Generated by Django 4.1.2 on 2022-12-12 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_rename_afeatured_image1_products_featured_image1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='detail',
        ),
    ]
