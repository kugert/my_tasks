# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cocktail_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Compose',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingredient_value', models.PositiveIntegerField()),
                ('cocktails', models.ForeignKey(to='cocktail.Cocktail')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingredient_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('measure_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='compose',
            name='ingredients',
            field=models.ForeignKey(to='cocktail.Ingredient'),
        ),
        migrations.AddField(
            model_name='compose',
            name='measures',
            field=models.ForeignKey(to='cocktail.Measure'),
        ),
    ]
