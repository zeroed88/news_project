# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20170501_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='news.Category', verbose_name='Категория'),
        ),
    ]
