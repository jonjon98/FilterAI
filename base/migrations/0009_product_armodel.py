# Generated by Django 3.1.4 on 2022-10-01 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_review_createdat'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ARModel',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
