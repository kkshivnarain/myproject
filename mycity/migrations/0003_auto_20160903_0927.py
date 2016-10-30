# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycity', '0002_mycity'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=50)),
                ('nelatitude', models.DecimalField(max_digits=10, decimal_places=7)),
                ('nelongitude', models.DecimalField(max_digits=10, decimal_places=7)),
                ('swlatitude', models.DecimalField(max_digits=10, decimal_places=7)),
                ('swlongitude', models.DecimalField(max_digits=10, decimal_places=7)),
            ],
        ),
        migrations.AlterField(
            model_name='mycity',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='mycity',
            name='latitude',
            field=models.DecimalField(max_digits=10, decimal_places=7),
        ),
        migrations.AlterField(
            model_name='mycity',
            name='longitude',
            field=models.DecimalField(max_digits=10, decimal_places=7),
        ),
    ]
