# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0005_auto_20170407_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='call_act',
            field=models.ForeignKey(verbose_name='Действие оператора:', to='call.ActOperator', default=10914368),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_aim',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Причина обращения:', to='call.reason_otdel', default=10914368),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_entite',
            field=models.ForeignKey(blank=True, verbose_name='Лицо:', to='call.legalEntity', default=10914368),
        ),
    ]
