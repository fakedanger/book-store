# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-13 11:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newbooks', '0045_auto_20170813_1712'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='returnbook',
            unique_together=set([]),
        ),
    ]
