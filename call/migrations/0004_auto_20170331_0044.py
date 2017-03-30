# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0003_auto_20170331_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='call_date_end',
            field=models.DateTimeField(verbose_name='Время закрытия звонка:'),
        ),
    ]
