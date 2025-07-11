# Generated by Django 5.2 on 2025-04-15 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('factory_year', models.IntegerField(blank=True, max_length=4, null=True)),
                ('model_year', models.IntegerField(blank=True, max_length=4, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('mileage', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
