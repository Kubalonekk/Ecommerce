# Generated by Django 3.0.5 on 2020-05-07 11:12

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0059_auto_20200507_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
