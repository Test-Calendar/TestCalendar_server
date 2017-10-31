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

    def __lt__(self, other):
        # self < other
        return self.start < other.start

class TimeZone:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_hour(self):
        hour = self.end - self.start
        return hour

# class Study:
#     def __init__(self, name, stype, start, end):
#         self.name = name
#         self.stype = stype
#         self.start = start
#         self.end = end
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
