# -*- coding: utf-8 -*-
import numpy as np
# import onemax as ga
import binary as binary
import cvxpy
import datetime
# from api.models import Task, Test, TimeZone, Study
""""""
# # from django.conf import settings
# import os, sys
# # sys.path.append(os.pardir)
# sys.path.append('../../')
# from api.models import Task, Test, TimeZone, Study
# from server.server import se ttings
from models import Task, Test, TimeZone, Study
import ga
""""""
import random
import evaluation as eva
import pandas as pd

def task_check(task_list, time_zone):
	pass

# def make_schedule(b_sche, test_list):
# 	schedule = [i.name for i in test_list if]
# 	for i, j in zip(test_list, b_sche):
# 		schedule.append(i.name if j != 0)
# 	return schedule
#
# def get_stype(b_sche, test_list):
# 	type_list = []
# 	for i, j in zip(test_list, b_sche):
# 		type_list.append(i.stype if j != 0)
# 	return type_list

def processing(task_list, test_list, time_zones):
	""" parameter """
	today = datetime.datetime.today()
	sizeCol = len(test_list)
	max_daye = max([tes.start for tes in test_list])
	sizeLow = max_daye - today
	study_hour = time_zones.get_hour() + 1

	""""""
	# schedule = pd.date_range({
	#
	# })

	""" set up """
	# size = np.array([1 for i in range(sizeCol * sizeLow.days)])
	size = sizeCol * sizeLow.days
	# size = np.array([[1 for i in range(sizeCol)] for j in range(sizeLow.days)])
	# weight = np.array([22, 16, 53, 32])
	weight = np.array(eva.evaluation_func(test_list, task_list))
	# print(weight)

	# result = binary.binary(size, weight, study_hour)
	result = ga.main(weight, size)
	# result = ga.oneMax(weight, binary.binary(size, weight, study_hour))
	# df = pd.DataFrame({'date' : pd.to_datetime('today'),
	# 'name' : np.array(make_schedule(result, test_list)),
	# 'stype' : np.array(get_stype(result, test_list)),
	# 'start' : np.array([3] * 4,dtype='int32'),
	# 'end' : pd.Categorical(["test","train","test","train"])})

	# for r in result:
	# 	print("result", r)
	sche = np.array(result[-1])
	print(sche.reshape(sizeLow.days, sizeCol))

if __name__ == "__main__":
	# django.conf.settings.configure(default_settings=server.server.settings)
	processing()
