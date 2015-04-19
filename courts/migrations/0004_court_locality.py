# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0003_auto_20150419_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='court',
            name='locality',
            field=models.CharField(default=b'SOME STRING', max_length=200),
        ),
    ]
