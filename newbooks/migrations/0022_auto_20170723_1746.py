# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-23 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newbooks', '0021_auto_20170723_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.FileField(blank=True, default='/pic/photo.jpg', null=True, upload_to='pic'),
        ),
    ]
