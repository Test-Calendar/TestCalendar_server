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
# from server.server import settings
from models import Task, Test, TimeZone, Study
""""""

def evaluation_value (oneday):
	return len([st for st in oneday if st.name != "none"])

def days_difference(first, second):
	dif = first.strftime('%s') - second.strftime('%s')
	return datetime.fromtimestamp(dif)

def processing(task_list, test_list, time_zones):
# def processing():
	""" parameter """
	today = datetime.datetime.today()
	# sorted(tests, key=lambda tes: tes.start)
	# sizeCol = 5
	sizeCol = len(test_list)
	upcoming = max([tes.start for tes in test_list])
	sizeLow = upcoming - today
	# studyTime = 3

	# size = np.array([21, 11, 15, 9, 34, 25, 41, 52])
	size = np.array([[1 for i in range(sizeCol)] for j in range(sizeLow.days)])
	# weight = np.array([22, 12, 16, 10, 35, 26, 42, 53])
	weight = np.array([22, 16, 53])
	study_hour = time_zones.get_hour()

	result = binary.binary(size, weight, study_hour)
	for r in result:
		print("result", r)

if __name__ == "__main__":
	# django.conf.settings.configure(default_settings=server.server.settings)
	processing()
