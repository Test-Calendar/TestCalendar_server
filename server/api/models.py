# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=10)
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        db_tablespace = "task"

class Test(models.Model):
    name = models.CharField(max_length=15)
    stype = models.IntegerField()
    studyTime = models.IntegerField()
    start = models.DateTimeField()

    def __lt__(self, other):
        # self < other
        return self.start < other.start

    class Meta:
        db_tablespace = "test"

class TimeZone(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    class Meta:
        db_tablespace = "time_zone"



class Study(models.Model):
    name = models.CharField(max_length=15)
    stype = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    class Meta:
        db_tablespace = "study"
