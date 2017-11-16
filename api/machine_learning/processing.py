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
	date_to = max([tes.start for tes in test_list]) + datetime.timedelta(hours=-1)
	# schedule size
	# sizeCol = len(test_list)
	sizeCol = time_zones.get_hour()
	# print(sizeCol)
	# sizeCol = time_zones.get_hour() + 1
	sizeLow = (date_to.date() - date_from).days

	""" set up """
	myschedule = time_manege(time_zone=time_zones, date_to=date_to)
	# sizeLow = len(myschedule)
	# sizeLow = (date_to.date() - today.date()).days
	size = sizeCol * sizeLow
	weight = np.array(eva.evaluation_func(test_list=test_list, task_list=task_list, sizeLow=sizeLow))
	for we in weight:
		for w in we:
			print(format(round(w, 2))),
		print("")

	para = Para(
		size=size,
		weight=weight,
		sizeCol=sizeCol,
		sizeLow=sizeLow,
		test_list=test_list)

	result = ga.main(para)

	schedule = np.array(result[-1])
	# print(schedule.reshape(sizeLow, sizeCol))
	# print(np.sum(schedule.reshape(sizeLow, sizeCol), axis=0))
	# print(np.sum(schedule.reshape(sizeLow, sizeCol), axis=1))

	schedule_list = make_schedule(schedule.reshape(sizeLow, sizeCol), test_list)
	# print(weight.reshape(sizeLow, sizeCol))
	# for i in schedule_list:
	# 	print([j.stype for j in i])
	# 	print([j.name for j in i])

	# print(weight.reshape(sizeLow, sizeCol))
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
	if time_zone.start > time_zone.end:
		finish_study = date_to + datetime.timedelta(hours=time_zone.end + 1)
		time_zone_fin = [True] * (time_zone.end + 1)
		if today.hour >= time_zone.start or today.hour < time_zone.end:
			begin_study = datetime.datetime.combine(today.date(), datetime.time()) + datetime.timedelta(hours=today.hour + 1)
			time_zone_st = [True] * (23 - today.hour)
		else:
			begin_study = datetime.datetime.combine(today.date(), datetime.time()) + datetime.timedelta(hours=time_zone.start)
			time_zone_st = [True] * (24 - time_zone.start)
	else:
		if today.hour >= time_zone.start and today.hour < time_zone.end:
			begin_study = datetime.datetime.combine(date_from, datetime.time()) + datetime.timedelta(days=-1, hours=today.hour + 1)
			time_zone_st = [True] * (time_zone.end - today.hour)
		else:
			time_zone_st = [True] * (time_zone.end - time_zone.start)

	if time_zone.start > time_zone.end:
		time_zones = [True if time_zone.start <= i or time_zone.end >= i else False for i in range(24)]
	else:
		time_zones = [True if time_zone.start <= i and time_zone.end >= i else False for i in range(24)]
	until_test = date_to.date() - date_from
	dtidx = pd.date_range(start=begin_study, end=finish_study, freq = 'H')
	selector = time_zone_st + time_zones * (until_test.days + 1) + time_zone_fin
	dtidx = dtidx[selector].asobject.tolist()
	# for dt in dtidx:
	# 	print(dt)
	return dtidx

if __name__ == "__main__":
	processing()
