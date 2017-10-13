import string
import random
import datetime
import processing
from models import Task, Test, TimeZone, Study

def tests_process():
    tasks = []
    for i in range(5):
        day_start = datetime.datetime(2017, 10, 25 + i, 17)
        day_end = datetime.datetime(2017, 10, 25 + i, 20)
        tasks.append(Task("task", day_start, day_end))
    tests = []
    # random_str = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(4)])
    tests.append(Test("math", 2, 8, datetime.datetime(2017, 10, 31)))
    tests.append(Test("math", 1, 6, datetime.datetime(2017, 10, 30)))
    tests.append(Test("math", 1, 8, datetime.datetime(2017, 10, 31)))
    tests.append(Test("poko", 1, 7, datetime.datetime(2017, 11, 1)))
    tests.append(Test("poko", 2, 7, datetime.datetime(2017, 11, 1)))
    tests.append(Test("taku", 2, 7, datetime.datetime(2017, 11, 2)))
    tests.append(Test("taku", 1, 7, datetime.datetime(2017, 11, 2)))
    tests.append(Test("poko", 2, 9, datetime.datetime(2017, 11, 3)))

    time_zone = TimeZone(18, 23)
    processing.processing(task_list=tasks, test_list=tests, time_zones=time_zone)

if __name__ == '__main__':
    tests_process()
