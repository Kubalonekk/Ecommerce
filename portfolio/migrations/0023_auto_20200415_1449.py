# Generated by Django 3.0.5 on 2020-04-15 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_refund_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.Cupon'),
        ),
    ]
