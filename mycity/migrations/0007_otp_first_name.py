<<<<<<< HEAD
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycity', '0006_auto_20160908_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='first_name',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
=======
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycity', '0006_auto_20160908_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='first_name',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
>>>>>>> 01375511faeadc5485caff722ece85c561f19e85
