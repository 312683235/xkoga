# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 19:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('he', '0030_auto_20171217_1939'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Consul',
            new_name='consultation',
        ),
    ]
