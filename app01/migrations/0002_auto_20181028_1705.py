# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='作者年龄'),
        ),
    ]
