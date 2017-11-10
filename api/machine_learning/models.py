import string
import random
import datetime
import numpy as np

class Task:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

    def get_start_time(self, study_start):
        if self.start.hour < study_start:
            return study_start
        else:
            return self.start.hour
    def get_end_time(self, study_end):
        if self.end.hour < study_end:
            return study_end
        else:
            return self.end.hour

class Test:
    def __init__(self, name, stype, studyTime, start):
        self.name = name
        self.stype = stype
        self.studyTime = studyTime
        self.start = start

class TimeZone:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_hour(self):
        return abs (self.end - self.start)

    def get_time_zone(self):
        if self.start > self.end:
            time_zones = [True if self.start <= i or self.end >= i else False for i in range(24)]
        else:
            time_zones = [True if sel.start <= i and sel.end >= i else False for i in range(24)]
        return time_zones


class Study:
    def __init__(self, name, stype):
        self.name = name
        self.stype = stype

class Para:
    def __init__(self, size, weight, sizeCol, sizeLow, study_time, test_list):
        self.size = size
        self.weight = np.array(weight)
        self.sizeCol = sizeCol
        self.sizeLow = sizeLow
        self.study_time = study_time
        self.test_list = test_list
