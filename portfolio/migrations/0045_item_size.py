# Generated by Django 3.0.5 on 2020-04-23 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0044_auto_20200423_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.BooleanField(default=False),
        ),
    ]
