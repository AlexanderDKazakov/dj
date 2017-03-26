# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='call_act',
            field=models.ForeignKey(to='call.ActOperator', default=140595769076384, verbose_name='Действие оператора:'),
        ),
        migrations.AddField(
            model_name='call',
            name='call_kontact',
            field=models.CharField(max_length=150, null=True, blank=True, verbose_name='Контакты для связи:'),
        ),
        migrations.AddField(
            model_name='call',
            name='call_user_man_filial',
            field=models.CharField(max_length=100, null=True, blank=True, verbose_name='Филиал оператора:'),
        ),
        migrations.AddField(
            model_name='call',
            name='call_user_man_otdel',
            field=models.CharField(max_length=100, null=True, blank=True, verbose_name='Отдел оператора'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_aim',
            field=models.ForeignKey(to='call.Aim_call', default=140595769076384, verbose_name='Цель звонка:'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время звонка:'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_entite',
            field=models.ForeignKey(to='call.legalEntity', default=140595769076384, verbose_name='Лицо:'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_otvet',
            field=models.BooleanField(default=False, verbose_name='Необходимо подготовить ответ:'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_title',
            field=models.CharField(max_length=200, verbose_name='ФИО абонента:'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_filial',
            field=models.ForeignKey(to='call.Filial', null=True, blank=True, verbose_name='Филиал'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_otdel',
            field=models.ForeignKey(to='call.Otdel', null=True, blank=True, verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_res',
            field=models.ForeignKey(to='call.Res', null=True, blank=True, verbose_name='РЭС'),
        ),
    ]
