# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-12 16:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='设备名称')),
                ('attribute', models.TextField(verbose_name='属性')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='负责人')),
            ],
            options={
                'verbose_name': '设备管理',
                'verbose_name_plural': '设备管理',
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='区域名称')),
            ],
            options={
                'verbose_name': '设备区域',
                'verbose_name_plural': '设备区域',
            },
        ),
        migrations.AddField(
            model_name='equipment',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Zone', verbose_name='所属区域'),
        ),
    ]
