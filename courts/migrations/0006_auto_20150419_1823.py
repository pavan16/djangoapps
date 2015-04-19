# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0005_auto_20150419_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='shoes_type_allowed',
            field=models.CharField(max_length=1, choices=[(b'Marking shoes', b'Marking shoes'), (b'Non Marking shoes', b'Non Marking shoes'), (b'Both', b'Both')]),
        ),
    ]
