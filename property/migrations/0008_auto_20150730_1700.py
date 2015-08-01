# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20150730_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='text',
            new_name='rated',
        ),
    ]
