# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-10 14:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kucun', '0002_backstock_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backstock',
            name='product_id',
        ),
    ]