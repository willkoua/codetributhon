# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-22 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=50, verbose_name="Nom d'utilisateur")),
                ('email', models.EmailField(max_length=254, verbose_name='Courriel')),
                ('url', models.URLField(max_length=255, verbose_name='URL')),
                ('description', models.TextField(verbose_name='Description du projet')),
                ('enabled', models.BooleanField(default=False, verbose_name='Valider')),
            ],
            options={
                'verbose_name_plural': 'Contributions',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nom')),
                ('enabled', models.BooleanField(default=False, verbose_name='Activer')),
                ('url', models.URLField(blank=True, max_length=255, verbose_name='URL')),
            ],
            options={
                'verbose_name_plural': 'Organizations',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nom du projet')),
                ('description', models.TextField(verbose_name='Description du projet')),
                ('enabled', models.BooleanField(default=False, verbose_name='Activer')),
                ('logo', models.ImageField(blank=True, upload_to='media/avatars_projects', verbose_name='Logo')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='projects.Organization', verbose_name='Organization')),
            ],
            options={
                'verbose_name_plural': 'Projets',
            },
        ),
        migrations.AddField(
            model_name='contribution',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributions', to='projects.Project', verbose_name='Project'),
        ),
    ]
