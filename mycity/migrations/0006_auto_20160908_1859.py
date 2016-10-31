<<<<<<< HEAD
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycity', '0005_auto_20160903_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCredit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.CharField(max_length=10)),
                ('credit', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='UserCreditDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.CharField(max_length=10)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='citylist',
            name='ne_latitude',
            field=models.DecimalField(max_digits=10, decimal_places=7, blank=True),
        ),
        migrations.AlterField(
            model_name='citylist',
            name='ne_longitude',
            field=models.DecimalField(max_digits=10, decimal_places=7, blank=True),
        ),
        migrations.AlterField(
            model_name='citylist',
            name='sw_latitude',
            field=models.DecimalField(max_digits=10, decimal_places=7, blank=True),
        ),
        migrations.AlterField(
            model_name='citylist',
            name='sw_longitude',
            field=models.DecimalField(max_digits=10, decimal_places=7, blank=True),
        ),
    ]
=======
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycity', '0005_auto_20160903_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCredit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.CharField(max_length=10)),
                ('credit', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='UserCreditDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.CharField(max_length=10)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='citylist',
            name='ne_latitude',
            field=models.DecimalField(max_digits=10, decimal_places=7, blank=True),
        ),
        migrations.AlterField(
            model_name='citylist',
            name='ne_longitude',
            field=models.DecimalField(max_digits=10, decimal_places=7, blank=True),
        ),
        migrations.AlterField(
            model_name='citylist',
            name='sw_latitude',
            field=models.DecimalField(max_digits=10, decimal_places=7, blank=True),
        ),
        migrations.AlterField(
            model_name='citylist',
            name='sw_longitude',
            field=models.DecimalField(max_digits=10, decimal_places=7, blank=True),
        ),
    ]
>>>>>>> 01375511faeadc5485caff722ece85c561f19e85
