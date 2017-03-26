# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0004_auto_20170130_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='call_act',
            field=models.ForeignKey(to='call.ActOperator', default=140625483864736, verbose_name='Действие оператора:'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_aim',
            field=models.ForeignKey(to='call.Aim_call', default=140625483864736, verbose_name='Цель звонка:'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_entite',
            field=models.ForeignKey(to='call.legalEntity', default=140625483864736, verbose_name='Лицо:'),
        ),
    ]
