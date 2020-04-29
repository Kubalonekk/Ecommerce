# Generated by Django 3.0.5 on 2020-04-21 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0037_itemwariant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemwariant',
            name='klucz',
        ),
        migrations.RemoveField(
            model_name='itemwariant',
            name='wartosc',
        ),
        migrations.AddField(
            model_name='itemwariant',
            name='ilosc',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='itemwariant',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.Item'),
        ),
        migrations.AlterField(
            model_name='itemwariant',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
