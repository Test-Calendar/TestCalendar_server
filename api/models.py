# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


class Task(models.Model):
    name = models.CharField(max_length=10)
    start = models.DateTimeField('date published')
    end = models.DateTimeField('date published')

    # class Meta:
        # db_tablespace = "task"

class Test(models.Model):
    name = models.CharField(max_length=15)
    # 1:test 2:report 0:another
    stype = models.IntegerField(default=0)
    studyTime = models.IntegerField(default=10)
    start = models.DateTimeField('date published')

    def __lt__(self, other):
        # self < other
        return self.start < other.start

    # class Meta:
    #     db_tablespace = "test"

class TimeZone(models.Model):
    start = models.IntegerField(default=18)
    end = models.IntegerField(default=23)
    # class Meta:
    #     db_tablespace = "time_zone"



class Study(models.Model):
    name = models.CharField(max_length=15)
    stype = models.IntegerField(default=0)
    start = models.DateTimeField('date published')
    end = models.DateTimeField('date published')
    # class Meta:
    #     db_tablespace = "study"
