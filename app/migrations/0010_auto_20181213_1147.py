# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-13 11:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20181213_1144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainshow',
            old_name='proudctid1',
            new_name='prouductid1',
        ),
        migrations.RenameField(
            model_name='mainshow',
            old_name='proudctid2',
            new_name='prouductid2',
        ),
        migrations.RenameField(
            model_name='mainshow',
            old_name='proudctid3',
            new_name='prouductid3',
        ),
    ]
