# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-23 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('based_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
