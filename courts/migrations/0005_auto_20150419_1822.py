# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0004_court_locality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='court_type',
            field=models.CharField(max_length=1, choices=[(b'wooden', b'wooden'), (b'polymer', b'polymer')]),
        ),
    ]
