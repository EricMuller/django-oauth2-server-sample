# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_application', '0005_auto_20170901_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='description',
            field=models.CharField(default='desc', max_length=200, verbose_name='description'),
            preserve_default=False,
        ),
    ]
