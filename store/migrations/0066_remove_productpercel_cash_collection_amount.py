# Generated by Django 3.2.15 on 2022-11-23 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0065_remove_productpercel_tracking_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpercel',
            name='cash_collection_amount',
        ),
    ]
