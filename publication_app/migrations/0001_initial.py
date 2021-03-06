# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-22 17:43
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auteurs', models.CharField(help_text='Suivre le format suivant: Prenom1 Nom1 and Prénom2 Nom2 and ...', max_length=300)),
                ('titre', models.CharField(max_length=300)),
                ('titre_livre', models.CharField(max_length=300)),
                ('editeur', models.CharField(max_length=300)),
                ('series', models.CharField(max_length=300)),
                ('adresse', models.CharField(max_length=300)),
                ('maison_edition', models.CharField(max_length=300)),
                ('volume', models.CharField(max_length=300)),
                ('pages', models.CharField(max_length=300)),
                ('url', models.CharField(max_length=300)),
                ('annee', models.PositiveIntegerField(help_text='Utilisez le format suivant: YYYY', validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2018)])),
            ],
        ),
    ]
