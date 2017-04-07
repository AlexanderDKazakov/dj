# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0007_auto_20170408_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время комментария:'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(verbose_name='Текст комментария:'),
        ),
    ]
