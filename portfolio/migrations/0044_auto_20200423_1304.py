# Generated by Django 3.0.5 on 2020-04-23 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0043_auto_20200422_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='rozmiar',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
