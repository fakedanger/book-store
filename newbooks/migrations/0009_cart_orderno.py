# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-14 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newbooks', '0008_auto_20170714_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='orderno',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
