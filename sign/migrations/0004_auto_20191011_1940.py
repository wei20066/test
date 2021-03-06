# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-10-11 11:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0003_pictures'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='pictures',
            name='title',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='pic',
            field=models.ImageField(blank=True, upload_to='img/', verbose_name='图片'),
        ),
    ]
