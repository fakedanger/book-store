# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-23 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newbooks', '0019_auto_20170723_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.FileField(blank=True, default='/static/photo.jpg', null=True, upload_to='pic'),
        ),
    ]
