# Generated by Django 3.0 on 2022-03-31 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='slug_field',
        ),
    ]
