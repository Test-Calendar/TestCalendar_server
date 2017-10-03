import string
import random
import datetime
from processing import processing

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

class Study:
    def __init__(self, name, stype, start, end):
        self.name = name
        self.stype = stype
        self.start = start
        self.end = end

# class oneday:
#     def __init__(self):
#         self.schedule = []

    # def toArray(self):
    #     return self.schedule


def tests_process():
    tasks = []
    for i in range(5):
        day_start = datetime.datetime(2017, 10, 25 + i, 18)
        day_end = datetime.datetime(2017, 10, 25 + i, 20)
        tasks.append(Task(r"task", day_start, day_end))
    tests = []
    # random_str = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(4)])
    tests.append(Test("math", 1, 8, datetime.datetime(2017, 10, 31)))
    tests.append(Test("poko", 1, 7, datetime.datetime(2017, 11, 1)))
    tests.append(Test("poko", 2, 7, datetime.datetime(2017, 11, 1)))

    time_zone = TimeZone(18, 23)
    # study_schedule = []
    # sorted_value = max(dic.items(), key=(lambda x: x[1]))[0]
    # sorted_value = sorted(dic, key=attrgetter('age'))
    # sorted_value = sorted(dic, key=lambda t: t[1])
    # print(sorted_value)

if __name__ == '__main__':
    tests_process()
