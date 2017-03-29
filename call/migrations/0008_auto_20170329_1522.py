# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0007_auto_20170328_0009'),
    ]

    operations = [
        migrations.CreateModel(
            name='reason_call_operator_CA',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('rc_name', models.CharField(blank=True, null=True, max_length=200, verbose_name='Причина обращения:')),
            ],
            options={
                'db_table': 'reason_call_operator_CA',
            },
        ),
        migrations.CreateModel(
            name='reason_call_operator_CPES',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('rc_name', models.CharField(blank=True, null=True, max_length=200, verbose_name='Причина обращения:')),
            ],
            options={
                'db_table': 'reason_call_operator_CPES',
            },
        ),
        migrations.CreateModel(
            name='reason_call_operator_dispetcher',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('rc_name', models.CharField(blank=True, null=True, max_length=200, verbose_name='Причина обращения:')),
            ],
            options={
                'db_table': 'reason_call_operator_dispetcher',
            },
        ),
        migrations.CreateModel(
            name='reason_call_operator_PTO',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('rc_name', models.CharField(blank=True, null=True, max_length=200, verbose_name='Причина обращения:')),
            ],
            options={
                'db_table': 'reason_call_operator_PTO',
            },
        ),
        migrations.CreateModel(
            name='reason_call_operator_secretar',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('rc_name', models.CharField(blank=True, null=True, max_length=200, verbose_name='Причина обращения:')),
            ],
            options={
                'db_table': 'reason_call_operator_secretar',
            },
        ),
        migrations.AlterField(
            model_name='call',
            name='call_aim',
            field=models.ForeignKey(verbose_name='Цель звонка:', blank=True, default=10914368, to='call.Aim_call', null=True),
        ),
    ]
