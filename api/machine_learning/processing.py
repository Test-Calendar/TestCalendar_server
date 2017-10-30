# -*- coding: utf-8 -*-
import numpy as np
import datetime
""""""
# # from django.conf import settings
# import os, sys
# # sys.path.append(os.pardir)
# sys.path.append('../../')
# from api.models import Task, Test, TimeZone, Study
# from server.server import se ttings
from models import Task, Test, TimeZone, Study, Para
import ga
""""""
import random
import evaluation as eva
import pandas as pd

def processing(task_list, test_list, time_zones):
	""" parameter """
	today = datetime.datetime.today()
	sizeCol = len(test_list)
	max_date = max([tes.start for tes in test_list])
	sizeLow = (max_date - today).days - 1
	study_time = time_zones.get_hour() + 1

	""" set up """
	# size = np.array([1 for i in range(sizeCol * sizeLow.days)])
	# size = sizeCol * sizeLow.days * study_time
	size = sizeCol * sizeLow
	weight = np.array(eva.evaluation_func(test_list, task_list, sizeLow))

	para = Para(size=size, weight=weight, sizeCol=sizeCol, sizeLow=sizeLow, study_time=study_time)

	result = ga.main(para)

	schedule = np.array(result[-1])

	schedule_list = make_schedule(schedule.reshape(sizeLow, sizeCol), test_list)
	for i in schedule_list:
		print([j.name for j in i])
		print([j.stype for j in i])

	# print(weight.reshape(sizeLow, sizeCol))
	# print(schedule.reshape(sizeLow, sizeCol))
	return schedule_list

def make_schedule(sche, test_list):
	schedule_list = []
	for x in sche:
		count = 0
		schedule = []
		for i, test in zip(x, test_list):
			if i == 1:
				schedule.append(Study(name=test.name, stype=test.stype))
			else:
				schedule.append(Study(name="none", stype=0))

			count = count + 1
		schedule_list.append(schedule)

	return schedule_list

def time_manege(time_zone, test_fin_day):
	today = datetime.datetime.today()
	st_day = today.date() + time_zone.start


if __name__ == "__main__":
	processing()
