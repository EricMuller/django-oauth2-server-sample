# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 13:11
from __future__ import unicode_literals

from django.db import migrations, models
import oauth2_provider.validators


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_application', '0006_application_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='description',
            field=models.TextField(blank=True, validators=[oauth2_provider.validators.validate_uris]),
        ),
        migrations.AlterField(
            model_name='application',
            name='url',
            field=models.CharField(max_length=200, verbose_name='description'),
        ),
    ]
