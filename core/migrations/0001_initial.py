# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 17:48
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicPremiumField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, default=None, upload_to='company_logo/')),
                ('registration_no', models.CharField(blank=True, default=None, max_length=12)),
                ('no_of_emp', models.IntegerField(blank=True, default=None)),
                ('sale_volume', models.CharField(blank=True, default=None, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Brochure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brochure', models.FileField(upload_to='company_brouchure/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certi_name', models.CharField(max_length=100)),
                ('certi_description', models.CharField(blank=True, default=None, max_length=200)),
                ('certi_doc', models.FileField(blank=True, default=None, upload_to='company_certification/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClaimCompanyRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150, unique=True)),
                ('company_email', models.CharField(max_length=150)),
                ('company_phone_no', models.CharField(max_length=10)),
                ('ad_reference', models.CharField(choices=[('B', 'Blog'), ('W', 'Website'), ('A', 'Advertisement'), ('S', 'Social Media'), ('O', 'Other')], default='A', max_length=1)),
                ('is_claimed', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('sub_begin_date', models.DateField(default=datetime.date.today)),
                ('sub_end_date', models.DateField(default=datetime.date.today)),
                ('is_sub_active', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FreeField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, default=None, max_length=120)),
                ('city', models.CharField(blank=True, default=None, max_length=30)),
                ('pin', models.CharField(blank=True, default=None, max_length=6)),
                ('website', models.CharField(blank=True, default=None, max_length=200)),
                ('year_founded', models.CharField(blank=True, default=None, max_length=200)),
                ('about', models.CharField(blank=True, default=None, max_length=100)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.CompanyModel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='company_gallery/')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CompanyModel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KeyAlliance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='core.CompanyModel')),
                ('key_alliance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alliance', to='core.CompanyModel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KeyClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_client', models.CharField(max_length=150)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CompanyModel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_type', models.CharField(blank=True, default=None, max_length=30)),
                ('location', models.CharField(blank=True, default=None, max_length=200)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CompanyModel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, default=None, max_length=200)),
                ('twitter', models.CharField(blank=True, default=None, max_length=200)),
                ('linkedin', models.CharField(blank=True, default=None, max_length=200)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.CompanyModel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_type', models.CharField(choices=[('F', 'Free'), ('P', 'Premium'), ('S', 'Super Premium')], max_length=4, unique=True)),
                ('cost_per_month', models.FloatField()),
                ('discount', models.FloatField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=5)),
                ('dob', models.DateField()),
                ('user_phone_no', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_link', models.CharField(max_length=200)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CompanyModel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='companymodel',
            name='sub_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.SubscriptionPlan'),
        ),
        migrations.AddField(
            model_name='claimcompanyrequest',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CompanyModel'),
        ),
        migrations.AddField(
            model_name='claimcompanyrequest',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='certification',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CompanyModel'),
        ),
        migrations.AddField(
            model_name='brochure',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CompanyModel'),
        ),
        migrations.AddField(
            model_name='basicpremiumfield',
            name='company',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.CompanyModel'),
        ),
    ]