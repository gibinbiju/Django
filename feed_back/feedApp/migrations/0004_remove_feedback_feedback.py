# Generated by Django 2.2.5 on 2019-11-10 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedApp', '0003_auto_20191110_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='feedback',
        ),
    ]
