# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# Generated by Django 2.2.6 on 2019-10-31 15:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("issues", "0009_revision_optional_phab_references"),
    ]

    operations = [
        migrations.AlterField(
            model_name="revision",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]