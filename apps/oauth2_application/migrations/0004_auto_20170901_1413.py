# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_application', '0003_application_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='description',
            field=models.CharField(max_length=200, verbose_name='description'),
        ),
    ]
