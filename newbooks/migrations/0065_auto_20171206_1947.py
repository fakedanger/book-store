# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-06 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newbooks', '0064_resetpass_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpass',
            name='num',
            field=models.IntegerField(default=9),
        ),
    ]
