# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snacks_inventory', '0002_snackconsumer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snackconsumer',
            old_name='name',
            new_name='consumed_snack_name',
        ),
        migrations.RenameField(
            model_name='snackconsumer',
            old_name='user',
            new_name='consumed_user',
        ),
    ]
