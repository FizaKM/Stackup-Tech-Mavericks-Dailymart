# Generated by Django 4.2 on 2023-05-26 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0006_rename_grandtotal_cart_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
