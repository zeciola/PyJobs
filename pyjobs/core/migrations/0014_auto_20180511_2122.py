# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-11 21:22
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0013_profile_cellphone")]

    operations = [
        migrations.AlterField(
            model_name="jobapplication",
            name="job",
            field=models.ForeignKey(
                default="", on_delete=django.db.models.deletion.CASCADE, to="core.Job"
            ),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="user",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
