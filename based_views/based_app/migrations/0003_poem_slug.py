# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-23 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('based_app', '0002_poem_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='slug',
            field=models.SlugField(default='', max_length=100),
        ),
    ]
