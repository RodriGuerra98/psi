# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-29 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_workflow_delete_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflow',
            name='delete_id',
            field=models.CharField(default='', max_length=40),
        ),
    ]
