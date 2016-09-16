# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycity', '0007_otp_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercredit',
            name='lastweekcredit',
            field=models.DecimalField(default=0.0, editable=False, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='usercredit',
            name='lastweekrank',
            field=models.DecimalField(default=0, editable=False, max_digits=3, decimal_places=0),
        ),
        migrations.AddField(
            model_name='usercredit',
            name='thisweekcredit',
            field=models.DecimalField(default=0.0, editable=False, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='usercredit',
            name='thisweekrank',
            field=models.DecimalField(default=0, editable=False, max_digits=3, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='mycity',
            name='city',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
