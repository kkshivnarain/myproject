# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycity', '0004_auto_20160903_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=20)),
                ('category_desc', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='mycity',
            name='category',
            field=models.CharField(max_length=20),
        ),
    ]
