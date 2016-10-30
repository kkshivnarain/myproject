# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=10)),
                ('latitude', models.DecimalField(max_digits=9, decimal_places=6)),
                ('longitude', models.DecimalField(max_digits=9, decimal_places=6)),
                ('timestamp', models.DecimalField(max_digits=13, decimal_places=3)),
                ('city', models.CharField(max_length=50, blank=True)),
            ],
        ),
    ]
