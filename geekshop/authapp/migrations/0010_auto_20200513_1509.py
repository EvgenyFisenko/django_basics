# Generated by Django 2.2.10 on 2020-05-13 12:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0009_auto_20200510_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 15, 12, 9, 0, 259267, tzinfo=utc)),
        ),
    ]
