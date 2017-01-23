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
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('call_title', models.CharField(verbose_name='ФИО абонента', max_length=200)),
                ('call_face', models.CharField(choices=[('Физическое лицо', 'Физическое лицо'), ('Юридическое лицо', 'Юридическое лицо')], default='Физическое лицо', verbose_name='Абонент', max_length=30)),
                ('call_otvet', models.BooleanField(default=False, verbose_name='Требуется подготовить ответ?')),
                ('call_aim', models.CharField(choices=[('Оказание услуг по передаче электрической энергии', 'Оказание услуг по передаче электрической энергии'), ('Осуществление технологического присоединения', 'Осуществление технологического присоединения'), ('Коммерческий учет электрической энергии', 'Коммерческий учет электрической энергии'), ('Качество обслуживания потребителей', 'Качество обслуживания потребителей'), ('Техническое обслуживание электросетевых объектов', 'Техническое обслуживание электросетевых объектов')], default='Качество обслуживания потребителей', verbose_name='Цель звонка', max_length=100)),
                ('call_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('call_user_man', models.CharField(verbose_name='Логин оператора:', blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'call',
                'ordering': ['-call_date'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('user_otchestvo', models.CharField(verbose_name='Отчество', max_length=20)),
                ('user_filial', models.CharField(verbose_name='Филиал', max_length=100)),
                ('user_res', models.CharField(verbose_name='РЭС', max_length=100)),
                ('user_otdel', models.CharField(verbose_name='Отдел', max_length=100)),
                ('user_numphone', models.CharField(verbose_name='Номер телефона', max_length=20)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
