# Generated by Django 3.0.5 on 2020-04-20 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0032_auto_20200420_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='rozmiar',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=3, null=True),
        ),
    ]
