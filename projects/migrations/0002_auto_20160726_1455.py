# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-26 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='logo',
            field=models.ImageField(blank=True, upload_to='avatars_projects', verbose_name='Logo'),
        ),
    ]
