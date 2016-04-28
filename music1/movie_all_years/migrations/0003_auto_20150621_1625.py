# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_all_years', '0002_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='song',
        ),
        migrations.AddField(
            model_name='song',
            name='movie',
            field=models.ForeignKey(to='movie_all_years.Movie', null=True),
        ),
    ]
