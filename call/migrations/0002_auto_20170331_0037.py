# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='reason_call_operator_CA',
        ),
        migrations.DeleteModel(
            name='reason_call_operator_CPES',
        ),
        migrations.DeleteModel(
            name='reason_call_operator_PTO',
        ),
        migrations.DeleteModel(
            name='reason_call_operator_secretar',
        ),
        migrations.AlterField(
            model_name='call',
            name='call_aim',
            field=models.ForeignKey(null=True, blank=True, default=10914368, verbose_name='Причина обращения:', to='call.reason_otdel'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_title',
            field=models.CharField(max_length=200, verbose_name='Заявитель:'),
        ),
        migrations.DeleteModel(
            name='reason_call_operator_dispetcher',
        ),
    ]
