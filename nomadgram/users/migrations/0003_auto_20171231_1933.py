# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-31 10:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171231_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(related_name='_user_followers_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='followings',
            field=models.ManyToManyField(related_name='_user_followings_+', to=settings.AUTH_USER_MODEL),
        ),
    ]