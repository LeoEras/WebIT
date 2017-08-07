# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Application(models.Model):
    #applicationID = models.IntegerField(blank=True, null=True)
    application = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Application'
        #db_table = 'application'

class Activity(models.Model):
    #activityID = models.IntegerField(blank=True, null=True)
    activity = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Activity'
        #db_table = 'activity'

class Term(models.Model):
    #termID = models.IntegerField(blank=True, null=True)
    term = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Term'
        #db_table = 'term'

class Dates(models.Model):
    #datesID = models.IntegerField(blank=True, null=True)
    dates = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dates'
        #db_table = 'dates'

class Class_Type(models.Model):
    #classID = models.IntegerField(blank=True, null=True)
    class_name = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Class'
        #db_table = 'class'

class Users(models.Model):
    #usersID = models.IntegerField(blank=True, null=True)
    termID = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Users'
        #db_table = 'users'

class Log(models.Model):
    #logID = models.IntegerField(blank=True, null=True)
    termID = models.IntegerField(blank=True, null=True)
    activityID = models.IntegerField(blank=True, null=True)
    start_date = models.IntegerField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_date = models.IntegerField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    elapsed_time = models.TimeField(blank=True, null=True)
    applicationID = models.IntegerField(blank=True, null=True)
    classID = models.IntegerField(blank=True, null=True)
    relevance = models.IntegerField(blank=True, null=True)
    userID = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Log'
        #db_table = 'log'

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
