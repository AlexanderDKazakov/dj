# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0006_auto_20170407_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('comment_text', models.TextField()),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.RemoveField(
            model_name='call',
            name='call_comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_call',
            field=models.ForeignKey(to='call.Call'),
        ),
    ]
