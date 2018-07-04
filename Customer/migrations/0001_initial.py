# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-04 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerCondition',
            fields=[
                ('condition_id', models.AutoField(primary_key=True, serialize=False)),
                ('condition_name', models.CharField(blank=True, max_length=50, null=True)),
                ('condition_explain', models.CharField(blank=True, max_length=1000, null=True)),
                ('is_used', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerSource',
            fields=[
                ('source_id', models.AutoField(primary_key=True, serialize=False)),
                ('source_name', models.CharField(blank=True, max_length=50, null=True)),
                ('is_used', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerType',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(blank=True, max_length=50, null=True)),
                ('is_used', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
