# Generated by Django 3.0.5 on 2020-05-07 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0063_auto_20200507_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='phone',
        ),
    ]