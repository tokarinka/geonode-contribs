# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-09 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geonode_logstash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='centralizedserver',
            name='local_ip',
            field=models.GenericIPAddressField(
                default='127.0.0.1', help_text=b'Local Server IP address.', protocol='ipv4'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='centralizedserver',
            name='host',
            field=models.CharField(help_text=b'Centralized Server IP address/Host name.', max_length=255),
        ),
    ]
