# Generated by Django 3.2.15 on 2022-11-05 06:26

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0044_auto_20221027_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='MissionAndsVision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_information', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_information', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Returns_Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_information', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAndDelivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_information', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='TermsAndConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_information', ckeditor.fields.RichTextField()),
            ],
        ),
    ]