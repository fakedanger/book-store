# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-14 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newbooks', '0009_cart_orderno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Purchasedate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]