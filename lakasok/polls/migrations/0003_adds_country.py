# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_adds_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='adds',
            name='country',
            field=models.CharField(default='', max_length=200),
            preserve_default=True,
        ),
    ]
