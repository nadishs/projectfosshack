# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Not available', max_length=300)),
                ('text', models.TextField(default='Not available')),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Not available', max_length=300)),
                ('description', models.TextField(default='Not available')),
                ('url', models.URLField(default='Not available')),
                ('urlToImage', models.URLField(default='Not available')),
                ('publishedAt', models.CharField(default='Not available', max_length=100)),
            ],
        ),
    ]
