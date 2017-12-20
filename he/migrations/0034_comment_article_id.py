# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 21:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('he', '0033_remove_comment_add_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='article_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='he.Consultation', verbose_name='文章ID'),
            preserve_default=False,
        ),
    ]