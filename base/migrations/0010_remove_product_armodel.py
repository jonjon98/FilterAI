# Generated by Django 3.1.4 on 2022-10-01 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_product_armodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ARModel',
        ),
    ]
