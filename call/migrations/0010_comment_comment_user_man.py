# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0009_comment_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_user_man',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Логин'),
        ),
    ]
