# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_commentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='upvote_num',
            field=models.IntegerField(default=0),
        ),
    ]