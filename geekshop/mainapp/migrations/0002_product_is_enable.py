# Generated by Django 2.2 on 2020-04-10 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_enable',
            field=models.BooleanField(default=False, verbose_name='Доступен'),
        ),
    ]