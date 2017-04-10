# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0011_auto_20170408_0220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table_Num',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('table_name', models.CharField(verbose_name='Название стобца:', max_length=350, blank=True, null=True)),
                ('table_num', models.CharField(verbose_name='Номер столбца:', max_length=100, blank=True, null=True)),
                ('table_reason', models.ForeignKey(to='call.reason_otdel')),
            ],
            options={
                'db_table': 'table_num',
            },
        ),
        migrations.AlterField(
            model_name='call',
            name='call_act',
            field=models.ForeignKey(verbose_name='Действие оператора:', default=4467890256, to='call.ActOperator'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_aim',
            field=models.ForeignKey(verbose_name='Причина обращения:', blank=True, null=True, default=4467890256, to='call.reason_otdel'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_entite',
            field=models.ForeignKey(verbose_name='Лицо:', blank=True, default=4467890256, to='call.legalEntity'),
        ),
    ]
