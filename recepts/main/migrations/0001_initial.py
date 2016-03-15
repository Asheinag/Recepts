# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Ингредиент', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='InList',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Recept',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Рецепт', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='VariationIng',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('new_name', models.CharField(max_length=200)),
                ('ing', models.ForeignKey(to='main.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='inlist',
            name='recept',
            field=models.ForeignKey(to='main.Recept'),
        ),
    ]
