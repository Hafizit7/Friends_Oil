# Generated by Django 3.2.15 on 2022-09-19 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_order_order_complate_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='expire_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
