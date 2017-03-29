# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0006_auto_20170130_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='call_act',
            field=models.ForeignKey(verbose_name='Действие оператора:', default=10914368, to='call.ActOperator'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_aim',
            field=models.ForeignKey(verbose_name='Цель звонка:', default=10914368, to='call.Aim_call'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_entite',
            field=models.ForeignKey(verbose_name='Лицо:', default=10914368, blank=True, to='call.legalEntity'),
        ),
    ]
