# Generated by Django 3.0.5 on 2020-04-20 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0026_auto_20200415_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='dostepna_ilosc',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
