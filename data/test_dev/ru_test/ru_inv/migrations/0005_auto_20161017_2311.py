# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 23:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ru_inv', '0004_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='item',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
