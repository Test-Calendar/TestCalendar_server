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
import ga
""""""
import random
import evaluation as eva

def processing(task_list, test_list, time_zones):
	""" parameter """
	today = datetime.datetime.today()
	sizeCol = len(test_list)
	max_daye = max([tes.start for tes in test_list])
	sizeLow = max_daye - today

	""" function """
	size = np.array([[1 for i in range(sizeCol)] for j in range(sizeLow.days)])
	# weight = np.array([22, 16, 53, 32])
	weight = np.array(eva.evaluation_func(test_list))
	print(weight)
	# print(weight)
	study_hour = time_zones.get_hour() + 1

	result = binary.binary(size, weight, study_hour)
	# result = ga.oneMax(weight, binary.binary(size, weight, study_hour))

	for r in result:
		print("result", r)

if __name__ == "__main__":
	# django.conf.settings.configure(default_settings=server.server.settings)
	processing()
