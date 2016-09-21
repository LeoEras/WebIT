# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Datos(models.Model):
    id = models.IntegerField(primary_key=True)
    actividad = models.CharField(max_length=300, blank=True, null=True)
    dia_inicio = models.DateField(blank=True, null=True)
    hora_inicio = models.TimeField(blank=True, null=True)
    dia_final = models.DateField(blank=True, null=True)
    hora_final = models.TimeField(blank=True, null=True)
    tiempo = models.TimeField(blank=True, null=True)
    responsable = models.CharField(max_length=100, blank=True, null=True)
    clase = models.CharField(max_length=15, blank=True, null=True)
    importancia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datos'


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
