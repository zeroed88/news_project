# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 10:32
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pageposition',
            options={'verbose_name': 'Позиция', 'verbose_name_plural': 'Позиции на страницах'},
        ),
        migrations.AlterField(
            model_name='pageposition',
            name='number',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AlterModelTable(
            name='pageposition',
            table='positions',
        ),
    ]
