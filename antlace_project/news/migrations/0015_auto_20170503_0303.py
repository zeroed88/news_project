# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20170503_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, help_text='Метатег description', max_length=300, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='category',
            name='keywords',
            field=models.CharField(blank=True, help_text='Метатег keywords', max_length=300),
        ),
    ]
