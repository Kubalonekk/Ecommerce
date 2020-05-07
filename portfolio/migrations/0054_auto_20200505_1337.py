# Generated by Django 3.0.5 on 2020-05-05 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0053_ocena_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='ocena',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='ocena',
            name='ocena',
            field=models.IntegerField(choices=[('', 'Oceń produkt'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]