# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-23 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_states', '0011_auto_20180315_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflowstateaction',
            name='label',
            field=models.CharField(help_text='A simple identifier for this action.', max_length=255, verbose_name='Label'),
        ),
    ]
