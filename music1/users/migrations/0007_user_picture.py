# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(default=b'static/users/images/user_pictures/Unknown-3.png', upload_to=b'static/users/images/user_pictures/'),
        ),
    ]
