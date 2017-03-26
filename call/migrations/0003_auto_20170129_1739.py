# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0002_auto_20170127_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='call_aim_detail',
            field=models.CharField(blank=True, null=True, verbose_name='Детали звонка:', max_length=300),
        ),
        migrations.AddField(
            model_name='call',
            name='call_document',
            field=models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d/', verbose_name='Приложить документ:'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_act',
            field=models.ForeignKey(verbose_name='Действие оператора:', default=140402540759712, to='call.ActOperator'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_aim',
            field=models.ForeignKey(verbose_name='Цель звонка:', default=140402540759712, to='call.Aim_call'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_entite',
            field=models.ForeignKey(verbose_name='Лицо:', default=140402540759712, to='call.legalEntity'),
        ),
    ]
