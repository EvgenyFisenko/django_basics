# Generated by Django 2.2.10 on 2020-05-09 15:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20200509_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 11, 15, 37, 25, 609013, tzinfo=utc)),
        ),
    ]