import string
import random
import datetime
import processing
from models import Task, Test, TimeZone, Study

def tests_process():
    tasks = []
    for i in range(3):
        day_start = datetime.datetime(2017, 11, 13 + i, 17)
        day_end = datetime.datetime(2017, 11, 13 + i, 20)
        tasks.append(Task("task", day_start, day_end))
    tests = []
    tests.append(Test("math", 1, 6, datetime.datetime(2017, 11, 20)))
    tests.append(Test("poko", 1, 7, datetime.datetime(2017, 11, 20)))
    tests.append(Test("poko", 2, 7, datetime.datetime(2017, 11, 20)))
    tests.append(Test("math", 2, 8, datetime.datetime(2017, 11, 21)))
    tests.append(Test("taku", 2, 7, datetime.datetime(2017, 11, 22)))
    tests.append(Test("taku", 1, 7, datetime.datetime(2017, 11, 22)))
    tests.append(Test("poko", 1, 9, datetime.datetime(2017, 11, 23)))
    tests.append(Test("math", 1, 8, datetime.datetime(2017, 11, 24)))

    time_zone = TimeZone(19, 2)
    processing.processing(task_list=tasks, test_list=tests, time_zones=time_zone)

if __name__ == '__main__':
    tests_process()
