# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20161111_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReqSubscriptionPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.FloatField(unique=True)),
                ('free_price', models.FloatField()),
                ('premium_price', models.FloatField()),
                ('super_premium_price', models.FloatField()),
                ('free_discount', models.FloatField()),
                ('premium_discount', models.FloatField()),
                ('super_premium_discount', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_heading', models.CharField(max_length=100)),
                ('req_detail', models.CharField(max_length=2000)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CompanyModel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
