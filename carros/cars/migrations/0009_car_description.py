# Generated by Django 5.2 on 2025-06-25 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_rename_car_value_carinventory_cars_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
