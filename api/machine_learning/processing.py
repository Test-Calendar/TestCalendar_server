# -*- coding: utf-8 -*-
import numpy as np
import datetime
from models import Task, Test, TimeZone, Study, Para
import ga
import random
import evaluation as eva
import pandas as pd

today = datetime.datetime.today()
date_from = today.date() + datetime.timedelta(days=1)

def processing(task_list, test_list, time_zones):
	""" parameter """
	sizeCol = len(test_list)
	date_to = max([tes.start for tes in test_list]) + datetime.timedelta(days=-1, hours=-1)
	sizeLow = (date_to.date() - date_from).days
	study_time = time_zones.get_hour() + 1

	""" set up """
	myschedule = time_manege(time_zone=time_zones, date_to=date_to)
	size = sizeCol * sizeLow
	weight = np.array(eva.evaluation_func(test_list, task_list, sizeLow))

	para = Para(
		size=size,
		weight=weight,
		sizeCol=sizeCol,
		sizeLow=sizeLow,
		study_time=study_time,
		test_list=test_list)

	result = ga.main(para)

	schedule = np.array(result[-1])

	schedule_list = make_schedule(schedule.reshape(sizeLow, sizeCol), test_list)
	# print(weight.reshape(sizeLow, sizeCol))
	# for i in schedule_list:
		# print([j.name for j in i])
		# print([j.stype for j in i])

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

def time_manege(time_zone, date_to):
	until_test = date_to.date() - date_from
	dtidx = pd.date_range(start=date_from, end=date_to, freq = 'H')
	selector = time_zone.get_time_zone() * (until_test.days)
	dtidx = dtidx[selector].asobject.tolist()
	for dt in dtidx:
		print(dt)
	return dtidx

if __name__ == "__main__":
	processing()
