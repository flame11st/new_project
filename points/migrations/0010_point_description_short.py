# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-03 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0009_auto_20170917_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='description_short',
            field=models.CharField(default='', max_length=300),
        ),
    ]
