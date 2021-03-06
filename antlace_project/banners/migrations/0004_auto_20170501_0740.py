# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 07:40
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0003_auto_20170430_1105'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Views',
            new_name='View',
        ),
        migrations.AlterField(
            model_name='banner',
            name='layout',
            field=models.IntegerField(choices=[(1, 'горизонтально'), (2, 'вертикально')], verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='pageposition',
            name='index',
            field=models.IntegerField(default=1, unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='Индекс'),
        ),
        migrations.AlterField(
            model_name='pageposition',
            name='type',
            field=models.IntegerField(choices=[(1, 'горизонтально'), (2, 'вертикально')], verbose_name='Тип позиции'),
        ),
    ]
