import string
import random
import datetime
import numpy as np

class Task:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

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

class Study:
    def __init__(self, name, stype, start, end):
        self.name = name
        self.stype = stype
        self.start = start
        self.end = end

class Para:
    def __init__(self, size, weight, sizeCol, sizeLow):
        self.size = size
        self.weight = np.array(weight)
        self.sizeCol = sizeCol
        self.sizeLow = sizeLow
