# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 20:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billGenerator', '0006_auto_20170414_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='dateFirstAid',
            field=models.DateField(default=datetime.datetime(2017, 4, 14, 20, 31, 25, 610202, tzinfo=utc), verbose_name='latest first aid certificate'),
        ),
    ]
