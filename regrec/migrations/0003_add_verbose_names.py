# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 03:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regrec', '0002_use_datetimes_for_start_and_finish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'event', 'verbose_name_plural': 'events'},
        ),
        migrations.AlterModelOptions(
            name='race',
            options={'verbose_name': 'race', 'verbose_name_plural': 'races'},
        ),
        migrations.AlterModelOptions(
            name='run',
            options={'verbose_name': 'run', 'verbose_name_plural': 'runs'},
        ),
        migrations.AlterModelOptions(
            name='yacht',
            options={'verbose_name': 'yacht', 'verbose_name_plural': 'yachts'},
        ),
        migrations.AlterField(
            model_name='race',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='races', to='regrec.Event'),
        ),
        migrations.AlterField(
            model_name='run',
            name='comment',
            field=models.TextField(verbose_name='note'),
        ),
        migrations.AlterField(
            model_name='run',
            name='finish_time',
            field=models.DateTimeField(verbose_name='finish time'),
        ),
        migrations.AlterField(
            model_name='run',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='runs', to='regrec.Race', verbose_name='race'),
        ),
        migrations.AlterField(
            model_name='run',
            name='start_time',
            field=models.DateTimeField(verbose_name='start time'),
        ),
        migrations.AlterField(
            model_name='run',
            name='yacht',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='runs', to='regrec.Yacht', verbose_name='yacht'),
        ),
        migrations.AlterField(
            model_name='yacht',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yachts', to='regrec.Event', verbose_name='event'),
        ),
        migrations.AlterField(
            model_name='yacht',
            name='model',
            field=models.CharField(max_length=128, verbose_name='model'),
        ),
        migrations.AlterField(
            model_name='yacht',
            name='name',
            field=models.CharField(max_length=128, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='yacht',
            name='skipper',
            field=models.CharField(max_length=128, verbose_name='skipper'),
        ),
        migrations.AlterField(
            model_name='yacht',
            name='yardstick',
            field=models.PositiveSmallIntegerField(verbose_name='yardstick'),
        ),
    ]
