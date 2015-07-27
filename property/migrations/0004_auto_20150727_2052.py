# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20150727_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 20, 52, 29, 631572, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.ForeignKey(default=3, to='property.Rating'),
            preserve_default=False,
        ),
    ]
