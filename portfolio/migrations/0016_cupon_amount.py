# Generated by Django 3.0.5 on 2020-04-13 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_order_cupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='cupon',
            name='amount',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
