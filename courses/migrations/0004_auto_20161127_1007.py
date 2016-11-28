# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20161127_1001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='courses',
            new_name='course',
        ),
    ]
