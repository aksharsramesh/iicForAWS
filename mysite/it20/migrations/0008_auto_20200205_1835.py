# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-05 18:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it20', '0007_auto_20200203_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newidea',
            old_name='contact',
            new_name='Contact_Number',
        ),
        migrations.RenameField(
            model_name='newidea',
            old_name='title',
            new_name='Title_Of_Idea',
        ),
    ]