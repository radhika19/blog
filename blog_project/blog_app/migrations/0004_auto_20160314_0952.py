# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-14 09:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20160314_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='paragraph',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog_app.Paragraph'),
        ),
    ]