# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='url',
            field=models.CharField(default='ee', max_length=200, verbose_name='url'),
            preserve_default=False,
        ),
    ]
