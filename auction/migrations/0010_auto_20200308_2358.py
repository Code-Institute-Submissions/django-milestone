# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-08 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0009_auto_20200308_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='user_bid',
            field=models.IntegerField(blank=True, default=''),
        ),
    ]
