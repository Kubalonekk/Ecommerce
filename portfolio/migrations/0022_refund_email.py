# Generated by Django 3.0.5 on 2020-04-14 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0021_refund'),
    ]

    operations = [
        migrations.AddField(
            model_name='refund',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
