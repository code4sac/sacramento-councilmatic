# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2020-07-23 04:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('councilmatic_core', '0044_bill_restrict_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityBill',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('councilmatic_core.bill',),
        ),
    ]
