# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snacks_inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SnackConsumer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consumed_quantity', models.IntegerField(default=0)),
                ('date_consumed', models.DateTimeField(null=True, verbose_name=b'date consumed')),
                ('name', models.ForeignKey(to='snacks_inventory.Snack')),
                ('user', models.ForeignKey(to='snacks_inventory.User')),
            ],
        ),
    ]
