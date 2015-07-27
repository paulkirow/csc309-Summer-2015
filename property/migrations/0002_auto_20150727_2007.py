# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 20, 7, 27, 793162, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.ForeignKey(default=3, to='property.Rating'),
            preserve_default=False,
        ),
    ]
