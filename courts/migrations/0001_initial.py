# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('latitude', models.IntegerField(default=0)),
                ('longitude', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=200)),
                ('court_type', models.CharField(max_length=200)),
                ('shoes_type_allowed', models.CharField(max_length=200)),
                ('open_court_type', models.CharField(max_length=200)),
            ],
        ),
    ]
