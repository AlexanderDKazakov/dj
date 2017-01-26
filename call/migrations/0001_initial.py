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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('actoperator_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Действия оператора')),
            ],
            options={
                'db_table': 'actoperator',
            },
        ),
        migrations.CreateModel(
            name='Aim_call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('ac_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Цель звонка')),
            ],
            options={
                'db_table': 'aim_call',
            },
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('call_title', models.CharField(max_length=200, verbose_name='ФИО абонента')),
                ('call_otvet', models.BooleanField(verbose_name='Требуется подготовить ответ?', default=False)),
                ('call_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('call_user_man', models.CharField(blank=True, max_length=50, null=True, verbose_name='Логин оператора:')),
                ('call_aim', models.ForeignKey(verbose_name='Цель звонка', default=10771520, to='call.Aim_call')),
            ],
            options={
                'db_table': 'call',
                'ordering': ['-call_date'],
            },
        ),
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('filial_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Филиал')),
            ],
            options={
                'db_table': 'filial',
            },
        ),
        migrations.CreateModel(
            name='legalEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('le_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Тип лица (Физический/Юридический)')),
            ],
            options={
                'db_table': 'abonent',
            },
        ),
        migrations.CreateModel(
            name='Otdel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('otdel_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Отдел')),
            ],
            options={
                'db_table': 'otdel',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('user_otchestvo', models.CharField(max_length=20, verbose_name='Отчество')),
                ('user_numphone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('user_filial', models.ForeignKey(verbose_name='Филиал', null=True, to='call.Filial')),
                ('user_otdel', models.ForeignKey(verbose_name='Отдел', null=True, to='call.Otdel')),
            ],
        ),
        migrations.CreateModel(
            name='Res',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('res_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='РЭС')),
            ],
            options={
                'db_table': 'res',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='user_res',
            field=models.ForeignKey(verbose_name='РЭС', null=True, to='call.Res'),
        ),
        migrations.AddField(
            model_name='call',
            name='call_entite',
            field=models.ForeignKey(verbose_name='Лицо', default=10771520, to='call.legalEntity'),
        ),
    ]
