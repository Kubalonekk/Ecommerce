# Generated by Django 3.0.5 on 2020-04-13 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_cupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.Cupon'),
        ),
    ]
