# Generated by Django 4.2 on 2023-05-26 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0005_rename_total_cart_grandtotal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='grandtotal',
            new_name='total',
        ),
    ]
