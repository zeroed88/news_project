# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-19 19:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('spiders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spider',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Создано'),
        ),
    ]
