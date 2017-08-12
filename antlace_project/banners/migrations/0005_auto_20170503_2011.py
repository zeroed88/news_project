# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 20:11
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0004_auto_20170501_0740'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Тип страницы',
                'db_table': 'page_types',
                'verbose_name_plural': 'Типы страниц',
            },
        ),
        migrations.AddField(
            model_name='pageposition',
            name='layout',
            field=models.IntegerField(choices=[(1, 'горизонтально'), (2, 'вертикально')], default=1, verbose_name='Компоновка'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pageposition',
            name='index',
            field=models.IntegerField(blank=True, default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)], verbose_name='Индекс'),
        ),
        migrations.AlterField(
            model_name='pageposition',
            name='type',
            field=models.IntegerField(choices=[(1, 'main'), (2, 'detail')], verbose_name='Тип страницы'),
        ),
        migrations.AlterUniqueTogether(
            name='pageposition',
            unique_together=set([('layout', 'index', 'type')]),
        ),
    ]
