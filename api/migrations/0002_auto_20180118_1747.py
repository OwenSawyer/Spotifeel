# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('shortened', models.TextField(primary_key=True, serialize=False)),
                ('original', models.TextField()),
            ],
            options={
                'db_table': 'bitly',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('user', models.TextField()),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'table1',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
