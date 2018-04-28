# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-22 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='adresse',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='conference',
            name='editeur',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='conference',
            name='maison_edition',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='conference',
            name='pages',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='conference',
            name='series',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='conference',
            name='titre',
            field=models.CharField(help_text="Le titre de l'article", max_length=300),
        ),
        migrations.AlterField(
            model_name='conference',
            name='titre_livre',
            field=models.CharField(help_text="Le nom de la conférence dans laquelle l'article a été publié", max_length=300),
        ),
        migrations.AlterField(
            model_name='conference',
            name='url',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='conference',
            name='volume',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]