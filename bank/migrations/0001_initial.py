# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-26 19:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=1000)),
                ('type', models.CharField(choices=[('CCP', 'CCP'), ('LIVRET A', 'LIVRET A'), ('LDDS', 'LDDS'), ('CEL', 'CEL'), ('PEL', 'PEL')], max_length=2)),
                ('balance_offset', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date')),
                ('label', models.CharField(max_length=1000)),
                ('value', models.FloatField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.Account')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together=set([('identifier', 'type')]),
        ),
        migrations.AlterUniqueTogether(
            name='transaction',
            unique_together=set([('account', 'date', 'label', 'value')]),
        ),
    ]
