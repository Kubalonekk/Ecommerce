# Generated by Django 3.0.5 on 2020-04-10 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_auto_20200410_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='userr',
            new_name='user',
        ),
    ]
