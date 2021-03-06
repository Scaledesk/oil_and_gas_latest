# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_companymodel_is_req_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basicpremiumfield',
            options={'verbose_name': 'Basic Premium Field', 'verbose_name_plural': 'Basic Premium Fields'},
        ),
        migrations.AlterModelOptions(
            name='brochure',
            options={'verbose_name': 'Brochure', 'verbose_name_plural': 'Brochures'},
        ),
        migrations.AlterModelOptions(
            name='claimcompanyrequest',
            options={'verbose_name': 'Company Claim Requiest', 'verbose_name_plural': 'Company Claim Requests'},
        ),
        migrations.AlterModelOptions(
            name='companymodel',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='freefield',
            options={'verbose_name': 'Free Field', 'verbose_name_plural': 'Free Fields'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Gallery', 'verbose_name_plural': 'Galleries'},
        ),
        migrations.AlterModelOptions(
            name='keyalliance',
            options={'verbose_name': 'Key Alliance', 'verbose_name_plural': 'Key Alliances'},
        ),
        migrations.AlterModelOptions(
            name='keyclient',
            options={'verbose_name': 'Key Client', 'verbose_name_plural': 'Key Clients'},
        ),
        migrations.AlterModelOptions(
            name='reqsubscriptionplan',
            options={'verbose_name': 'Request Subscription Plans', 'verbose_name_plural': 'Request Subscription Plans'},
        ),
        migrations.AlterModelOptions(
            name='subscriptionplan',
            options={'verbose_name': 'Subscription Plan', 'verbose_name_plural': 'Subscription Plans'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'User Profile', 'verbose_name_plural': 'User Profiles'},
        ),
        migrations.AlterModelOptions(
            name='videolink',
            options={'verbose_name': 'Video Link', 'verbose_name_plural': 'Video Links'},
        ),
        migrations.AlterField(
            model_name='reqsubscriptionplan',
            name='plan_name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1),
        ),
    ]
