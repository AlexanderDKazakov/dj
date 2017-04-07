# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('call', '0008_auto_20170408_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_user',
            field=models.OneToOneField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
