# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-29 19:08
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='MapNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geometry', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('created_dttm', models.DateTimeField(auto_now_add=True)),
                ('modified_dttm', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.Map')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
