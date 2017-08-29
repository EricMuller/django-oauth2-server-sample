# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 11:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(default=None, max_length=2000, null=True)),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True)),
                ('rate', models.IntegerField(default=0)),
                ('favorite', models.BooleanField(default=False)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('public', models.BooleanField(default=False)),
                ('user_cre', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tag_user_cre', to=settings.AUTH_USER_MODEL)),
                ('user_upd', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tag_user_upd', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bookmark',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='bookmarks', to='bookmark.Tag'),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='user_cre',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bookmark_user_cre', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='user_upd',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bookmark_user_upd', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('name', 'user_cre')]),
        ),
    ]
