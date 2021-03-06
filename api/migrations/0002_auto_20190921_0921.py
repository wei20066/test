# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-09-21 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('macaddress', models.CharField(max_length=12)),
                ('type', models.IntegerField()),
                ('authnumber', models.IntegerField()),
                ('recordnumber', models.IntegerField()),
                ('workmode', models.IntegerField()),
                ('onlinestatus', models.IntegerField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='device',
            unique_together=set([('number', 'macaddress')]),
        ),
    ]
