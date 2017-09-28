# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=10)
    start = models.DateTimeField()
    end = models.DateTimeField()

class Test(models.Model):
    name = models.CharField(max_length=15)
    stype = models.IntegerField()
    studyTime = models.IntegerField()
    start = models.DateTimeField()

class TimeZone(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()



class Study(models.Model):
    name = models.CharField(max_length=15)
    stype = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField()
