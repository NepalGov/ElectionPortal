# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 04:11
from __future__ import unicode_literals

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('e2074', '0015_auto_20170427_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='about',
            field=markdownx.models.MarkdownxField(),
        ),
        migrations.AlterField(
            model_name='party',
            name='about',
            field=markdownx.models.MarkdownxField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
        migrations.AlterField(
            model_name='team',
            name='about',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
