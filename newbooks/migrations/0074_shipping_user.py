# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-12 08:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newbooks', '0073_remove_shipping_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping',
            name='user',
            field=models.ForeignKey(default='jai', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
