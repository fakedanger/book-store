# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-11 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newbooks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='bookisbn',
            field=models.IntegerField(blank=True, default='1'),
        ),
    ]