# -*- coding: utf-8 -*-
import numpy as np
import cvxpy
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
	max_daye = max([tes.start for tes in test_list])
	sizeLow = max_daye - today
	study_time = time_zones.get_hour() + 1

	""" set up """
	# size = np.array([1 for i in range(sizeCol * sizeLow.days)])
	# size = sizeCol * sizeLow.days * study_time
	size = sizeCol * sizeLow.days
	weight = np.array(eva.evaluation_func(test_list, task_list))

	para = Para(size=size, weight=weight, sizeCol=sizeCol, sizeLow=sizeLow, study_time=study_time)

	result = ga.main(para)

	sche = np.array(result[-1])

	schedule_list = make_schedule(sche.reshape(sizeLow.days, sizeCol), test_list)
	for i in schedule_list:
		print([j.name for j in i])
		print([j.stype for j in i])

	print(sche.reshape(sizeLow.days, sizeCol))

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

if __name__ == "__main__":
	# django.conf.settings.configure(default_settings=server.server.settings)
	processing()
