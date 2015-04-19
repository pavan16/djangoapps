# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0002_auto_20150419_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='court_type',
            field=models.CharField(max_length=1, choices=[(b'synthetic', b'synthetic'), (b'polymer', b'polymer')]),
        ),
        migrations.AlterField(
            model_name='court',
            name='open_court_type',
            field=models.CharField(max_length=1, choices=[(b'Open to air', b'Open to air'), (b'Closed', b'Closed')]),
        ),
        migrations.AlterField(
            model_name='court',
            name='shoes_type_allowed',
            field=models.CharField(max_length=1, choices=[(b'Marking shoes', b'Marking shoes'), (b'Non Marking shoes', b'Non Marking shoes')]),
        ),
    ]
