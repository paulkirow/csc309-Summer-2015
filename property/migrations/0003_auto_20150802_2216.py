# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20150802_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image_name',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
