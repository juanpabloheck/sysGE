# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sedes', '0007_coordinador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinador',
            name='titulo',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sede',
            name='nombre',
            field=models.CharField(unique=True, max_length=100, verbose_name=b'Paraje'),
            preserve_default=True,
        ),
    ]
