# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 10:27
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('code', models.TextField()),
                ('layout', models.IntegerField(choices=[(1, 'horizontal'), (2, 'vertical')])),
            ],
            options={
                'db_table': 'banners',
                'verbose_name_plural': 'Баннеры',
                'verbose_name': 'Баннеры',
            },
        ),
        migrations.CreateModel(
            name='PagePosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'horizontal'), (2, 'vertical')])),
                ('number', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(12)])),
            ],
        ),
        migrations.CreateModel(
            name='Views',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('meta', models.TextField(blank=True)),
                ('banner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='banners.Banner')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'views',
                'verbose_name_plural': 'Просмотры',
                'verbose_name': 'Просмотр',
            },
        ),
        migrations.AddField(
            model_name='banner',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banners.PagePosition'),
        ),
    ]
