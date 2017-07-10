# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20170706_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='college_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
