# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 20:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billGenerator', '0008_auto_20170414_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='customers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billGenerator.Customer'),
        ),
        migrations.AlterField(
            model_name='course',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billGenerator.Trainer'),
        ),
    ]
