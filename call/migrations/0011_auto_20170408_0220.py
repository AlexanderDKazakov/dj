# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0010_comment_comment_user_man'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_user_man',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
    ]
