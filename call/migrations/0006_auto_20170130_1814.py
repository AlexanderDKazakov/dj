# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0005_auto_20170130_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='call_act',
            field=models.ForeignKey(verbose_name='Действие оператора:', to='call.ActOperator', default=140545947830944),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_aim',
            field=models.ForeignKey(verbose_name='Цель звонка:', to='call.Aim_call', default=140545947830944),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_entite',
            field=models.ForeignKey(verbose_name='Лицо:', to='call.legalEntity', default=140545947830944),
        ),
    ]
