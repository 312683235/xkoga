# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('he', '0020_remove_consultation_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='images',
            field=models.ImageField(upload_to='image/consultation/%Y/%m', verbose_name='产品图片'),
        ),
    ]
