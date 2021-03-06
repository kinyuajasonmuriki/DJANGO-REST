# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-25 08:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20170323_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='consumers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountno', models.IntegerField(unique=True)),
                ('connectioncode', models.IntegerField()),
                ('custname', models.CharField(max_length=1000)),
                ('zoneid', models.IntegerField()),
                ('Route', models.IntegerField()),
                ('zonename', models.CharField(max_length=100)),
                ('routename', models.CharField(max_length=100)),
                ('plotnumber', models.CharField(max_length=50)),
                ('balance', models.CharField(max_length=100)),
                ('serialno', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('connectionstatus', models.CharField(choices=[('Activated', 'Activated'), ('Disconnected', 'Disconnected')], max_length=256)),
            ],
        ),
        migrations.RemoveField(
            model_name='readings',
            name='Connectioncode',
        ),
        migrations.AlterField(
            model_name='payments',
            name='connectionCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.consumers'),
        ),
        migrations.DeleteModel(
            name='customers',
        ),
        migrations.DeleteModel(
            name='readings',
        ),
    ]
