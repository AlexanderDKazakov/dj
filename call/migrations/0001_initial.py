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
                ('actoperator_name', models.CharField(max_length=200, verbose_name='Действия оператора', blank=True, null=True)),
            ],
            options={
                'db_table': 'actoperator',
            },
        ),
        migrations.CreateModel(
            name='Aim_call',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('ac_name', models.CharField(max_length=200, verbose_name='Цель звонка', blank=True, null=True)),
            ],
            options={
                'db_table': 'aim_call',
            },
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('call_title', models.CharField(max_length=200, verbose_name='Заявитель:')),
                ('call_document', models.FileField(verbose_name='Приложить документ:', blank=True, null=True, upload_to='documents/%Y/%m/%d/')),
                ('call_otvet', models.BooleanField(default=False, verbose_name='Необходимо подготовить ответ:')),
                ('call_aim_detail', models.CharField(max_length=300, verbose_name='Детали звонка:', blank=True, null=True)),
                ('call_kontact', models.CharField(max_length=150, verbose_name='Контакты для связи:', blank=True, null=True)),
                ('call_date_start', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время открытия звонка:')),
                ('call_date_end', models.DateTimeField(verbose_name='Время закрытия звонка:', blank=True, null=True)),
                ('call_user_man', models.CharField(max_length=50, verbose_name='Логин оператора:', blank=True, null=True)),
                ('call_user_man_filial', models.CharField(max_length=100, verbose_name='Филиал оператора:', blank=True, null=True)),
                ('call_user_man_otdel', models.CharField(max_length=100, verbose_name='Отдел оператора', blank=True, null=True)),
                ('call_act', models.ForeignKey(to='call.ActOperator', default=10914368, verbose_name='Действие оператора:')),
            ],
            options={
                'db_table': 'call',
                'ordering': ['-call_date_start'],
            },
        ),
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('filial_name', models.CharField(max_length=200, verbose_name='Филиал', blank=True, null=True)),
            ],
            options={
                'db_table': 'filial',
            },
        ),
        migrations.CreateModel(
            name='legalEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('le_type', models.CharField(max_length=200, verbose_name='Тип лица (Физический/Юридический)', blank=True, null=True)),
            ],
            options={
                'db_table': 'abonent',
            },
        ),
        migrations.CreateModel(
            name='Otdel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('otdel_name', models.CharField(max_length=200, verbose_name='Отдел', blank=True, null=True)),
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
                ('user_filial', models.ForeignKey(to='call.Filial', null=True, blank=True, verbose_name='Филиал')),
                ('user_otdel', models.ForeignKey(to='call.Otdel', null=True, blank=True, verbose_name='Отдел')),
            ],
        ),
        migrations.CreateModel(
            name='reason_otdel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('rc_name', models.CharField(max_length=200, verbose_name='Причина обращения:', blank=True, null=True)),
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
                ('res_name', models.CharField(max_length=200, verbose_name='РЭС', blank=True, null=True)),
            ],
            options={
                'db_table': 'res',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='user_res',
            field=models.ForeignKey(to='call.Res', null=True, blank=True, verbose_name='РЭС'),
        ),
        migrations.AddField(
            model_name='call',
            name='call_aim',
            field=models.ForeignKey(to='call.reason_otdel', null=True, blank=True, default=10914368, verbose_name='Причина обращения:'),
        ),
        migrations.AddField(
            model_name='call',
            name='call_entite',
            field=models.ForeignKey(to='call.legalEntity', blank=True, default=10914368, verbose_name='Лицо:'),
        ),
    ]
