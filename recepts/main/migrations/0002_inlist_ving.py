# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inlist',
            name='ving',
            field=models.ForeignKey(to='main.VariationIng', default=None),
        ),
    ]
