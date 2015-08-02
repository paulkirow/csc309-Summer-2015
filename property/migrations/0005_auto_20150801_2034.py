# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20150727_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='property',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
