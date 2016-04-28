# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_all_years', '0003_auto_20150621_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='location',
        ),
    ]
