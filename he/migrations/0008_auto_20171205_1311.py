# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 13:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('he', '0007_auto_20171201_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=10, unique=True, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='public',
            name='addr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='he.City', to_field='name'),
        ),
    ]