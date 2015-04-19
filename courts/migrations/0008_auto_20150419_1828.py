# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0007_auto_20150419_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='court',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]
