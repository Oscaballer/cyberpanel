# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-07 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='installedPackages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extensionName', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PHP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phpVers', models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='installedpackages',
            name='phpVers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managePHP.PHP'),
        ),
    ]
