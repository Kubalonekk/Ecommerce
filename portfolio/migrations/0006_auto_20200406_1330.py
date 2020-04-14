# Generated by Django 3.0.5 on 2020-04-06 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_item_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orderder',
            new_name='ordered',
        ),
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
