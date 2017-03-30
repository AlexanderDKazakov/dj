# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActOperator',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('actoperator_name', models.CharField(max_length=200, null=True, blank=True, verbose_name='Действия оператора')),
            ],
            options={
                'db_table': 'actoperator',
            },
        ),
        migrations.CreateModel(
            name='Aim_call',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('ac_name', models.CharField(max_length=200, null=True, blank=True, verbose_name='Цель звонка')),
            ],
            options={
                'db_table': 'aim_call',
            },
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('call_title', models.CharField(max_length=200, verbose_name='ФИО абонента:')),
                ('call_document', models.FileField(null=True, blank=True, verbose_name='Приложить документ:', upload_to='documents/%Y/%m/%d/')),
                ('call_otvet', models.BooleanField(default=False, verbose_name='Необходимо подготовить ответ:')),
                ('call_aim_detail', models.CharField(max_length=300, null=True, blank=True, verbose_name='Детали звонка:')),
                ('call_kontact', models.CharField(max_length=150, null=True, blank=True, verbose_name='Контакты для связи:')),
                ('call_date_start', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время звонка:')),
                ('call_user_man', models.CharField(max_length=50, null=True, blank=True, verbose_name='Логин оператора:')),
                ('call_user_man_filial', models.CharField(max_length=100, null=True, blank=True, verbose_name='Филиал оператора:')),
                ('call_user_man_otdel', models.CharField(max_length=100, null=True, blank=True, verbose_name='Отдел оператора')),
                ('call_act', models.ForeignKey(default=10914368, verbose_name='Действие оператора:', to='call.ActOperator')),
            ],
            options={
                'ordering': ['-call_date_start'],
                'db_table': 'call',
            },
        ),
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('filial_name', models.CharField(max_length=200, null=True, blank=True, verbose_name='Филиал')),
            ],
            options={
                'db_table': 'filial',
            },
        ),
        migrations.CreateModel(
            name='legalEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('le_type', models.CharField(max_length=200, null=True, blank=True, verbose_name='Тип лица (Физический/Юридический)')),
            ],
            options={
                'db_table': 'abonent',
            },
        ),
        migrations.CreateModel(
            name='Otdel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('otdel_name', models.CharField(max_length=200, null=True, blank=True, verbose_name='Отдел')),
            ],
            options={
                'db_table': 'otdel',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('user_otchestvo', models.CharField(max_length=20, verbose_name='Отчество')),
                ('user_numphone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('user_filial', models.ForeignKey(null=True, blank=True, verbose_name='Филиал', to='call.Filial')),
                ('user_otdel', models.ForeignKey(null=True, blank=True, verbose_name='Отдел', to='call.Otdel')),
            ],
        ),
        migrations.CreateModel(
            name='reason_call_operator_CA',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('rc_name', models.CharField(max_length=200, null=True, blank=True, verbose_name='Причина обращения:')),
            ],
            options={
                'db_table': 'reason_call_operator_CA',
            },
        ),
        migrations.CreateModel(
            name='reason_call_operator_CPES',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('rc_name', models.CharField(max_length=200, null=True, blank=True, verbose_name='Причина обращения:')),
            ],
            options={
                'db_table': 'reason_call_operator_CPES',
            },
        ),
        migrations.CreateModel(
            name='reason_call_operator_dispetcher',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('rc_name', models.CharField(max_length=200, null=True, blank=True, verbose_name='Причина обращения:')),
            ],
            options={
                'db_table': 'reason_call_operator_dispetcher',
            },
        ),
        migrations.CreateModel(
            name='reason_call_operator_PTO',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('rc_name', models.CharField(max_length=200, null=True, blank=True, verbose_name='Причина обращения:')),
            ],
            options={
                'db_table': 'reason_call_operator_PTO',
            },
        ),
        migrations.CreateModel(
            name='reason_call_operator_secretar',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('rc_name', models.CharField(max_length=200, null=True, blank=True, verbose_name='Причина обращения:')),
            ],
            options={
                'db_table': 'reason_call_operator_secretar',
            },
        ),
        migrations.CreateModel(
            name='reason_otdel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('rc_name', models.CharField(max_length=200, null=True, blank=True, verbose_name='Причина обращения:')),
                ('otdel_id', models.ForeignKey(to='call.Otdel')),
            ],
            options={
                'db_table': 'reason_otdel',
            },
        ),
        migrations.CreateModel(
            name='Res',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('res_name', models.CharField(max_length=200, null=True, blank=True, verbose_name='РЭС')),
            ],
            options={
                'db_table': 'res',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='user_res',
            field=models.ForeignKey(null=True, blank=True, verbose_name='РЭС', to='call.Res'),
        ),
        migrations.AddField(
            model_name='call',
            name='call_aim',
            field=models.ForeignKey(default=10914368, null=True, blank=True, verbose_name='Цель звонка:', to='call.reason_call_operator_dispetcher'),
        ),
        migrations.AddField(
            model_name='call',
            name='call_entite',
            field=models.ForeignKey(default=10914368, blank=True, verbose_name='Лицо:', to='call.legalEntity'),
        ),
    ]
