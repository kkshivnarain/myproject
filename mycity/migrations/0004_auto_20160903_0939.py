# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycity', '0003_auto_20160903_0927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citylist',
            old_name='nelatitude',
            new_name='ne_latitude',
        ),
        migrations.RenameField(
            model_name='citylist',
            old_name='nelongitude',
            new_name='ne_longitude',
        ),
        migrations.RenameField(
            model_name='citylist',
            old_name='swlatitude',
            new_name='sw_latitude',
        ),
        migrations.RenameField(
            model_name='citylist',
            old_name='swlongitude',
            new_name='sw_longitude',
        ),
    ]
