# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Task(models.Model):
    name = CharField(max_length=10)
    start = DateTimeField()
    end = DateTimeField()

class Test(models.Model):
    name = CharField(max_length=15)
    stype = IntegerField()
    studyTime = IntegerField()
    start = DateTimeField()

class Timezone(models.Model):
    start = DateTimeField()
    end = DateTimeField()



class Study(models.Model):
    name = CharField(max_length=15)
    stype = IntegerField()
    start = DateTimeField()
    end = DateTimeField()
