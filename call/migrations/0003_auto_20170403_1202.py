# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0002_auto_20170402_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='call_act',
            field=models.ForeignKey(verbose_name='Действие оператора:', default=4431259728, to='call.ActOperator'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_aim',
            field=models.ForeignKey(verbose_name='Причина обращения:', blank=True, null=True, default=4431259728, to='call.reason_otdel'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_entite',
            field=models.ForeignKey(verbose_name='Лицо:', blank=True, default=4431259728, to='call.legalEntity'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_user_man_filial',
            field=models.ForeignKey(verbose_name='Филиал оператора:', blank=True, null=True, to='call.Filial'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_user_man_otdel',
            field=models.ForeignKey(verbose_name='Отдел оператора', blank=True, null=True, to='call.Otdel'),
        ),
    ]
