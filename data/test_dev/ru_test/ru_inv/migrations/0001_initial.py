# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Manufacturer', models.CharField(max_length=250)),
                ('Serial', models.IntegerField()),
                ('Comments', models.CharField(max_length=1000)),
            ],
        ),
    ]
