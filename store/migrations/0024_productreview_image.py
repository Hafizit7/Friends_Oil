# Generated by Django 3.2.15 on 2022-10-22 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_productreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ReviewImg'),
        ),
    ]
