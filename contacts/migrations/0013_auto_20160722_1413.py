# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0012_auto_20160322_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactfield',
            name='check_for_logs',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalcontactfield',
            name='check_for_logs',
            field=models.BooleanField(default=True),
        ),
    ]
