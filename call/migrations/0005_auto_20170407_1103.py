# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0004_auto_20170403_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='call_comment',
            field=models.CharField(verbose_name='Комментарий:', max_length=500, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_act',
            field=models.ForeignKey(verbose_name='Действие оператора:', default=4311103568, to='call.ActOperator'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_aim',
            field=models.ForeignKey(verbose_name='Причина обращения:', blank=True, null=True, default=4311103568, to='call.reason_otdel'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_entite',
            field=models.ForeignKey(verbose_name='Лицо:', blank=True, default=4311103568, to='call.legalEntity'),
        ),
    ]
