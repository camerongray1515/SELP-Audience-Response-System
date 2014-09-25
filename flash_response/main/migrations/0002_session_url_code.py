# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='url_code',
            field=models.CharField(default='', max_length=5),
            preserve_default=True,
        ),
    ]
