# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20150727_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
    ]
