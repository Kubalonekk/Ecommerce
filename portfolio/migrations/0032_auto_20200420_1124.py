# Generated by Django 3.0.5 on 2020-04-20 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0031_auto_20200420_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='rozmiar',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='rozmiar',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=3, null=True),
        ),
    ]
