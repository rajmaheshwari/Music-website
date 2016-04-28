# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import movie_all_years.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('location', models.FileField(upload_to=movie_all_years.models.loc)),
            ],
        ),
    ]
