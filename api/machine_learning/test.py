import string
import random
import datetime
import processing
from models import Task, Test, TimeZone, Study

today = datetime.datetime.today().date()

def tests_process():
    tasks = []
    for i in range(3):
        day_start = today + datetime.timedelta(days=2 + i, hours=17)
        day_end = today + datetime.timedelta(days=2 + i, hours=20)
        tasks.append(Task("task", day_start, day_end))
    tests = []
    tests.append(Test("math", 1, 6, datetime.datetime.combine(today.date(), datetime.time()) + datetime.timedelta(days=7)))
    tests.append(Test("poko", 1, 7, datetime.datetime.combine(today.date(), datetime.time()) + datetime.timedelta(days=7)))
    tests.append(Test("poko", 2, 7, datetime.datetime.combine(today.date(), datetime.time()) + datetime.timedelta(days=7)))
    tests.append(Test("math", 2, 8, datetime.datetime.combine(today.date(), datetime.time()) + datetime.timedelta(days=8)))
    tests.append(Test("taku", 2, 7, datetime.datetime.combine(today.date(), datetime.time()) + datetime.timedelta(days=8)))
    tests.append(Test("taku", 1, 7, datetime.datetime.combine(today.date(), datetime.time()) + datetime.timedelta(days=9)))
    tests.append(Test("poko", 1, 9, datetime.datetime.combine(today.date(), datetime.time()) + datetime.timedelta(days=9)))
    tests.append(Test("math", 1, 8, datetime.datetime.combine(today.date(), datetime.time()) + datetime.timedelta(days=10)))

    time_zone = TimeZone(19, 2)
    processing.processing(task_list=tasks, test_list=tests, time_zones=time_zone)

if __name__ == '__main__':
    tests_process()
