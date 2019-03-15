# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 13:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bilet',
            name='seans_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.Seans'),
        ),
        migrations.AlterField(
            model_name='bron',
            name='seans_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.Seans'),
        ),
        migrations.AlterField(
            model_name='seans',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.Film'),
        ),
        migrations.AlterField(
            model_name='sell',
            name='seans_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.Seans'),
        ),
    ]
