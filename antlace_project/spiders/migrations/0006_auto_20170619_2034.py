# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-19 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiders', '0005_auto_20170619_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spider',
            name='name',
            field=models.CharField(help_text='ВНИМАНИЕ! ИСПОЛЬЗОВАТЬ ТОЛЬКО ЛАТИНСКИЕ БУКВЫ', max_length=50, unique=True, verbose_name='Имя паука'),
        ),
    ]
