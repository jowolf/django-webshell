# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('webshell', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='script',
            options={'ordering': ['-modified']},
        ),
        migrations.AddField(
            model_name='script',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 6, 20, 22, 19, 388782), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='script',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 6, 20, 22, 28, 940640), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='script',
            name='notes',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
