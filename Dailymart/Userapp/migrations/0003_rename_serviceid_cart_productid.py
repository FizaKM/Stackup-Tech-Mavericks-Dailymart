# Generated by Django 4.2 on 2023-05-25 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0002_remove_bookinguser_date_remove_bookinguser_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='serviceid',
            new_name='productid',
        ),
    ]
