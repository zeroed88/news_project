# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('description', models.TextField()),
                ('body', models.TextField()),
                ('source_url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cover_image', models.ImageField(upload_to='covers_images')),
            ],
            options={
                'verbose_name_plural': 'Статьи',
                'db_table': 'filials',
                'ordering': ['-created_at'],
                'verbose_name': 'Статья',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('slug', models.SlugField(help_text='Будет использоваться в роутинге', unique=True)),
            ],
            options={
                'verbose_name_plural': 'Категории',
                'db_table': 'categories',
                'verbose_name': 'Категория',
            },
        ),
    ]
