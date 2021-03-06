# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 23:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('he', '0012_auto_20171205_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='项目分类')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '项目分类',
                'verbose_name_plural': '项目分类',
            },
        ),
        migrations.CreateModel(
            name='Consultation',
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
                ('time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='he.Category', verbose_name='分类')),
            ],
            options={
                'verbose_name': '创新咨询',
                'verbose_name_plural': '创新咨询',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('img', models.ImageField(upload_to='image/server/%Y/%m', verbose_name='图片')),
                ('time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('desc', models.TextField(max_length=500, verbose_name='项目介绍')),
                ('images', models.ImageField(upload_to='image/server/%Y/%m', verbose_name='产品图片')),
                ('pro_data', models.TextField(max_length=500, verbose_name='数据')),
                ('pro_capital', models.TextField(max_length=500, verbose_name='资本')),
                ('pro_pro', models.TextField(max_length=500, verbose_name='产品')),
                ('pro_patent', models.TextField(max_length=500, verbose_name='专利')),
                ('pro_qua', models.TextField(max_length=500, verbose_name='资质')),
                ('pro_other', models.TextField(max_length=500, verbose_name='其他')),
                ('member', models.TextField(max_length=200, verbose_name='成员')),
                ('state', models.CharField(choices=[(1, '运营'), (2, '停运')], max_length=5, verbose_name='运营状态')),
                ('look_num', models.IntegerField(verbose_name='观看数量')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='he.Category', verbose_name='分类')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='he.City', verbose_name='城市')),
            ],
            options={
                'verbose_name': '服务文章',
                'verbose_name_plural': '服务文章',
            },
        ),
        migrations.RenameModel(
            old_name='Categroy',
            new_name='NaviCategroy',
        ),
        migrations.RemoveField(
            model_name='content',
            name='categroy',
        ),
    ]
