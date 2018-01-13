# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 13:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import person.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Not interested to tell')], default='M', max_length=1)),
                ('mobile_number', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('I', 'Individual'), ('C', 'Company')], default='I', max_length=20)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('pic', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=person.models.profile_pic_location, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
