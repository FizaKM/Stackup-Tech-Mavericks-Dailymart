# Generated by Django 4.2 on 2023-05-26 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0003_alter_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]