# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('phone', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('otp', models.CharField(max_length=4, editable=False)),
                ('verified', models.BooleanField(default=False, editable=False)),
            ],
        ),
    ]
