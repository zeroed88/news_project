# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_delete_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='article',
            name='cover_image',
            field=models.ImageField(upload_to='covers_images', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='ЧПУ'),
        ),
        migrations.AlterField(
            model_name='article',
            name='source_url',
            field=models.URLField(verbose_name='Источник статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text='Будет использоваться в роутинге', unique=True, verbose_name='ЧПУ'),
        ),
    ]
