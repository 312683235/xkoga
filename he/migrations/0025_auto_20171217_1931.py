# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 19:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('he', '0024_auto_20171217_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('tag', models.CharField(max_length=20, verbose_name='关键字')),
                ('company', models.CharField(max_length=20, verbose_name='公司')),
                ('desc', models.TextField(max_length=300, verbose_name='导读')),
                ('content', models.TextField(max_length=8000, verbose_name='内容')),
                ('follow', models.IntegerField(verbose_name='关注数量')),
                ('share', models.IntegerField(verbose_name='分享数量')),
                ('comment_num', models.IntegerField(verbose_name='评论数量')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数量')),
                ('images', models.ImageField(upload_to='image/consultation/%Y/%m', verbose_name='产品图片')),
                ('is_banner', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='he.Category', verbose_name='分类')),
            ],
            options={
                'verbose_name': '咨询文章',
                'verbose_name_plural': '咨询文章',
            },
        ),
        migrations.RemoveField(
            model_name='consultation',
            name='category',
        ),
        migrations.RemoveField(
            model_name='consultation',
            name='city_id',
        ),
        migrations.DeleteModel(
            name='Consultation',
        ),
    ]
