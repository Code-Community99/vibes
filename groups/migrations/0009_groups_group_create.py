# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-03-13 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0008_auto_20200312_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='group_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
