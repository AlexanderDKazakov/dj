# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0002_auto_20170331_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='call_date_end',
            field=models.DateTimeField(verbose_name='Время закрытия звонка:', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_date_start',
            field=models.DateTimeField(verbose_name='Время открытия звонка:', default=django.utils.timezone.now),
        ),
    ]
