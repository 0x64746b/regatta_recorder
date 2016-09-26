# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 22:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regrec', '0004_make_short_notes_optional'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='start time')),
                ('finish_time', models.DateTimeField(verbose_name='finish time')),
                ('note', models.CharField(blank=True, max_length=128, null=True, verbose_name='note')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='times', to='regrec.Race', verbose_name='race')),
                ('yacht', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='times', to='regrec.Yacht', verbose_name='yacht')),
            ],
            options={
                'verbose_name': 'time',
                'verbose_name_plural': 'times',
            },
        ),
        migrations.RemoveField(
            model_name='run',
            name='race',
        ),
        migrations.RemoveField(
            model_name='run',
            name='yacht',
        ),
        migrations.DeleteModel(
            name='Run',
        ),
    ]