# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('original_quantity', models.IntegerField(default=0)),
                ('remaining_quantity', models.IntegerField(default=0, null=True)),
                ('date_consumed', models.DateTimeField(null=True, verbose_name=b'date consumed')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=200)),
                ('user_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='snack',
            name='user',
            field=models.ForeignKey(to='snacks_inventory.User'),
        ),
    ]
