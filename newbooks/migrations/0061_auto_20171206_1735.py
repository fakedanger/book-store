# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-06 12:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newbooks', '0060_auto_20171206_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resetpass',
            old_name='id',
            new_name='serialid',
        ),
    ]
